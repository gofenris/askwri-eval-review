# Twin-Passage Resolution Workflow — EN counterpart passages (2026-09-04)

Status: applied to clusters 1-2 (zero-emission trucks q1-q4, commit `bbca02e`;
bike-sharing q5-q7, commit `4b605dc`). This note records the process so future
clusters (or new fact additions) can repeat it without rediscovering the
decisions.

## Purpose

Per spec §2.1 / §8 item 1: a fact whose source passage is zh/es gets an
additional `expected_passages` entry pointing at the corresponding passage in
the document's English twin, so Answer-mode chunk-level scoring can credit
retrieval against the English edition too.

## Prerequisite: a confirmed twin

Only **confirmed** translation pairs count. The evalset's top-level `twins`
array (in `evalsets/evalset_answer_02.json`) lists the pairs relevant to this
evalset; it is derived from
`eval-generation-notes/documents-list_20260817.txt`'s
`translation_of`/`has_translations` entries, which mirror the DB's
`document_relations` where `relation_type='translation_of' AND
status='confirmed'`. Entries marked `rejected` in the documents list are not
twins and never get twin passages.

## Steps (per cluster, as actually executed)

1. **Locate the fact's passage in the twin's markdown.** For each fact of the
   cluster's test cases, find the passage in
   `kp-docs/markdown/<twin-external-id>.md` that states the fact. Use the
   zh/es passage's `text_snippet_translation_en` (on the source-doc entry) and
   the fact's `supports_key_fact` text as finding aids. Important: the twin is
   WRI's official English publication — its passage must be found in the
   twin's own English text. The `text_snippet_translation_en` field is only a
   finding aid for locating the passage; it is never the anchor source and
   never copied into the twin entry.
2. **Pick a 15-40 character anchor phrase from the REAL EN text** and verify
   its normalized occurrence count in the twin's markdown is exactly 1
   (same normalization as `scripts/lookup_chunk_id.py`'s `normalize()` —
   full/half-width folding, whitespace collapse). Never anchor on the
   translation field's wording unless it happens to match the twin's
   publication text verbatim.
3. **Batch-resolve via the lookup script.** Collect the anchors into a JSON
   file `[{"id": "<case_id>#fact<fact_index>", "external_id": "<twin-id>",
   "quote": "<anchor>"}]` and run its batch mode (see DB access below).
4. **Append the resolved chunk as another `expected_passages` entry**, using
   the twin's external_id as `doc_id`, `chunk_id`/`page` from the resolution,
   `text_snippet` = the returned `chunk_text` (byte-accurate DB text — never
   the anchor phrase), and `supports_key_fact` = the exact `key_facts` string
   (join with `" | "` only when one twin chunk backs several facts, same
   dedup rule as the main migration). **No `text_snippet_translation_en` on
   twin entries** — the passage is already English.
5. **Never fabricate.** A fact with no confident EN counterpart in the twin
   (low-confidence match, or the claim is simply absent — e.g. it exists only
   in the source edition's own framing) gets NO entry; flag it in the case's
   `note` with a `[twin-resolution YYYY-MM-DD]` line explaining what was
   skipped and why. Worked example: q7's "multi-win" fact has no EN
   counterpart (zh-edition framing) — skipped and flagged in `4b605dc`.

## DB access (two options, both verified working)

- **The script's own docstring way:** put `PGPASSWORD` in a local, gitignored
  `mise.local.toml` `[env]` block, RDS CA bundle at `../../global-bundle.pem`,
  run via `mise exec -- uv run scripts/lookup_chunk_id.py ...`.
- **From the app repo (what this PR's sessions actually used):**
  `scripts/with-remote-env.sh qa uv --directory evaluation/eval-review run
  scripts/lookup_chunk_id.py --input <quotes.json> --output <resolved.json>
  --sslmode require` — the wrapper reads the qa environment's ECS task
  definition for credentials and exports the libpq vars; `--sslmode require`
  avoids needing the CA bundle.

## Patching and committing

Patch the evalset via a one-off Python script
(`json.load` → append → `json.dump(..., ensure_ascii=False, indent=2)`),
never hand-edit — same reasoning as the main migration (long strings with
embedded non-ASCII text are error-prone to edit by hand). Diff before
committing to confirm untouched test cases are byte-identical. Commit per
cluster.
