---
name: purchase-order-drafter
description: Drafts purchase orders from quantities and a vendor rate card. Status flow draft, approved, sent, confirmed.
---
# Purchase order drafter

## When to use
When quantities for a project or restock are known and the owner wants a PO.

## Steps
1. Read quantities and the vendor rate card. Group by item family.
2. For large orders above the parallel-quote threshold, request quotes from at least three suppliers in parallel before committing.
3. Draft lines: description, quantity, unit, unit price, line total; subtotal; PO number.
4. Set status draft. {{OWNER_ROLE}} approves; then sent; then confirmed on vendor acknowledgement.
5. Log in the PO register.

## Outputs
PO draft (`../../templates/purchase-order.md`).

## Gates
Never invent a price; missing rate means flag. Vendor names are internal-only. No PO is sent without approval.
