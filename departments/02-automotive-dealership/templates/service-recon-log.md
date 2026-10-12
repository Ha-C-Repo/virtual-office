# Recon Log: {{STOCK_NUMBER}}

One log per unit. A unit is not listed until recon is closed and the grade reflects what was found and fixed.

Unit: {{YEAR}} {{MAKE}} {{MODEL}}   VIN: {{VIN}}   Arrived: {{ARRIVAL_DATE}}   Front-line date: {{FRONT_LINE_DATE}}   Days in recon: {{DAYS}}

| # | Date opened | Item | Defect id | Assigned to | Parts and labor (internal) | Date closed | Photo id | We-owe ref | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 1 | {{DATE}} | {{ITEM}} | {{DEFECT_ID}} | {{ROLE_OR_VENDOR_CATEGORY}} | {{COST}} | {{DATE_OR_OPEN}} | {{PHOTO_ID}} | {{WO_OR_NONE}} | {{NOTES}} |

## Status
Open items: {{COUNT}}   Closed: {{COUNT}}   Spend: {{SPEND}} vs budget {{RECON_BUDGET}}
Grade before: {{GRADE_BEFORE}}   Grade after re-run: {{GRADE_AFTER}}
Front-line ready signal sent to Inventory: {{YES_NO}} on {{DATE}}

## Rules
- Cost columns are internal. They never appear on a client copy.
- Closing an item and fulfilling its we-owe is one action.
- Items found after front-line are logged as defects, disclosed, and escalated to {{OWNER}}.
