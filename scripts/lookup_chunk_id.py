"""Resolve real `document_chunks.legacy_chunk_id` values for verbatim quotes
pulled from a source document, via a direct psycopg connection to Postgres.

This is the "Session 0" tooling described in
eval-generation-notes/answer-eval-migration_20260831.md: given a document's
`external_id` and a verbatim quote a human/LLM extracted from that document
(while grounding an Answer-mode `key_facts` entry), find which chunk in
`document_chunks` contains it, and report its `chunk_id`/`page`.

Deliberately non-circular: this NEVER calls the live hybrid search service or
any embedding model. It only does plain text matching (exact substring, with a
character-n-gram fallback for near-verbatim quotes) against the known set of
chunks belonging to ONE already-identified document - there is no
retrieval/ranking step at all, so this cannot inherit bias from AskWRI's
production retrieval/embedding system the way the existing (and explicitly
flagged-as-circular) evaluation/map-passages-to-chunks.ts approach does by
querying the live /query endpoint.

Connection pattern mirrors scripts/db_text_to_markdown_askwri-qa.py: direct
psycopg connection (no docker/psql), PGPASSWORD read from the environment by
libpq (set it in a local, gitignored mise.local.toml's [env] block, then run
via `mise exec -- uv run scripts/lookup_chunk_id.py ...`), RDS CA bundle at
../../global-bundle.pem (one level above this repo, same as the sibling
script).

Usage:
  # Single ad-hoc lookup.
  uv run scripts/lookup_chunk_id.py \\
      --external-id 2020_dockless-bike-sharing_00124 \\
      --quote "<verbatim quote text>"

  # Batch mode: read [{"id":..., "external_id":..., "quote":...}, ...] from a
  # JSON file, write the same entries back out with chunk_id/page/score added.
  uv run scripts/lookup_chunk_id.py --input quotes.json --output resolved.json

  # Validation (Session 0, step (a) - see migration plan): round-trip a real
  # chunk's own text back through the matcher and confirm it resolves to
  # itself.
  uv run scripts/lookup_chunk_id.py --self-test 2020_dockless-bike-sharing_00124

  # Inspect a document's chunks directly (manual sanity-checking).
  uv run scripts/lookup_chunk_id.py --list-chunks 2020_dockless-bike-sharing_00124

  # Override connection details (same defaults as db_text_to_markdown_askwri-qa.py).
  uv run scripts/lookup_chunk_id.py --host ... --user ... --db qa ...
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

import psycopg

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SSLROOTCERT = REPO_ROOT.parent.parent / "global-bundle.pem"
DEFAULT_HOST = "askwri-db1.cty8g4ssygz9.us-east-2.rds.amazonaws.com"

# Below this score, a match is reported but flagged for manual review rather
# than accepted outright - see "Edge case" in the migration plan doc.
LOW_CONFIDENCE_THRESHOLD = 0.5

CHUNKS_QUERY = """
SELECT dc.chunk_index, dc.legacy_chunk_id, dc.page, dc.text
FROM document_chunks dc
JOIN documents d ON dc.document_id = d.id
WHERE d.external_id = %s AND dc.chunk_index >= 0
ORDER BY dc.chunk_index;
""".strip()


# --- Connection (mirrors scripts/db_text_to_markdown_askwri-qa.py) ---


def build_conn_str(host: str, port: int, db: str, user: str, sslmode: str, sslrootcert: Path) -> str:
    """No password embedded - psycopg/libpq reads PGPASSWORD from the
    environment automatically, same as pgcli/psql do."""
    return f"postgresql://{user}@{host}:{port}/{db}?sslmode={sslmode}&sslrootcert={sslrootcert}&connect_timeout=5"


def fetch_chunks(conn_str: str, external_id: str) -> list[dict[str, Any]]:
    """All text chunks (chunk_index >= 0, i.e. excluding the synthetic
    `_summary` node) for one document, ordered by chunk_index."""
    with psycopg.connect(conn_str) as conn:
        with conn.cursor() as cur:
            cur.execute(CHUNKS_QUERY, (external_id,))
            rows = cur.fetchall()
            return [
                {"chunk_index": r[0], "chunk_id": r[1], "page": r[2], "text": r[3]}
                for r in rows
            ]


# --- Text normalization / matching ---
#
# Deliberately plain string/set operations only - no embeddings, no calls to
# any search service. See module docstring.

_WHITESPACE_RE = re.compile(r"\s+")
_MD_EMPHASIS_RE = re.compile(r"[*_#`]")


def normalize(text: str) -> str:
    """Make a quote and a chunk's stored text directly comparable: strip
    markdown emphasis characters a human/LLM might have accidentally carried
    over while copying a quote, collapse all whitespace runs (including
    newlines) to single spaces, and trim. Case-folding is harmless for
    CJK/Spanish text and helps for any Latin-script content."""
    text = _MD_EMPHASIS_RE.sub("", text)
    text = _WHITESPACE_RE.sub(" ", text)
    return text.strip().lower()


def char_ngrams(text: str, n: int = 8) -> set[str]:
    """Character n-grams, not word n-grams: word-level tokenization (splitting
    on whitespace) is meaningless for Chinese, which has no inter-word spaces.
    Character n-grams work uniformly across zh/es/en without needing
    language-specific tokenization."""
    if len(text) < n:
        return {text} if text else set()
    return {text[i : i + n] for i in range(len(text) - n + 1)}


def ngram_overlap_score(quote: str, chunk_text: str, n: int = 8) -> float:
    """Jaccard similarity over character n-grams. Used as a fallback when the
    quote isn't found as an exact substring (e.g. it straddles two adjacent,
    overlapping chunks, or has minor whitespace/punctuation drift)."""
    q_grams = char_ngrams(quote, n)
    c_grams = char_ngrams(chunk_text, n)
    if not q_grams or not c_grams:
        return 0.0
    intersection = len(q_grams & c_grams)
    union = len(q_grams | c_grams)
    return intersection / union if union else 0.0


def containment_score(quote: str, chunk_text: str, n: int = 8) -> float:
    """What fraction of the quote's n-grams appear in the chunk. More
    forgiving than Jaccard when the chunk is much longer than the quote (the
    normal case: a one-sentence quote against a ~400-char chunk) - Jaccard's
    union term penalizes that size mismatch even for a perfect containment."""
    q_grams = char_ngrams(quote, n)
    c_grams = char_ngrams(chunk_text, n)
    if not q_grams:
        return 0.0
    return len(q_grams & c_grams) / len(q_grams)


@dataclass
class MatchResult:
    chunk_id: str | None
    page: int | None
    chunk_index: int | None
    match_method: str  # "exact" | "ngram" | "none"
    score: float
    low_confidence: bool


def find_matching_chunk(quote: str, chunks: list[dict[str, Any]]) -> MatchResult:
    """Find the chunk in `chunks` (already scoped to one document, via
    fetch_chunks) that best contains `quote`. Tries exact substring
    containment first (expected to be the common case, since quotes are
    extracted verbatim from kp-docs/markdown/*.md, which is itself a direct
    copy of the same document_texts.full_text the chunker split); falls back
    to n-gram containment for quotes that straddle a chunk boundary or have
    minor formatting drift.
    """
    if not chunks:
        return MatchResult(None, None, None, "none", 0.0, True)

    norm_quote = normalize(quote)

    # Pass 1: exact substring containment. Prefer the chunk where the quote
    # makes up the largest share of the chunk's own text (tie-break toward a
    # tighter, more specific match rather than e.g. a near-empty chunk that
    # happens to contain a short quote as a fluke).
    exact_candidates = []
    for c in chunks:
        norm_chunk = normalize(c["text"])
        if norm_quote and norm_quote in norm_chunk:
            specificity = len(norm_quote) / len(norm_chunk) if norm_chunk else 0.0
            exact_candidates.append((specificity, c))
    if exact_candidates:
        exact_candidates.sort(key=lambda t: t[0], reverse=True)
        _, best = exact_candidates[0]
        return MatchResult(
            chunk_id=best["chunk_id"],
            page=best["page"],
            chunk_index=best["chunk_index"],
            match_method="exact",
            score=1.0,
            low_confidence=False,
        )

    # Pass 2: n-gram containment fallback, scored against every chunk.
    scored = [
        (containment_score(norm_quote, normalize(c["text"])), c) for c in chunks
    ]
    scored.sort(key=lambda t: t[0], reverse=True)
    best_score, best = scored[0]
    return MatchResult(
        chunk_id=best["chunk_id"],
        page=best["page"],
        chunk_index=best["chunk_index"],
        match_method="ngram",
        score=round(best_score, 4),
        low_confidence=best_score < LOW_CONFIDENCE_THRESHOLD,
    )


# --- CLI ---


def resolve_one(conn_str: str, external_id: str, quote: str, cache: dict[str, list[dict[str, Any]]]) -> MatchResult:
    if external_id not in cache:
        cache[external_id] = fetch_chunks(conn_str, external_id)
    return find_matching_chunk(quote, cache[external_id])


def cmd_self_test(conn_str: str, external_id: str) -> None:
    """Round-trip identity check (migration plan, Session 0 validation (a)):
    feed a real chunk's own text back through the matcher and confirm it
    resolves to itself. Uses the first and last text chunk (index 0 and the
    max index) as two independent trials."""
    chunks = fetch_chunks(conn_str, external_id)
    if not chunks:
        print(f"No chunks found for external_id={external_id!r} - check the id and corpus status.")
        sys.exit(1)
    print(f"{external_id}: {len(chunks)} text chunks found.\n")

    trial_chunks = [chunks[0]]
    if len(chunks) > 1:
        trial_chunks.append(chunks[-1])

    all_ok = True
    for trial in trial_chunks:
        result = find_matching_chunk(trial["text"], chunks)
        ok = result.chunk_id == trial["chunk_id"]
        all_ok = all_ok and ok
        status = "OK" if ok else "MISMATCH"
        print(
            f"[{status}] chunk_index={trial['chunk_index']} "
            f"expected chunk_id={trial['chunk_id']!r} "
            f"-> matched chunk_id={result.chunk_id!r} "
            f"(method={result.match_method}, score={result.score})"
        )
    print()
    print("Self-test PASSED" if all_ok else "Self-test FAILED")
    sys.exit(0 if all_ok else 1)


def cmd_list_chunks(conn_str: str, external_id: str) -> None:
    chunks = fetch_chunks(conn_str, external_id)
    if not chunks:
        print(f"No chunks found for external_id={external_id!r}.")
        return
    print(f"{external_id}: {len(chunks)} text chunks\n")
    for c in chunks:
        preview = c["text"][:80].replace("\n", " ")
        print(f"  [{c['chunk_index']:>4}] page={c['page']} id={c['chunk_id']}  {preview!r}...")


def cmd_single(conn_str: str, external_id: str, quote: str) -> None:
    chunks = fetch_chunks(conn_str, external_id)
    result = find_matching_chunk(quote, chunks)
    print(json.dumps(asdict(result), indent=2, ensure_ascii=False))
    if result.low_confidence:
        print("\n! low-confidence match - review manually before trusting this chunk_id.", file=sys.stderr)


def cmd_batch(conn_str: str, input_path: Path, output_path: Path) -> None:
    entries = json.loads(input_path.read_text(encoding="utf-8"))
    cache: dict[str, list[dict[str, Any]]] = {}
    flagged = []
    for entry in entries:
        result = resolve_one(conn_str, entry["external_id"], entry["quote"], cache)
        entry["chunk_id"] = result.chunk_id
        entry["page"] = result.page
        entry["match_method"] = result.match_method
        entry["score"] = result.score
        if result.low_confidence:
            flagged.append(entry.get("id", entry["external_id"]))
    output_path.write_text(json.dumps(entries, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Resolved {len(entries)} quotes -> {output_path}")
    if flagged:
        print(f"! {len(flagged)} low-confidence match(es), review manually: {flagged}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--host", default=DEFAULT_HOST, help="Postgres host")
    parser.add_argument("--port", type=int, default=5432, help="Postgres port")
    parser.add_argument("--db", default="qa", help="Postgres database name")
    parser.add_argument("--user", default="askwri", help="Postgres user")
    parser.add_argument("--sslmode", default="verify-full", help="libpq sslmode")
    parser.add_argument("--sslrootcert", type=Path, default=DEFAULT_SSLROOTCERT, help="Path to RDS CA bundle PEM")

    parser.add_argument("--external-id", help="Document external_id, for --quote or --list-chunks/--self-test")
    parser.add_argument("--quote", help="Verbatim quote text to resolve (single ad-hoc lookup)")
    parser.add_argument("--input", type=Path, help="Batch mode: JSON file of [{id, external_id, quote}, ...]")
    parser.add_argument("--output", type=Path, help="Batch mode: where to write resolved entries")
    parser.add_argument("--self-test", metavar="EXTERNAL_ID", help="Validation: round-trip a real chunk's own text")
    parser.add_argument("--list-chunks", metavar="EXTERNAL_ID", help="Dump a document's chunks for inspection")

    args = parser.parse_args()
    conn_str = build_conn_str(args.host, args.port, args.db, args.user, args.sslmode, args.sslrootcert)

    if args.self_test:
        cmd_self_test(conn_str, args.self_test)
    elif args.list_chunks:
        cmd_list_chunks(conn_str, args.list_chunks)
    elif args.input:
        if not args.output:
            parser.error("--input requires --output")
        cmd_batch(conn_str, args.input, args.output)
    elif args.external_id and args.quote:
        cmd_single(conn_str, args.external_id, args.quote)
    else:
        parser.error("Specify --self-test, --list-chunks, --input/--output, or --external-id/--quote")


if __name__ == "__main__":
    main()
