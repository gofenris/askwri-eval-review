# AskWRI Eval Review


## Evalset Review Notebooks: 

Review Expected Documents (Cite Mode)
* Use this link to start your review using the notebook
* [![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/gofenris/askwri-eval-review/blob/main/notebooks/review_expected_docs-cite.py)

**Propose new query (Cite mode)**
* Use this link to propose a new query
* [![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/gofenris/askwri-eval-review/blob/main/notebooks/propose_query_cite.py)


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
