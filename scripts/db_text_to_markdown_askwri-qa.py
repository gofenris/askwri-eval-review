"""Refresh kp-docs/markdown/*.md frontmatter (and, optionally, body text) from
the live askwri-qa Postgres database via a direct psycopg connection.

Unlike scripts/db_text_to_markdown.py and scripts/db_text_to_markdown_s3_docs.py
(which use `docker exec ... psql` against a local container and only ever
*create* a .md file once, never touching it again), this script:

  - Connects directly to the remote RDS instance with psycopg (no docker, no
    psql binary required - portable to any machine with psycopg[binary]
    installed).
  - Treats Postgres as the source of truth and DIFFS every existing local .md
    file's frontmatter against fresh `documents` (+ `document_summaries`)
    metadata, rather than only writing files that don't exist yet.
  - Splits work into two cost/risk tiers:
      * metadata refresh (documents + document_summaries): cheap, expected to
        run often.
      * full-text refresh (document_texts.full_text): expensive/rare, only
        runs when --refresh-text is passed.
  - Never silently overwrites "critical" fields (external_id-matching,
    language, languages, status) that differ from what's on disk - those are
    only reported until a human passes --approve-critical.

Usage:
  # Report-only: diff every local .md's metadata against Postgres, write nothing.
  uv run scripts/db_text_to_markdown_askwri-qa.py

  # Apply non-critical metadata changes (title, authors, dates, doi, url, summary, ...).
  uv run scripts/db_text_to_markdown_askwri-qa.py --update

  # Also apply critical field changes (language/languages/status) once reviewed.
  uv run scripts/db_text_to_markdown_askwri-qa.py --update --approve-critical

  # Also check for brand-new docs and full_text drift (expensive).
  uv run scripts/db_text_to_markdown_askwri-qa.py --update --refresh-text

  # Override connection details.
  uv run scripts/db_text_to_markdown_askwri-qa.py --host ... --user ... --db qa
"""

from __future__ import annotations

import argparse
import datetime
import json
import sys
from pathlib import Path
from typing import Any

import psycopg
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from db_text_to_markdown import find_local_pdf_ids, yaml_escape  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_KP_DOCS_DIR = REPO_ROOT / "kp-docs"
DEFAULT_PDF_DIRS = [
    DEFAULT_KP_DOCS_DIR / "CN-KPs-PDF",
    DEFAULT_KP_DOCS_DIR / "ES-KPs-PDF",
]
DEFAULT_OUTPUT_DIR = DEFAULT_KP_DOCS_DIR / "markdown"
DEFAULT_SSLROOTCERT = REPO_ROOT.parent.parent / "global-bundle.pem"
DEFAULT_HOST = "askwri-db1.cty8g4ssygz9.us-east-2.rds.amazonaws.com"

# Frontmatter keys that describe *how/where the text was extracted*, not
# document metadata. Preserved verbatim from whatever's already on disk for
# existing files during a metadata-only run; only touched by --refresh-text.
LINEAGE_FIELD_ORDER = [
    "doc_id",
    "source_pdf",
    "extraction_method",
    "parse_backend",
    "parse_model",
    "char_count",
]

# Frontmatter keys sourced straight from `documents` (+ document_summaries),
# in the order they're rendered. This is the full "care about" set from
# Postgres - anything not listed here (source_metadata, metadata_source,
# content_hash, extraction_confidence, created_at, updated_at, etc.) is
# intentionally left out of the markdown frontmatter.
DB_FIELD_ORDER = [
    "title",
    "title_en",
    "authors",
    "date_published",
    "year_published",
    "publication_title",
    "article_type",
    "wri_primary_office",
    "language",
    "languages",
    "doi",
    "url",
    "status",
    "summary",
]

# Fields where a DB/disk mismatch must never be auto-written - only reported -
# until a human passes --approve-critical. These directly affect eval
# resolution (external_id/language) or corpus inclusion (status), per the
# 2026-08-17 corpus-refresh incident where UUID/status churn silently broke
# evalset references.
CRITICAL_FIELDS = {"language", "languages", "status"}

METADATA_QUERY = """
SELECT json_agg(row_to_json(t)) FROM (
  SELECT
    d.external_id, d.title, d.title_en, d.authors, d.doi, d.url,
    d.date_published, d.year_published, d.publication_title,
    d.article_type, d.wri_primary_office, d.language, d.languages,
    d.status, s.text AS summary
  FROM documents d
  LEFT JOIN document_summaries s
    ON s.document_id = d.id AND s.language = 'en' AND s.kind = 'long'
) t;
""".strip()

TEXT_QUERY = """
SELECT json_agg(row_to_json(t)) FROM (
  SELECT
    d.external_id, d.s3_key,
    dt.full_text, dt.char_count, dt.parse_backend, dt.parse_model
  FROM documents d
  JOIN document_texts dt ON dt.document_id = d.id
  WHERE dt.parse_backend = 'mistral'
) t;
""".strip()


def build_conn_str(host: str, port: int, db: str, user: str, sslmode: str, sslrootcert: Path) -> str:
    """No password embedded - psycopg/libpq reads PGPASSWORD from the
    environment automatically, same as pgcli/psql do."""
    return f"postgresql://{user}@{host}:{port}/{db}?sslmode={sslmode}&sslrootcert={sslrootcert}&connect_timeout=5"


def fetch_rows(conn_str: str, query: str) -> list[dict[str, Any]]:
    """Run `query` (expected to be a `SELECT json_agg(row_to_json(t)) ...`
    shape) and return the result as a native list of dicts. psycopg adapts
    Postgres json/jsonb columns to Python objects automatically; the
    isinstance check below is just a safety net, not the old
    docker-exec-then-json.loads(stdout) indirection."""
    with psycopg.connect(conn_str) as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            row = cur.fetchone()
            data = row[0] if row and row[0] else []
            if isinstance(data, str):
                data = json.loads(data)
            return data or []


def normalize(value: Any) -> Any:
    """Make DB values and YAML-parsed disk values directly comparable:
    dates/datetimes -> ISO strings, everything else passed through as-is
    (str/int/list/None)."""
    if isinstance(value, (datetime.date, datetime.datetime)):
        return value.isoformat()
    return value


def prepare_db_row(row: dict[str, Any]) -> dict[str, Any]:
    return {k: normalize(v) for k, v in row.items()}


def parse_existing_markdown(path: Path) -> tuple[dict[str, Any], str, str]:
    """Return (frontmatter_dict, body, raw_text) for an existing --- delimited
    markdown file. If no frontmatter block is found, frontmatter_dict is {}
    and body is the full file content."""
    raw_text = path.read_text(encoding="utf-8")
    lines = raw_text.split("\n")
    if not lines or lines[0].strip() != "---":
        return {}, raw_text, raw_text
    try:
        close_idx = lines.index("---", 1)
    except ValueError:
        return {}, raw_text, raw_text
    fm_text = "\n".join(lines[1:close_idx])
    try:
        fm = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError:
        fm = {}
    if not isinstance(fm, dict):
        fm = {}
    body_lines = lines[close_idx + 1 :]
    while body_lines and body_lines[0] == "":
        body_lines.pop(0)
    body = "\n".join(body_lines)
    return fm, body, raw_text


def render_frontmatter(fm: dict[str, Any]) -> str:
    lines = ["---"]
    for key in LINEAGE_FIELD_ORDER + DB_FIELD_ORDER:
        if key not in fm:
            continue
        value = fm[key]
        if value in (None, ""):
            continue
        if isinstance(value, list):
            if not value:
                continue
            lines.append(f"{key}: [" + ", ".join(yaml_escape(v) for v in value) + "]")
        else:
            lines.append(f"{key}: {yaml_escape(value)}")
    lines.append("---")
    return "\n".join(lines)


def render_full(fm: dict[str, Any], body: str) -> str:
    return f"{render_frontmatter(fm)}\n\n{body}"


def diff_descriptive_fields(old_fm: dict[str, Any], db_row: dict[str, Any]) -> dict[str, tuple[Any, Any]]:
    """Compare old_fm's DB_FIELD_ORDER values against fresh db_row values.
    Returns {field: (old_value, new_value)} for every field that differs."""
    diffs: dict[str, tuple[Any, Any]] = {}
    for key in DB_FIELD_ORDER:
        old_val = old_fm.get(key)
        new_val = db_row.get(key) if db_row.get(key) not in ("", []) else None
        if old_val != new_val:
            diffs[key] = (old_val, new_val)
    return diffs


def build_updated_fm(
    old_fm: dict[str, Any],
    db_row: dict[str, Any],
    diffs: dict[str, tuple[Any, Any]],
    approve_critical: bool,
) -> dict[str, Any]:
    """Build the target frontmatter dict for an EXISTING file: lineage fields
    preserved verbatim, descriptive fields taken from the DB except critical
    fields that changed and aren't approved (those keep their old value/absence)."""
    new_fm: dict[str, Any] = {}
    for key in LINEAGE_FIELD_ORDER:
        if key in old_fm:
            new_fm[key] = old_fm[key]
    for key in DB_FIELD_ORDER:
        if key in diffs and key in CRITICAL_FIELDS and not approve_critical:
            if key in old_fm:
                new_fm[key] = old_fm[key]
            continue
        value = db_row.get(key)
        if value not in (None, "", []):
            new_fm[key] = value
    return new_fm


def build_new_doc_fm(doc_id: str, source_pdf: str, db_row: dict[str, Any], text_row: dict[str, Any]) -> dict[str, Any]:
    """Build frontmatter for a brand-new file (no prior on-disk state to
    preserve or gate against - point A: new docs are rare and purely
    additive, so no critical-field gating applies here)."""
    fm: dict[str, Any] = {
        "doc_id": doc_id,
        "source_pdf": source_pdf,
        "extraction_method": "postgres-full-text",
        "parse_backend": text_row.get("parse_backend"),
        "parse_model": text_row.get("parse_model"),
        "char_count": text_row.get("char_count"),
    }
    for key in DB_FIELD_ORDER:
        value = db_row.get(key)
        if value not in (None, "", []):
            fm[key] = value
    return fm


def resolve_source_pdf(doc_id: str, local_pdf_ids: dict[str, Path], s3_key: str | None) -> str:
    if doc_id in local_pdf_ids:
        return f"kp-docs/{local_pdf_ids[doc_id].name}/{doc_id}.pdf"
    return s3_key or f"documents/{doc_id}.pdf"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--host", default=DEFAULT_HOST, help="Postgres host")
    parser.add_argument("--port", type=int, default=5432, help="Postgres port")
    parser.add_argument("--db", default="qa", help="Postgres database name")
    parser.add_argument("--user", default="askwri", help="Postgres user")
    parser.add_argument("--sslmode", default="verify-full", help="libpq sslmode")
    parser.add_argument("--sslrootcert", type=Path, default=DEFAULT_SSLROOTCERT, help="Path to RDS CA bundle PEM")
    parser.add_argument("--pdf-dirs", type=Path, nargs="+", default=DEFAULT_PDF_DIRS,
                         help="Local CN/ES PDF directories, used to resolve source_pdf for new docs")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR, help="Where .md files live/are written")
    parser.add_argument("--update", action="store_true",
                         help="Actually write non-critical field/text changes (default: report only)")
    parser.add_argument("--approve-critical", action="store_true",
                         help="Also write critical field changes (external_id/language/languages/status). "
                              "Requires --update to take effect.")
    parser.add_argument("--refresh-text", action="store_true",
                         help="Additionally query document_texts (expensive): detect brand-new docs and "
                              "full_text drift on existing docs.")
    parser.add_argument("--min-chars", type=int, default=1000,
                         help="With --refresh-text, flag docs whose full_text is shorter than this many chars")
    args = parser.parse_args()

    conn_str = build_conn_str(args.host, args.port, args.db, args.user, args.sslmode, args.sslrootcert)

    print(f"Fetching document metadata from {args.user}@{args.host}:{args.port}/{args.db} ...")
    db_rows = fetch_rows(conn_str, METADATA_QUERY)
    docs_by_id = {r["external_id"]: prepare_db_row(r) for r in db_rows}
    print(f"  {len(docs_by_id)} rows in documents")

    print(f"Scanning local PDFs under: {[str(p) for p in args.pdf_dirs]} ...")
    local_pdf_ids = find_local_pdf_ids(args.pdf_dirs)
    print(f"  {len(local_pdf_ids)} local PDFs found")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    local_md_paths = {p.stem: p for p in args.output_dir.glob("*.md")}

    matched_ids = sorted(set(local_md_paths) & set(docs_by_id))
    orphaned_local = sorted(set(local_md_paths) - set(docs_by_id))
    new_in_db = sorted(set(docs_by_id) - set(local_md_paths))

    unchanged: list[str] = []
    metadata_written: list[str] = []
    metadata_pending: list[str] = []
    critical_pending: dict[str, dict[str, tuple[Any, Any]]] = {}

    for doc_id in matched_ids:
        path = local_md_paths[doc_id]
        old_fm, body, raw_text = parse_existing_markdown(path)
        db_row = docs_by_id[doc_id]
        diffs = diff_descriptive_fields(old_fm, db_row)
        if not diffs:
            unchanged.append(doc_id)
            continue

        new_fm = build_updated_fm(old_fm, db_row, diffs, args.approve_critical)
        new_content = render_full(new_fm, body)

        has_critical = any(k in CRITICAL_FIELDS for k in diffs)
        has_noncritical = any(k not in CRITICAL_FIELDS for k in diffs)

        if has_critical and not args.approve_critical:
            critical_pending[doc_id] = {k: v for k, v in diffs.items() if k in CRITICAL_FIELDS}

        if new_content == raw_text:
            # Everything that *could* change was critical and held back.
            unchanged.append(doc_id)
            continue

        if has_noncritical or (has_critical and args.approve_critical):
            if args.update:
                path.write_text(new_content, encoding="utf-8")
                metadata_written.append(doc_id)
            else:
                metadata_pending.append(doc_id)

    new_created: list[str] = []
    new_pending: list[str] = []
    text_written: list[str] = []
    text_pending: list[str] = []
    flagged_short: list[tuple[str, int]] = []

    if args.refresh_text:
        print(f"Fetching full_text from document_texts (parse_backend='mistral') ...")
        text_rows = fetch_rows(conn_str, TEXT_QUERY)
        text_by_id = {r["external_id"]: r for r in text_rows}
        print(f"  {len(text_by_id)} mistral-parsed rows in document_texts")

        for doc_id, text_row in sorted(text_by_id.items()):
            char_count = text_row.get("char_count") or 0
            if char_count < args.min_chars:
                flagged_short.append((doc_id, char_count))

            if doc_id in local_md_paths:
                path = local_md_paths[doc_id]
                old_fm, body, _ = parse_existing_markdown(path)
                new_body = f"{text_row.get('full_text') or ''}\n"
                if new_body == body:
                    continue
                # Re-derive frontmatter with fresh lineage fields (char_count etc.)
                # plus the same descriptive-field handling as the metadata pass.
                db_row = docs_by_id.get(doc_id, {})
                diffs = diff_descriptive_fields(old_fm, db_row)
                new_fm = build_updated_fm(old_fm, db_row, diffs, args.approve_critical)
                new_fm["char_count"] = text_row.get("char_count")
                new_fm["parse_backend"] = text_row.get("parse_backend")
                new_fm["parse_model"] = text_row.get("parse_model")
                new_content = render_full(new_fm, new_body)
                if args.update:
                    path.write_text(new_content, encoding="utf-8")
                    text_written.append(doc_id)
                else:
                    text_pending.append(doc_id)
            else:
                db_row = docs_by_id.get(doc_id, {})
                source_pdf = resolve_source_pdf(doc_id, local_pdf_ids, text_row.get("s3_key"))
                new_fm = build_new_doc_fm(doc_id, source_pdf, db_row, text_row)
                new_body = f"{text_row.get('full_text') or ''}\n"
                new_content = render_full(new_fm, new_body)
                if args.update:
                    (args.output_dir / f"{doc_id}.md").write_text(new_content, encoding="utf-8")
                    new_created.append(doc_id)
                else:
                    new_pending.append(doc_id)

    print()
    print("=== Metadata (documents + document_summaries) ===")
    print(f"  {len(unchanged)} unchanged")
    print(f"  {len(metadata_written)} written" if args.update else f"  {len(metadata_pending)} pending (rerun with --update to write)")
    if metadata_written:
        print(f"    written: {metadata_written}")
    if metadata_pending:
        print(f"    pending: {metadata_pending}")
    if critical_pending:
        print(f"  ! {len(critical_pending)} docs with CRITICAL field changes held back "
              f"(pass --update --approve-critical to apply):")
        for doc_id, fields in critical_pending.items():
            for field, (old, new) in fields.items():
                print(f"    - {doc_id}: {field}: {old!r} -> {new!r}")
    if orphaned_local:
        print(f"  ! {len(orphaned_local)} local .md files with no matching external_id in DB "
              f"(possibly renamed/removed - not touched):")
        for doc_id in orphaned_local:
            print(f"    - {doc_id}")
    if new_in_db and not args.refresh_text:
        print(f"  {len(new_in_db)} DB rows with no local .md yet (rerun with --refresh-text to fetch/create):")
        for doc_id in new_in_db:
            print(f"    - {doc_id}")

    if args.refresh_text:
        print()
        print("=== Full text (document_texts) ===")
        print(f"  {len(new_created)} new docs created" if args.update else f"  {len(new_pending)} new docs pending (rerun with --update to create)")
        if new_created:
            print(f"    created: {new_created}")
        if new_pending:
            print(f"    pending: {new_pending}")
        print(f"  {len(text_written)} existing docs with text updated" if args.update else f"  {len(text_pending)} existing docs with text-drift pending (rerun with --update to write)")
        if text_written:
            print(f"    written: {text_written}")
        if text_pending:
            print(f"    pending: {text_pending}")
        if flagged_short:
            print(f"  ! {len(flagged_short)} docs with full_text shorter than {args.min_chars} chars:")
            for doc_id, count in flagged_short:
                print(f"    - {doc_id}: {count} chars")


if __name__ == "__main__":
    main()
