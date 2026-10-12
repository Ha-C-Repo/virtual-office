# Purchase Order Workflow

Skill: `../skills/purchase-order-drafter/SKILL.md`. Template: `../templates/purchase-order.md`.

## Steps
1. Quantities confirmed from the project or the consumables trigger.
2. Rate card applied; missing rate means flag.
3. Above the threshold: three parallel supplier quotes.
4. Draft the PO.
5. GATE: {{OWNER_ROLE}} approves.
6. Send; record confirmation; status confirmed.
7. Receive goods; match to PO; log differences.
8. Update the opex register.
