---
name: floorplan-reading
description: Read a floor plan or sketch into a room graph with dimensions and confidence tags, reconciled to stated GLA.
---
# Floor Plan Reading

## When to use
Building a tour, checking GLA, or preparing a feature sheet.

## Inputs
Floor plan image or sketch, stated GLA and its source, listing photos.

## Steps
1. Identify levels and rooms; name each room as labeled on the plan.
2. Record stated dimensions only where printed. Mark scaled measurements MEDIUM. Mark anything inferred from photos LOW.
3. Build the room graph: rooms, doors/openings, adjacency, level.
4. Compute total area with a script and compare to stated GLA. Report the difference and a tolerance of {{AREA_TOLERANCE_PCT}} percent.
5. List ambiguities as questions for the agent or seller.

## Outputs
Room graph (rooms, dimensions, confidence), area reconciliation, question list.

## Gates
Never certify a measurement from an image alone. If the computed area does not reconcile, flag and hold the tour. Verify, do not generate.
