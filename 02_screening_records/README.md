# 02_screening_records — Screening Provenance

This folder documents the screening process that reduced 2,881 identified records to the 14 studies included in the systematic review. All files together provide an auditable trail consistent with PRISMA-2020.

## Files in this folder

| File | Contents | Records |
|---|---|---|
| `screening_log.xlsx` | All records retained for detailed title/abstract screening, with per-record decision (retain / exclude) and standardized exclusion reason. | 63 |
| `fulltext_excluded_studies.xlsx` | The 16 reports excluded at full-text eligibility assessment, with first author, year, title, reported sample size, reported population description, SCI(E) indexing status, and exclusion reason. | 16 |
| `included_studies_list.xlsx` | The 14 studies included in the review, cross-referenced to the data-extraction sheet (`../03_data_extraction/data_extraction_sheet.xlsx`). | 14 |
| `prisma_counts_check.xlsx` | Arithmetic verification of every count and intermediate sum shown in the PRISMA-2020 flow diagram (Figure 1 of the manuscript). | — |
| `prisma_flow_data.csv` | Compact CSV of the PRISMA stage counts. | — |
| `ieee_acm_screening_log.xlsx` | Complete record-level screening log for the supplementary IEEE Xplore + ACM Digital Library search conducted in response to Reviewer 4. Four sheets: Summary (search dates, filters, PRISMA stages, Bertini construct-validity justification, references), IEEE (18 records with full authors, journal/volume, sample, population, classification, eligibility decision), ACM (24 records with DOI and venue), Legend. | 42 |
| `ieee_acm_fulltext_excluded.xlsx` | The seven full-text candidates from the IEEE/ACM supplementary search, with per-record exclusion reasons. Includes the detailed construct-validity justification for excluding Bertini et al. (2018, *Proc IEEE*). | 7 |

## Standardized exclusion reasons (matches PRISMA Figure 1)

### At detailed title/abstract screening (n = 33)

- Hospital-based studies (n = 15)
- Other unrelated topics (n = 7)
- Not original research — reviews, protocols, opinions, etc. (n = 6)
- Not related to frailty (n = 2)
- Additional duplicates identified during detailed screening (n = 3)

### At full-text eligibility assessment (n = 16)

- Sample size <1,000 only (n = 8)
- Population aged <60 years only (n = 4)
- Both sample-size and age criteria (n = 2)
- Published in non-SCI(E)-indexed journals (n = 2)

The per-study basis for each of the 16 full-text exclusions is shown in `fulltext_excluded_studies.xlsx`; the arithmetic verification of all PRISMA stage counts (including this subcategory breakdown) is in `prisma_counts_check.xlsx`.

## Cross-references

- The 14 `included_studies_list.xlsx` records correspond, one-to-one, to the 14 rows of `../03_data_extraction/data_extraction_sheet.xlsx` (study_id S01–S14).
- PRISMA counts in `prisma_counts_check.xlsx` correspond, line-by-line, to the boxes in Figure 1 of the manuscript.
- The raw EndNote exports underlying the four per-database counts (PubMed 65, Embase 39, Web of Science 35, Scopus 2,742) are retained by the authors.

## Supplementary IEEE Xplore + ACM Digital Library search (Reviewer 4)

The supplementary search (executed May 12, 2026) is documented separately because it followed the primary search and was added during peer review. The methodological rationale, Boolean string, filters, and PRISMA flow for this supplementary search are in `../01_search_strategy/ieee_acm_supplementary_search.md`. The record-level evidence is in:

- `ieee_acm_screening_log.xlsx` — all 42 records (IEEE 18 + ACM 24) with per-record decisions.
- `ieee_acm_fulltext_excluded.xlsx` — the seven full-text candidates with per-record exclusion reasons. Reasons span sample size <1,000 (Amjad 2025, Eskandari 2022, Minici 2022, Ozaki 2024), age criterion not met (Olugbenga 2025), search-record duplicate of a primary-search record (Jung 2021; not a new eligible study and not among the 14 included studies), and construct-validity mismatch (Bertini 2018).

The supplementary search yielded **0 new inclusions**; the original 14-study inclusion is unchanged. Figure 1 was revised to document the supplementary IEEE Xplore and ACM Digital Library search, with record-level decisions provided in Supplementary File S8 / `ieee_acm_screening_log.xlsx` and Supplementary Table S7 / `ieee_acm_fulltext_excluded.xlsx`.
