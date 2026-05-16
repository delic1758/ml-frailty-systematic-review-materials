# Change Log

This log records substantive changes made to the manuscript and supporting materials during peer review and pre-submission quality control.

---

## 2026-05-16 (post-second-revision precision QC pass) — Age-criterion alignment, title alignment, and Figure 1 cross-reference clarification (v7p6 → v7p7)

A final precision QC pass synchronised the repository's age criterion, citation title, and Figure 1 cross-reference language with the manuscript's prespecified eligibility criteria and current title.

### Age criterion alignment

The repository's `ieee_acm_supplementary_search.md`, `02_screening_records/ieee_acm_screening_log.xlsx`, and `02_screening_records/ieee_acm_fulltext_excluded.xlsx` previously stated "Community-dwelling adults aged ≥65 years" or "Fails the prespecified ≥65-year eligibility criterion" in several places. The manuscript's PROSPERO-registered eligibility criterion is **community-dwelling adults aged ≥60 years**. All three files were updated to state ≥60 consistently.

For the Olugbenga et al. (2025) full-text exclusion, the exclusion reason was rewritten with precision: the AGELESS+MELoR combined cohort may include MELoR participants aged 55–59 at baseline (i.e., younger than 60), and the article does not provide a ≥60-only subgroup analysis — hence the cohort fails the prespecified ≥60-year eligibility criterion. The previously stated "younger than 65 years" formulation, which was inconsistent with the manuscript's ≥60 criterion, has been removed.

Paper-specific age statements that reflect a study's own cohort characteristics — e.g., Eskandari et al. (Arizona Frailty Cohort, ≥65) and Bertini et al. (Municipality of Bologna ≥65 retrospective cohort) — are retained as accurate descriptions of the cited cohorts, since ≥65 cohorts are a subset of the review's ≥60 eligibility criterion and therefore satisfy the age requirement.

### Title alignment

The README.md citation block and CITATION.cff previously listed the working title "Public Health Implementation of Machine Learning–Based Frailty Prediction for Community-Dwelling Older Adults: A Systematic Review." The current manuscript title is "Machine Learning–Based Frailty Prediction and Classification in Community-Dwelling Older Adults: A Systematic Review of Validation, Explainability, and Implementation Readiness." Both files were updated to the current title.

### Figure 1 cross-reference clarification

The previous statement in `ieee_acm_supplementary_search.md` — "The final inclusion of 14 studies and the PRISMA flow diagram (Figure 1) of the manuscript therefore do not require revision" — was reworded to: "The final inclusion of 14 studies is therefore unchanged. The main PRISMA flow diagram (Figure 1) covers the primary searches; the supplementary-search PRISMA-stage summary is provided separately in Supplementary Table S6 of the manuscript and in the record-level files in this repository." The Figure 1 caption in the manuscript was also extended to explicitly note the supplementary IEEE/ACM search (May 12, 2026; 42 records identified; 0 new eligible studies) and cross-reference Supplementary Table S6 and Supplementary File S8.

---

## 2026-05-16 (post-second-revision QC pass) — Repository structural alignment with manuscript final numbering, IEEE/ACM record-level evidence, and Figure 4 production version (v7p6)


A post-second-revision QC pass aligned this repository with the final, post-peer-review state of the manuscript and synchronised file naming with the corrected Table and Figure numbering.

### Repository structure

**Figure renaming:**

- `Figure6_AUROC_by_algorithm.png` → `Figure4_AUROC_by_algorithm.png` — the AUROC figure is now Figure 4 in the manuscript (previously Figure 6 in earlier drafts; renumbering follows the Reviewer 3 request to consolidate AUROC presentation under a single figure).
- `figure6_script.py` → `figure4_script.py` (rewritten to produce a two-panel layout: (a) classification of current frailty status, (b) incident prediction of future frailty; markers colour-coded by validation type — internal / same-cohort temporal / independent external — using `adjustText` for non-overlapping point labels).
- `figure6_source_data.csv` → `figure4_source_data.csv` (expanded to long-format with explicit task_type, algorithm, and validation_type columns; Huang and Hughes "external" entries reclassified as "Temporal" to reflect same-cohort temporal validation per the manuscript Section 2.3 definitions).

**Table renaming (to match manuscript final numbering):**

- `table4_ml_performance_source.xlsx` → `table5_ml_performance_source.xlsx`
- `table5_xai_implementation_source.xlsx` → `table4_xai_source.xlsx`
- `table6_probast_source.xlsx` → `table7_probast_source.xlsx`
- **New file:** `table6_implementation_readiness_source.xlsx` — RE-AIM framework (Reach, Effectiveness, Adoption, Implementation, Maintenance) plus a Technology Readiness Level (TRL)-style maturity rubric assessment for all 14 included studies. Added in response to Reviewer 3 Comment on implementation-readiness assessment.

### IEEE/ACM supplementary search — record-level evidence

- **New file:** `02_screening_records/ieee_acm_screening_log.xlsx` — complete 42-record (IEEE 18 + ACM 24) screening log with Summary, IEEE, ACM, and Legend sheets. Each record carries author, title, journal/volume, year, sample size, population description, prior-screening status, and PRISMA-stage decision (title/abstract screened, full-text assessed, exclusion reason).
- **New file:** `02_screening_records/ieee_acm_fulltext_excluded.xlsx` — focused table for the seven full-text candidates excluded at eligibility, with per-record exclusion reasons. The Bertini et al. (2018, *Proc IEEE*) entry includes the full construct-validity justification: Bertini operationalises frailty as a surrogate outcome (1-year hospitalization OR mortality), whereas all 14 included studies use phenotypic frailty assessment (Fried CHS / FRAIL / J-CHS); inclusion would conflate cause and effect (academic basis: Rockwood 2005; Fried 2001; Kim & Schneeweiss 2020; PRISMA 2020 item 6; Cochrane Handbook §3.2).
- `01_search_strategy/ieee_acm_supplementary_search.md` — fully rewritten:
  - Corrected requester attribution: Reviewer 4 (not Reviewer 3, as previously stated).
  - Search execution date now explicit: May 12, 2026.
  - Filters applied now explicit: IEEE Xplore Journals 2018–2025; ACM Digital Library Research Article 2015–2025.
  - PRISMA flow for the supplementary search added (42 → 2 duplicates → 40 screened → 33 excluded at title/abstract → 7 assessed → 7 excluded → 0 new inclusions).
  - Bertini 2018 construct-validity case discussion added.
  - Cross-references to the new record-level xlsx files added.
- `01_search_strategy/search_execution_log.md` — supplementary-search section updated with the execution date (May 12, 2026), exact records-retrieved counts (IEEE 18, ACM 24, total 42), filters applied, and a one-paragraph PRISMA-flow summary with cross-references to the record-level files.

### README

- Repository-content list updated to reflect renamed and added files.
- Methodological-notes section: "Figures 1–5" → "Figures 1–4"; the Figure 6 paragraph rewritten as a Figure 4 paragraph describing the two-panel task-type × algorithm stratification and the `adjustText`-based label placement.
- Section "Researchers conducting future systematic reviews on this topic" extended to point to the IEEE/ACM record-level evidence files and the Bertini construct-validity justification.

### Manuscript-side alignment (for cross-reference)

The corresponding manuscript-side changes — Supplementary Materials list extended with Table S6 (supplementary IEEE/ACM PRISMA-stage summary) and Table S7 (per-record exclusion reasons for the seven full-text candidates); Response Letter §1.4 detailing the Bertini construct-validity rationale; Figure 4 caption explicitly stating the "highest-reported AUROC in the study's primary validation setting" selection rule and the trajectory-study (Wu et al.) handling; Table 6 reformatted in LTR layout with `cantSplit` row breaks — are described in the manuscript's own revision history and the Response to Reviewers document.

---

## 2026-05-15 (same day, eleventh QC iteration) — Limitations punctuation, eligibility tightening, XAI breadth wording, and Gomez-Cabrero country correction (v11 → v12; Cover Letter v8 → v9)

An eleventh pre-submission QC pass corrected one orphaned ellipsis, tightened the eligibility wording to match the exclusion criterion exactly, broadened the §4.1 / Conclusion XAI language to include predictor-level interpretability (consistent with §2.4 and §3.7), and corrected a Gomez-Cabrero country listing that had drifted between Table 1, Table 2, the narrative, and the GitHub repository.

### Manuscript v11 → v12

1. **§4.5 Limitations — Orphaned ellipsis removed.** "restricted inclusion to English-language articles published in SCI(E)-indexed journals ... to ensure consistency" → "restricted inclusion to English-language articles published in SCI(E)-indexed journals to ensure consistency".

2. **Eligibility criteria — Tightened to match exclusion criterion exactly.** "SCI(E)-indexed journal or an equivalent peer-reviewed journal ensuring comparable methodological rigor" → "SCI(E)-indexed peer-reviewed journal ensuring comparable methodological rigor". This eliminates a small inconsistency with the "Published in non-SCI(E)-indexed journals" exclusion reason shown on Figure 1.

3. **§4.1 Summary and Conclusion — XAI wording broadened.** Two sentences that previously read "Explainable AI (XAI) methods were applied in six studies / fewer than half of the studies" have been rephrased as "Formal XAI or predictor-level interpretability analyses were reported in six studies / fewer than half of the studies". This aligns the §4.1 / Conclusion summary with the distinction made in Methods §2.4 (formal XAI = SHAP/SAGE; predictor-level interpretability = Boruta/permutation/Gini/LASSO/SESv) and avoids re-conflating the two categories. Three other occurrences of "XAI methods" elsewhere in the manuscript already used "formal XAI methods" or an explicit classification context and were left unchanged.

4. **Gomez-Cabrero et al. (S02) country listing — Corrected from four countries to three countries.** The Gomez-Cabrero 2021 study included four European cohorts (TSHA, AMI, 3C-Bordeaux, InCHIANTI) spanning three countries (Spain, France, Italy). Table 1 already showed the correct three-country listing; Table 2 and the §3.1 narrative previously showed an incorrect four-country listing including Finland. Both have been corrected:
   - Manuscript Table 2: "Europe(Spain · France · Italy · Finland)" → "Europe(Spain · France · Italy)".
   - Manuscript §3.1 narrative: "across cohorts from Spain, France, Italy, and Finland" → "across cohorts from Spain, France, and Italy".
   - `03_data_extraction/data_extraction_sheet.xlsx` (S02 country column): "Europe (ES/FR/IT/FI)" → "Europe (ES/FR/IT)".
   - `02_screening_records/included_studies_list.xlsx` (S02 country column): "Europe (ES/FR/IT/FI)" → "Europe (ES/FR/IT)".
   - `05_figures_and_tables_source/table2_general_characteristics_source.xlsx`: "Europe (ES/FR/IT/FI)" → "Europe (ES/FR/IT)".

### Marked manuscript v12

5. **§2.3 PRISMA-flow sentence — Sentence-level tracked change re-applied.** As in the v11 repair, the four character-level `<w:ins>`/`<w:del>` pairs generated by LibreOffice in §2.3 were consolidated into a single sentence-level deletion of the previous sentence followed by a single sentence-level insertion of the new sentence, so that the marked file shows the previous and new versions of the PRISMA exclusion sentence as two visually distinct, complete sentences rather than as character fragments.

6. **§4.1 Summary — Orphaned `<w:moveFrom>` cleaned up.** The LibreOffice document compare incorrectly flagged the phrase "Explainable AI (XAI) methods were applied" in §4.1 as a `<w:moveFrom>` with no corresponding `<w:moveTo>`. This orphan `<w:moveFrom>` was converted to a normal `<w:del>` so that the marked file's accepted state matches the clean v12 (111,603 characters of body text in both).

### Cover Letter v8 → v9

7. **Filename references updated** from v11 to **v12** to match the actual submission package.

---

## 2026-05-15 (same day, tenth QC iteration) — Response Letter cross-reference cleanup, repository L3 label harmonization, and Marked-manuscript §2.3 readability (Response Letter v8 → v9; Marked manuscript v11 patched in place)

A tenth and final pre-submission QC pass corrected three small consistency issues that surfaced in a final cross-review of the v11 / v8 package, and improved the readability of the tracked-change display for §2.3 in the marked manuscript.

### Response Letter v8 → v9

1. **Opening sentence — "three reviewers" → "reviewers".** The document opens with point-by-point responses to four numbered reviewer sections (Reviewer 1, Reviewer 2, Reviewer 3, Reviewer 4); the opening sentence "We thank you and the three reviewers" was internally inconsistent with that structure and has been changed to "We thank you and the reviewers".

2. **R3.1 cross-reference — "R1 Comment 2" → "R2 Comment 2".** When the Reviewer 1 / 2 / 3 sections were shifted to Reviewer 2 / 3 / 4 in the previous (ninth) iteration, one cross-reference in R3.1 pointing to the implementation-readiness explanation in R1.2 was not updated. The implementation-readiness explanation is now in R2.2 (formerly R1.2), so the cross-reference has been updated accordingly.

3. **R4.4 — Figure preparation description rewritten.** The previous wording "Figures 1–5 were prepared in Microsoft Excel ... Figure 6 was prepared in Python" was inconsistent with the actual repository contents (Figure 1 is also prepared in Python via `figure1_prisma_script_v4.py` against `figure1_prisma_flow_source.csv`). The new wording reads: "Figure 1 (PRISMA flow) and Figure 6 (best-model AUROC by algorithm class) were prepared in Python (matplotlib) — for Figure 6 from a CSV input, and for Figure 1 from numerical inputs encoded in the regeneration script — and both scripts are provided in the repository (`figure1_prisma_script_v4.py` with `figure1_prisma_flow_source.csv`; `figure6_script.py` with `figure6_source_data.csv`). Figures 2–5 were prepared from the corresponding source data tables provided in the repository."

### Repository

4. **`03_data_extraction/variable_dictionary.md` — L3 label harmonized.** The `readiness_level` entry now reads "L3 (prototype with temporal or external validation)" instead of "L3 (externally validated prototype)", matching the manuscript Abstract, §4.4, and Response Letter.

5. **`06_implementation_readiness/framework_definitions.md` — Level 3 heading and definition harmonized.** The Level 3 heading was changed from "Externally validated prototype" to "Prototype with temporal or external validation", and the definition text now explicitly states that L3 includes temporal re-sampling within the same source cohort, matching the manuscript §4.4 wording.

### Marked manuscript v11 — §2.3 tracked-change display improved

6. **§2.3 PRISMA-flow sentence — Character-level tracked changes consolidated into a single sentence-level replacement.** The original LibreOffice-generated character-level tracked changes in §2.3 produced visually ambiguous fragments (e.g., "87 studies", "2, 3 studies") when read directly in the marked file. The four separate `<w:ins>`/`<w:del>` pairs in §2.3 have been replaced by a single sentence-level deletion of the previous full sentence and a single sentence-level insertion of the new full sentence, so that the marked file now shows the previous and new versions of the sentence as two visually distinct, complete sentences. The total tracked-change count is now 962 ins / 948 del (was 965 / 949). The accepted state of the marked file is byte-equivalent to the clean v11 manuscript (111,595 characters of body text in both).

---

## 2026-05-15 (same day, ninth QC iteration) — Response Letter reviewer remapping and final summary harmonization (Response Letter v7 → v8; Cover Letter v7 → v8)

A ninth and final pre-submission QC pass corrected a Response Letter reviewer-mapping error and added a missing Reviewer 1 point-by-point section. The manuscript itself (v11) was not modified in this iteration.

### Response Letter v7 → v8

1. **Reviewer numbering remapped to match the official decision package.** In v7, the Response Letter's "Reviewer 1" section addressed comments that the journal's decision package actually attributes to Reviewer 2 (implications of XAI absence, formal evaluation of implementation readiness, systematic synthesis of performance-metric reporting). A reviewer reading v7 would not have found their own comments under their assigned reviewer number. In v8, the sections have been shifted by one position so that each numbered Reviewer N section corresponds to the comments attributed to Reviewer N in the journal's decision package:

   - **Reviewer 1 (new)** — Classification vs prediction, high AUROC and predictor–outcome overlap, temporal vs independent external validation, missing-data handling as analysis-domain bias, PROBAST findings, and Discussion repetition reduction. (Six new point-by-point items, R1.1 – R1.6, were drafted and inserted.)
   - **Reviewer 2 (former Reviewer 1)** — Implications of XAI absence; implementation-readiness evaluation; metric-reporting synthesis. (Items R1.* internally renumbered to R2.*; three "R1, Comment N" sub-headers renumbered to "R2, Comment N".)
   - **Reviewer 3 (former Reviewer 2)** — Search-strategy completeness; systematic-review design; heterogeneity; XAI comparison; validation; metrics; etc. (Items R2.* → R3.*; twelve "R2, Comment N" → "R3, Comment N".)
   - **Reviewer 4 (former Reviewer 3)** — IEEE/ACM supplementary search; Figure 6 / forest-plot suggestion; computational complexity; GitHub transparency; abstract/conclusion numerical specificity. (Items R3.* → R4.*; five "R3, Comment N" → "R4, Comment N".)

2. **Repository summary at the top of the Response Letter — Two new public files acknowledged.** The opening summary bullet now lists the GitHub package as "(screening log, full-text exclusion list, data-extraction sheet, scoring sheets, search strings, PRISMA data, figure source data and scripts)", consistent with the actual repository contents added in earlier iterations.

### Cover Letter v7 → v8

3. **"the three reviewers" → "reviewers".** The phrasing "We have carefully addressed all comments raised by the Editor and the three reviewers" was changed to "the Editor and reviewers", because the journal's decision package contains four reviewer reports.

---

## 2026-05-15 (same day, eighth QC iteration) — Repository cleanup and Data Availability synchronization (v10 → v11)

An eighth pre-submission QC pass cleaned up the screening folder, removed obsolete artifacts, harmonized the v3 → v4 PRISMA figure references throughout the repository, and synchronized the manuscript Data Availability statement, Cover Letter, and Response Letter with the actual contents of the public repository (which now includes a per-record screening log and a per-study full-text exclusion list).

### Repository cleanup

1. **`02_screening_records/prisma_flow_data.csv` — Subcategory counts aligned with manuscript v10.** `sample_size_below_1000_only` 7 → 8 and `both_sample_size_and_age_criteria` 3 → 2. The total (16 full-text exclusions) is unchanged. All four counts in this CSV now match Manuscript Figure 1, Methods §2.3, and `fulltext_excluded_studies.xlsx`.

2. **`02_screening_records/full_text_assessed_template.csv` and `excluded_full_text_with_reasons_template.csv` — Deleted.** These empty item-level schema templates were superseded by the populated `screening_log.xlsx` (63 records) and `fulltext_excluded_studies.xlsx` (16 records) added in v10. Keeping empty templates alongside the populated workbooks could confuse a reader; the populated workbooks alone now document the screening provenance.

3. **`02_screening_records/README.md` — "±1 sensitivity" caveat removed.** Now that Figure 1, §2.3, the screening log, and the prisma_counts_check are all aligned at 8 / 4 / 2 / 2, the previously documented uncertainty about a single borderline study no longer exists; the relevant paragraph has been replaced with a clean, definitive subcategory listing. The corresponding template rows in the README files table were also removed.

4. **`05_figures_and_tables_source/` — v3 PRISMA artifacts removed.** `Figure1_PRISMA_v3.png` and `figure1_prisma_script_v3.py` were deleted from the repository so that only the current (v4) figure and script remain. The main README's directory tree and figure-creation notes were updated from v3 to v4.

### Manuscript v10 → v11 (Data Availability)

5. **Data Availability — Two new repository contents listed.** The Data Availability statement now explicitly lists "the screening log for the 63 records retained for detailed title/abstract screening" and "the list of 16 full-text–excluded studies with standardized exclusion reasons" before the data-extraction sheet, matching the actual repository contents added in v10.

### Cover Letter v6 → v7

6. **Cover Letter — Repository contents description updated.** The GitHub contents paragraph now also mentions the screening log and the full-text exclusion list, in addition to the items previously listed.

7. **Cover Letter — Filename references** updated from v10 to **v11** to match the actual submission package.

### Response Letter v6 → v7

8. **R3.4 — Repository statement rewritten.** The "item-level templates documenting the screening schema ... per-record item-level screening logs are retained by the authors and available upon reasonable request" sentence was replaced. The new sentence enumerates the actual public files: per-record screening log (63 records), full-text exclusion list (16 records), included studies cross-reference (14 records), PRISMA counts verification workbook, data-extraction sheet, PROBAST/TRIPOD assessments, search strings, PRISMA flow data, and figure source data and scripts. The "upon reasonable request" phrasing was removed because the materials are now publicly available, not held back pending request.

9. **R3.5 — External AUROC range wording aligned with Abstract.** The numerical-results paragraph was updated from "external AUROC range 0.54–0.977" to "best-model external AUROC range 0.611–0.977, with one non-best KNN model in Isaradech et al. showing AUROC 0.54", mirroring the corresponding change made to the Abstract in v9.

### Repository final cleanup (added after v11 manuscript submission preparation)

10. **`01_search_strategy/search_execution_log.md` — Figure 1 reference updated.** The narrative footer referenced `../05_figures_and_tables_source/Figure1_PRISMA_v3.png`; now points to `Figure1_PRISMA_v4.png` (the only PRISMA figure now present in the repository).

11. **`02_screening_records/included_studies_list.xlsx` — `sample_size` column populated.** Previously empty; now populated for all 14 studies using the authoritative values in `03_data_extraction/data_extraction_sheet.xlsx`. For studies with external validation, the sample-size cell records both the development and external-validation sample sizes (e.g., S04 Liu 2023: "Total N = 2,802 (development 2,241; external validation 1,721)"); for studies without external validation, only the total N is recorded.

---

## 2026-05-15 (same day, seventh QC iteration) — Screening provenance package and PRISMA subcategory alignment (v9 → v10)

A seventh pre-submission QC pass added a full screening provenance package to this repository and aligned the full-text exclusion subcategory breakdown shown on Figure 1 of the manuscript with the per-study data recorded in the screening log.

### Screening provenance package added to `02_screening_records/`

1. **`screening_log.xlsx`** — 63 records retained for detailed title/abstract screening, with per-record decision (retain / exclude) and standardized exclusion reason. Generated from the authors' working classification spreadsheet (`대상논문_frailty_ml_63-30-16-14_250919.xlsx`).

2. **`fulltext_excluded_studies.xlsx`** — The 16 reports excluded at full-text eligibility assessment, with first author, year, title, reported sample size, reported population description, SCI(E) indexing status, exclusion reason, and criterion reference.

3. **`included_studies_list.xlsx`** — The 14 included studies, cross-referenced to `../03_data_extraction/data_extraction_sheet.xlsx` (study_id S01–S14).

4. **`prisma_counts_check.xlsx`** — Arithmetic verification of every count and intermediate sum shown in Figure 1, plus a Notes sheet explaining the relation between this workbook and the rest of the repository.

5. **`02_screening_records/README.md`** — Folder-level overview listing all files, standardized exclusion reasons, and cross-references.

### Manuscript v9 → v10 (Figure 1 and §2.3 alignment)

6. **PRISMA Figure 1 full-text exclusion subcategory breakdown — Updated for data alignment.** The original Figure 1 listed the 16 full-text exclusions as: Sample size <1,000 only (n=7), Population aged <60 years only (n=4), Both sample-size and age criteria (n=3), Published in non-SCI(E)-indexed journals (n=2). On re-examination against the per-study data in `02_screening_records/fulltext_excluded_studies.xlsx`, one study previously assigned to "Both criteria" (a small-sample study whose age-inclusion criterion was at the ≥60 boundary, i.e., the population was not <60) was reclassified to "Sample size <1,000 only". The updated subcategory breakdown is **8 / 4 / 2 / 2 = 16**, with the total of 16 full-text exclusions unchanged. Figure 1 PNG was regenerated (`Figure1_PRISMA_v4.png`) and embedded in the manuscript; `figure1_prisma_script_v4.py` and `figure1_prisma_flow_source.csv` in the repository were updated to match.

7. **Methods §2.3 — Sentence updated** to read: "Following full-text assessment, 8 studies were excluded due to sample sizes below 1,000 only, 4 studies due to inclusion of participants younger than 60 years only, 2 studies because both sample-size and age criteria applied, and 2 studies because they were not published in SCI(E)-indexed journals."

### Response Letter v5 → v6

8. **R1.2 / R1.5 — PRISMA breakdown updated** from "(7 for n<1,000, 4 for age<60, 3 for both, 2 for non-SCI(E))" to "(8 for n<1,000 only, 4 for age<60 only, 2 for both sample-size and age criteria, 2 for non-SCI(E))".

### Cover Letter v5 → v6

9. **File-name references** updated from v9 to **v10** to match the actual submission package (`Manuscript_FINAL_MARKED_v10.docx`, `Manuscript_FINAL_CLEAN_v10.docx`).

### Repository updates

10. **`05_figures_and_tables_source/figure1_prisma_flow_source.csv`** — `sample_size_below_1000_only` 7 → 8; `both_sample_size_and_age_criteria` 3 → 2.

11. **`05_figures_and_tables_source/Figure1_PRISMA_v4.png`** — Updated PRISMA flowchart PNG. `Figure1_PRISMA_v3.png` is retained for the historical record.

12. **`05_figures_and_tables_source/figure1_prisma_script_v4.py`** — Updated regeneration script with v4-changelog header. `figure1_prisma_script_v3.py` is retained for the historical record.

13. **`02_screening_records/prisma_counts_check.xlsx`** — All subcategory rows now bear "✓" (previously two rows were flagged "⚠" while the manuscript Figure 1 used the 7/4/3/2 distribution; the alignment is now complete).

---

## 2026-05-15 (same day, sixth QC iteration) — Abstract numerical precision, Table 5 column semantics, and L3 label generalization (v8 → v9)

A sixth pre-submission QC pass closed the last three substantive issues identified in a final cross-review of the v8 package: an Abstract external-AUROC range that could be misread as the best-model range, a Table 5 column header that did not match the actual content of the cells in studies that reported selected predictors without explicit importance analysis, and the L3 implementation-readiness label that did not explicitly accommodate temporal validation.

### Manuscript v8 → v9 (3 edits)

1. **Abstract — External AUROC range split.** The sentence "external AUROCs were typically lower and more variable (range 0.54–0.977)" was rewritten so that the best-performing externally validated models and the one non-best KNN outlier are reported as two separate quantities: "external AUROCs for best-performing externally validated models ranged from 0.611 to 0.977, with several models showing substantial degradation under temporally distinct or external validation settings (e.g., Liu 2023/2024/2025: 0.611–0.620, representing temporal validation within the same parent cohort rather than fully independent external validation), and one non-best KNN model in Isaradech et al. showed substantially lower external discrimination (AUROC 0.54)." This brings the Abstract into alignment with Table 4 (which reports best-model AUROC) and Figure 6 (which plots best-model AUROC) while still acknowledging the single 0.54 KNN value that appears in §3.5.

2. **Table 5 — Column 4 header renamed.** "Reported Selected/Key Predictors (if available)" → "**Key Predictors from Explicit Importance/Contribution Analysis**". The previous header could be misread as listing all selected predictors per study, which conflicted with Table 3 (where selected predictors are listed for studies that reported them). The new header clarifies that the column only contains predictors identified through explicit importance/contribution analysis. "None" in this column therefore now means "no explicit importance-based ranking", not "no selected predictors". Selected predictors continue to appear in Table 3 and in `03_data_extraction/data_extraction_sheet.xlsx`.

3. **L3 label — Temporal validation included.** The Abstract, §4.4 implementation-readiness framework, and Response Letter R1.2 table all relabeled "Level 3 (externally validated prototype)" → "**Level 3 (prototype with temporal or external validation)**". The §4.4 definition now explicitly states that L3 includes temporal re-sampling within the same source cohort. This is consistent with the existing manuscript text that already distinguishes temporal validation (Liu 2023/2024/2025) from fully independent external validation (e.g., Isaradech), but removes the residual risk that a reader scanning only the L3 label would conclude that all six L3 studies achieved fully independent external validation.

### Response Letter and Cover Letter

4. **Response Letter v4 → v5.** The L3 row in the implementation-readiness summary table was updated to "Prototype with temporal or external validation" to match the manuscript Abstract and §4.4.

5. **Cover Letter v4 → v5.** File-name references updated from v8 to **v9** to match the actual submission package (`Manuscript_FINAL_MARKED_v9.docx`, `Manuscript_FINAL_CLEAN_v9.docx`).

### Repository updates

6. **`05_figures_and_tables_source/table5_xai_implementation_source.xlsx`.** Column 5 header renamed from "Reported Selected/Key Predictors (if available)" to "Key Predictors from Explicit Importance/Contribution Analysis" to mirror the manuscript Table 5 change.

---

## 2026-05-15 (same day, fifth QC iteration) — Methods §2.4 XAI terminology and final repository alignment (v7 → v8)

A fifth pre-submission QC pass closed the last remaining inconsistencies: the Methods §2.4 sentence that listed Boruta and permutation importance as XAI examples, the slightly ambiguous Table 5 "XAI Method" column header, and minor mismatches between the manuscript Table 3 / Table 5 and the GitHub `data_extraction_sheet.xlsx`.

### Manuscript v7 → v8 (4 edits)

1. **Methods §2.4 — Separate formal XAI from feature-selection/importance methods.** The data-extraction items list was rewritten so that formal XAI methods and predictor-level feature-selection or importance methods are listed as two distinct categories. The previous formulation grouped SHAP, SAGE, Boruta, and permutation importance under one "XAI methods" bullet; the revised text reads "...calibration assessment, formal XAI methods (e.g., SHAP, SAGE), predictor-level feature-selection or importance methods (e.g., Boruta, permutation importance, Gini-based importance, LASSO-based selection, SESv), implementation strategies...". This aligns Methods §2.4 with the formal-XAI / predictor-level interpretability distinction used throughout Abstract, §3.3, §3.7, Figure 5, and Table 5.

2. **Table 5 — Column 2 header renamed.** "XAI Method" → "**Explanation / Predictor-Level Reporting Method**". The previous header implied that the column listed XAI methods, which conflicted with the rows in which Formal XAI Reported = No but the column listed methods such as SESv, Gini importance, or Boruta. The new header accommodates both formal XAI and predictor-level reporting methods without internal contradiction.

### Repository updates

3. **`03_data_extraction/data_extraction_sheet.xlsx` — Final alignment with manuscript Table 3 / Table 5.**
   - **S09 (Du)** `top_predictors`: expanded from 7 items to the full 10 items shown in manuscript Table 3 (added "Falls within last 2 years; Arthritis/rheumatism; Community elderly association").
   - **S13 (Dong)** `top_predictors`: "Nationality; Natural teeth" → "Ethnicity; Dental status" to mirror the wording in manuscript §3.3 and Table 3.
   - **S14 (Isaradech)** `top_predictors`: expanded abbreviations to match Table 3 wording ("Household living arrangement", "Waist circumference", "Calf circumference").
   - **S04 (Liu 2023)** `xai_method`: "Variable importance (no explicit XAI framework)" → "No formal XAI; feature selection only; no explicit variable-importance analysis".
   - **S05 (Liu 2024)** `xai_method`: "LASSO-based selection; modified Poisson importance" → "No formal XAI; LASSO-based selection only".
   - **S07 (Liu 2025)** `xai_method`: "Not reported" → "No formal XAI reported".
   - **Column 33 header**: `xai_method` → `explainability_or_feature_selection_method`, with a corresponding entry in `variable_dictionary.md` clarifying the new semantics (formal XAI vs predictor-level/feature-selection methods).

4. **`05_figures_and_tables_source/table5_xai_implementation_source.xlsx`.** Column 3 header renamed from "XAI Method" to "Explanation / Predictor-Level Reporting Method" to mirror manuscript Table 5.

### Cover Letter

5. **Cover Letter — Filename references.** Updated from v7 to **v8** to match the actual submission package (`Manuscript_FINAL_MARKED_v8.docx`, `Manuscript_FINAL_CLEAN_v8.docx`).

---

## 2026-05-15 (same day, fourth QC iteration) — Full Table 3 ↔ data_extraction_sheet alignment and Table 5 column clarification (v6 → v7)

A fourth pre-submission QC pass eliminated all remaining inconsistencies between the manuscript Table 3 and the GitHub `data_extraction_sheet.xlsx`, and clarified the Table 5 column headers so that "predictor-importance not reported" no longer reads as logically inconsistent with the per-study top predictors shown in Table 3.

### Manuscript v6 → v7 (manuscript)

1. **Table 3 — Top predictors.** Eight rows updated so that the listed top predictors now exactly mirror the `top_predictors` column of `03_data_extraction/data_extraction_sheet.xlsx`. Updated rows: Gomez-Cabrero (vitamin D3, lutein/zeaxanthin, miRNA-125b-5p, troponin T, pro-BNP, sRAGE); Wu (IADL, ADL, MMSE, marital status, weight, hypertension, heart disease); Liu 2023 (waist circumference, age, cognition, self-rated health, material wealth, medical insurance); Liu 2024 (age, education, contact with children, medical insurance, vision impairment, heart disease); Zhang (age, ADL, MMSE, income, sleep hours, education, housework); Park (TUG, education, PF-M, MNA, ABC, K-ADL); Qi (age, BMI, monthly income, living arrangement, visit frequency, pension, smoking); Hughes (age, education, self-reported health, falls, ADL, cognitive score, depression).

2. **§3.3 narrative — Liu 2024 / Liu 2025 and Wu.** Sentences rewritten to reflect the actual top selected predictors that emerged from each study's feature-selection procedure, rather than the framework-level domain names. The duplicate Wu sentence in the preceding paragraph was removed, and a more accurate Wu description (IADL, ADL, MMSE, marital status, weight, hypertension, heart disease) was retained in the predictor-domain summary paragraph.

3. **Table 5 — Column header clarification.** Three column headers were rewritten to resolve the logical conflict in which a study with reported top predictors in Table 3 was simultaneously marked as "Predictor Analysis Not Reported" in Table 5. The new headers explicitly refer to *importance/contribution analysis* rather than to predictor information generally:
   - "Predictor Importance Reported" → "**Explicit Importance/Contribution Analysis Reported**"
   - "Top Predictors" → "**Reported Selected/Key Predictors (if available)**"
   - "Predictor Analysis Not Reported" → "**No Explicit Importance/Contribution Analysis Reported**"

4. **§3.7 closing sentence — Precision improvement.** The closing sentence of §3.7 was tightened to: "the remaining eight studies did not report formal XAI or explicit variable-importance/contribution analyses beyond selected predictors or standard feature-selection procedures, limiting cross-study synthesis of relative predictor contributions". The same updated formulation appears in §3.3.

5. **Figure 5 caption — Additional clarification.** Appended the sentence: "Feature-importance methods (e.g., Gini importance, Boruta, SESv, model-derived feature importance) were treated as predictor-level interpretability rather than formal XAI unless explicitly framed as explanation methods in the original study."

### Cover Letter and supporting materials

6. **Cover Letter.** File-name references updated from v5 to v6, then to **v7** in the present iteration, to match the manuscript actually submitted. The cover letter now references `Manuscript_FINAL_MARKED_v7.docx` and `Manuscript_FINAL_CLEAN_v7.docx`.

7. **Cover Letter, Response Letter, Manuscript Data Availability — Scope of repository.** The phrase "complete review materials" was rephrased to "review materials, including the **complete** data-extraction sheet for the 14 included studies" so that the word "complete" modifies the data-extraction sheet (which is complete: 504 data points across 14 studies × 36 variables) rather than the repository overall, which intentionally does not include item-level full-text screening logs.

### Repository updates

8. **`05_figures_and_tables_source/table3_predictors_source.xlsx`.** The `top_predictors` column updated for the eight studies listed above, so that the GitHub source xlsx, the manuscript Table 3, and the data-extraction sheet are now in three-way agreement.

9. **`05_figures_and_tables_source/table5_xai_implementation_source.xlsx`.** Column headers renamed in alignment with the manuscript Table 5 changes (columns 4, 5, and 6).

---

## 2026-05-15 (same day, third QC iteration) — Cross-file consistency and XAI terminology (v5 → v6)

A third pre-submission QC pass addressed cross-file consistency between the manuscript, the supplementary materials, and this repository, and tightened the terminology around explainable AI (XAI). The substantive changes:

### Manuscript v5 → v6 (7 edits)

1. **Table 3 — Top predictors.** Four rows were rewritten so that the manuscript Table 3 matches Supplementary Table S3 and the data-extraction sheet in this repository: Liu 2025 (now: age, medical insurance, self-rated health, SO₂ exposure, sunshine duration); Huang (functional-ability indicators: shopping, walking 1 km, carrying 5 kg, cooking, crouching/standing, washing, public transport); Du (living city, BMI, peak expiratory flow, in-house shower facility, weight, chest pain on exertion, age, falls, arthritis, community elderly association); and Isaradech (age, sex, household living arrangement, hypertension, dyslipidemia, BMI, waist and calf circumference, exhaustion).

2. **§3.3 body text — Huang.** The narrative description of Huang et al.'s top predictors was rewritten to be consistent with the corrected Table 3 entry above (functional-ability indicators from CGA, replacing the previous thematic summary of "ADL/IADL deficits, sensory impairments, memory decline").

3. **Table 5 — Column header and reclassification.** Column 2 header renamed from "XAI / Interpretability Analysis Applied" to "**Formal XAI Reported**". Four studies (Gomez-Cabrero, Zhang, Huang, Qi) reclassified from "Yes" to "No" in this column because their reported analyses (SESv-based signatures, Gini importance, Boruta) constitute predictor-level interpretability or feature-importance methods rather than formal XAI; only Wu and Du (SHAP and SAGE) retain "Yes". Methods and predictor-level information columns are unchanged and continue to reflect each study's specific analyses.

4. **Figure 5 caption.** Renamed from "Distribution of Explainable AI (XAI) Methods Used in Included Studies" to "**Distribution of Formal XAI and Predictor-Level Interpretability Methods Used in Included Studies**", to mirror the Table 5 terminology and prevent conflation of formal XAI with feature-importance / feature-selection methods.

5. **§3.7 (Explainability) — Rewritten.** Now opens with: "Two studies explicitly applied formal explainable AI (XAI) methods, while four additional studies reported predictor-level interpretability or feature-importance analyses." The remainder of the section clearly separates the two categories.

6. **§3.3 — Same split applied.** The sentence summarizing predictor-importance analyses in §3.3 was rewritten to use the same formal-XAI / predictor-level-interpretability distinction.

7. **Abstract — XAI and validation wording.** The Results paragraph was split into two clearer claims about XAI ("Two studies explicitly applied formal XAI methods (SHAP and/or SAGE), while four additional studies reported predictor-level interpretability or feature-importance analyses..."). In the same paragraph, the phrase "substantial degradation under independent validation (e.g., Liu 2023/2024/2025: 0.611–0.620)" was replaced by "substantial degradation under temporally distinct or external validation settings (e.g., Liu 2023/2024/2025: 0.611–0.620, representing temporal validation within the same parent cohort rather than fully independent external validation)" to avoid mischaracterizing the Liu temporal validation as independent external validation.

### Cover Letter and Response Letter

8. **Cover Letter.** File-name references updated from `Manuscript_FINAL_MARKED_v4.docx` and `Manuscript_FINAL_CLEAN_v4.docx` to the v5 equivalents (note: the actual files submitted are v6; the cover letter's v5 references reflect the version that was finalized at the time the cover letter was last drafted, and the editor will see v6 in the submission system).

9. **Response Letter.** GitHub language harmonized in the opening section: "will be deposited in an open repository upon publication" → "has been made publicly available on GitHub and will be archived in Zenodo with a citable DOI upon acceptance". This aligns with the rest of the response letter, which already states that the repository is live.

### Repository updates

10. **`05_figures_and_tables_source/table3_predictors_source.xlsx`.** The `top_predictors` cells for Liu 2025, Huang, Du, and Isaradech were updated to match the corrected manuscript Table 3.

11. **`05_figures_and_tables_source/table5_xai_implementation_source.xlsx`.** Column B header renamed to "Formal XAI Reported"; cells for Gomez-Cabrero, Zhang, Huang, and Qi reclassified from "Yes" to "No" in that column.

12. **`02_screening_records/`.** README language clarified to be explicit that the screening-stage CSV files in this repository are item-level templates documenting the structure of records (per-study fields and exclusion reasons), not a complete reproduction of every excluded full-text article's bibliographic metadata. Item-level records are retained by the authors and available upon reasonable request.

---

## 2026-05-15 (same day, second QC iteration) — Numerical and consistency fixes (v4 → v5)

A second pre-submission QC pass identified additional numerical and consistency issues that were corrected in the v5 manuscript and reflected in the repository:

### Manuscript v4 → v5 (4 edits)

1. **Table 2 — Year of publication.** Counts were corrected to 2025 = 6 (42.9%) and 2024 = 4 (28.6%) (previously incorrectly listed as 5/5). The included-studies tally by year is: 2020 = 1 (Peng), 2021 = 1 (Gomez-Cabrero), 2022 = 1 (Wu), 2023 = 1 (Liu 2023), 2024 = 4 (Liu 2024, Zhang, Huang, Du), 2025 = 6 (Liu 2025, Hughes, Park, Qi, Dong, Isaradech). Total = 14.

2. **Table 3 — Candidate / final predictor counts.** Six rows were corrected to align with the per-study predictor counts reported in Supplementary Table S3 and the data extraction sheet. The corrections involved Gomez-Cabrero, Liu 2023, Liu 2024, Huang, Hughes, and Isaradech. Each row now shows the candidate pool size and the final post-selection predictor count consistent with the original study's feature-selection method (LASSO, Boruta, RFE, or backward elimination).

3. **Acknowledgments — AI-tools disclosure.** Updated from "Not applicable." to: "During the preparation and revision of this manuscript, the authors used generative AI-based language-editing tools solely for language editing, organization of revision notes, and consistency checking. The authors reviewed and edited all outputs and take full responsibility for the content of the manuscript." This aligns the Acknowledgments with the Cover Letter declaration that any use of language-editing tools is disclosed in the Acknowledgments.

4. **Abstract — Conclusions paragraph (PROBAST emphasis).** Added a closing sentence: "PROBAST assessment indicated that only two studies had both low risk of bias and low applicability concern, underscoring the need for cautious interpretation and more rigorous methodological standards before routine implementation."

5. **§3.9 Missing Data — Bias-mechanism framing.** Added one explicit sentence: "Because missing-data mechanisms were rarely justified and sensitivity analyses were seldom reported, missing-data handling was considered a recurrent analysis-domain limitation and a potential source of bias across the included prediction models."

### Repository updates

6. **CITATION.cff.** Removed the ORCID placeholder line (`orcid: "https://orcid.org/0000-0000-0000-0000"`) for the first author. Real ORCIDs may be added at publication.

7. **interrater_reliability.md.** Updated the reference from `disagreement_resolution_log.csv` (file name no longer in use) to `probast_disagreement_summary.csv` (the actual aggregated summary file in the repository).

8. **figure6_script.py.** Rewritten so that the script loads data from `figure6_source_data.csv` rather than from hard-coded values, and emits files using the same filenames present in the repository (`Figure6_AUROC_by_algorithm.png` and `Figure6_AUROC_by_algorithm.pdf`). End-to-end reproducibility verified by running the script in isolation against the CSV.

9. **table2_general_characteristics_source.xlsx and table3_predictors_source.xlsx.** Updated to match the corrected manuscript Tables 2 and 3.

---

## 2026-05-15 — Pre-submission quality-control consolidation

A focused internal QC pass identified six numerical and labeling inconsistencies in the revised manuscript and three corresponding alignment items in the Response Letter. All were corrected before resubmission. A separate Supplementary Table cross-reference issue was identified after this pass and corrected immediately (see entry below).

---

## 2026-05-15 (same day, post-GitHub-package QC) — Supplementary Table S4/S5 cross-reference correction

During preparation of the GitHub repository, a numbering mismatch was identified between the manuscript and the supplementary materials file. The supplementary file labels its five tables as S1 (Search strategy), S2 (Study characteristics and modeling details), S3 (Predictive features), S4 (Handling of missing data), and S5 (TRIPOD reporting quality checklist). The manuscript v3 cross-referenced TRIPOD as Supplementary Table S4 in §3.6 and §3.10, and the Supplementary Materials list at the end of the manuscript enumerated only S1–S4 with no reference to S5.

The mismatch was resolved by preserving the supplementary file structure (which contains both an explicit Missing Data table and a TRIPOD checklist) and updating the manuscript to consistently cite TRIPOD as S5:

- §3.6: "Supplementary Table S4" → "Supplementary Table S5" (TRIPOD reference)
- §3.10: "Supplementary Table S4" → "Supplementary Table S5" (TRIPOD reference)
- §3.9: added one sentence at the end of the Missing Data section explicitly cross-referencing Supplementary Table S4
- End-of-manuscript Supplementary Materials list: "Supplementary Table S1, S2, S3, S4, and Supplementary Methods S1" → "Supplementary Tables S1–S5 and Supplementary Methods S1"

The Data Availability statement and the corresponding Action paragraph of the Response Letter (R3.4) were also upgraded from "available upon request via review-only link, to be deposited upon publication" to a direct citation of the public GitHub repository URL, with Zenodo archiving language for post-acceptance citable DOI assignment.

### Manuscript edits

1. **Performance-metric reporting synthesis (§4.3, §3.5).** Reporting frequencies were recalculated against Table 4. AUROC was reported by 12 of 14 studies (85.7%), not all 14 — Peng et al. (HR-based survival) and Gomez-Cabrero et al. (OR- and signature-based) did not report AUROC. Threshold-dependent metrics were itemized by metric: F1 score in five studies (Wu; Liu 2025; Huang; Du; Qi), accuracy in three (Huang; Du; Park), sensitivity and specificity in two (Park; Isaradech), PPV/NPV in none.

2. **Zhang et al. validation labeling (Table 1).** The 2,612-subject set was relabeled from "External val." to "Validation/test set" to align with the study's 75:25 split + 4-fold CV design and with the implementation-readiness framework's L2 (internal-only prototype) assignment.

3. **Supplementary Table cross-references (§3.6).** TRIPOD checklist cross-reference normalized to align with §3.10.

4. **Table 5 column header.** "XAI Applied" broadened to "XAI / Interpretability Analysis Applied" to encompass Gini importance and Boruta, which some readers do not classify strictly as XAI.

5. **Data Availability statement.** Strengthened (later finalized in v4; see entry above) to specify that complete review materials are available in a public GitHub repository, with Zenodo archiving for a citable DOI upon acceptance.

6. **Figure 1 PRISMA flowchart (regenerated as v3).** Three wording refinements were applied without changing any numeric values:
   - "Unexcluded duplicates at preliminary stage" → "Additional duplicates identified during detailed screening"
   - "Records excluded by automated / preliminary screening" → "Records excluded by automated filters and preliminary screening"
   - "Overlap of criteria 1 & 2" → "Both sample-size and age criteria"

   Arithmetic preserved: 2,881 − 90 dup − 2,728 automated/preliminary = 63; 63 − 33 = 30; 30 − 16 = 14.

### Response Letter alignment

The metric-synthesis table in the response to Reviewer 1 (Comment 3) and the description of the Data Availability action in the response to Reviewer 3 (Comment 4) were updated to match the revised manuscript wording and counts. No additional content changes were made.

---

## Earlier history (round-1 to round-2 revision)

Substantive content additions made in response to peer review are documented in the Response Letter accompanying the resubmission. Principal additions:

- New §4.4 four-level implementation-readiness framework (L1–L4) with per-study assignments.
- New §4.3 paragraph systematically synthesizing metric reporting across five dimensions (discrimination, calibration, rare-event sensitivity, decision-analytic utility, equity).
- New §4.6 paragraph on computational footprint and deployment characteristics.
- New §4.5 expanded limitations (geographic concentration, AUPRC absence, calibration gaps, individual-level explanation absence, prototype-stage implementation, sample-size threshold trade-off).
- New supplementary IEEE Xplore and ACM Digital Library search documented in Supplementary Table S1.
- New Figure 6 (best-model AUROC by algorithm class across 14 included studies).
- XAI comparison expanded with method-specific scope, robustness, and clinical-interpretability considerations (SHAP, SAGE, Gini, Boruta, SESv).
- Abstract Results updated with specific numerical performance ranges; Conclusion updated with caveats regarding overlap between predictors and frailty-defining components.
