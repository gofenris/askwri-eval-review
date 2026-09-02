# Answer-mode eval review notebook — planning (2026-09-02)

## Goal

Build a human-review notebook for `evalsets/evalset_answer_02.json`, the
Answer-mode counterpart to `notebooks/review_expected_docs-cite.py`. Only one
evalset exists today (16 test cases, 5 source-doc clusters — see
`eval-generation-notes/answer-eval-migration_20260831.md`), all with real
`retrieval_ground_truth.expected_passages` and quote-grounded
`synthesis_ground_truth.canonical_answer`/`key_facts`, still flagged
"pending AskWRI expert review" in the evalset's top-level `description`.
This notebook is how that expert review actually happens.

Scope is deliberately narrow: review UI + saved output only. Not covered
here: anything about how AskWRI's own retrieval/synthesis pipeline works,
scoring/harness code, or the chunk-lookup migration itself (already done).

## What's different from Cite mode (why this isn't a copy-paste)

| | Cite mode | Answer mode |
|---|---|---|
| Unit reviewed | whole documents (`expected_external_ids`) | **passages/chunks** (`expected_passages[]`) + a **synthesized answer** (`canonical_answer`/`key_facts`) |
| Source text for review | not embedded in evalset — notebook reads `kp-docs/markdown/<id>.md` frontmatter (title/summary/url) per document | **already embedded** in the evalset itself: each passage carries `text_snippet` (verbatim zh/es), `text_snippet_translation_en`, and `supports_key_fact` |
| "Suggest more" affordance | `DocumentPicker` widget lets reviewer add missing expected documents directly | **not feasible the same way** — adding a passage requires resolving a real `chunk_id` via `scripts/lookup_chunk_id.py` against Postgres, which this read-only review notebook doesn't have DB access to run. Out of scope for v1 (see below). |
| Number of reviewable items per query | N documents (flat list) | N passages (list, like Cite) **plus** 1 synthesized answer (a single item, structurally different) |

Practical implication: passage review can reuse the Cite notebook's
`molabel` `SimpleLabel` pattern almost as-is (a list of items, yes/no/skip
per item). Synthesis review cannot — there's exactly one `canonical_answer`
per query, not a list, so it needs a different (simpler) widget.
`key_facts` review is explicitly deferred per your note, so the synthesis
step only judges the `canonical_answer` as a whole.

## Proposed notebook

One combined notebook: **`notebooks/review-evalset-answer.py`**, per your
preferred workflow (select evalset -> select query -> review passages ->
review synthesized answer -> save), rather than splitting into
`review_expected_passages-answer.py` + `review_synthesis-answer.py`. Open
question below on whether to actually split it once built, if the combined
page feels overloaded.

### Reused as-is from `review_expected_docs-cite.py`

- Boilerplate: script header/deps, `REPO_ROOT`/`EVALSET_DIR`/`REVIEW_OUTPUT_DIR`
  constants, reviewer-name input.
- `submit_to_review_dashboard()` + `SUBMIT_ENDPOINT_URL` POST-to-Drive/Sheet
  pattern (see open question below on reusing the same deployment vs. a
  separate one).
- Evalset dropdown pattern (filtered to `"answer"` in filename instead of
  `"cite"` — trivial swap; still only one match today).
- Query dropdown + selected-query info panel (question/id/query_type/difficulty/note).
- `molabel` `SimpleLabel` + `render=...` card pattern for the passage-review
  step (list of items, yes/no/skip, notes, timestamp).
- Save button + saved-JSON-to-`REVIEW_OUTPUT_DIR` + dashboard-submit cell
  shape.
- Progress checklist grid (chip per query, ✅ once reviewed) — redefine
  "done" for Answer mode (see open question below).
- Unsaved-switch warning (`dirty_query_ids` / `last_selected_query_id_box`)
  pattern, extended to cover both passage and synthesis edits.

### New pieces needed

1. **Evalset loading**: same `json.load` + `test_cases` as Cite, but each
   test case's reviewable content comes from
   `tc["retrieval_ground_truth"]["expected_passages"]` and
   `tc["synthesis_ground_truth"]` instead of `tc["expected_external_ids"]`.
   No `kp-docs/markdown/` or `documents-list_*.txt` reads needed for the
   core review flow, since passage text/translation is already inline in
   the JSON (simpler than Cite mode here).
2. **Passage-review card**: new `render_molabel_card`-equivalent showing,
   per passage: `doc_id`, `page`, native-language `text_snippet` (zh/es,
   rendered so CJK/Spanish text is legible), `text_snippet_translation_en`,
   and the `supports_key_fact` it's meant to back — with the review
   question "Does this passage actually support the stated key fact?"
   (yes/no/skip, same as Cite's "is this document a correct match?").
3. **Synthesis-review widget**: a small new component (not `molabel`,
   since there's one item, not a list) showing the full
   `canonical_answer` plus the list of `key_facts` for context (read-only,
   not individually labeled — per your note to leave key_facts out for
   now), with a simple approve/needs-work control:
   - Recommended: `mo.ui.radio(["good", "needs_edit", "skip"])` + an
     optional `mo.ui.text_area` for reviewer notes (e.g. what's wrong, a
     suggested rewording). Simpler and more appropriate than trying to
     force this into the same drag/click `molabel` card UI, which is
     designed for streams of same-shaped items.
   - Open question below on exact control shape.
4. **Output schema** for saved review JSON — proposed, mirroring Cite's
   shape but with an added `synthesis_review` section:
   ```json
   {
     "query_id": "q1_zero-emission-heavy-duty-trucks",
     "question": "...",
     "reviewer": "...",
     "reviewed_passages": [
       {"chunk_id": "...", "doc_id": "...", "label": "yes|no|skip", "notes": "", "timestamp": "..."}
     ],
     "synthesis_review": {
       "label": "good|needs_edit|skip",
       "notes": "",
       "timestamp": "..."
     }
   }
   ```
   Filename: `annot-{EVALSET_NAME}-{query_id}-by-{reviewer}.json`, same
   convention as Cite.
5. **Progress checklist semantics**: needs a new definition of "done" per
   query now that there are two independent sub-tasks (passages, synthesis)
   instead of one. Simplest: chip turns green only once *both* have been
   saved at least once for that query; alternative is two small indicators
   per chip. Open question below.

### Explicitly out of scope for v1

- Reviewing/labeling individual `key_facts` (per your instruction).
- Suggesting *new* passages or documents (no DB access from this notebook;
  the real fix — running `scripts/lookup_chunk_id.py` — is a maintainer
  task outside this review flow, same as it was for building the evalset
  in the first place).
- Any changes to the askwri retrieval/synthesis system itself — this is
  purely reviewing the static evalset file.
- Editing `evalsets/evalset_answer_02.json` in place — like Cite mode, all
  review output is a side-channel JSON file in `review-output/` (+ dashboard
  submit), never a direct edit to the evalset.

## Decisions (2026-09-02)

1. **Combined notebook**: `notebooks/review-evalset-answer.py`. Can split
   into `review_expected_passages-answer.py` / `review_synthesis-answer.py`
   later if the combined page gets unwieldy — not expected at 16 test cases.
2. **Synthesis-review control**: reuse `molabel`'s `SimpleLabel` widget as-is
   (same yes/no/skip + notes UI as passage review), fed a single-item list
   (the `canonical_answer`, with `key_facts` shown read-only in the card for
   context). No custom radio/text-area control, no "suggested replacement
   answer" field.
3. **Submission endpoint**: reuse the existing `SUBMIT_ENDPOINT_URL` /
   Apps Script / Drive-folder / Sheet deployment from Cite mode as-is.
   Distinguished only by filename prefix
   (`annot-evalset_answer_02-...-by-...json`) in the shared Sheet/folder.
4. **Progress checklist "done"**: a query's chip is ✅ only once **both**
   the passage-review save and the synthesis-review save have happened for
   that query at least once in the session.
5. **No source-doc link** for v1 — review passages using only the inline
   `text_snippet` / `text_snippet_translation_en` already in the evalset
   JSON. No `documents-list_*.txt` lookup.

## Suggested build order (once questions above are resolved)

1. Scaffold `notebooks/review-evalset-answer.py` from
   `review_expected_docs-cite.py`'s boilerplate (deps header, constants,
   submit helper, reviewer-name input, evalset/query dropdowns filtered to
   `"answer"`).
2. Wire up passage-review step (molabel `SimpleLabel` + new render card for
   `expected_passages`).
3. Wire up synthesis-review step (new lightweight widget/controls for
   `canonical_answer` + read-only `key_facts` display).
4. Wire up combined save (one button, one payload with both
   `reviewed_passages` and `synthesis_review`) + dashboard submit + local
   write to `review-output/`.
5. Progress checklist + unsaved-changes warning, adapted per question 4
   above.
6. Manual smoke-test locally (`uvx marimo run/edit`) and, if used for
   external reviewers, on molab/WASM the same way Cite mode is.
