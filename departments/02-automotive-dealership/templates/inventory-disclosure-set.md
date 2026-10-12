# Disclosure Set: {{STOCK_NUMBER}}

The defects that must appear together in the listing copy, the buyer's guide, the disclosure register and the photos. One list, four places.

VIN: {{VIN}}   Grade: {{GRADE}}   Title status: {{TITLE_STATUS}}   Odometer: {{MILEAGE}} (source {{MILEAGE_SOURCE}})
Prepared: {{DATE}}   Reviewed by: {{OWNER}}

| Defect id | Description (plain words) | Severity | In listing | In buyer's guide | In register | Photo id | Recon status |
|---|---|---|---|---|---|---|---|
| {{DEFECT_ID}} | {{DESCRIPTION}} | {{SEVERITY}} | {{YES_NO}} | {{YES_NO}} | {{YES_NO}} | {{PHOTO_ID}} | {{OPEN_CLOSED}} |

## Checks
- [ ] Every defect has all four places filled. A single NO is a gate failure.
- [ ] Every open recon item has a work order (`inventory-recon-work-order.md`).
- [ ] Recall cross-check done: {{RECALL_RESULT}}.
- [ ] Title brand or history, if any, is stated in plain words.
- [ ] Description does not claim a condition beyond the grade.
- [ ] Buyer acknowledgment will be collected before delivery.
