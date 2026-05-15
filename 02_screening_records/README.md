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
