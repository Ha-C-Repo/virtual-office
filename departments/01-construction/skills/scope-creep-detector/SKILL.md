---
name: scope-creep-detector
description: Finds items outside the contracted scope in takeoff, specifications or inbound client communications and routes them to change-order.
---
## When to use
On every inbound GC email, RFI response, meeting minute and revised drawing; and during takeoff for out-of-scope items.

## Inputs
Contract scope, inbound text, always-out-of-scope list.

## Steps
1. Scan for trigger phrases: "can you also", "not in the drawings", "client now wants", "additional work", "design change", "while you are there".
2. Qualify: scope creep or clarification? If unclear, ask.
3. Check against the always-out-of-scope list: engineering calculations (engineer of record), unit-system conversion, new structural elements, revisions beyond the contracted submittal allowance, connection redesign for geometry changes, extra site visits.
4. If creep: log in the correspondence register and open `../change-order/SKILL.md`.
5. If client-caused delay: also open `../contract-notice/SKILL.md`.

## Outputs
Scope-creep flag with quote, source and recommended action.

## Gates
No extra work proceeds on a verbal request. Written change order first.
