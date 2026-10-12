---
name: damage-documentation-photo-log
description: Build a timestamped, geotagged, labeled photo log that supports estimates, claims, supplements and warranty records.
---
# Damage Documentation and Photo Log

## When to use
Every inspection, dry-in, final, warranty visit, and mitigation event.

## Inputs
Original photo files with timestamps and location data, the inspection record, any AI auto-labeling output.

## Steps
1. Keep the **original files** untouched in {{PHOTO_STORAGE}}. Work on copies for labels and crops.
2. Confirm timestamps and geotags are present. If location is off, note it; do not add data after the fact.
3. Shoot in a fixed order: address/house front, elevations, each slope overview, each damaged area wide then close, test square with a marker, flashing, penetrations, vents, valleys, gutters, collateral damage, interior stains if allowed.
4. Label each photo: slope or area, direction, what it shows, test-square id. Use `../../templates/photo-log.md`.
5. If an automated tool labels photos, a person reviews every label and corrects errors. Mark `reviewed_by`.
6. Do not stage, retouch, or reuse photos from another property. Flag any photo whose source is uncertain and remove it.
7. For jobs in progress capture: tear-off (deck condition), underlayment and ice barrier, drip edge, flashing, dry-in, ridge/vents, final, cleanup.
8. Link photo ids into estimate line items, supplement requests and QC checklists.

## Outputs
Photo log, labeled set for the claim or estimate, missing-shot list.

## Gates
- Missing required shots block the QC milestone (`../qc-checklists/SKILL.md`).
- Photos with customer faces, plates or documents are cropped or excluded before marketing use, and marketing use needs written consent (`../review-and-referral-compliance/SKILL.md`).
- Owner or claim coordinator reviews any photo set going to a carrier.
