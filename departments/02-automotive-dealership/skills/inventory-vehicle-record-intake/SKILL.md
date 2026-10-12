---
name: inventory-vehicle-record-intake
description: Open a unit record from a VIN, stock number or acquisition packet using permitted sources only, and attach classified documents.
---
## When to use
Any new vehicle, or a new document for an existing unit. Function 01 Inventory.

## Inputs
VIN, stock number, or acquisition packet (auction run list and condition report, title and odometer documents, lot photos, history report from the dealership's own paid account).

## Steps
1. Assign a unique stock number {{STOCK_NUMBER}}.
2. Decode the VIN {{VIN}} through the public decode source. Record year, make, model, trim as HIGH. A decode failure is a recorded gap, not a guess.
3. Classify and attach each document (`../inventory-document-classifier/SKILL.md`).
4. Check the open-recall lookup and store results.
5. Create the unit record using `../../templates/inventory-unit-record.md`.
6. Set status INTAKE; grade NOT_GRADED.

## Outputs
Unit record with facts, documents, recalls and gaps.

## Gates
- Permitted sources only. No web research for vehicle facts.
- Every fact carries confidence and source.
- VIN, mileage, title status are never set by the model.
