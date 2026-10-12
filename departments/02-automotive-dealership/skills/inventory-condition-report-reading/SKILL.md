---
name: inventory-condition-report-reading
description: Converts auction or inspection condition reports into a ranked defect list, never copying the report's own summary grade.
---
## When to use
When a condition report, window sticker or inspection sheet is on file.

## Steps
1. Read each line item. Capture category (structural, mechanical, cosmetic, wear), severity (critical, major, minor), description, source.
2. Ignore the document's own summary grade. Evidence only.
3. Cross-check open recalls.
4. Compare against photos. A defect visible in a photo but not in the report is added as LOW and flagged.
5. Produce the disclosure set (defects that must appear in copy, guide, register and photos) and the recon work order in the same pass (`../../templates/inventory-disclosure-set.md`, `../../templates/inventory-recon-work-order.md`).

## Outputs
Ranked defect list, disclosure set, recon work order.

## Gates
Vision on report images or lot photos is advisory. A human confirms. It never auto-discloses. Conflicting evidence is a defect to resolve, never averaged.
