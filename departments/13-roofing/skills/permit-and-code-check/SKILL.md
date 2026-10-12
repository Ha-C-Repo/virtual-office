---
name: permit-and-code-check
description: Prepare the permit packet and check the job design against general code points, local amendments and manufacturer requirements.
---
# Permit and Code Check

## When to use
After contract signature and before material order, and again before dry-in and final inspection.

## Inputs
Contract scope, measurement sheet, product data sheets, local permit requirements ({{LOCAL_CODE_OFFICE}}), adopted code edition ({{CODE_EDITION}}), site photos.

## Steps
1. Confirm that a re-roof permit is required and who pulls it (contract). Build the packet from `../../templates/permit-packet-checklist.md`: application, license and insurance proof, product approvals, wind and fire classification, site plan if requested.
2. Check design points against `../../knowledge/rules.md` and local amendments (all VERIFY):
   - layers: maximum two of asphalt; tear-off if more or if the deck or manufacturer requires;
   - deck: inspect, repair, re-nail; replace damaged sections;
   - ice barrier: eave to at least 24 in inside the exterior wall where required;
   - underlayment: about 2 in side laps, 4 in end laps offset about 6 ft; slopes 2:12 to 4:12 need double or special underlayment; shingles not below 2:12;
   - flashing: step flashing, kickouts, valleys, penetrations, drip edge;
   - ventilation: balance intake and exhaust; net free area ratio about 1/150 or 1/300 depending on edition and conditions;
   - product wind and fire classification matches the requirement.
3. Note manufacturer installation requirements that exceed the code. The more demanding one applies.
4. Schedule inspections: deck/nailing if required, dry-in, final. Photograph each with date stamps.
5. Track permit status and results in the project file.
6. If the inspector fails an item, create a correction task, retest and record.

## Outputs
Permit packet, code check table with VERIFY resolution notes, inspection schedule.

## Gates
- No crew start without the permit posted where required.
- No customer document states a code rule that is still tagged VERIFY.
- Owner or production manager signs the packet before submission.
- Product-specific installation specs are read from the current manufacturer instructions, not from this department (open gap, `../../knowledge/research-notes.md`).

Workflow: `../../workflows/05-permit-to-dryin-to-final.md`.
