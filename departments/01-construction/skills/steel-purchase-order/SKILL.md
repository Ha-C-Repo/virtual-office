---
name: steel-purchase-order
description: Drafts material purchase orders from project tonnage by shape family using the supplier rate card, with the three-supplier parallel quote rule for high-value items.
---
## When to use
After award, when material must be bought.

## Inputs
Verified takeoff tonnage by shape family, supplier rate card, quote log.

## Steps
1. Group required material by family: wide-flange by weight class, hollow sections, channel, angle, plate, pipe.
2. For high-value anchors and any item above the configured threshold, obtain three supplier quotes in parallel (`../supplier-quote-tracker/SKILL.md`).
3. Draft PO lines: description, quantity, unit, unit price, total. Subtotal by calculator.
4. Fill `../../templates/purchase-order.md`. Status: draft, approved, sent, confirmed.
5. Check domestic-material requirements if the contract has them.

## Outputs
PO draft and quote comparison (internal).

## Gates
The {{APPROVER_ROLE}} approves before sending. Supplier names and prices never appear in client documents.
