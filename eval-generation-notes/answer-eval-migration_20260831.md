# Answer Mode Eval Migration — Quote-First Passage Ground Truth (2026-08-31)

Status: planning complete, execution not yet started.

## Goal

Populate `evalsets/evalset_answer_02.json`'s `retrieval_ground_truth.expected_passages`
(currently empty in all 16 test cases) with real, chunk-level ground truth, and
replace the current LLM-paraphrased `synthesis_ground_truth` (`canonical_answer`/
`key_facts`) with versions grounded in verbatim quotes from the source documents.
This session's output is also the reusable *methodology* for a future pass that
creates entirely new Answer-mode test cases.

This is "Option C" from the 2026-08-31 planning discussion: keep the 16 existing
questions and their already-correct doc-level ground truth; regenerate only the
per-test-case content that requires reading the source document.

## Decisions locked in

- Keep unchanged: `id`, `question`, `query_type`, `difficulty`,
  `expected_external_ids`, `expected_document_ids` (see below), `source_document_id`,
  `source_language`.
- `expected_document_ids`: keep the field in the schema, but its contents become
  empty arrays going forward — neither harness that consumes this repo's fixtures
  (`run-evalset.ts` for doc-level `eval:qa`, nor `lib/types.ts`'s `ExpectedPassage`/
  `expected_doc_ids` for chunk-level eval) reads Postgres document UUIDs; both key
  on `external_id` strings only. (The UUIDs currently present are also stale
  relative to the 2026-08-17 corpus refresh — moot once dropped.)
- Regenerate `synthesis_ground_truth` (`canonical_answer`, `key_facts`) **quote-first**:
  every fact must trace to an actual verbatim sentence/passage in the source
  document (in its original language — zh or es), not a paraphrase of reviewer
  notes. This absorbs the fact-check step that was previously deferred as
  out-of-scope — that's an intentional, acknowledged scope change from earlier
  in the discussion.
- No separate quotation-storage field. `retrieval_ground_truth.expected_passages[]`
  carries the verbatim evidence directly. Each entry:

  ```json
  {
    "doc_id": "2025_zero-emission-heavy-duty-trucks_00015",
    "chunk_id": "<resolved via lookup script>",
    "page": 12,
    "text_snippet": "<verbatim, untranslated quote/chunk text, zh or es>",
    "text_snippet_translation_en": "<English translation, for reviewers who don't read zh/es>",
    "supports_key_fact": "<verbatim copy of the key_facts entry this backs>"
  }
  ```

  Rejected an earlier idea of a separate `synthesis_ground_truth.source_quotations`
  array — it would have duplicated the verbatim quote text in two places (risk of
  drift). `text_snippet` already is the verbatim-quote field per
  `lib/types.ts`'s `ExpectedPassage`; `text_snippet_translation_en` and
  `supports_key_fact` are the only genuinely new pieces of information needed,
  so they're added directly onto the existing structure instead.
  This is purely additive and harmless to the actual consumer
  (`run-evalset.ts` passes through arbitrary fixture keys verbatim and does not
  validate against `lib/types.ts`'s stricter interface — that interface belongs
  to a different harness that reads a different file entirely, see "Two
  harnesses" below).
- Passages come only from the actually-reviewed `source_document_id`'s doc, not
  its cross-lingual twin (e.g. q1-q4's twin `2025_charging-toward-2035-...` stays
  in `expected_external_ids` for doc-level scoring, but is not read for quote
  extraction).
- Edge case: a quote extracted for a key_fact that can't be confidently resolved
  to a `chunk_id` (low overlap score, awkward chunk-boundary split) is not given
  a fabricated/low-confidence `expected_passages` entry. Instead, flag it in that
  test case's `note` field for manual follow-up. Expected to be rare, since
  quotes are only extracted from documents we already know contain them.
- I (the assistant) draft all quotes/facts/translations directly from the zh/es
  source markdown already in `kp-docs/markdown/`; the user does not read zh/es
  and will not review this content directly — sign-off comes from AskWRI's
  expert review team downstream, not this session. Treat all regenerated
  content as provisional pending that expert review — update the `note` field
  per test case accordingly, replacing the current "LLM-drafted from reviewer's
  notes, not yet reviewed" caveat with something reflecting the new
  quote-grounded-but-still-pending-expert-review status.
- Versioning: bump `evalset_answer_02.json`'s top-level `version`/`updated` ONCE,
  after all 5 clusters are done — not per-cluster.
- Validation of the chunk-lookup script does NOT use
  `source_evalsets/answer-golden-dataset.json` — its chunk_ids are stale (corpus
  re-ingested since gen-1). Instead: (a) trivial identity test — feed the script
  a chunk's own `text` from a live `document_chunks` row and confirm it
  round-trips to that same `chunk_id`; (b) real first trial on the smallest
  cluster (bike-sharing, ~17K chars) before running on the two large docs.

## Two harnesses (context for why this schema works)

- `npm run eval:qa` (`run-evalset.ts`, askwri repo) reads this repo's
  `evalsets/*.json` via a git submodule and scores doc-level retrieval only,
  keyed on `expected_external_ids`. It already runs successfully against
  `evalset_answer_02.json` as-is (baseline MAP ~0.78 across several tracked
  runs) and ignores `expected_document_ids`, `expected_passages`, and
  `synthesis_ground_truth` entirely. Nothing in this migration is required for
  that harness to keep working — it's additive groundwork for future
  chunk-level scoring.
- `npm run eval:answer-retrieval` / `eval:answer-synthesis` (askwri repo) read a
  *separate* local file, `evaluation/answer-golden-dataset.json` (9 test cases),
  generated via a different, circular pipeline (queries AskWRI's own production
  hybrid retrieval, then LLM-labels the results — flagged as a real limitation
  in that repo's own README). This migration does not touch that file or that
  pipeline; it's establishing an independent, non-circular alternative sourced
  from this repo's own manually-reviewed corpus instead.

## Document / cluster mapping (5 source documents, 16 test cases)

| Cluster | Source doc (`external_id`, lang)                                         | Test cases   | Size (chars) | Est. chunks |
| ------- | ---------------------------------------------------------------------- | ------------ | ------------ | ----------- |
| 1       | `2025_zero-emission-heavy-duty-trucks_00015` (zh)                        | q1-q4        | 255,135      | ~800        |
| 2       | `2020_dockless-bike-sharing_00124` (zh)                                  | q5-q7        | 16,818       | ~52         |
| 3       | `2024_optimizing-container-ports-transportation-and_9894` (zh)           | q8-q10       | 203,150      | ~635        |
| 4       | `2022_impactos-economicos-pandemia-covid19-transporte-publico_0070` (es) | q11-q12, q16 | 106,619      | ~330        |
| 5       | `2023_analisis-de-los-mecanismos-financieros-para-la_3765` (es)          | q13-q15, q16 | 90,473       | ~282        |

`q16` spans clusters 4 and 5 — handle it during whichever of those two sessions
finishes second (needs quotes from both docs).

Twin documents (`2025_charging-toward-2035-...`, `2020_how-dockless-bike-sharing-...`)
are NOT read for quote extraction — they stay in `expected_external_ids` for
doc-level retrieval scoring only.

## Chunk-lookup script

Non-circular by construction: it never queries the live hybrid search service or
any embedding model. Given `(external_id, quote_text)`, it should:

1. Connect to Postgres directly, following the connection pattern already used
   by `scripts/db_text_to_markdown_askwri-qa.py` (`mise exec -- uv run ...`,
   `PGPASSWORD` from `mise.local.toml`, RDS CA bundle at `../global-bundle.pem`).
2. Query `document_chunks` joined to `documents` filtered by `external_id`,
   ordered by `chunk_index`.
3. Match `quote_text` against each chunk's `text` via substring containment
   first, falling back to word-overlap/Jaccard scoring for near-verbatim
   matches (port the scoring approach from
   `evaluation/map-passages-to-chunks.ts`'s `textOverlapScore`, but applied only
   within one document's own chunks — never via the live retrieval/embedding
   service).
4. Return `legacy_chunk_id` (→ `chunk_id`), `page`, match method, and overlap
   score; flag low-confidence matches (e.g. score below ~0.5) rather than
   silently accepting them.

Suggested location: `scripts/lookup_chunk_id.py`.

## Session plan

**Session 0 (tooling):**
1. Write the chunk-lookup script per spec above.
2. Validate per "Validation" above (identity test + bike-sharing trial run).

**Sessions 1-5 (one per cluster, one commit each):**
For each cluster's source document:
1. Delegate a subagent (Task tool) to read the full source markdown +
   the relevant slice of `eval-generation-notes/docreview_20260807.md` +
   that cluster's current `key_facts`, and return ONLY a compact structured
   result: candidate verbatim quotes (source language), English translations,
   and which existing/revised fact each supports. (Keeps the orchestrating
   session's context small regardless of document size — critical for
   clusters 1 and 3, ~200-255K chars each.)
2. Review the subagent's output, finalize `canonical_answer`/`key_facts` and
   the quote/translation/supports_key_fact triples for that cluster's test
   cases.
3. Run the chunk-lookup script for each `(external_id, quote)` pair to
   populate `expected_passages`.
4. Update `evalsets/evalset_answer_02.json` for that cluster's test cases only
   (leave others untouched); update each test case's `note` field.
5. Commit (mirroring the existing per-doc-review-batch commit granularity:
   `95d8d52`, `a2d8705`, `cbd70e0`, `4688c9c`, `bcaa892`).

**Final step (after all 5 clusters):** bump `version`/`updated` at the top of
`evalset_answer_02.json`, one commit.

## Resuming after an interrupted session

No separate progress tracking needed — resumability is visible directly in
`evalsets/evalset_answer_02.json`: any test case whose `expected_passages` is
still `[]` and whose `note` still reads the old "LLM-drafted, not yet reviewed"
caveat has not been migrated yet. Pick up at the next un-migrated cluster.
</content>
