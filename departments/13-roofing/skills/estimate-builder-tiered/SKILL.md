---
name: estimate-builder-tiered
description: Build good/better/best line-item estimates from verified quantities and the price book, with margin checks and a fast turnaround.
---
# Estimate Builder (Tiered)

## When to use
After inspection and verified measurement, for retail re-roofs, repairs and insured jobs (line-item format).

## Inputs
Verified takeoff, product lines per tier, price book ({{PRICE_BOOK}}), labor rates ({{LABOR_RATES}}), disposal and permit fees, markup/margin target ({{LOCAL_MARKUP}}, {{TARGET_GROSS_MARGIN}}), measurement variance, photo log.

## Steps
1. Define three tiers by product and system, for example a standard tier, an upgraded tier, and a premium tier with system warranty eligibility (check certified installer requirement, `../warranty-registration-and-tracker/SKILL.md`).
2. Build line items for each tier: tear-off (layers), deck allowance and unit price for replacement decking, underlayment, ice barrier where required, drip edge, starter, shingles, ridge, vents/ventilation correction, pipe boots, flashing, chimney/skylight work, cleanup, disposal, permit.
3. Quantities from `../roof-takeoff-calculator/SKILL.md`. Never retype them.
4. Costs from the price book. If a price is unknown or unconfirmed, leave `{{PRICE}}` and ask; unconfirmed material prices are a margin leak.
5. Compute price from cost and target margin with `python ../../harnesses/job_cost.py price --cost C --margin M`, and confirm margin versus markup with `convert`. Do not set price by adding the margin as a markup.
6. Write unknowns as allowances or unit prices with a change-order trigger (hidden decking, code items).
7. Fill `../../templates/estimate-good-better-best.md`. Keep a copy of the cost build-up internal; the customer sees price and scope only.
8. Turnaround: send within {{ESTIMATE_TURNAROUND}}. Long delays lose jobs; track `days_to_estimate`.

## Outputs
Three-tier estimate, internal cost build-up, margin check.

## Gates
- Owner approves estimates above {{ESTIMATE_APPROVAL_THRESHOLD}} and any margin below {{MIN_MARGIN}}.
- Insured jobs: no price is set from the claim amount alone; do not mention the deductible as an adjustable item (`../deductible-and-inducement-gate/SKILL.md`).
- No fabricated prices; illustrative ranges are labeled illustrative.
