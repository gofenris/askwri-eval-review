# 2026-08-24 — Expert review process log

This document logs the expert (SME) review process conducted roughly
2026-08-24 through 2026-09-15. Review was conducted using the notebooks in
`notebooks/`, with reviewer annotations captured in
`review-output/nb-evals-review-output/`.

## Scope

- **evalset_cite_01**
- **evalset_cite_02**
- **evalset_answer_02**
- Creation of new queries (none yet added as of this writing; may be
  incoming)

## Major decisions

### Authorship criterion (2026-09-04)

**Issue**: Several documents in the corpus are co-published under
WRI-affiliated series or coalitions (e.g., the Coalition for Urban
Transitions) but formally authored by a partner organization (University of
Leeds, LSE, OECD, African Centre for Cities, New Climate Economy). During
review, one reviewer (Gorka) rejected several of these documents from
expected-answer sets on the grounds that they weren't "written by WRI,"
across both Cite mode queries (cite_01 q5, q7, q11; cite_02 d11, d12, d15)
and, by extension, potentially Answer mode.

**Decision**: The system should not exclude documents from AskWRI responses
(Cite or Answer mode) on the basis that authorship doesn't explicitly state
or include WRI. The corpus itself is already curated to only include
documents WRI has published (gone through WRI's process, carries WRI
branding/logo, appears on WRI's site) — a document's presence in the corpus
already answers the "is this a WRI publication" question. Individual
queries should not re-litigate authorship. WRI staff do contribute to
external, non-WRI-branded publications, but those are not "WRI KPs" and are
not in the AskWRI corpus at all — so this distinction doesn't need to be
drawn within the eval sets.

**Effect**: All documents disputed or excluded on authorship grounds are
confirmed as correctly included in their respective `expected_document_ids`
lists (cite_01: q5, q7, q11; cite_02: d11, d12, d15) — no removals, no
additions. Per-test-case notes were added recording this decision;
see each affected test case's `note` field:

> Authorship reviewed 2026-09-04: Document included regardless of
> authorship affiliation.

### q1 doc removal (2026-09-04)

Removed `2020_acciones-federales-planeacion-urbana_0152` from
`evalset_cite_01` q1 (`q1_land_value_capture`) — SME review (Gorka)
determined land value capture is not the document's primary focus, only
cited as an illustrative example from other geographies. 6 -> 5 expected
docs.
