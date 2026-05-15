# Scopus — Search Strategy

**Database:** Scopus (Elsevier)
**Search execution date:** July 4, 2025
**Records retrieved:** 2,742

---

## Boolean search string

```
("Frailty" OR "Pre-frailty" OR "Cognitive Frailty" OR "Physical Frailty")
AND
("Machine learning" OR "Artificial Intelligence" OR "Deep learning"
 OR "Predictive Model" OR "Prediction Model" OR "Classification Model")
AND
("Community-dwelling older adults" OR "Community-living older adults"
 OR "Community-dwelling elderly" OR "Older adults living in community")
```

## Search scope

- **Search field:** "All field"

## Filters applied

| Filter | Value |
|---|---|
| Publication years (box check) | 2015–2025 |
| Document type | Article |
| Language | English |

## Notes on year filter

Only year-level box-check filters were available via the Scopus interface; no month- or day-level filters were applied.

- No records were retrieved prior to 2019 in any iteration, so the box-check range 2015–2025 captures all records that would have been eligible under the prespecified 2015-01-01 to 2025-06-30 window.
- After verifying publication dates, studies published after June 30, 2025 were manually excluded prior to title and abstract screening.

## Note on record count

Scopus returned a substantially larger record set than the other primary databases (2,742 vs 35–65). This is consistent with Scopus's broader "All field" search scope, which retrieves matches in author keywords, indexed terms, and bibliographic references. The large initial pool was reduced through downstream eligibility screening; the PRISMA flow is documented in `../02_screening_records/prisma_flow_data.csv`.

## Conceptual domain structure

Identical three-domain structure as the primary search (see `pubmed_search_strings.md`).
