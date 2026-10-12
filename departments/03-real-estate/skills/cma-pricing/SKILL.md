---
name: cma-pricing
description: CMA pricing protocol: record inventory, GLA sourcing, comps, adjustment grid, three price scenarios, gates. Use when preparing a listing price opinion.
---
# CMA Pricing

## When to use
Preparing a listing presentation, a price reduction review, or a buyer-side value check for {{PROPERTY_ADDRESS}}.

## Inputs
Classified listing documents (see `../listing-doc-classifier/SKILL.md`), public record extract, floor plan or sketch, photos, comp candidates with sources, {{AREA_OR_SUBDIVISION}}, market conditions note from the principal.

## Steps
1. Confirm the record set is complete. If anything required is missing, stop and list the gaps.
2. Source GLA by rank: records or measured sketch = HIGH; scaled floor plan image = MEDIUM; photo-inferred or assumed = LOW. Record the source and confidence beside the figure.
3. Select comps. Each needs address, sale price, GLA, sale date, source. Drop any comp missing one of these.
4. Build the adjustment grid (comp to subject) with a calculator or script. Never do arithmetic in prose.
5. Compute the comp corridor (price per square foot range) with the script.
6. Produce three scenarios: aggressive, recommended, floor. State the basis for each.
7. Run `../cma-sanity-check/SKILL.md`.
8. Fill `../../templates/cma-report.md`. Keep net sheet math in `../../templates/net-sheet-internal.md` (internal only).

## Outputs
CMA report with comp grid and scenarios; internal net sheet; gap list; confidence tags on every figure.

## Gates
- No pricing from an incomplete record set.
- Any value sourced from the public web is LOW and cannot set a fact, comp or valuation.
- The principal approves the recommended price. The CMA is an opinion of value, not an appraisal, and says so.
