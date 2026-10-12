---
name: inventory-pricing-appraisal
description: Produces a market corridor, recommended price and floor from at least three sourced comparables and a named, dated book value, using the calculator only.
---
## When to use
After the unit record is graded and before listing or trade-in offers.

## Inputs
Comparables (source, date, mileage, price), book value (named source and date), unit record.

## Steps
1. Require at least three sourced comps. Fewer is a refusal, not an estimate (`../../templates/inventory-comp-grid.md`).
2. Calculator: corridor from the comps; recommended price = median blended with the named book value if present.
3. Floor = the higher of 8 percent below the recommendation or 5 percent below the corridor minimum (use the owner-locked tolerance if set).
4. Grade is recorded but never moves the arithmetic.
5. Aged-inventory markdown is a report with a simulation. A human decides.

## Outputs
Corridor, recommendation, floor, comp grid, confidence.

## Gates
The model never sets the number. The owner (one named human) owns the price. No web research for comps or valuation beyond permitted purchased sources.
