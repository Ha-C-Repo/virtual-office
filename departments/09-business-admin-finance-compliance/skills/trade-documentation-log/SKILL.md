---
name: trade-documentation-log
description: Logs import, export and transfer documents per movement of regulated assets and blocks movements with incomplete paperwork.
---
# Trade documentation log

## When to use
For every movement of regulated assets in or out of the facility.

## Steps
1. Create the row: date, direction, asset IDs, species or type, origin, destination, permit number, sanitary certificate number, customs reference, status.
2. Check that the permit covers the type and period (`../permit-tracker/SKILL.md`).
3. Status: draft, complete, filed. Incomplete rows block shipment or receipt.
4. Link the row to intake records for arrivals (`../../workflows/intake-quarantine.md`).

## Outputs
Log rows (`../../templates/trade-documentation-log.md`).

## Gates
Do not invent references. Legal interpretation goes to counsel through {{OWNER_ROLE}}.
