---
name: bid-sanity-check
description: Cross-checks a priced bid with two independent methods, benchmark bands and rate divergence flags before any document is produced.
---
## When to use
After pricing, before composing documents.

## Inputs
Priced estimate, takeoff summary, benchmark bands by building type, locked baseline rates.

## Steps
1. Path A: bottom-up total from takeoff and rates. Path B: top-down from intensity (weight per square foot) and price per ton or per square foot in the benchmark band.
2. Compare. Within tolerance: pass. Over 10 percent divergence: STOP and re-take-off. Do not footnote.
3. Band check: intensity and price against the p25 and p75 of the building type, with floor and ceiling.
4. Rate divergence: flag any line rate outside tolerance from the locked baseline.
5. Completeness: confirm the takeoff-completeness-check passed.
6. Flag low-confidence area and show the contingency carried.

## Outputs
Gate table with PASS / FLAG / BLOCK per gate and a confidence score (minus 40 per BLOCK, minus 20 per FLAG, minus 10 per CAUTION).

## Gates
No bypass argument exists. A bypass is the same mistake as skipping the output scrubber.
