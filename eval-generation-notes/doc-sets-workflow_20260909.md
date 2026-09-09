# Doc sets (two-step-flow fixture) — workflow and conventions

**Date:** 2026-09-09
**Spec:** app repo `docs/superpowers/specs/2026-09-08-answer-eval-two-step-flow-design.md` (§3),
on `qa` since PR #399. **Harness:** PR #401 (merged on `qa`).

## What changed and why

Answer mode no longer searches the whole corpus: the user starts in cite mode,
(sub)selects documents, and answer mode retrieves only within those docs'
chunks. The evalset now models that selection explicitly: every case is asked
**against a doc set**, and the harness answers it the same way the product does
(`mode: 'answer'` + `cite_doc_ids`).

## The structure

- **`doc_sets`** (new top-level array, alongside `twins`): each entry is
  `{ "id", "doc_ids", "note" }`. A set is the basket of documents a question
  is asked against — the fixture's stand-in for a user's selection.
- Every test case carries **`doc_set_id`** referencing one set. Multiple
  questions share one set (the old clusters map 1:1).

The sets extracted from the existing clusters (v3.2):

| set | docs | cases |
|---|---|---|
| `zero-emission-trucks` | trucks study (zh) + its EN twin | q1–q4; negatives q17, q18 |
| `dockless-bike-sharing` | bikeshare report (zh) + its EN twin | q5–q7 |
| `yantian-port` | container-port study (zh) | q8–q10 |
| `mexico-covid-transport` | COVID transport impacts (es) | q11, q12 |
| `mexico-transport-finance` | financing mechanisms (es) | q13–q15 |
| `mexico-transport` | **union** of the two Mexico sets | q16; negative q19 |

**Why the union:** q16's `expected_external_ids` span both Mexico clusters —
its question is answerable from either document — so it must be asked against
a set containing both (the harness hard-errors when expected docs fall outside
the case's set).

**Why twins are in-set:** the translation twin of a set's source doc is part
of the same selection surface; retrieving either counts (same rationale as
the `twins` array and PR #2's twin passages).

**Negative cases:** a negative question is asked against a set that cannot
answer it. q17/q18 (off-domain) → the trucks set; q19 (near-domain, the Lagos
commute) → the Mexico union. Pass condition remains abstention — now under a
realistic horizon, the way a user would actually hit it.

## What the harness enforces (free validation before any paid call)

- Case `doc_set_id` must resolve; expected docs (+ twins) must be **⊆ the
  set** — a mis-scoped set is a load/capture error, not a silent mismeasure.
- Preflight's existence gate checks each expected passage's text against the
  served chunks of the docs it names (snippet-derived query, never the case
  question). Question-retrievability is **not** gated: it is recorded as
  `rank_gaps` — input for the variant-passage review below.

## Adding a new set (the repeatable recipe)

1. Pick the documents (source docs; include translation twins when the pair
   is in the corpus). Add the `doc_sets` entry with a note saying what it is.
2. Author Q/A pairs you know are good fits for that set — question, key
   facts, canonical answer, expected passages quote-first from the docs'
   served chunk text (resolve chunk ids as before; the text must exist in
   the corpus per the preflight existence gate).
3. Where the source repeats a passage with variant wording (e.g. the trucks
   ES-summary vs body variants), listing **both** occurrences as expected
   passages lets passage-grain coverage credit either — same rationale as
   twin passages. The capture run's `rank_gaps` report tells you which
   passages the question doesn't surface doc-scoped; those are the
   candidates for a second expected occurrence.
4. Expert review through the mode-1 notebook as usual; ingest folds the
   review back in.

## Reviewer notes for this PR

- The doc-set extraction and `doc_set_id` wiring is mechanical (derived from
  the existing clusters per the spec); the **judgment calls to veto or
  confirm** are: the negative-set assignments (q17/q18 → trucks, q19 → the
  Mexico union), and the union-set treatment of q16.
- Variant-occurrence expected passages (step 3 above) are deliberately NOT
  in this PR — they need your eyes on the `rank_gaps` list.
- The notebook change is one line: `review-system-output-answer.py` now
  accepts `answer-eval/capture@2` (the selection-bearing capture schema from
  PR #401) in addition to `@1`.
