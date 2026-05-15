# Variable Dictionary — Data Extraction Sheet

This dictionary documents the 36 variables extracted from each of the 14 included studies (14 × 36 = 504 data points total).

Variables are organized into eight conceptual groups.

---

## A. Study identification (5 variables)

| Variable | Definition | Type |
|---|---|---|
| `study_id` | Internal ID (e.g., S01, S02, ..., S14) | Text |
| `first_author` | Surname of first author | Text |
| `publication_year` | Year published | Integer |
| `journal` | Journal name | Text |
| `doi` | Digital Object Identifier | Text |

## B. Study design and setting (5 variables)

| Variable | Definition | Type |
|---|---|---|
| `country` | Country/region of cohort | Text |
| `cohort_name` | National/community cohort (e.g., CHARLS, ELSA, KFACS) | Text |
| `study_design` | Cross-sectional / prospective / retrospective / nested case-control | Categorical |
| `setting` | Community-dwelling / mixed / primary care | Categorical |
| `data_source_type` | Survey / claims / multi-omics / sensor | Categorical |

## C. Participants (4 variables)

| Variable | Definition | Type |
|---|---|---|
| `total_n` | Total analyzed sample size | Integer |
| `n_training` | Training/development cohort size | Integer |
| `n_external` | External validation cohort size (if applicable) | Integer or "NR" |
| `age_eligibility` | ≥60 / ≥65 / ≥70 / other | Categorical |

## D. Frailty operationalization (4 variables)

| Variable | Definition | Type |
|---|---|---|
| `frailty_definition` | Fried / FI / SOF / TFI / cognitive frailty / RCF / other | Categorical |
| `frailty_cutoff` | Operational threshold (e.g., FI ≥0.25) | Text |
| `outcome_label_type` | Binary / multi-class / ordinal / trajectory | Categorical |
| `frailty_prevalence_pct` | Prevalence of frailty in training cohort (%) | Numeric or "NR" |

## E. Predictors (3 variables)

| Variable | Definition | Type |
|---|---|---|
| `n_predictors` | Total number of predictors after variable selection | Integer |
| `predictor_domains` | Domains included (sociodemographic, chronic disease, ADL/IADL, physical performance, cognitive, mental health, nutrition, behavior, social, sensory, oral, omics, imaging, other) — semicolon-separated | Text |
| `top_predictors` | Top 5 predictors by reported importance | Text |

## F. ML algorithms and modeling (5 variables)

| Variable | Definition | Type |
|---|---|---|
| `ml_algorithms` | All compared algorithms (semicolon-separated) | Text |
| `best_algorithm` | Algorithm with best reported performance | Text |
| `class_imbalance_handling` | None / SMOTE / SMOTENC / class weighting / other | Categorical |
| `missing_data_handling` | Complete-case / MICE / PMM / KNN imputation / missForest / NR | Categorical |
| `feature_selection_method` | LASSO / Boruta / RF importance / domain expert / none / other | Categorical |

## G. Performance and validation (6 variables)

| Variable | Definition | Type |
|---|---|---|
| `internal_validation_method` | Train-test split / k-fold CV / bootstrap / nested CV | Categorical |
| `auroc_internal` | Best internal AUROC reported | Numeric |
| `external_validation_conducted` | Yes / No | Boolean |
| `external_validation_type` | Temporal / geographic / institutional / other / not applicable | Categorical |
| `auroc_external` | Best external AUROC reported | Numeric or "NA" |
| `metrics_reported` | AUROC, AUPRC, F1, sensitivity, specificity, PPV, NPV, accuracy, calibration, DCA — semicolon-separated | Text |

## H. Explainability and implementation (4 variables)

| Variable | Definition | Type |
|---|---|---|
| `xai_method` | SHAP / SAGE / Gini / Boruta / SESv / permutation / none — semicolon-separated | Text |
| `implementation_form` | None / nomogram / web calculator / risk score / EMR integration concept | Categorical |
| `readiness_level` | L1 (concept only) / L2 (internal-only prototype) / L3 (externally validated prototype) / L4 (real-world deployment) | Categorical |
| `prospective_evaluation` | Yes / No | Boolean |

---

## Notes on coding

- "NR" = Not Reported in the original publication.
- "NA" = Not Applicable to the study design.
- Boolean variables coded as `Yes` / `No` (text), not 0/1.
- Multi-value fields use **semicolon** as separator, e.g., `RF; XGB; LR; SVM`.
- Numeric AUROC values reported to three decimal places when available in the source paper; otherwise to the precision of the source.
