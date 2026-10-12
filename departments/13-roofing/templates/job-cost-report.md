# Job Cost Report

Project {{PROJECT_NAME}} | Contract {{CONTRACT_ID}} | Week ending {{WEEK_ENDING}} | Prepared by {{PREPARER}}

Run rollup: `python ../harnesses/job_cost.py rollup --file job.json --overhead-hours {{LABOR_HOURS}} --overhead-rate {{OVERHEAD_RATE}}`

## Revenue
Contract {{CONTRACT_PRICE}} | Change orders {{CHANGE_ORDER_TOTAL}} | Recognized to date {{REVENUE_RECOGNIZED}} | Deposit held as liability {{DEPOSIT_LIABILITY}}

## Direct costs (tagged to this job)
| Category | Estimate | This week | To date | Variance |
|---|---|---|---|---|
| Labor | {{EST}} | {{WEEK}} | {{TODATE}} | {{VAR}} |
| Labor taxes | {{EST}} | {{WEEK}} | {{TODATE}} | {{VAR}} |
| Materials | {{EST}} | {{WEEK}} | {{TODATE}} | {{VAR}} |
| Subcontractors | {{EST}} | {{WEEK}} | {{TODATE}} | {{VAR}} |
| Disposal | {{EST}} | {{WEEK}} | {{TODATE}} | {{VAR}} |
| Permits | {{EST}} | {{WEEK}} | {{TODATE}} | {{VAR}} |
| Commissions | {{EST}} | {{WEEK}} | {{TODATE}} | {{VAR}} |
| Transportation | {{EST}} | {{WEEK}} | {{TODATE}} | {{VAR}} |
| Warranty reserve | {{EST}} | {{WEEK}} | {{TODATE}} | {{VAR}} |
| Workers compensation | {{EST}} | {{WEEK}} | {{TODATE}} | {{VAR}} |

## Results (from the harness)
Gross profit {{GROSS_PROFIT}} | Gross margin {{GROSS_MARGIN}} (target {{TARGET_GROSS_MARGIN}}) | Markup on cost {{MARKUP}} | Overhead absorbed {{OVERHEAD_ABSORBED}} | Net after overhead {{NET}} | Net margin {{NET_MARGIN}}

## Leakage check
- [ ] Material prices confirmed
- [ ] Verbal add-ons invoiced
- [ ] Late sub costs captured
- [ ] Dump and permit fees captured
- [ ] Final invoice issued on time

Notes {{NOTES}}. Reviewed by {{FINANCE_CONTROLLER}}; approved by {{OWNER}}.
