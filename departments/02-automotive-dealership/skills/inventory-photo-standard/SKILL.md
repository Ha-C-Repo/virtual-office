---
name: inventory-photo-standard
description: Checks the photo set for count, required angles and defect coverage, and fails any set containing generated imagery.
---
## Requirements
- Minimum 8 photos.
- Required tags: front_3q, rear_3q, driver_side, passenger_side, interior_front, vin_plate, odometer, and one defect:<id> photo for each disclosed defect.
- Every photo entry has tag and is_generated attestation (`../../templates/inventory-photo-manifest.md`).

## Steps
1. Compare the manifest to the requirement list.
2. Verify the VIN plate photo matches the record.
3. Verify the odometer photo matches the stated mileage.
4. Verify each disclosed defect has a photo.
5. Fail on any generated image.
6. If photos were touched, apply the four-part rule: office owns the source pixels; only background, exposure or crop altered; labeled and the label travels; original retained and paired.

## Outputs
PASS or a list of missing tags.

## Gates
Any generated vehicle image fails the set and goes to the owner and Compliance.
