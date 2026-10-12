---
name: inventory-pricing-sanity-check
description: Mechanical four-gate review of an already-set price with a confidence score.
---
## Gates
1. **Price versus comp corridor.** No corridor is CAUTION.
2. **Mileage sourced.** None = BLOCK. Low-tier source = FLAG. Mid-tier = CAUTION.
3. **Price versus named, dated book value.**
4. **Package completeness** (record, documents, photos, disclosures).

## Scoring
Start at 100. Minus 40 per BLOCK, minus 20 per FLAG, minus 10 per CAUTION.

## Steps
1. Run each gate against the unit record.
2. Report each gate with its observed result.
3. Return the score and the blockers.

## Gates on the gates
A bypass is the same mistake as bypassing the blocklist. There is no override flag. The check does not change the price.
