# Search Execution Log

This log summarizes all database searches executed for this systematic review, including the primary search and the supplementary search added in response to peer-review feedback.

---

## Primary search

**Execution date:** July 4, 2025
**Publication date range covered:** January 1, 2015 to June 30, 2025
**Language:** English only

| # | Database | Provider | Records retrieved | Filters applied |
|---|---|---|---|---|
| 1 | PubMed | NCBI / NLM | 65 | Date 2015-01-01 to 2025-06-30; Language English; Species Humans |
| 2 | Embase | Elsevier | 39 | Date 2015-01-01 to 2025-06-30; Article; English; Human |
| 3 | Web of Science Core Collection | Clarivate | 35 | Publication years 2018–2025 (box-check); Article; English |
| 4 | Scopus | Elsevier | 2,742 | "All field"; Publication years 2015–2025 (box-check); Article; English |
| **—** | **Primary total** | | **2,881** | — |

## Supplementary search

**Execution date:** May 12, 2026
**Execution:** Conducted in response to peer-review feedback (Reviewer 4), after the primary search.
**Eligibility criteria:** Same prespecified criteria as the primary search (PROSPERO CRD420251081555 protocol, unchanged).

| # | Database | Provider | Records retrieved | Filters applied | Eligible additional records |
|---|---|---|---:|---|---:|
| 5 | IEEE Xplore Digital Library | IEEE | 18 | Journals only, 2018–2025 | 0 |
| 6 | ACM Digital Library | ACM | 24 | Research Article, 2015–2025 | 0 |
| **—** | **Supplementary total** | | **42** | — | **0** |

**Detailed PRISMA flow for the supplementary search (42 records):** 2 duplicates with existing records (IEEE #5 Yang 2025 SR = search-record duplicate of an already-screened systematic review; IEEE #16 Jung 2021 = search-record duplicate of a record previously retrieved through the primary searches — not a new eligible study and not among the 14 included studies); 33 excluded at title/abstract screening (hospital-based, off-topic, not original article, or not frailty-related); 7 assessed at full-text eligibility; 7 excluded at eligibility (sample size, age criterion, or construct-validity reasons). Notable case: Bertini et al. (2018, *Proc IEEE* 106(4):723–737) passed sample-size and age criteria but was excluded for construct-validity mismatch — Bertini operationalises frailty as a surrogate outcome (1-year emergency hospitalization OR all-cause mortality), whereas all 14 included studies use phenotypic frailty assessment (Fried CHS / FRAIL / J-CHS). See `ieee_acm_supplementary_search.md` for the full methodological rationale and `../02_screening_records/ieee_acm_fulltext_excluded.xlsx` for per-record full-text exclusion reasons. The complete 42-record screening log is in `../02_screening_records/ieee_acm_screening_log.xlsx`.

---

## Search execution roles

- **Search design:** S.K. and J.-H.P., guided by PRISMA 2020 and the PROSPERO-registered protocol (CRD420251081555).
- **Search execution:** S.K.
- **Record consolidation and deduplication:** EndNote reference manager.

---

## Downstream flow

The full PRISMA 2020 record flow — from 2,881 identified records through duplicates, automated and preliminary screening, detailed title/abstract screening, full-text assessment, and final inclusion of 14 studies — is documented numerically in `../02_screening_records/prisma_flow_data.csv` and visually in `../05_figures_and_tables_source/Figure1_PRISMA_v4.png`.
