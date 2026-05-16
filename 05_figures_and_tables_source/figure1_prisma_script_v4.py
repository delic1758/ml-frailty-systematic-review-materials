"""
Regenerate Figure 1 PRISMA flowchart - v4 (post-screening-log alignment).

v2 changes: replaced "Unexcluded duplicates at preliminary stage" with
"Additional duplicates identified during detailed screening".
v3 changes: removed slash construction; clarified vague reference.
v4 changes: aligned full-text exclusion subcategory counts with the per-study
data recorded in the GitHub screening log (02_screening_records/
fulltext_excluded_studies.xlsx). Previously 7/4/3/2; now 8/4/2/2. Total of
16 full-text exclusions is unchanged. The single reclassified study was a
small-sample report whose age-inclusion criterion was at the ≥60 boundary;
upon careful re-examination it satisfies only the sample-size exclusion
criterion (not both), and is therefore counted under "Sample size <1,000
only" rather than "Both sample-size and age criteria".

Arithmetic preserved: 2,881 - 90 - 2,728 = 63; 63 - 33 = 30; 30 - 16 = 14.
8 + 4 + 2 + 2 = 16.
"""
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(10, 12), dpi=200)
ax.set_xlim(0, 100)
ax.set_ylim(0, 130)
ax.axis('off')

# Header
header = FancyBboxPatch((5, 122), 90, 6,
                        boxstyle="round,pad=0.4",
                        linewidth=1.0, edgecolor='black',
                        facecolor='#F4B66B')
ax.add_patch(header)
ax.text(50, 125, "Identification of studies via databases and registers",
        ha='center', va='center', fontsize=13, fontweight='bold')

# Phase labels (left bar)
def phase_label(y_center, height, text):
    bar = FancyBboxPatch((0, y_center - height/2), 4, height,
                         boxstyle="round,pad=0.2",
                         linewidth=0.6, edgecolor='black',
                         facecolor='#9BC4E2')
    ax.add_patch(bar)
    ax.text(2, y_center, text, ha='center', va='center',
            fontsize=10, fontweight='bold', rotation=90)

phase_label(108, 25, "Identification")
phase_label(60,  60, "Screening")
phase_label(13,  15, "Included")

def box(x, y, w, h, text, fontsize=9.5):
    r = FancyBboxPatch((x, y), w, h,
                       boxstyle="round,pad=0.3",
                       linewidth=1.0, edgecolor='black',
                       facecolor='white')
    ax.add_patch(r)
    ax.text(x + w/2, y + h/2, text,
            ha='center', va='center', fontsize=fontsize)

def arrow(x1, y1, x2, y2):
    a = FancyArrowPatch((x1, y1), (x2, y2),
                        arrowstyle='->', mutation_scale=15,
                        color='black', linewidth=1.0)
    ax.add_patch(a)

# === IDENTIFICATION ===
box(8, 100, 50, 14,
    "Records identified from:\n"
    "  Databases (n = 2,881)\n"
    "    PubMed (n = 65)\n"
    "    Embase (n = 39)\n"
    "    Web of Science (n = 35)\n"
    "    Scopus (n = 2,742)")

box(62, 100, 35, 14,
    "Records removed before\n"
    "detailed screening:\n"
    "  Duplicate records removed (n = 90)\n"
    "  Records excluded by automated filters\n"
    "  and preliminary screening (n = 2,728)")

arrow(58, 107, 62, 107)
arrow(33, 100, 33, 76)

# === SCREENING - level 1: records retained for detailed screening ===
box(8, 65, 50, 11,
    "Records retained for detailed\n"
    "title and abstract screening\n"
    "(n = 63)")

box(62, 60, 35, 18,
    "Records excluded** (n = 33):\n"
    "  Additional duplicates identified\n"
    "    during detailed screening (n = 3)\n"
    "  Other unrelated topics (n = 7)\n"
    "  Hospital-based studies (n = 15)\n"
    "  Not original research\n"
    "    (reviews, protocols,\n"
    "     opinions, etc.) (n = 6)\n"
    "  Not related to frailty (n = 2)")

arrow(58, 70, 62, 70)
arrow(33, 65, 33, 49)

# === SCREENING - level 2: full-text assessed ===
box(8, 38, 50, 11,
    "Reports assessed for eligibility\n"
    "(n = 30)")

# v4 UPDATE: full-text exclusion subcategory counts now match per-study
# data in 02_screening_records/fulltext_excluded_studies.xlsx
box(62, 32, 35, 18,
    "Reports excluded (n = 16):\n"
    "  Sample size < 1,000 only\n"
    "    (n = 8)\n"
    "  Population aged < 60 years\n"
    "    only (n = 4)\n"
    "  Both sample-size and age\n"
    "    criteria (n = 2)\n"
    "  Published in non-SCI(E)-\n"
    "    indexed journals (n = 2)")

arrow(58, 43, 62, 43)
arrow(33, 38, 33, 21)

# === INCLUDED ===
box(8, 8, 50, 12,
    "Studies included in review\n"
    "(n = 14)")

ax.text(50, 2,
        "**Records excluded during detailed title and abstract screening.",
        ha='center', va='center', fontsize=8, style='italic')

plt.subplots_adjust(left=0.02, right=0.98, top=0.98, bottom=0.02)
plt.savefig('Figure1_PRISMA_v4.png', dpi=200, bbox_inches='tight',
            facecolor='white')
plt.close()
print("Saved Figure1_PRISMA_v4.png")
