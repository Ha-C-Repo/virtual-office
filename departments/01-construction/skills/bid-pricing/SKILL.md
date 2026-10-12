---
name: bid-pricing
description: Applies locked unit rates, assemblies, stage adders and the small-project override to a verified takeoff, and validates the payment structure against cash flow.
---
## When to use
After takeoff and completeness check have passed.

## Inputs
Verified takeoff, locked rate table, assembly library, drawing stage, scope (fab only, fab and erection, full package), tax rules.

## Steps
1. Confirm the rate table is the locked version. Rates are owned by the role named in the company profile; no session overrides.
2. Map takeoff rows to assemblies (materials, labor hours, equipment time, subcontract streams). Unknown rates emit TBD placeholders and a supplier-quote request (`../supplier-quote-tracker/SKILL.md`).
3. Fold engineering into fabrication and erection rates. Never create a separate engineering line.
4. Apply the stage adder and contingency from `../drawing-stage-classifier/SKILL.md`.
5. Apply the small-project override only if its trigger condition is met.
6. Run all arithmetic in the calculator. Record the rate basis on every line.
7. Validate the three-milestone payment structure against cash flow. The rationale stays internal.
8. Apply tax rules for the jurisdiction as configured.

## Outputs
Priced estimate lines (fields in `../../knowledge/schemas.md`), totals, cash-flow check, TBD list.

## Gates
- The model never sets a rate.
- Hand to bid-reviewer; do not release.
