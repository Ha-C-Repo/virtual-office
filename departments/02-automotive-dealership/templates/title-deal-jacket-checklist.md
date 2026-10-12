# Deal Jacket Checklist: {{DEAL_REF}}

Deal type: CASH / OUTSIDE FINANCE / IN-HOUSE PAPER
Unit: {{STOCK_NUMBER}}   VIN: {{VIN}}   Sale date: {{SALE_DATE}}   Buyer: {{CUSTOMER_NAME}}   Checked by: {{TITLE_CLERK}}   Date: {{DATE}}
No deal is reported funded with a jacket missing a required document.

## All deals
| Document | Present | Executed date | Path | Notes |
|---|---|---|---|---|
| Buyer's guide, matches the contract | {{YES_NO}} | {{DATE}} | {{PATH}} | as-is / warranty box agrees with ad and contract |
| Executed odometer statement | {{YES_NO}} | {{DATE}} | {{PATH}} | |
| Assigned title with transfer application | {{YES_NO}} | {{DATE}} | {{PATH}} | |
| Covered-borrower check record | {{YES_NO}} | {{DATE}} | {{PATH}} | indeterminate treated as covered |
| Bill of sale / purchase agreement | {{YES_NO}} | {{DATE}} | {{PATH}} | |
| Buyer acknowledgment of disclosed defects | {{YES_NO}} | {{DATE}} | {{PATH}} | |
| We-owe (client copy) if any | {{YES_NO}} | {{DATE}} | {{PATH}} | |

## Add for outside finance or in-house paper
| Document | Present | Path |
|---|---|---|
| Credit application and approval | {{YES_NO}} | {{PATH}} |
| Retail installment contract | {{YES_NO}} | {{PATH}} |
| Stipulations satisfied (`fi-stipulation-tracker.md`) | {{YES_NO}} | {{PATH}} |
| Adverse-action notice, if any | {{YES_NO}} | {{PATH}} |
| Lien perfected | {{YES_NO}} | {{PATH}} |

## Add for in-house paper
| Document | Present | Path |
|---|---|---|
| Servicing terms | {{YES_NO}} | {{PATH}} |
| Payment schedule and notices | {{YES_NO}} | {{PATH}} |

## Result
Missing: {{MISSING_LIST}}   Complete: {{YES_NO}}   If missing at funding: STOP and escalate to {{OWNER}}.
Internal twin present for this deal (`fi-deal-recap-int.md`): {{YES_NO}}
