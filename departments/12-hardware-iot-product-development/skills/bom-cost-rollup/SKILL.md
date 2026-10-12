---
name: bom-cost-rollup
description: Build a BOM with quoted costs and roll it up to unit cost, landed cost and margin using the script.
---
# BOM Cost Rollup

## When to use
Pricing a design, comparing options in a design lock, preparing investor unit economics, or checking a supplier change.

## Inputs
`../../templates/bom.md`, supplier quotes (with date and expiry), assembly and test cost estimates, freight and duty estimates, target price.

## Steps
1. List every part, assembly step and packaging item. One row each, with quantity per unit.
2. Enter price breaks by volume tier from the quote. Record quote date and expiry.
3. Add non-part costs: assembly, test, freight, duty, warranty reserve, scrap allowance.
4. Run `python ../../harnesses/bom_rollup.py rollup --file bom.json --volume <n>`.
5. Compare to the target price and margin. List the top five cost drivers.
6. Mark each figure: quote, estimate, or target.

## Outputs
Unit cost table by volume tier, margin vs target, cost driver list, stale-quote list.

## Gates
Principal reviews before a cost figure goes into an investor document. Targets are never shown as quotes.
