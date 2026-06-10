 # Machine Learning–Based Frailty Prediction in Community-Dwelling Older Adults — Systematic Review Materials

This repository accompanies the systematic review:

> Kim S, Shin M-J, Choi BK, Obradovic Z, Rubin DJ, Park J-H. *Machine Learning–Based Frailty Prediction and Classification in Community-Dwelling Older Adults: A Systematic Review of Validation, Explainability, and Implementation Readiness.* (Under peer review at *Healthcare* [MDPI], 2026; Manuscript ID: healthcare-4324907)

**PROSPERO registration:** CRD420251081555
**PRISMA 2020 compliance:** Yes
**Search execution date:** July 4, 2025
**Included studies:** 14 original full-length articles published 2020–2025

---

## Purpose

This repository provides all materials required to reproduce the screening, data-extraction, risk-of-bias, and reporting-quality assessments conducted in the systematic review. Per PRISMA 2020 and PROBAST methodological standards, these tasks were performed manually by two independent reviewers; no machine-learning code, scraping scripts, or automated extraction tools were used. The materials below are therefore the records of human-conducted screening and extraction, not an executable analysis pipeline.

---

## Repository contents

```
.
├── README.md
├── LICENSE
├── CITATION.cff
├── CHANGE_LOG.md
│
├── 01_search_strategy/
│   ├── pubmed_search_strings.md
│   ├── embase_search_strings.md
│   ├── webofscience_search_strings.md
│   ├── scopus_search_strings.md
│   ├── ieee_acm_supplementary_search.md
│   └── search_execution_log.md
│
├── 02_screening_records/
│   ├── README.md                                          # folder-level overview
│   ├── screening_log.xlsx                                 # 63 records, detailed title/abstract screening
│   ├── fulltext_excluded_studies.xlsx                     # 16 full-text exclusions with reasons
│   ├── included_studies_list.xlsx                         # 14 included studies, cross-linked to extraction
│   ├── prisma_counts_check.xlsx                           # arithmetic verification of Figure 1 counts
│   ├── prisma_flow_data.csv                               # compact PRISMA stage counts
│   ├── ieee_acm_screening_log.xlsx                        # 42-record IEEE/ACM supplementary-search screening log (Summary, IEEE, ACM, Legend sheets)
│   └── ieee_acm_fulltext_excluded.xlsx                    # 7 full-text candidates from the IEEE/ACM search, with per-record exclusion reasons (incl. Bertini construct-validity justification)
│
├── 03_data_extraction/
│   ├── data_extraction_sheet.xlsx          # 14 studies × 36 variables
│   ├── variable_dictionary.md
│   └── extraction_discrepancies_summary.csv    # 8 discrepancies, 1.6%; aggregated by domain
│
├── 04_quality_assessment/
│   ├── probast_scoring.xlsx                # 14 studies × 7 domains
│   ├── tripod_checklist.xlsx               # 22-item TRIPOD per study
│   ├── interrater_reliability.md           # 89/98 agreement, κ = 0.82
│   └── probast_disagreement_summary.csv    # aggregated by domain
│
├── 05_figures_and_tables_source/
│   ├── Figure1_PRISMA_v4.png
│   ├── figure1_prisma_script_v4.py
│   ├── figure1_prisma_flow_source.csv
│   ├── Figure4_AUROC_by_algorithm.png
│   ├── figure4_script.py
│   ├── figure4_source_data.csv
│   ├── table1_baseline_characteristics_source.xlsx
│   ├── table2_general_characteristics_source.xlsx
│   ├── table3_predictors_source.xlsx
│   ├── table4_xai_source.xlsx
│   ├── table5_ml_performance_source.xlsx
│   ├── table6_implementation_readiness_source.xlsx
│   └── table7_probast_source.xlsx
│
└── 06_implementation_readiness/
    ├── readiness_level_assignments.csv     # L1–L4 framework × 14 studies
    └── framework_definitions.md
```

---

## How to use this repository

### 1. Reviewers and editors verifying the review

Open `02_screening_records/prisma_counts_check.xlsx` to verify every count and intermediate sum shown in the PRISMA-2020 flow diagram (Figure 1 of the manuscript). The per-record decision trail for all 63 records retained for detailed title/abstract screening is in `02_screening_records/screening_log.xlsx`, the 16 reports excluded at full-text eligibility assessment with first author, year, title, and standardized exclusion reason are in `fulltext_excluded_studies.xlsx`, and the 14 included studies — cross-referenced to the data-extraction sheet — are in `included_studies_list.xlsx`. See `02_screening_records/README.md` for a folder-level overview.

For data verification, see `03_data_extraction/data_extraction_sheet.xlsx` (504 data points across 14 studies × 36 variables) with definitions in `variable_dictionary.md`. Risk-of-bias and reporting-quality assessments are in `04_quality_assessment/` with inter-rater reliability summarized in `interrater_reliability.md` and disagreements aggregated in `probast_disagreement_summary.csv`.

### 2. Researchers conducting future systematic reviews on this topic

The `01_search_strategy/` folder contains the complete, copy-pasteable Boolean search strings for each database, including the supplementary IEEE Xplore and ACM Digital Library search added during peer review (`ieee_acm_supplementary_search.md`; search executed May 12, 2026). The record-level evidence for the supplementary search — all 42 records (IEEE 18 + ACM 24) with screening decisions, and the seven full-text candidates with per-record exclusion reasons (including the Bertini 2018 construct-validity justification) — is provided in `02_screening_records/ieee_acm_screening_log.xlsx` and `02_screening_records/ieee_acm_fulltext_excluded.xlsx`. The data-extraction template in `03_data_extraction/variable_dictionary.md` and the PROBAST/TRIPOD templates in `04_quality_assessment/` may be adapted for future reviews.

### 3. Researchers extending the implementation-readiness analysis

The four-level scheme used in this review is documented in `06_implementation_readiness/framework_definitions.md`, with per-study assignments in `readiness_level_assignments.csv`. No included study reached Level 4 (real-world prospective deployment); this gap delineates priority directions for future research.

---

## Methodological notes

- **Data extraction:** conducted by two reviewers (S.K., J.-H.P.) using a structured Excel template. Each record extracted independently; discrepancies resolved by consensus. Of 504 extracted data points, discrepancies were identified in 8 instances (1.6%) and are aggregated by domain in `extraction_discrepancies_summary.csv` (item-level reviewer records retained by the authors).
- **Risk of bias:** assessed using PROBAST (Wolff et al. 2019). 7-domain assessment per study. Substantial inter-rater agreement: Cohen's κ = 0.82, with 89 of 98 domain-level judgments in agreement. Disagreements aggregated by domain in `probast_disagreement_summary.csv`.
- **Reporting quality:** TRIPOD checklist (Collins et al. 2015), 22 items applied descriptively per study.
- **Figures:** Figures 1–4 prepared using diagrammatic, Excel-based, and Python tools from the source data tables in `05_figures_and_tables_source/`. Figure 1 (PRISMA flow) was finalized in Python (matplotlib); the script (`figure1_prisma_script_v4.py`) and source CSV are provided. Figure 4 (highest-reported AUROC stratified by task type and algorithm) was prepared in Python (matplotlib, with `adjustText` for non-overlapping point labels) from a CSV input; the script (`figure4_script.py`) and source CSV are provided.

No scraping, automated extraction, or LLM-based summarization was used in any stage of the review.

---

## License

Data files (CSV, XLSX), markdown documentation, and Python scripts are released under **CC BY 4.0** (see `LICENSE`). Anyone may copy, redistribute, and adapt the materials for any purpose with attribution. No included full-text article PDFs are redistributed in this repository, as they remain under the copyright of their respective publishers; DOIs are provided for each included study in `data_extraction_sheet.xlsx`.

---

## Citation

If you use any material in this repository, please cite the source publication and this repository. A machine-readable citation is provided in `CITATION.cff`.

```
Kim S, Shin M-J, Choi BK, Obradovic Z, Rubin DJ, Park J-H.
Machine Learning–Based Frailty Prediction and Classification in
Community-Dwelling Older Adults: A Systematic Review of Validation,
Explainability, and Implementation Readiness.
Healthcare (Basel), 2026. [DOI to be assigned upon acceptance]

Repository archived on Zenodo. DOI: [to be assigned upon repository release]
```

---

## Contact

- **Corresponding author:** Jong-Hwan Park, PhD — Department of Clinical Bio-Convergence, Graduate School of Convergence in Biomedical Science, Pusan National University School of Medicine (parkj@pusan.ac.kr)
- **First author / repository maintainer:** Seungmi Kim, MPH — Department of Convergence Medicine, Pusan National University School of Medicine (delos1758@gmail.com)

For questions during peer review, please contact the corresponding author. After publication, questions may also be submitted through GitHub Issues.
