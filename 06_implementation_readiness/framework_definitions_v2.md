# Implementation Readiness Framework — Definitions

The four-level implementation-readiness scheme applied in this review is adapted from established technology-readiness and implementation-science frameworks (PROBAST, TRIPOD, RE-AIM). Each included study was assigned to exactly one level based on the strongest evidence reported in the original publication.

---

## Level 1 — Concept only

**Definition.** The study developed and evaluated a model but did not describe any concrete tool intended for deployment.

**Evidence required.**
- Model development reported.
- No nomogram, web calculator, risk score, or EMR integration concept presented.

**Assignment in this review.** Five studies: Gomez-Cabrero 2021, Wu 2022, Hughes 2025, Park 2025, Qi 2025.

---

## Level 2 — Internal-only prototype

**Definition.** The study produced a deployment artefact (nomogram, web calculator, risk score, or EMR integration concept) but did not independently validate model performance in a separate cohort or time period.

**Evidence required.**
- Deployment artefact described or implemented.
- Internal validation only (data splitting, cross-validation, bootstrap).
- No external validation reported.

**Assignment in this review.** Two studies: Peng 2020, Du 2024.

---

## Level 3 — Prototype with temporal or external validation

**Definition.** The study produced a deployment artefact and additionally reported model performance in an independent cohort, time period, or institution (including temporal re-sampling within the same source cohort).

**Evidence required.**
- Deployment artefact described or implemented.
- External validation reported with AUROC and at least one additional performance metric.

**Assignment in this review.** Seven studies: Liu 2023, Liu 2024, Zhang 2024, Liu 2025, Huang 2024, Dong 2025, Isaradech 2025.

**Note.** Among Level 3 studies, the form of external validation varied: most relied on temporal validation within the same source cohort (e.g., later CHARLS or CLHLS waves), with limited geographic or institutional independence. Sub-classification of Level 3 by external-validation type may be useful in future reviews. Zhang 2024 was classified as Level 3 because it reported same-cohort temporal external validation using a later CLHLS wave, although it did not provide validation in an independent institution or geographically distinct cohort.

---

## Level 4 — Real-world deployment

**Definition.** The study prospectively evaluated its tool in routine clinical or community workflows, with documented usability, workflow integration, post-deployment monitoring, and recalibration.

**Evidence required.** All of:
- Deployment artefact integrated into a real-world workflow (primary care, community-screening program, EMR-embedded screen).
- Prospective impact evaluation (effects on screening rates, downstream care, patient-relevant outcomes).
- Reported usability or acceptability assessment.
- Documented post-deployment monitoring or recalibration plan.

**Assignment in this review.** **None** of the 14 included studies met Level 4 criteria.

---

## Crosswalk with RE-AIM

The four levels correspond approximately to the RE-AIM (Glasgow et al. 1999) framework components as follows:

| Readiness Level | Predominant RE-AIM components addressed |
|---|---|
| L1 | None |
| L2 | Reach (potential) |
| L3 | Reach + partial Effectiveness |
| L4 | Reach + Effectiveness + Adoption + Implementation + Maintenance |

---

## Inter-rater note

Readiness-level assignment was carried out independently by both reviewers (S.K. and J.-H.P.) after data extraction was complete. Disagreement occurred in 1 of 14 studies (Du 2024, between L2 and L3); resolved through discussion (final assignment: L2, because external validation was reported but limited to bootstrap-based internal procedures rather than an independent cohort).
