---
name: job-costing-and-margin-review
description: Roll up job costs weekly per roof, compute margins and overhead through the harness, and review margin leakage monthly.
---
# Job Costing and Margin Review

## When to use
Weekly cost tagging, at job completion, and in the monthly review.

## Inputs
Job revenue (contract plus change orders), costs tagged to the job: labor, labor taxes, materials, subcontractors, disposal, permits, commissions, transportation, warranty reserve, workers compensation. Annual overhead and billable hours. Targets {{TARGET_GROSS_MARGIN}}, {{TARGET_NET_MARGIN}}.

## Steps
1. Tag every cost to a project weekly using `../../templates/job-cost-report.md`. Untagged cost is a finding.
2. Roll up: `python ../../harnesses/job_cost.py rollup --file job.json --overhead-hours H --overhead-rate R`.
3. Overhead per billable hour: `python ../../harnesses/job_cost.py overhead --annual-overhead A --billable-hours B`.
4. Workers compensation: payroll / 100 x rate per class code (`job_cost.py wc`); rates from the carrier (VERIFY).
5. Convert between margin and markup with `job_cost.py convert`; never use them interchangeably.
6. Compare estimate to actual. Look for leakage: unconfirmed material prices, verbal add-ons not invoiced, late sub costs, delayed final invoices, extra dump or permit fees, scope growth without change orders.
7. Check deposits (liabilities until earned), WIP position, receivables age and cash flow around insurance payment stages.
8. Review the warranty reserve against callback cost.
9. Write actions: price book updates, process fixes, crew coaching, collections.

## Outputs
Job cost reports, monthly margin review, leakage list, price book change requests.

## Gates
- Harness numbers win over model arithmetic.
- Gross margin planning range roughly 25 to 40 percent and net high single digits to low teens are illustrative; use the company's own books (VERIFY).
- Owner approves price changes and write-offs.
- Tax and bookkeeping questions go to `../../../09-business-admin-finance-compliance/README.md`.

Workflow: `../../workflows/14-monthly-job-costing-review.md`.
