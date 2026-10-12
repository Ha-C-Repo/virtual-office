---
name: subcontractor-vetting-and-payments
description: Vet roofing subcontractors, agree piece or day rates, and release payments by milestone with holdbacks.
---
# Subcontractor Vetting and Payments

## When to use
Before first use of any sub, at each insurance renewal, and for every payment.

## Inputs
License (where required), certificate of insurance, workers compensation status, references, sample job photos, safety record, rate proposal, signed agreement.

## Vetting steps
1. Collect and verify: license status, certificate of insurance with {{COI_MINIMUMS}} and expiry date, workers compensation coverage or exemption (VERIFY {{STATE}}), tax form, two references, photos of recent work.
2. Check quality: visit a recent job or inspect photos against `../qc-checklists/SKILL.md`.
3. Safety: orientation, fall protection equipment, training records, plan acceptance (`../fall-protection-plan/SKILL.md`).
4. Classification questions (employee versus contractor) go to {{COUNSEL}}; do not decide here (VERIFY).
5. Execute `../../templates/sub-agreement.md`: scope, rate basis (per square piece rate or day rate), insurance, safety, warranty on labor, cleanup, defect repair, payment milestones, holdback, termination.
6. Record in the crew record: `coi_expires_at`, certifications, pay basis.

## Payment steps
1. Use `../../templates/sub-payment-milestone-sheet.md`. Milestones: dry-in inspection passed; photo-documented final; punch list closed. Holdback held until the last two are met ({{HOLDBACK_PERCENT}}).
2. Verify squares installed using the takeoff and photos; piece rate is paid on verified squares.
3. Check for lien waiver from the sub for each payment (`../lien-waiver-tracker/SKILL.md`).
4. Withhold for failed QC items until fixed.
5. Pay only after the owner approves the sheet.

## Outputs
Vetting file, signed agreement, milestone sheet.

## Gates
- No work without a valid COI, agreement and safety orientation.
- Payment requires evidence (photos, inspection result).
- Owner approves new subs and every payment release.
- Piecework creates quality risk; increase spot checks and record a quality score.
