---
name: bid-reconciliation
description: Advisory coverage diff of the estimate against the requirement and exclusion registers. Reports gaps, orphans, double-counts, arithmetic, unit and rate-band issues.
---
## When to use
Before release, in a fresh session with no memory of the estimating work.

## Inputs
Requirement register, inclusions and exclusions, estimate lines with rate basis, rate-band library.

## Steps
1. Gap: a requirement with no priced line and no exclusion.
2. Orphan: an estimate line citing no requirement.
3. Double-count: two lines covering the same requirement.
4. Arithmetic: recompute extended = qty x unit_rate with the calculator.
5. Unit: unit mismatch between requirement, takeoff and estimate.
6. Rate band: rate outside p25 to p75, or outside floor and ceiling.
7. Verdict: READY or NOT READY.

## Outputs
Reconciliation report (status Gap / Orphan / ok, issues, verdict), optionally rendered as a dashboard.

## Gates
Advisory only. It never sets the price and never edits the estimate.
