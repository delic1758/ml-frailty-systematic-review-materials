"""
Figure 4. Highest-reported AUROC values, stratified by task type and algorithm.

Two panels (Classification vs. Incident prediction) plot the highest-reported
AUROC value for each (study × algorithm) cell, colour-coded by validation type
(internal vs. same-cohort temporal vs. independent external).

Inputs
------
figure4_source_data.csv  — long-format AUROC values per study × algorithm × validation type.

Outputs
-------
Figure4_AUROC_by_algorithm.png, .pdf, .svg

Notes
-----
1. The single trajectory-prediction study (Wu et al. 2022) is recorded in the
   CSV with task_type = "Trajectory prediction" but is NOT plotted, because
   trajectory prediction is incommensurable with binary classification /
   incident prediction AUROC. See manuscript Section 3.5 and Figure 4 caption.

2. Peng et al. (2020) and Gomez-Cabrero et al. (2021) reported no comparable
   AUROC (HR-based survival and biomarker OR / SESv respectively) and are
   therefore excluded from the plot.

3. Validation type definitions (manuscript Section 2.3):
     - Internal:     resampling / cross-validation / random split within the
                     development cohort.
     - Temporal:     validation in a later wave of the SAME parent cohort
                     (e.g., a subsequent CHARLS or ELSA wave).
     - External:     validation in a geographically or institutionally distinct
                     cohort (e.g., Dong et al. 2025 external validation in
                     independent cohorts; Isaradech et al. 2025 in an independent
                     external cohort).

4. Dependencies: matplotlib, numpy, adjustText, pandas.
"""

import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from adjustText import adjust_text

HERE = os.path.dirname(os.path.abspath(__file__))
CSV  = os.path.join(HERE, "figure4_source_data.csv")

# ---------- Load and filter ----------
df = pd.read_csv(CSV)
# Drop rows without AUROC (Peng, Gomez-Cabrero)
df = df.dropna(subset=["auroc"])
# Exclude trajectory prediction from the AUROC panels
df = df[df["task_type"].isin(["Classification", "Incident prediction"])].copy()
# Short study label for plotting (first author + year clue)
df["label"] = df["study"].str.replace(r" et al\.", "", regex=True).str.replace(r" \(20", " 20", regex=True).str.rstrip(")")

# ---------- Plot config ----------
COLOUR = {"Internal": "#7F7F7F", "Temporal": "#2E75B6", "External": "#C00000"}
MARKER = {"Internal": "o",       "Temporal": "s",       "External": "^"}
TITLES = {
    "Classification":      "(a) Classification of current frailty status",
    "Incident prediction": "(b) Incident prediction of future frailty",
}

def algo_order(panel_df):
    counts = panel_df["algorithm"].value_counts()
    return list(counts.sort_values(ascending=False).index)

FIG_W, FIG_H = 5.31, 3.08   # inches; matches manuscript embed (13.5 × 7.8 cm)
fig, axes = plt.subplots(1, 2, figsize=(FIG_W, FIG_H), sharey=True)
rng = np.random.default_rng(seed=42)

for ax, panel in zip(axes, ["Classification", "Incident prediction"]):
    sub = df[df["task_type"] == panel].copy()
    algos = algo_order(sub)
    xpos = {a: i for i, a in enumerate(algos)}

    text_objs = []
    for _, row in sub.iterrows():
        x = xpos[row["algorithm"]] + rng.uniform(-0.07, 0.07)
        v = row["validation_type"]
        ax.scatter(x, row["auroc"],
                   c=COLOUR[v], marker=MARKER[v],
                   s=32, edgecolors="black", linewidths=0.4, zorder=3)
        # Short label for points (drop "et al.")
        label_short = str(row["study"]).split(" et al.")[0]
        # Add year for the two Liu / Zhang / Jung duplicates
        if "(" in str(row["study"]):
            year = str(row["study"]).split("(")[1].rstrip(")")
            label_short = f"{label_short} {year}"
        text_objs.append(
            ax.text(x, row["auroc"], label_short,
                    fontsize=5.2, color="black", alpha=0.9, zorder=4)
        )

    # Alternating algorithm-column shading
    for i in range(len(algos)):
        if i % 2 == 0:
            ax.axvspan(i - 0.4, i + 0.4, color="#F5F5F5", zorder=1)

    ax.set_xticks(range(len(algos)))
    ax.set_xticklabels(algos, fontsize=6.5)
    ax.set_xlim(-0.55, len(algos) - 0.5 + 0.25)
    ax.set_ylim(0.55, 1.00)
    ax.set_title(TITLES[panel], fontsize=7, fontweight="bold", pad=3)
    ax.grid(True, axis="y", alpha=0.3, linestyle="--", zorder=0)
    ax.tick_params(axis="both", which="major", labelsize=6)
    ax.set_axisbelow(True)

    adjust_text(
        text_objs, ax=ax,
        arrowprops=dict(arrowstyle="-", color="gray", alpha=0.5, lw=0.3),
        expand=(1.3, 1.4),
        force_text=(0.6, 0.8),
        force_static=(0.4, 0.5),
        max_move=12,
    )

axes[0].set_ylabel("Highest-reported AUROC", fontsize=7)
fig.suptitle("Highest-reported AUROC, stratified by task type and algorithm",
             fontsize=7.5, fontweight="bold", y=0.98)

handles = [
    Line2D([0], [0], marker="o", color="w", markerfacecolor=COLOUR["Internal"],
           markeredgecolor="black", markersize=5, label="Internal validation only"),
    Line2D([0], [0], marker="s", color="w", markerfacecolor=COLOUR["Temporal"],
           markeredgecolor="black", markersize=5, label="Same-cohort temporal validation"),
    Line2D([0], [0], marker="^", color="w", markerfacecolor=COLOUR["External"],
           markeredgecolor="black", markersize=5, label="Independent external validation"),
]
fig.legend(handles=handles, loc="lower center", ncol=3,
           bbox_to_anchor=(0.5, 0.0), frameon=False, fontsize=6)

plt.subplots_adjust(left=0.10, right=0.97, bottom=0.17, top=0.86, wspace=0.10)

for ext in (".png", ".pdf", ".svg"):
    fig.savefig(os.path.join(HERE, f"Figure4_AUROC_by_algorithm{ext}"),
                dpi=300 if ext == ".png" else None, facecolor="white")
plt.close()
print("Wrote Figure4_AUROC_by_algorithm.{png,pdf,svg}")
