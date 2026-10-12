# ACV / RCV Tracker

Claim {{CLAIM_NUMBER}} | Carrier {{CARRIER}} | Property {{PROPERTY_ADDRESS}} | Updated {{DATE}} by {{PREPARER}}

All figures from carrier documents. Computations come from the harness: `python ../harnesses/claim_math.py --rcv {{RCV}} --dep-amount {{DEPRECIATION}} --deductible {{DEDUCTIBLE}} --json`

## Position
| Item | Amount | Source |
|---|---|---|
| RCV (scope) | {{RCV}} | {{CARRIER_DOC_REF}} |
| Depreciation | {{DEPRECIATION}} | {{CARRIER_DOC_REF}} |
| ACV | {{ACV}} | harness |
| Deductible | {{DEDUCTIBLE}} | policy |
| Supplements approved (RCV) | {{SUPPLEMENTS}} | letters |
| Recoverable depreciation expected | {{RECOVERABLE}} | harness |
| Total expected payments | {{TOTAL_EXPECTED}} | harness |

## Payments received
| Stage | Date | Amount | Payees on check | Mortgagee endorsement needed (y/n) | Deposited |
|---|---|---|---|---|---|
| Initial ACV | {{DATE}} | {{AMOUNT}} | {{PAYEES}} | {{YES_NO}} | {{DEPOSIT_DATE}} |
| Supplement {{N}} | {{DATE}} | {{AMOUNT}} | {{PAYEES}} | {{YES_NO}} | {{DEPOSIT_DATE}} |
| Recoverable depreciation | {{DATE}} | {{AMOUNT}} | {{PAYEES}} | {{YES_NO}} | {{DEPOSIT_DATE}} |

## Supplements
| No. | Submitted | Items | Amount | Status | Response date |
|---|---|---|---|---|---|
| {{N}} | {{DATE}} | {{ITEMS}} | {{AMOUNT}} | {{STATUS}} | {{RESPONSE_DATE}} |

## Deadlines (VERIFY)
Work completion {{WORK_DEADLINE}} | Recoverable depreciation request {{RD_DEADLINE}} | Proof of loss {{POL_DEADLINE}}

Illustrative example for training: RCV 30,000, depreciation 10,000, ACV 20,000 before deductible.
