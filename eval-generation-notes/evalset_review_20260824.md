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
review, one reviewer rejected several of these documents from
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
lists (cite_01: q5, q7, q11; cite_02: d11, d12, d15). Added note in each
test case as follows: 

> Authorship reviewed 2026-09-04: Document included regardless of
> authorship affiliation.

### q1 doc removal (2026-09-04)

Removed `2020_acciones-federales-planeacion-urbana_0152` from
`evalset_cite_01` q1 (`q1_land_value_capture`) — SME review (Gorka)
determined land value capture is not the document's primary focus, only
cited as an illustrative example from other geographies. 6 -> 5 expected
docs.

### q3 additions (2026-09-04)

`evalset_cite_01` q3 (`q3_children_pollution`): kept
`2019_climate-emergency-urban-opportunity_4461` as expected (both
reviewers ultimately said yes, though Gorka flagged it as a weak/borderline
match -- minimal direct references to children/pollution).

Added 2 candidate docs Gorka surfaced during that same review as
comparably-thin-coverage precedents:
- `2023_ciencia-participativa-accion-para-un-aire-limpio_6722`
- `2026_fortaleciendo-sinergias-electromovilidad-calidad-aire_XXXX`

**NEEDS FURTHER SME REVIEW**: both added on Gorka's recommendation. May
require confirmation against this query's strict "primary focus"
requirement: `fortaleciendo-sinergias...`' summary describes it as an
internal WRI multi-office report with "school environments" appearing as
just one of several strategic lines of work -- "children and pollution"
isn't necessarily a primary focus. 

### d2 confirmation (2026-09-04)

`evalset_cite_02` d2 (`d2_dockless-bike-sharing-discovery`):
`2019_the-evolution-of-bike-sharing-10-questions-on-the_1977` : Both
reviewers had skipped it (broken PDF link). Reviewing extracted
text: includes a dedicated case study (Box 3, Beijing DBS
regulation) plus Hangzhou/Guangzhou public-bike-share coverage. 

Working URL/DOI for reviewer reference:
https://www.wri.org/research/evolution-bike-sharing 
https://doi.org/10.46830/wriwp.18.00035.

### q5 cleanup (2026-09-04)

`evalset_cite_01` q5 (`q5_micromobility`), 12 -> 8 expected docs. SME
review (Gorka) surfaced content mismatches within the "Mexico Frontrunners"
case-study series -- the evalset had swept in all 3 Mexico case studies,
but only 1 is actually about micromobility:

Removed:
- `2021_mexico-frontrunners-creating-safe-affordable-and_5127` -- actual
  topic is EcoCasa housing finance, not micromobility.
- `2021_mexico-frontrunners-adapting-to-climate-change-in_8904` -- actual
  topic is climate adaptation in mountain cities (Xalapa), not
  micromobility.
- `2025_seguridad-de-motociclistas-infraestructura-vias-urbanas_0030` /
  `2025_motorcycle-safety-and-urban-road-infrastructure_8478` -- per the
  NEEDS SME REVIEW flag already on this pair: motorcycles are generally
  excluded from micromobility definitions, and the content itself is
  road-safety/speed-management countermeasures, not micromobility
  implementation.

Kept:
- `2021_mexico-frontrunners-sustainable-mobility-for_2332` -- the correct
  Mexico Frontrunners case study (cycling schemes in Mexico City and
  Guadalajara).
- `2023_assessing-the-viability-of-using-autorickshaws_2146` -- SME
  approved (yes, no notes). Flagging for a second look regardless: its
  actual subject is autorickshaws for *urban freight delivery*, which this
  query's task_description explicitly excludes ("do not retrieve papers...
  about... freight"). Retained per SME judgment pending confirmation.

Re-added:
- `2024_enabling-the-shift-to-electric-auto-rickshaws-a_6804` -- previously
  dropped from this test case as "not in corpus"; confirmed back in the
  current corpus (`status: searchable`). Content is a guidebook for cities
  on electrifying auto-rickshaw fleets (policy, financing, charging
  infrastructure, case studies from Amritsar/Kochi/ Delhi) -- seems 
  a good fit for this query.
