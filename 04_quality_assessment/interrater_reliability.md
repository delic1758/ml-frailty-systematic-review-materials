# Inter-rater Reliability

## Overview

Risk-of-bias and applicability assessments using the PROBAST tool (Wolff et al. 2019) were carried out independently by two reviewers:

- **Reviewer 1 (S.K.):** Seungmi Kim, Department of Convergence Medicine, Pusan National University School of Medicine.
- **Reviewer 2 (J.-H.P.):** Jong-Hwan Park, Department of Clinical Bio-Convergence, Pusan National University School of Medicine.

All 14 included studies were assessed across 7 PROBAST domains (4 risk-of-bias domains and 3 applicability domains), yielding **98 domain-level judgments** (14 × 7).

---

## Quantitative agreement

| Metric | Value |
|---|---|
| Domain-level judgments compared | 98 |
| Agreement count | 89 |
| Agreement rate | 90.8% |
| Cohen's κ | 0.82 |
| Interpretation (Landis & Koch 1977) | Substantial agreement |

---

## Distribution of disagreements

Disagreements were not evenly distributed across PROBAST domains. They concentrated in two domains where the original studies frequently reported incomplete methodological detail, requiring interpretive judgment:

- **Predictors domain (ROB and Applicability):** Disagreement arose primarily from whether the predictor set was clearly defined and consistently measured. Several studies described predictors only in supplementary materials with partial detail on measurement timing or method.
- **Analysis domain (ROB):** Disagreement arose primarily from whether internal validation procedures were sufficiently described to permit independent reproduction, and whether the predictor-to-event ratio was clearly justified.

Disagreements in the Participants, Outcome, Applicability/Participants, and Applicability/Outcome domains were rare and typically resolved by re-reading the original Methods section.

---

## Resolution process

All disagreements were resolved through **structured consensus discussion** between the two reviewers without arbitration by a third party. The resolution process consisted of:

1. Both reviewers brought the source publication and their independent scoring sheets to the discussion.
2. Each disagreement was reviewed by re-reading the relevant section of the original publication.
3. Where the original publication was ambiguous, the more conservative judgment (i.e., toward "unclear" or "high risk") was adopted, in line with PROBAST guidance.
4. The consensus value was recorded as the final score in `probast_scoring.xlsx`.

Per-item resolutions are aggregated by domain in `probast_disagreement_summary.csv`; item-level reviewer records are retained by the authors and available upon reasonable request.

---

## TRIPOD checklist

The TRIPOD reporting-quality checklist (Collins et al. 2015) was applied descriptively rather than scored with formal inter-rater reliability, in keeping with the original TRIPOD guidance that the checklist is intended as a reporting aid rather than a scoring instrument. The completed per-item assessment is in `tripod_checklist.xlsx` and was finalized by S.K. with verification by J.-H.P. for all 14 included studies.

---

## References

- Wolff RF, Moons KGM, Riley RD, et al. PROBAST: a tool to assess risk of bias and applicability of prediction model studies. *Ann Intern Med*. 2019;170(1):51–58.
- Collins GS, Reitsma JB, Altman DG, Moons KGM. Transparent reporting of a multivariable prediction model for individual prognosis or diagnosis (TRIPOD): the TRIPOD statement. *Ann Intern Med*. 2015;162(1):55–63.
- Landis JR, Koch GG. The measurement of observer agreement for categorical data. *Biometrics*. 1977;33(1):159–174.
