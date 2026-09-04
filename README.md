# AskWRI Eval Review


## Evalset Review Notebooks: 

Review Expected Documents (Cite Mode)
* Use this link to start your review using the notebook
* [![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/gofenris/askwri-eval-review/blob/main/notebooks/review_expected_docs-cite.py/wasm?show-code=false)

**Propose new query (Cite mode)**
* Use this link to propose a new query
* [![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/gofenris/askwri-eval-review/blob/main/notebooks/propose_query_cite.py/wasm?show-code=false)

**Review Expected Passages & Synthesized Answers (Answer mode)**
* Use this link to start your review using the notebook
* [![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/gofenris/askwri-eval-review/blob/main/notebooks/review-evalset-answer.py/wasm?show-code=false)

**Review System Output (Answer mode)**
* Use this link to label stored system output captures for judge calibration
* [![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/gofenris/askwri-eval-review/blob/main/notebooks/review-system-output-answer.py/wasm?show-code=false)


## Review workflow (Answer mode)

1. **Review the evalset** with `notebooks/review-evalset-answer.py` (first
   notebook above): per-passage, canonical-answer, and (on negative cases)
   negative-case-validity yes/no/skip labels. It saves `annot-*.json` files
   to `review-output/` and the shared Drive folder.
2. **Ingest the labels.** The maintainer runs
   `uv run scripts/ingest_review_status.py --evalset
   evalsets/evalset_answer_02.json --annot review-output/ [--dry-run]`, which
   writes `review_status` onto cases: all-yes cases become
   `expert_approved`; a `no` drops the passage from `expected_passages` and
   flags the affected facts in the case note; reviewer conflicts stay
   `draft`. ALWAYS pass the whole annot directory (ingestion is idempotent,
   but drops are irreversible and a partial directory can miss recorded
   no-votes).
3. **Judge calibration.** With `notebooks/review-system-output-answer.py`
   (second notebook above), label stored harness captures (upload
   `capture-<label>.json`), producing `labels-*.json` files consumed by the
   app repo's answer-eval harness via `run-score --labels`.

For adding English twin passages to a fact whose source passage is zh/es,
see [eval-generation-notes/twin-passages-workflow_20260904.md](eval-generation-notes/twin-passages-workflow_20260904.md).


## Overview 

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


## Details 

See [TECH_INFO.md](TECH_INFO.md)
