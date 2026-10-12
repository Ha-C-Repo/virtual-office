---
name: material-order-builder
description: Turn a verified takeoff into a purchase order with delivery, roof loading, dumpster and color confirmation gates.
---
# Material Order Builder

## When to use
After contract signature, measurement verification and permit confirmation.

## Inputs
Takeoff sheet, product selections and colors from the contract, supplier terms, schedule window, site access notes, weather outlook.

## Steps
1. Re-run `../../harnesses/takeoff_calc.py` with the verified inputs; compare to the takeoff sheet. Differences stop the order.
2. Confirm the waste percent and coverage values with the supplier (VERIFY) and record the contact placeholder {{SUPPLIER_CONTACT}}.
3. Build the order in `../../templates/material-order.md`: shingles (bundles rounded up), starter, ridge cap, drip edge sticks, underlayment rolls, ice barrier, vents, flashing, pipe boots, nails, sealant, decking allowance.
4. Color and product confirmation: the customer confirms in writing before ordering. Record the date.
5. Delivery plan: date window, location on site, roof loading plan (spread over framing; VERIFY structural limits), access for the truck, dumpster placement and permit.
6. Substitutions require written approval from the owner and, if it changes the contract, the customer.
7. On delivery: count against the order, check lot and color, photograph, note damage, and mark `delivery_confirmed_at`.
8. Returns: record leftover and return process with date and credit reference.

## Outputs
Purchase order, delivery plan, delivery confirmation record.

## Gates
- **Delivery confirmation gates crew scheduling** (`../crew-scheduling-weather/SKILL.md`).
- No order without verified measurements and written color confirmation.
- Owner approves orders above {{PO_APPROVAL_THRESHOLD}}.

Workflow: `../../workflows/06-material-order-to-delivery.md`.
