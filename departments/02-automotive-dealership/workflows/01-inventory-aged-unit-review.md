# 01 Inventory: Aged Unit Review (weekly)

Owner: Inventory agent. Runs weekly and on request. A markdown simulation is a report; a human decides.

## Inputs
Units past the days-to-turn threshold ({{DAYS_TO_TURN_THRESHOLD}}), owner-locked markdown schedule, floorplan interest rate, recon status, live channel status, comp grid.

## Steps
1. List units past threshold with days in inventory, current price, floor, recon status and photo status.
2. Re-run comps for each (`../templates/inventory-comp-grid.md`). Note corridor movement.
3. Calculator: run the markdown schedule on each unit and show the effect on floor, accrued floorplan interest and gross. The model does not compute these.
4. Check drift: confirm the unit is live on every channel it should be, and not on any it should not.
5. Check listing freshness: photos current, description matches grade, defects disclosed.
6. Recommend one action per unit: hold, markdown to step N, re-photograph, wholesale, or fix recon. Give the reason in one line.
7. Send the report to {{OWNER}} through the approval queue.

## Gates
- No price changes without owner approval. Any new price goes through the sanity gates and compliance check again.
- Markdown shown to customers is never framed as "was/now" or savings on a used vehicle.

## Output
One table and a short recommendation list. Confidence tier and open flags at the end.
