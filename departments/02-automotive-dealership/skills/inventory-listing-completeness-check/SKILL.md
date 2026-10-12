---
name: inventory-listing-completeness-check
description: Runs the vehicle output gate and reports each check PASS, FAIL or SKIP before a listing is published.
---
## Checks
1. VIN reconciles (decode versus documents and photos).
2. Title status stated.
3. Odometer stated with source.
4. Defects present in copy and photographed.
5. Buyer's guide generated and consistent with the listing.
6. No banned phrase (single blocklist, fail-closed).
7. Financing figures carry the full disclosure block.
8. No generated imagery.
9. No superlative.
10. Specificity: at least one of year, mileage, price, stock number.
11. Price passes the sanity check.
12. Client document has its `-INT` twin.

## Steps
Run in order. Report the exit code observed (0 clean, 1 blocked, 2 input error). SKIP rows are coverage holes and must be explained.

## Outputs
Gate report with per-check result.

## Gates
Clean gates over LOW-confidence input is still a LOW-confidence deliverable; say so. No override flags.
