# AskWRI Eval Review

This repository builds ground-truth evaluation datasets for AskWRI. It covers
two query modes:

- **Cite mode** retrieves the correct source documents for a question.
- **Answer mode** retrieves relevant passages and generates a correct answer.

The repository outputs JSON fixtures compatible with AskWRI's evaluation
harness. It does not run AskWRI or calculate evaluation scores.

Ground truth is created independently from AskWRI's retrieval system. Source
documents and identifiers may be read from AskWRI's Postgres database, but
AskWRI's retrieval and production embedding model must not be used to create or
expand expected results. Query expansion uses `qmd` with Qwen embeddings.

## Directory layout

- `kp-docs/` - the underlying corpus documents (PDFs plus generated
  markdown).
- `notebooks/` - marimo notebook(s) for human review of eval sets, e.g.
  `review_expected_docs-cite.py`, a `molabel`-based tool for confirming
  whether each `expected_document_ids` entry is actually a correct match.
  These are designed to also run online via [molab](https://molab.marimo.io)
  (including its WebAssembly preview) so external reviewers don't need a
  local Python setup -- see "Submitting notebook output to a filedrop you
  own" below for how reviews get collected back from those sessions.
- `review-output/` - saved output from the review notebook(s) above.
- `source_evalsets/` - the original ("generation 1") golden datasets:
  `cite-golden-dataset.json` and `answer-golden-dataset.json`. Read-only
  reference data, covering the original 169-document corpus.
- `evalsets/` - newer eval sets, built from the manual doc-review process
  described below (e.g. `evalset_cite_02.json`, `evalset_answer_02.json`).
  This is where newly generated eval sets will be added. Also includes:
  - `evalset_cite_01.json` - a schema-migrated copy of
    `source_evalsets/cite-golden-dataset.json` (v3.1), converted to the
    generation-2+ parallel-array schema. `expected_document_ids` (UUIDs)
    are left as empty-string placeholders pending a full-corpus
    reconciliation pass; the original `source_evalsets/` file is untouched.
  - `evalset_cite_02_bkup01.json` (v4.0) - the original 16 `fact_lookup`
    queries, frozen/unchanged, renamed from `evalset_cite_02.json` on
    2026-08-12 so that name could be reused for the
    `topic_discovery`/`geography_constrained`/`date_constrained` expansion
    (formerly `evalset_cite_03.json`, now `evalset_cite_02.json` v4.1+).
- `eval-generation-notes/` - working notes from manual document review,
  tracked in git for diffability. Includes:
  - `docreview_*.md` - human-authored notes per document reviewed (query +
    draft answer), the raw input to the eval-generation process below.
  - `documents-list-207_*.txt` - mapping between each document's UUID
    (`document_id`), stable slug (`external_id`), title, and language, for
    the full 207-document cross-lingual corpus (151 en, 15 es, 4 pt, 37 zh).
  - `issuelog_*.md` - known corpus issues (e.g. suspected duplicate/twin
    documents across languages) to check or validate later.

## Submitting notebook output to a filedrop you own

When a review notebook runs on [molab](https://molab.marimo.io) -- especially
its `/wasm` (WebAssembly/Pyodide) preview -- there is no durable, shared
filesystem to write output to. Local file writes (e.g. to `review-output/`)
either land in a real backend's disk (an "ephemeral server" molab preview --
fine, but not synced back to this repo or visible to anyone but that
reviewer) or in an in-browser, per-session virtual filesystem (the `/wasm`
preview -- lost on refresh, and never visible in molab's own file
explorer/storage sidebar, which only reflects real backend storage). Either
way, reviewers would otherwise have to manually download and send you their
output file.

The fix used in `review_expected_docs-cite.py`: the notebook POSTs each save
directly to a small Google Apps Script Web App, which writes the file into a
Drive folder you own and logs an index row (timestamp, filename, link) in a
Sheet. No reviewer-facing extra step, no server to run/maintain, and it works
identically whether the notebook is running locally, on an ephemeral molab
server, or fully client-side in `/wasm`.

**Setup (one-time, ~10 minutes):**

1. Create a Google Sheet (this becomes your submissions index) and note its
   default tab name, `Sheet1`.
2. Create a Drive folder for the actual output files; copy its folder ID out
   of the URL (`drive.google.com/drive/folders/<FOLDER_ID>`).
3. In the Sheet: **Extensions -> Apps Script**, replace the default code
   with:

   ```javascript
   const FOLDER_ID = "<your Drive folder ID>";

   function doPost(e) {
     const data = JSON.parse(e.postData.contents);
     const folder = DriveApp.getFolderById(FOLDER_ID);
     const file = folder.createFile(data.filename, data.content, "application/json");

     const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Sheet1");
     sheet.appendRow([new Date(), data.filename, file.getUrl()]);

     return ContentService.createTextOutput("ok");
   }
   ```

4. **Deploy -> New deployment -> Web app**. Execute as **Me**, who has
   access **Anyone**. Deploy, then authorize the OAuth consent prompt (click
   through the "unverified app" warning -- it's your own script asking your
   own account for permission to your own Drive/Sheet).
5. Copy the resulting `.../exec` URL. This is what the notebook POSTs to
   (see `SUBMIT_ENDPOINT_URL` near the top of `review_expected_docs-cite.py`)
   as `{"filename": ..., "content": <json-as-text>}`, using `httpx` so it
   works from both native Python and Pyodide/WASM.

**Security model (read before reusing this pattern):** the deployed URL is
**not a secret** in any meaningful sense -- it lives in a public notebook's
source, so treat it as security-through-obscurity only. The blast radius is
intentionally small: at worst, someone who finds the URL can write junk
files/rows into that one Drive folder/Sheet, nothing more (no read access to
other data, no access to this repo or any other Google resource). This is
appropriate for a short-lived, low-stakes review period. When a review round
ends, **delete or disable the Apps Script deployment** (Deploy -> Manage
deployments -> Archive) rather than leaving it open indefinitely, and create
a fresh deployment (new Sheet/Folder, or just a new script version) for the
next notebook/review round instead of reusing an old one.

To test a deployment directly (bypassing the notebook):

```bash
curl -L "<your deployed .../exec URL>" \
  -H "Content-Type: application/json" \
  -d '{"filename":"test.json","content":"{\"hello\":\"world\"}"}'
# -> ok
```

Note: use `-d` (not `-X POST`) with `-L`. Apps Script delivers the response
via a redirect that must be followed as a `GET` -- curl does this
automatically with `-d` alone, but `-X POST` forces POST through the whole
redirect chain, which this endpoint rejects with a 405.

## Eval-generation process (generation 2+)

Eval sets for the 207-document cross-lingual corpus are built as follows:

1. A human reviewer works through the corpus one document (or
   cross-lingual twin-pair) at a time, recording notes in
   `eval-generation-notes/docreview_*.md`:
   - The document's `document_id` (UUID) and `external_id` (slug).
   - A high-level English-language query whose expected answer is that
     document (queries are always written in English, regardless of the
     source document's language).
   - A draft answer to that query, as bullet points, based on the source
     document's content.
   - No chunk/passage-level excerpts are captured at this stage.
2. An LLM (Claude Sonnet 5) converts each doc-review entry into a matching
   pair of test cases - one in `evalsets/evalset_cite_NN.json` and one in
   `evalsets/evalset_answer_NN.json` - sharing the same `id` and
   `question`, so the two files stay 1:1 aligned per doc-review entry,
   **except** when a query has no drafted answer yet (Cite mode only
   requires the query + expected document(s), so such queries get a Cite
   entry with a `note` explaining the missing Answer-mode counterpart, and
   are added to `evalset_answer_NN.json` once a draft answer exists). This
   includes:
   - Resolving `external_id`/`document_id` for the source document, using
     `documents-list-207_*.txt`.
   - **Writing the `canonical_answer` and `key_facts` fields for Answer
     mode.** These are synthesized by the LLM from the reviewer's bullet
     notes (reformatted into prose / verbatim-ish bullets). **This content
     has not yet been human-reviewed or fact-checked against the source
     document**, and should be treated as a first draft pending review.
   - `difficulty` and `query_type` are partially LLM-inferred.
3. A human reviews the generated test cases (starting with the Cite-mode
   file, since it's simpler) and edits directly as needed - e.g. simplifying
   `description`/`note` fields - before moving on to review the Answer-mode
   file.
4. **Expand expected matches**. Use a generic retrieval system (such as `tobi/qmd`) to perform
   variations of these queries against the corpus. Use search results to
   expand the `expected_document_*` arrays in Cite mode eval sets.
   - This requires the corpus to be available in text/markdown.
   - Details to be added here.
5. **Expert review** using the marimo notebook.
   - Details to be added here.

### Schema notes (generation 2 vs. generation 1)

Relative to the `source_evalsets/*-golden-dataset.json` schema, the new
`evalsets/` files:

- Replace a single `expected_document_ids` list (of `external_id` strings)
  with **two parallel arrays**, `expected_external_ids` and
  `expected_document_ids` (now a list of UUIDs) - same index refers to the
  same document, so they can be used together or independently. 
- Add `source_document_id` and `source_language` - the UUID and language of
  the specific document the reviewer was reading when the query was
  drafted (useful for traceability).
- Keep the `task_description` field in **Cite mode** test cases (only),
  kept for consistency with generation 1's Cite schema but not populated. 
- Leave `expected_passages` empty in Answer mode test cases - chunk/passage
  -level ground truth is not captured during this round of doc review.

**Caveat:** `canonical_answer`/`key_facts` values in `evalsets/evalset_answer_*.json`
files are LLM-drafted (Claude Sonnet 5) from human notes, not
human-authored or human-verified. Treat them as provisional until reviewed.
