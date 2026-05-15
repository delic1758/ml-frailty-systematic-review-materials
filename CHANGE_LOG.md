# Change Log

This log records substantive changes made to the manuscript and supporting materials during peer review and pre-submission quality control.

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

5. **Data Availability statement.** Strengthened to specify that complete review materials are available to editors and reviewers via a review-only repository link upon request during peer review, and will be deposited in a public open-access repository (Zenodo or OSF) with a citable DOI upon publication.

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
