"""
Figure 6: Best-model AUROC by algorithm class across included studies.

This figure visualizes the best-model AUROC reported by each of the 14 included
studies, color-coded by the algorithm class that achieved the best performance.
Two panels show internal and external AUROC where reported.

DATA SOURCE
===========
All values extracted directly from Table 4 of the present systematic review,
which in turn was derived from the prespecified data-extraction sheet
(14 studies × 36 variables = 504 data points). Values not reported in an
original study are shown as "NR" and were not imputed.

For studies that reported only a best-model AUROC without explicitly listing
RF and XGBoost performance, only the best-model value is plotted. This is the
faithful representation of the reported evidence.

RATIONALE
=========
Reviewer R3 requested a forest-style subgroup analysis for AUROC values across
the most commonly used models (RF, XGBoost). Because most included studies
reported only the best-performing model's AUROC rather than separate AUROCs
for each algorithm tested, the most evidence-faithful presentation is to plot
each study's best-model AUROC and indicate which algorithm class achieved it.
This makes the cross-study distribution of RF, XGBoost, and other algorithm
class performance visually apparent.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Data extracted from Table 4 of the manuscript
# Format: (study_label, internal_AUROC, external_AUROC, best_algorithm_class)
# Use None for values not reported in the original publication
studies = [
    # study_label,                   int,     ext,      class
    ("Peng et al. 2020",             None,    None,    "Other (Cox-based)"),
    ("Gomez-Cabrero et al. 2021",    None,    None,    "Other"),
    ("Wu et al. 2022",               0.702,   None,    "Random Forest"),
    ("Liu et al. 2023",              0.701,   0.612,   "XGBoost"),
    ("Liu et al. 2024",              0.809,   0.620,   "Other (Poisson)"),
    ("Zhang et al. 2024",            0.77,    None,    "Random Forest"),
    ("Liu et al. 2025",              0.765,   0.611,   "Other (GLMM)"),
    ("Huang et al. 2024",            0.974,   0.970,   "Logistic Regression"),
    ("Du et al. 2024",               0.756,   None,    "Other (CatBoost)"),
    ("Hughes et al. 2025",           0.981,   0.971,   "Logistic Regression"),
    ("Park et al. 2025",             0.843,   None,    "Logistic Regression"),
    ("Qi et al. 2025",               0.735,   None,    "Random Forest"),
    ("Dong et al. 2025",             0.80,    0.85,    "XGBoost"),
    ("Isaradech et al. 2025",        0.81,    0.75,    "Logistic Regression"),
]

# Color map for algorithm classes
color_map = {
    "Random Forest":         "#1f77b4",  # blue
    "XGBoost":               "#d62728",  # red
    "Logistic Regression":   "#2ca02c",  # green
    "Other (Poisson)":       "#ff7f0e",  # orange
    "Other (GLMM)":          "#ff7f0e",
    "Other (CatBoost)":      "#ff7f0e",
    "Other (Cox-based)":     "#9467bd",  # purple
    "Other":                 "#7f7f7f",  # gray
}

# Marker map - all circles, simpler
fig, axes = plt.subplots(1, 2, figsize=(12, 9), sharey=True)
fig.subplots_adjust(left=0.22, right=0.97, top=0.80, bottom=0.07, wspace=0.10)

y = np.arange(len(studies))[::-1]
labels = [s[0] for s in studies]
algs = [s[3] for s in studies]
colors = [color_map[a] for a in algs]

# ===== Left panel: Internal AUROC =====
ax = axes[0]
for i, (yi, s) in enumerate(zip(y, studies)):
    label, int_val, ext_val, alg = s
    color = color_map[alg]
    if int_val is not None:
        ax.plot(int_val, yi, marker='o', markersize=11, color=color,
                markeredgecolor='black', markeredgewidth=0.7, zorder=3)
    else:
        ax.text(0.77, yi, "AUROC not reported", fontsize=9,
                color='gray', style='italic', va='center', ha='center')

for v in [0.7, 0.8, 0.9]:
    ax.axvline(v, color='gray', linestyle=':', linewidth=0.8, alpha=0.6)

ax.set_yticks(y)
ax.set_yticklabels(labels, fontsize=10.5)
ax.set_ylim(-0.5, len(studies) - 0.5)
ax.set_xlim(0.55, 1.0)
ax.set_xlabel('AUROC (Internal Validation)', fontsize=11)
ax.set_title('A. Internal Validation', fontsize=12.5, fontweight='bold', loc='left')
ax.grid(axis='x', linestyle='--', alpha=0.3)
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

# ===== Right panel: External AUROC =====
ax = axes[1]
for i, (yi, s) in enumerate(zip(y, studies)):
    label, int_val, ext_val, alg = s
    color = color_map[alg]
    if ext_val is not None:
        ax.plot(ext_val, yi, marker='o', markersize=11, color=color,
                markeredgecolor='black', markeredgewidth=0.7, zorder=3)
    else:
        ax.text(0.77, yi, "External not reported", fontsize=9,
                color='gray', style='italic', va='center', ha='center')

for v in [0.7, 0.8, 0.9]:
    ax.axvline(v, color='gray', linestyle=':', linewidth=0.8, alpha=0.6)

ax.set_xlim(0.55, 1.0)
ax.set_ylim(-0.5, len(studies) - 0.5)
ax.set_xlabel('AUROC (External Validation)', fontsize=11)
ax.set_title('B. External Validation', fontsize=12.5, fontweight='bold', loc='left')
ax.grid(axis='x', linestyle='--', alpha=0.3)
for spine in ['top', 'right', 'left']:
    ax.spines[spine].set_visible(False)
ax.tick_params(left=False)

# Legend
legend_handles = [
    mpatches.Patch(color="#1f77b4", label="Random Forest (best model)"),
    mpatches.Patch(color="#d62728", label="XGBoost (best model)"),
    mpatches.Patch(color="#2ca02c", label="Logistic Regression (best model)"),
    mpatches.Patch(color="#ff7f0e", label="Other ensemble/regression"),
    mpatches.Patch(color="#9467bd", label="Cox-based survival"),
    mpatches.Patch(color="#7f7f7f", label="Other / AUROC not reported"),
]
fig.legend(handles=legend_handles, loc='upper center', ncol=3,
           bbox_to_anchor=(0.5, 0.95), frameon=False, fontsize=10)

fig.suptitle('Figure 6. Best-model AUROC by algorithm class across included studies',
             fontsize=13.5, fontweight='bold', y=0.99)

plt.savefig('figure6_v2.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.savefig('figure6_v2.pdf', bbox_inches='tight', facecolor='white')
plt.close()
print("Saved figure6_v2.png and .pdf")
print("\nData summary from Table 4:")
for s in studies:
    label, i, e, a = s
    print(f"  {label:30s} int={str(i):8s} ext={str(e):8s} alg={a}")
