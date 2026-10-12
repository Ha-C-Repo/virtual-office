---
name: title-deadline-risk-detector
description: Watches per-deal and office-level deadlines and raises URGENT and THIS WEEK warnings with confidence labels.
---
## Per-deal deadline set
odometer disclosure, title application, temp tag expiry, lien perfection (financed only), covered-borrower check recorded, buyer's guide on file, warranty or service-contract administrator filing (skipped for as-is), 30-day post-sale check-in.

## Office-level
Dealer license renewal, continuing education per licensed person.

## Steps
1. Compute due dates from anchor dates and rule day counts. Unknown day count: NEEDS_INPUT.
2. Label each: VERIFY (authority text) or OFFICE (house rule).
3. Warn: URGENT at 3 days, THIS WEEK at 7. Flag dependency risk earlier if the anchor date is missing.
4. Distinguish filed from recorded.
5. Output the timeline (`../../templates/title-deadline-timeline.md`).

## Gates
Anything inside the warning window with no filed action escalates to the owner.
