# Photo Manifest: {{STOCK_NUMBER}}

Minimum 8 photos. Every photo is a real image of this unit taken by the office. Any generated image fails the whole set. A touched image must pass the four-part rule: office owns the pixels, the vehicle is unaltered (background, exposure and crop only), the image is labeled and the label travels, the unaltered original is kept and paired.

| # | Tag | File | is_generated (must be FALSE) | Touched (Y/N) | Original paired | Label | Taken |
|---|---|---|---|---|---|---|---|
| 1 | front_3q | {{FILE}} | FALSE | {{YES_NO}} | {{ORIGINAL_FILE}} | {{LABEL}} | {{DATE}} |
| 2 | rear_3q | {{FILE}} | FALSE | {{YES_NO}} | {{ORIGINAL_FILE}} | {{LABEL}} | {{DATE}} |
| 3 | driver_side | {{FILE}} | FALSE | {{YES_NO}} | {{ORIGINAL_FILE}} | {{LABEL}} | {{DATE}} |
| 4 | passenger_side | {{FILE}} | FALSE | {{YES_NO}} | {{ORIGINAL_FILE}} | {{LABEL}} | {{DATE}} |
| 5 | interior_front | {{FILE}} | FALSE | {{YES_NO}} | {{ORIGINAL_FILE}} | {{LABEL}} | {{DATE}} |
| 6 | vin_plate | {{FILE}} | FALSE | {{YES_NO}} | {{ORIGINAL_FILE}} | {{LABEL}} | {{DATE}} |
| 7 | odometer | {{FILE}} | FALSE | {{YES_NO}} | {{ORIGINAL_FILE}} | {{LABEL}} | {{DATE}} |
| 8 | defect:{{DEFECT_ID}} | {{FILE}} | FALSE | {{YES_NO}} | {{ORIGINAL_FILE}} | {{LABEL}} | {{DATE}} |

## Checks
- [ ] Minimum count met and all required angles present.
- [ ] VIN plate photo matches the VIN on the record.
- [ ] Odometer photo matches the stated mileage.
- [ ] One photo per disclosed defect.
- [ ] No generated vehicle, building or person.
- [ ] No other customer's plate, face or paperwork visible.
Result: {{PASS / FAIL}}   Reviewer: {{REVIEWER}}
