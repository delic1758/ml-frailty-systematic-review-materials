"""
Figure 6: Best-model AUROC by algorithm class across included studies.

This figure visualizes the best-model AUROC reported by each of the 14 included
studies, color-coded by the algorithm class that achieved the best performance.
Two panels show internal and external AUROC where reported.

DATA SOURCE
===========
All values are loaded from figure6_source_data.csv in this same folder. The CSV
in turn was derived from Table 4 of the present systematic review and the
prespecified data-extraction sheet (14 studies x 36 variables = 504 data
points). Values not reported in an original study are left empty in the CSV and
rendered as "AUROC not reported" / "External not reported" in the figure.

For studies that reported only a best-model AUROC without explicitly listing
RF and XGBoost performance, only the best-model value is plotted. This is the
faithful representation of the reported evidence.

RATIONALE
=========
Reviewer 3 requested a forest-style subgroup analysis for AUROC values across
the most commonly used models (RF, XGBoost). Because most included studies
reported only the best-performing model's AUROC rather than separate AUROCs
for each algorithm tested, the most evidence-faithful presentation is to plot
each study's best-model AUROC and indicate which algorithm class achieved it.

USAGE
=====
    python figure6_script.py
produces Figure6_AUROC_by_algorithm.png (and .pdf) in the current directory.
CSV is expected at ./figure6_source_data.csv.
"""
import csv
import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ---------- Load data from CSV ----------
csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "figure6_source_data.csv")

studies = []
with open(csv_path, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        label = row["study"].strip()
        internal = row.get("internal_auroc", "").strip()
        external = row.get("external_auroc", "").strip()
        algo = row.get("best_algorithm_class", "").strip()
        int_val = float(internal) if internal not in ("", "NA", "NR") else None
        ext_val = float(external) if external not in ("", "NA", "NR") else None
        studies.append((label, int_val, ext_val, algo))

# ---------- Color mapping for algorithm classes ----------
color_map = {
    "Random Forest":           "#1f77b4",
    "XGBoost":                 "#d62728",
    "Logistic Regression":     "#2ca02c",
    "Other (Poisson)":         "#ff7f0e",
    "Other (GLMM)":            "#ff7f0e",
    "Other (CatBoost)":        "#ff7f0e",
    "Other (Cox-based)":       "#9467bd",
    "Other":                   "#7f7f7f",
}

# ---------- Plot ----------
fig, axes = plt.subplots(1, 2, figsize=(12, 9), sharey=True)
fig.subplots_adjust(left=0.22, right=0.97, top=0.80, bottom=0.07, wspace=0.10)

y = np.arange(len(studies))[::-1]
labels = [s[0] for s in studies]

# --- Left panel: Internal AUROC ---
ax = axes[0]
for yi, (label, int_val, ext_val, alg) in zip(y, studies):
    color = color_map.get(alg, "#7f7f7f")
    if int_val is not None:
        ax.plot(int_val, yi, marker="o", markersize=11, color=color,
                markeredgecolor="black", markeredgewidth=0.7, zorder=3)
    else:
        ax.text(0.77, yi, "AUROC not reported", fontsize=9,
                color="gray", style="italic", va="center", ha="center")

for v in [0.7, 0.8, 0.9]:
    ax.axvline(v, color="gray", linestyle=":", linewidth=0.8, alpha=0.6)

ax.set_yticks(y)
ax.set_yticklabels(labels, fontsize=10.5)
ax.set_ylim(-0.5, len(studies) - 0.5)
ax.set_xlim(0.55, 1.0)
ax.set_xlabel("AUROC (Internal Validation)", fontsize=11)
ax.set_title("A. Internal Validation", fontsize=12.5, fontweight="bold", loc="left")
ax.grid(axis="x", linestyle="--", alpha=0.3)
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

# --- Right panel: External AUROC ---
ax = axes[1]
for yi, (label, int_val, ext_val, alg) in zip(y, studies):
    color = color_map.get(alg, "#7f7f7f")
    if ext_val is not None:
        ax.plot(ext_val, yi, marker="o", markersize=11, color=color,
                markeredgecolor="black", markeredgewidth=0.7, zorder=3)
    else:
        ax.text(0.77, yi, "External not reported", fontsize=9,
                color="gray", style="italic", va="center", ha="center")

for v in [0.7, 0.8, 0.9]:
    ax.axvline(v, color="gray", linestyle=":", linewidth=0.8, alpha=0.6)

ax.set_xlim(0.55, 1.0)
ax.set_ylim(-0.5, len(studies) - 0.5)
ax.set_xlabel("AUROC (External Validation)", fontsize=11)
ax.set_title("B. External Validation", fontsize=12.5, fontweight="bold", loc="left")
ax.grid(axis="x", linestyle="--", alpha=0.3)
for spine in ["top", "right", "left"]:
    ax.spines[spine].set_visible(False)
ax.tick_params(left=False)

# --- Legend ---
legend_handles = [
    mpatches.Patch(color="#1f77b4", label="Random Forest (best model)"),
    mpatches.Patch(color="#d62728", label="XGBoost (best model)"),
    mpatches.Patch(color="#2ca02c", label="Logistic Regression (best model)"),
    mpatches.Patch(color="#ff7f0e", label="Other ensemble/regression"),
    mpatches.Patch(color="#9467bd", label="Cox-based survival"),
    mpatches.Patch(color="#7f7f7f", label="Other / AUROC not reported"),
]
fig.legend(handles=legend_handles, loc="upper center", ncol=3,
           bbox_to_anchor=(0.5, 0.95), frameon=False, fontsize=10)

fig.suptitle("Figure 6. Best-model AUROC by algorithm class across included studies",
             fontsize=13.5, fontweight="bold", y=0.99)

# --- Output (filenames match repository) ---
plt.savefig("Figure6_AUROC_by_algorithm.png", dpi=300, bbox_inches="tight",
            facecolor="white")
plt.savefig("Figure6_AUROC_by_algorithm.pdf", bbox_inches="tight", facecolor="white")
plt.close()

print("Saved Figure6_AUROC_by_algorithm.png and .pdf")
print(f"\nData summary loaded from {os.path.basename(csv_path)}:")
for label, i, e, a in studies:
    print(f"  {label:30s} int={str(i):8s} ext={str(e):8s} alg={a}")
