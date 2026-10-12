# Harnesses

Three small, stdlib-only Python 3 tools. They exist for one reason: **verify, do not generate**. When a skill needs a quantity, a payment or a margin, the harness result wins over any arithmetic done by a model. If the harness and a model disagree, the harness is right until the inputs are shown to be wrong.

Run from this folder. Each file has built-in tests:

```
python takeoff_calc.py --selftest
python claim_math.py --selftest
python job_cost.py --selftest
```

Exit code 0 means success, 2 means bad input.

## takeoff_calc.py
Pitch factor (sqrt(rise^2 + run^2) / run), sloped area from a footprint, squares, ordering squares with waste, shingle bundles (rounded up), starter bundles, ridge cap bundles, drip edge sticks with lap allowance, underlayment rolls.

Example (the selftest case): 40 by 30 footprint, 6/12, 10 percent waste, 3 bundles per square gives 13.416 roof squares, 14.758 ordering squares, 45 bundles.

```
python takeoff_calc.py --length 40 --width 30 --rise 6 --waste 10 --bundles-per-square 3 --eave-lf 80 --rake-lf 33.54 --ridge-lf 40
```
Coverage defaults (starter, ridge, drip edge stick length, roll coverage) are planning values. VERIFY against the data sheet and supplier; change them with arguments. Waste percent is an input, never a hidden default for the customer.

Called by: `../skills/roof-takeoff-calculator/SKILL.md`, `../skills/material-order-builder/SKILL.md`, `../skills/estimate-builder-tiered/SKILL.md`, `../skills/aerial-measurement-verification/SKILL.md`.

## claim_math.py
RCV, depreciation (by amount or percent), ACV, deductible, recoverable depreciation, supplement totals and expected payment stages. Uses decimal arithmetic. The selftest uses the illustrative 30,000 RCV, 10,000 depreciation case (ACV 20,000 before deductible). Note: 33 percent of 30,000 is 9,900; the illustrative 10,000 is one third, so enter amounts when the carrier gives amounts.

```
python claim_math.py --rcv 30000 --dep-amount 10000 --deductible 2000 --supplement 1500
```
It is arithmetic only. It does not interpret policies. Whether depreciation is recoverable, whether O&P applies, and deadlines come from the policy and state rules (VERIFY).

Called by: `../skills/acv-rcv-depreciation-math/SKILL.md`, `../skills/insurance-claim-support/SKILL.md`, `../skills/scope-comparison-and-supplement/SKILL.md`.

## job_cost.py
Subcommands: `rollup` (direct costs, gross profit, gross margin, markup, overhead absorption, net), `convert` (margin to markup and back), `price` (price for a target margin), `overhead` (annual overhead per billable hour), `wc` (workers compensation premium = payroll / 100 x rate).

```
python job_cost.py convert --margin 30
python job_cost.py price --cost 10000 --margin 32
python job_cost.py overhead --annual-overhead 240000 --billable-hours 6000
python job_cost.py wc --payroll 50000 --rate 12.5
```
Selftest figures are illustrative. Real rates and targets are `{{PLACEHOLDERS}}` supplied by the owner.

Called by: `../skills/job-costing-and-margin-review/SKILL.md`, `../skills/estimate-builder-tiered/SKILL.md`.

## How skills call them
1. The skill collects the inputs and writes them into the project file with the source of each.
2. The skill runs the harness command and pastes the output into the deliverable with the command used.
3. A reviewer re-runs the command before sign-off.
4. If an input is unknown, the skill leaves the placeholder and asks. It does not guess.

## Changing a harness
Edit the code, add or update an assertion in `selftest()`, and run all three selftests. Never change a default silently; record the reason in the file header and in `../knowledge/research-notes.md`.
