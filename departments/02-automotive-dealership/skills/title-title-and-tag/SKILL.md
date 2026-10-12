---
name: title-title-and-tag
description: Title transfer, odometer disclosure, temp tag issuance and expiry, and lien perfection mechanics.
---
## Steps
1. Verify the title is assigned to the dealership before an advertised sale.
2. Executed odometer statement on file (federal and state). Record source.
3. Title application submitted inside the state deadline (day count from the authority; unknown = NEEDS_INPUT).
4. Temp tag issued in the allowed window; log issue and expiry (`../../templates/title-temp-tag-log.md`). Expiry is aggressively enforced.
5. Lien perfection for financed deals (`../../templates/title-lien-filing-tracker.md`).
6. License display and renewal {{LICENSE_NUMBER}}, {{LICENSE_EXPIRY}}.
7. Record "filed" and "recorded" separately.

## Outputs
Deadline entries, logs, tracker updates.

## Gates
Verify state-specific rules against the current authority text before relying on them ({{STATE}}). Never guess a day count.
