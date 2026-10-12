# Recon Work Order: {{STOCK_NUMBER}}

Produced by the condition audit in one pass with the disclosure set. Goes to {{RECON_LEAD}}. Closing a recon item and fulfilling its we-owe (if any) is one action, recorded once.

Unit: {{YEAR}} {{MAKE}} {{MODEL}}   VIN: {{VIN}}   Opened: {{DATE}}   Target front-line date: {{TARGET_DATE}}
Recon budget for grade {{GRADE}}: {{RECON_BUDGET}}   (owner-locked)

| Item | Defect id | Category | Severity | Repair to perform | Who (in-house / vendor category) | Estimate | Actual | Opened | Closed | Photo after | We-owe ref |
|---|---|---|---|---|---|---|---|---|---|---|---|
| {{ITEM_1}} | {{DEFECT_ID}} | {{CATEGORY}} | {{SEVERITY}} | {{REPAIR}} | {{WHO}} | {{ESTIMATE}} | {{ACTUAL}} | {{DATE}} | {{DATE_OR_OPEN}} | {{PHOTO_ID}} | {{WO_NUMBER_OR_NONE}} |

Spend to date: {{SPEND}} vs budget {{RECON_BUDGET}}. Over budget: {{YES_NO}} (tell {{OWNER}} before further spend).

## Close-out
- [ ] Every critical and major item closed or disclosed.
- [ ] Recall work done or scheduled and disclosed.
- [ ] Grade re-run on the new evidence (`../skills/inventory-condition-grading/SKILL.md`).
- [ ] Front-line-ready signal sent back to Inventory.
- [ ] Internal cost recorded on the INT side only.
