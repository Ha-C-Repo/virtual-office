---
name: lien-waiver-tracker
description: Track lien waivers exchanged for each payment, matching partial waivers to progress payments and the final waiver to final payment.
---
# Lien Waiver Tracker

## When to use
At every progress or final payment, in both directions: waivers we give customers and waivers we collect from subs and suppliers.

## Inputs
Payment schedule, payment received or issued, state rules and statutory forms ({{STATE_RULES}}; VERIFY), notice-of-commencement or preliminary notice requirements (VERIFY).

## Steps
1. Open a row for each payment in `../../templates/lien-waiver-tracker.md`: party, amount, through date, waiver type (partial or final, conditional or unconditional where the state uses them).
2. Use the statutory form where the state requires one. Where no form is required, use counsel-approved language.
3. Partial waivers accompany progress payments; the final waiver accompanies final payment.
4. Never issue an unconditional final waiver before the funds clear.
5. For subs: collect their waiver before releasing each payment; collect supplier waivers or releases where used.
6. Track missing waivers by age; chase weekly.
7. Check notice deadlines to preserve the company's own lien rights on unpaid balances (VERIFY {{STATE}}).

## Outputs
Waiver ledger, missing-waiver list, deadline alerts.

## Gates
- Waiver forms and rights are legal matters; counsel approves templates.
- Owner signs waivers and approves exceptions.
- Do not state lien rights to a customer as a threat; follow `../../knowledge/rules.md`.
