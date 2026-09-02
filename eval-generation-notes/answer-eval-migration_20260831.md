# Answer Mode Eval Migration — Quote-First Passage Ground Truth (2026-08-31)

Status: Sessions 0-5 all complete (all 5 clusters, q1-q16). Remaining:
the "Final step" (top-level `version`/`updated` bump) — not yet done, see
bottom of "Session plan".

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

| Cluster | Source doc (`external_id`, lang)                                         | Test cases   | Size (chars) | Est. chunks | Status |
| ------- | ---------------------------------------------------------------------- | ------------ | ------------ | ----------- | ------ |
| 1       | `2025_zero-emission-heavy-duty-trucks_00015` (zh)                        | q1-q4        | 255,135      | ~800        | ✅ done (commit `adf8b00`) |
| 2       | `2020_dockless-bike-sharing_00124` (zh)                                  | q5-q7        | 16,818       | ~52         | ✅ done (commit `357dc81`) |
| 3       | `2024_optimizing-container-ports-transportation-and_9894` (zh)           | q8-q10       | 203,150      | ~635        | ✅ done (commit `a1ac2e0`) |
| 4       | `2022_impactos-economicos-pandemia-covid19-transporte-publico_0070` (es) | q11-q12, q16 | 106,619      | ~330        | ✅ done (commit `3366abe`) |
| 5       | `2023_analisis-de-los-mecanismos-financieros-para-la_3765` (es)          | q13-q15, q16 | 90,473       | ~282        | ✅ done (commit `94dd3a9`) |

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

**Session 0 (tooling) — DONE.** Wrote `scripts/lookup_chunk_id.py` per spec
above. Validated via identity round-trip self-test
(`--self-test 2020_dockless-bike-sharing_00124`) and two real quotes from the
bike-sharing doc, both resolving exactly. Committed in `e9bc67c` together with
this plan doc and the Postgres schema reference notes.

**Session 1 (cluster 1: zero-emission trucks, q1-q4) — DONE.** Committed in
`adf8b00`. All 4 test cases now have real `expected_passages` (13 total
lookups, all exact matches, zero low-confidence) and quote-grounded
`key_facts`/`canonical_answer`. Caught and corrected two real errors in the
prior LLM-paraphrased `key_facts` in the process (see commit message for
detail) — concrete evidence the quote-first approach is worth the extra
effort, not just a formality.

Also hardened `scripts/lookup_chunk_id.py`'s `normalize()` during this
session against two real OCR artifacts found in the trucks document (see
"Refined workflow" below) — this hardening is generic and already applies to
all future clusters, no further action needed for it specifically.

**Session 2 (cluster 2: bike-sharing, q5-q7) — DONE.** Committed in
`357dc81`. All 3 test cases now have real `expected_passages` (10 lookups,
all exact matches, zero low-confidence — this doc has none of the OCR
punctuation quirks the trucks document had). Caught one real imprecision in
q7's `key_facts`/`canonical_answer` (an unsupported "changing the broader
urban mobility ecosystem" clause tacked onto the source's actual "多赢
方案"/"multi-win" framing) and corrected it. Also exercised the
`expected_passages` dedup rule for the first time: q6's 3 facts and 3 of
q7's 4 facts each collapse onto one shared chunk, merged via `" | "` per
the "Refined workflow" step 9 below.

**Session 3 (cluster 3: container ports, q8-q10) — DONE.** Committed in
`a1ac2e0`. All 3 test cases now have real `expected_passages` (25 lookups
across 7/12/6 passages for q8/q9/q10 — this cluster's facts are denser and
more granular than q1-q7's, hence more passages per question). 26/29 quotes
matched exactly; the 3 n-gram fallbacks were all genuine artifacts in the
`document_chunks` text itself (an OCR "水中中转"/"水水中转" typo, and two
chunk-internal line breaks landing mid-word) rather than transcription
errors, and all resolved unambiguously. Caught two real errors carried over
from the prior LLM-drafted facts: (1) a fabricated railway name
("Yantian-Pinghunan railway") that doesn't match either of the two real
railways the source discusses (平盐铁路 Ping-Yan, retrofitted; 平南铁路
Pingnan, demolished) — fixed across q8/q9; (2) an imprecise "2035 BAU
baseline of 392" figure in q10 that only existed as jumbled numeric labels
inside a chart's OCR'd text (this doc's extraction_method is
cache-plaintext, which drops chart structure) — reworded to keep only the
figures confirmed in clean prose. This is this document's second
same-source-passage collision worth noting for future reference: unlike
clusters 1-2 where OCR punctuation/spacing was the main hazard, this
document's `document_chunks` text itself has a few uncorrected
typos/line-break artifacts baked in from ingestion — the n-gram fallback
handled them correctly, so no special handling was needed beyond trusting
`low_confidence=false` results even when `match_method` isn't `exact`.

**Session 4 (cluster 4: Mexico COVID transport impacts, q11-q12, q16) — DONE.**
Committed in `3366abe`. All 3 test cases now have real `expected_passages`
(19 lookups across 8/5/6 passages for q11/q12/q16 - all exact matches, zero
low-confidence). q16's `expected_external_ids` lists both this cluster's doc
and cluster 5's financing doc (per the original docreview notes), but all of
its key_facts trace only to this document, so it was handled here rather
than in cluster 5 (both done in the same session anyway). Caught one real
imprecision in q11's key_facts (the "supply falls in the same proportion as
demand" assumption is scoped to the whole data-scarce bus/ECI segment in the
source, not to the ECI model alone as the prior draft implied) - corrected.
q12 and q16's facts were all already accurate. Also flagged (not corrected)
a genuine internal inconsistency in the source document itself: prose states
trains' worst-case pandemic demand drop was "up to 28 percent" while the
document's own Tabla 2 shows trains falling to 33% of prior demand (a 67%
drop) for the same period - the two figures likely describe different
scopes (single system vs. pooled average across 5 train systems) but the
document doesn't reconcile them, and no current key_fact depends on either
number being "the" figure. Exercised the `expected_passages` dedup rule
again: q12's chunk_9 and two of q16's chunks each collapse two distinct
facts onto one chunk, merged via `" | "`.

**Session 5 (cluster 5: Mexico transport financing mechanisms, q13-q15) —
DONE.** Committed in `94dd3a9`. All 3 test cases now have real
`expected_passages` (25 lookups across 7/5/6 passages for q13/q14/q15 - all
exact matches, zero low-confidence). Unlike every prior cluster, no factual
errors were found in the existing key_facts here - all 14 checked out
verbatim against the source, only minor rewording for precision. Surfaced
this migration's first genuine *chunk-resolution* gap (distinct from a
low-confidence match): q14's key_facts[4] (2020 carbon-tax rates by fuel
type) is verbatim-confirmable in `kp-docs/markdown/...` (the fuel-to-rate
pairing required reconstructing via the source's own MXN/USD 20.12
exchange-rate footnote, since the OCR'd table separates the fuel-name and
numeric columns), but the corresponding `document_chunks` row renders that
same table as an unindexed image (`img-5.jpeg`) rather than extracted text -
no chunk in the live production DB contains these figures as text at all.
Per the "Edge case" rule above, no `expected_passages` entry was fabricated
for this fact; it's flagged in the test case's `note` for manual follow-up
instead, while the fact itself is kept (it's still accurate per the source
document). This is a different failure mode than cluster 3's OCR-mangled
chart numbers: there the number existed as garbled chart-axis text; here
the production chunk has no text for the table at all.

**Final step (after all 5 clusters):** bump `version`/`updated` at the top of
`evalset_answer_02.json`, one commit.

## Refined workflow (per cluster, learned executing Session 1)

The original plan assumed a subagent's "verbatim quote" could be trusted
as-is and fed straight into the lookup script. In practice, on real OCR'd zh
text, roughly 2 of every 13 subagent-provided quotes did NOT match the source
document exactly on the first try — not because the subagent misread the
document, but because it silently normalized punctuation while transcribing
(e.g. writing "，" where the OCR'd source actually has a bare "," in that
spot, or adding/dropping a space next to a comma). The actual words were
never wrong; only incidental formatting drifted. Do not skip the verification
step below because of this.

1. **Delegate a subagent** (Task tool, `general` type) to read the full source
   markdown (`kp-docs/markdown/<external_id>.md`) + the relevant slice of
   `eval-generation-notes/docreview_20260807.md` + that cluster's current
   `key_facts`, and return a compact structured result per question: a
   revised `canonical_answer`, and per `key_facts` bullet, a verbatim
   source-language quote + English translation + notes on any revision (or a
   flag if the existing fact looks wrong/unsupported — this is genuinely
   useful, it caught 2 real errors in cluster 1). Keep this in the prompt
   explicitly: it should flag suspected errors rather than force-fitting a
   quote to an existing fact. Instruct it to return ONLY this structured
   result, not large document excerpts, to keep the response compact.
2. **Do not trust the subagent's quote strings as byte-exact.** Independently
   verify every quote against the actual `kp-docs/markdown/<external_id>.md`
   file, using punctuation/whitespace-normalized containment (exactly what
   `lookup_chunk_id.py`'s `normalize()` does - full-width/half-width
   punctuation folding, whitespace-around-punctuation folding). A quick way:
   load the file, normalize it once, and check `normalize(quote) in
   normalized_full_text` for every quote before touching the DB at all.
3. **For quotes that fail verification:** don't try to fix the subagent's
   transcription by hand-editing punctuation — instead, `grep` for a shorter,
   distinctive fragment of the quote to find its real location in the file,
   then pick a new anchor phrase (see next point) directly from the real
   text at that location.
4. **Prefer short (roughly 15-40 character), unique anchor phrases over
   full-paragraph quotes** for the actual DB lookup. Check each anchor's
   occurrence count in the normalized full document text is exactly 1 before
   using it (ambiguous anchors risk silently matching the wrong passage in a
   ~250K-char document). Short anchors also sidestep embedded noise that
   breaks exact matching on longer spans - footnote markers
   (`$^{2}$`, superscript digits), markdown table pipes, image reference
   lines - none of which need to be reproduced perfectly since:
5. **The final stored `text_snippet` is the chunk's actual DB text, not the
   search anchor.** Once `scripts/lookup_chunk_id.py` finds the right chunk,
   use its returned `chunk_text` field (byte-accurate from `document_chunks`)
   as `text_snippet` - never the hand-typed anchor/quote. This is why steps
   2-4 only need to find the *right chunk*, not reproduce it perfectly.
6. **Split any multi-sentence "quote" that spans non-adjacent parts of the
   document** (a subagent will sometimes join two supporting sentences with
   "...") into separate atomic anchors before verification/lookup - exact
   substring matching requires contiguity, so a joined quote will never match
   as one unit even if both halves independently exist verbatim.
7. **Run the lookup script in batch mode** (`--input`/`--output`, one entry
   per `(test_case_id, fact_index, external_id, quote)`) once all anchors are
   verified, rather than one-off `--external-id`/`--quote` calls - it's one
   DB round-trip per unique `external_id` (cached), and surfaces every
   low-confidence flag together for review before writing anything.
8. **Translate the actual resolved `chunk_text`**, not just the short anchor
   - the chunk is usually longer than the anchor phrase (it's a fixed
   ~400-char window), and `text_snippet_translation_en` should cover what's
   actually stored, not just the fragment that was searched for.
9. **Deduplicate `expected_passages` by `chunk_id` within a test case.**
   Adjacent key_facts often resolve to the same or an adjacent chunk (e.g.
   two facts drawn from consecutive sentences in one paragraph); merge their
   `supports_key_fact` strings with `" | "` rather than adding two entries
   for the same chunk - this matters for any future chunk-level
   precision/recall scoring, where a duplicated expected chunk would
   artificially double-count.
10. **Patch `evalsets/evalset_answer_02.json` via a small one-off Python
    script**, not the Edit tool - the content includes long strings with
    embedded zh/es text, quotation marks, and em-dashes that are error-prone
    to hand-edit reliably. Load the file with `json.load`, replace only the
    target cluster's test cases' `synthesis_ground_truth` and
    `retrieval_ground_truth` fields plus `note`, `json.dump(...,
    ensure_ascii=False, indent=2)` to match the file's existing style, and
    diff the result before committing to confirm untouched test cases are
    byte-identical.
11. **Commit per cluster** (mirroring the existing per-doc-review-batch
    commit granularity: `95d8d52`, `a2d8705`, `cbd70e0`, `4688c9c`,
    `bcaa892`), including in the commit message any errors the quote-first
    process caught in the previous `key_facts` - that's the concrete
    evidence of this migration's value, worth preserving in history.

## Resuming after an interrupted session

No separate progress tracking needed — resumability is visible directly in
`evalsets/evalset_answer_02.json`: any test case whose `expected_passages` is
still `[]` and whose `note` still reads the old "LLM-drafted, not yet reviewed"
caveat has not been migrated yet. Pick up at the next un-migrated cluster.
</content>
