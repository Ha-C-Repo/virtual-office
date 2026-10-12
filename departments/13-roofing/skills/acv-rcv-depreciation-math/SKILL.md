---
name: acv-rcv-depreciation-math
description: Compute RCV, depreciation, ACV, deductible, recoverable depreciation and expected payment stages with the claim math harness.
---
# ACV / RCV / Depreciation Math

## When to use
Any time a claim payment, homeowner out-of-pocket, or expected next check is explained or tracked.

## Inputs
RCV from the carrier scope, depreciation amount or percent, deductible, approved supplements, whether depreciation is recoverable, whether O&P applies. All from the carrier documents or policy.

## Definitions
- RCV: replacement cost value.
- ACV = RCV minus depreciation.
- Initial payment = ACV minus deductible.
- Recoverable depreciation: paid after completion and documentation, within policy deadlines (VERIFY).
- Illustrative example: RCV 30,000, depreciation 10,000 (about one third), ACV 20,000 before deductible.

## Steps
1. Collect inputs. Do not estimate depreciation yourself; take it from the carrier statement.
2. Run: `python ../../harnesses/claim_math.py --rcv R --dep-amount A --deductible D [--supplement S ...] [--op-pct P] [--non-recoverable] --json`.
3. Paste the result and the command into `../../templates/acv-rcv-tracker.md`.
4. Explain it in plain language: what has been paid, what is held back, what the homeowner owes, what is expected after completion.
5. Update after each payment or supplement; re-run, do not adjust by hand.

## Outputs
Tracker rows with stage amounts and the harness command.

## Gates
- Harness output wins over model arithmetic (`../../harnesses/README.md`).
- This is arithmetic, not a coverage opinion. Policy terms control (VERIFY).
- A percent entered as 33 gives 9,900 on 30,000; enter the carrier's dollar amount when given.
- Never describe the deductible as negotiable by the contractor.
