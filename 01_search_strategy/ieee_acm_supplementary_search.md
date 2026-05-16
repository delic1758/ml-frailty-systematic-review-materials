# IEEE Xplore and ACM Digital Library — Supplementary Search

**Databases:** IEEE Xplore Digital Library; ACM Digital Library
**Search type:** Supplementary search added in response to peer-review feedback
**Search execution date:** May 12, 2026

---

## Background

Reviewer 4 requested the inclusion of references from IEEE Xplore and ACM
Digital Library — two databases that index computer-science journals,
conference proceedings, and workshops. In response, supplementary searches
were conducted in these databases using the same three-domain conceptual
structure as the primary search, applying the prespecified eligibility
criteria registered in PROSPERO (CRD420251081555) without modification.

## Boolean search string

Identical conceptual structure to the primary search:

```
("Frailty" OR "Pre-frailty" OR "Prefrailty" OR "Cognitive Frailty" OR "Physical Frailty")
AND
("Machine Learning" OR "Artificial Intelligence" OR "Deep Learning"
 OR "Predictive Model" OR "Prediction Model" OR "Classification Model")
AND
("Community-dwelling" OR "Community dwelling" OR "Community-living"
 OR "Older adults" OR "Elderly" OR "Geriatric")
```

## Filters applied

- **IEEE Xplore:** Journals only; publication years 2018–2025.
- **ACM Digital Library:** Research Articles; publication years 2015–2025.

## Eligibility criteria applied

The same prespecified eligibility criteria from the primary search and
the PROSPERO-registered protocol (CRD420251081555) were applied:

1. Community-dwelling adults aged ≥60 years (matching the prespecified review eligibility criterion).
2. ML-based frailty prediction or classification model.
3. Original full-length peer-reviewed journal article.
4. Sample size ≥ 1,000 participants.
5. SCI(E)-indexed journal.
6. Non-hospital-based study.
7. Phenotypic frailty assessment as the construct (Fried CHS, FRAIL,
   J-CHS, or comparable phenotype-based instruments).

## Records identified

| Source | Records identified | Filter |
|---|---:|---|
| IEEE Xplore Digital Library | 18 | Journals only, 2018–2025 |
| ACM Digital Library | 24 | Research Article, 2015–2025 |
| **Total** | **42** | |

## PRISMA flow for the supplementary search

| Stage | n | Notes |
|---|---:|---|
| Identified (IEEE + ACM) | 42 | IEEE 18 + ACM 24 |
| Duplicates with existing records | 2 | IEEE #5 Yang 2025 SR (search-record duplicate of an already-screened systematic review record); IEEE #16 Jung 2021 (search-record duplicate of a record previously retrieved through the main databases — not a new eligible study and not among the 14 included studies) |
| Screened (title/abstract) | 40 | |
| Excluded at title/abstract screening | 33 | Hospital-based, off-topic (not frailty prediction), not original (review/SR/MA), not frailty-related |
| Assessed for eligibility (full-text) | 7 | 6 new candidates + 1 search-record duplicate of an existing inclusion |
| Excluded at eligibility | 7 | See `02_screening_records/ieee_acm_fulltext_excluded.xlsx` for per-record reasons |
| **Final new inclusions** | **0** | Original 14 studies maintained |

## Per-record evidence

- **Complete record-level metadata and screening decisions for all 42
  records** are provided in `02_screening_records/ieee_acm_screening_log.xlsx`
  (sheets: Summary, IEEE [n=18], ACM [n=24], Legend).
- **Per-record exclusion justifications for the 7 full-text candidates** are
  provided in `02_screening_records/ieee_acm_fulltext_excluded.xlsx`.

## Notable case: Bertini et al. (2018)

The Bertini et al. (2018, *Proc IEEE* 106(4):723–737) record passed the
sample size (n = 95,368), age (≥65 years), SCI(E) indexing, and
community-dwelling criteria. It was nonetheless excluded at the
eligibility stage for **construct-validity mismatch**:

- **Bertini et al.** operationalise frailty as a **surrogate outcome** —
  emergency hospitalization OR all-cause mortality within one year —
  using these adverse outcomes as the model's prediction label.
- **All 14 included studies** in this review operationalise frailty
  using **phenotypic frailty assessment** (Fried 2001 CHS, FRAIL scale,
  J-CHS, or comparable phenotype-based instruments). Frailty is treated
  as a clinical **syndrome** characterised by reduced physiologic
  reserve, of which hospitalization and mortality are adverse
  **outcomes** rather than defining features.
- Including a study that operationalises frailty *as* its adverse
  outcomes would conflate cause and effect and introduce
  outcome-operationalisation heterogeneity that undermines the
  integrity of the synthesis.

Academic basis: Rockwood (2005, *Age Ageing* 34:432–4) on frailty
construct validity; Fried et al. 2001, *J Gerontol A* 56:M146–57; Fried
et al. 2004; Xue 2011; Kim & Schneeweiss 2020, *Ann Geriatr Med Res*
24:62–74; PRISMA 2020 item 6 (Page et al. 2021, *BMJ* 372:n71); Cochrane
Handbook §3.2 (Higgins & Thomas 2023, v6.4).

## Outcome

After applying the prespecified eligibility criteria, **no additional
eligible studies** were identified beyond those captured in the primary
search of PubMed, Embase, Web of Science, and Scopus. The final
inclusion of 14 studies and the PRISMA flow diagram (Figure 1) of the
manuscript therefore do not require revision.

## Methodological rationale

The supplementary search was conducted to address the reviewer's
concern about database coverage. Expanding the included set to add
records that did not meet the prespecified eligibility criteria — in
particular conference proceedings, workshop papers, qualitative HCI
studies, hospital-based feasibility studies, samples below n = 1,000,
or studies operationalising frailty as a surrogate outcome — would
have:

- compromised the integrity of the PROSPERO-registered protocol
  (CRD420251081555);
- introduced studies below the threshold of robust prediction-model
  evidence as defined by Debray et al. (2017) and PROBAST (Wolff et
  al. 2019);
- introduced construct-validity heterogeneity (frailty syndrome vs.
  frailty surrogate outcome) that undermines synthesis integrity; and
- reduced, rather than enhanced, the methodological rigor of the
  review.

The supplementary search outcome is documented in Supplementary Table
S1 (search strings), Supplementary Table S6 (PRISMA-stage summary), and
Supplementary Table S7 (per-record exclusion reasons for the seven
full-text candidates) of the manuscript, with the full record-level
data provided in this repository so that readers can independently
verify the search execution and exclusion reasoning.
