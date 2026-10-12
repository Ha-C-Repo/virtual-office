---
name: review-and-referral-compliance
description: Screen marketing, canvassing, review requests, referral programs and automated outreach for consent, solicitation and inducement rules.
---
# Review and Referral Compliance

## When to use
Before any marketing, canvass, text, email, call script, review request, referral offer, sign, gallery or financing mention is used.

## Inputs
The draft item, channel, audience, consent records, local solicitation rules ({{CITY_OR_COUNTY}}), state rules.

## Checks
1. **Consent and lists:** texts and auto-dialed or prerecorded calls need consent; scrub calls against national, state and internal do-not-call lists and keep evidence; email carries truthful headers, a mailing address and a working opt-out (VERIFY counsel guidance).
2. **Missed-call text-back:** sent only to the caller, once, human callback promise, opt-out language, no pricing or claim talk.
3. **Door knocking:** local permit or registration, permitted hours, honor posted do-not-solicit signs, carry ID, give the cancellation notice for off-premises sales (VERIFY).
4. **Deductible and claim language:** run `../deductible-and-inducement-gate/SKILL.md`.
5. **Referral programs:** rewards not tied to insurance claims or to waiving deductibles; disclose any incentive where reviews are involved; follow state rules (VERIFY).
6. **Reviews:** ask all customers at the right moment after completion and satisfaction; do not gate by sentiment, write reviews, or offer pay for positive ones.
7. **Photos and signs:** written consent for yard signs and gallery use; remove identifying details.
8. **Storm messaging:** local presence, license number, insurance, honest timelines; no pressure or "act now" claims without basis.
9. **Financing:** disclose terms and the lender as required; the office does not quote rates.
10. **Claims in ads:** no unsupported statistics or superlatives; vendor statistics on lead speed are unverified.
11. **AI use:** automated replies identify as automated if required and offer a human.

## Outputs
Gate report with pass/fail, evidence and fixes; approved copy; ledger of consent bases (`../../knowledge/schemas.md`, Outbound / consent).

## Gates
Any fail blocks. Owner approves campaigns. Templates: `../../templates/review-request-message.md`, `../../templates/canvass-script.md`.
