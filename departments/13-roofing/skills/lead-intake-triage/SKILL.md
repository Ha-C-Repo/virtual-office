---
name: lead-intake-triage
description: Capture, classify and respond to new roofing leads within minutes, including missed-call text-back, source tracking and escalation to a human.
---
# Lead Intake Triage

## When to use
Every inbound call, form, message, referral or canvass contact. During a storm event, switch to `../storm-surge-playbook/SKILL.md`.

## Inputs
Channel, contact details, property address, what the caller says, source, time received. Consent basis for any text or call back.

## Steps
1. Log the lead with the fields in `../../knowledge/schemas.md` (Lead). Record `source` and `source_detail` every time; an untracked lead cannot be measured.
2. Classify service type: repair, re-roof, storm/insurance, commercial, maintenance, warranty callback (route callbacks to `../service-call-leak-triage/SKILL.md`).
3. Classify urgency: active leak or damage (same day), planned replacement, information only.
4. First response: aim for minutes, not hours ({{SPEED_TO_LEAD_TARGET}}). For a missed call, send the missed-call text-back only to the number that called, with the company name, a human callback promise, and opt-out wording. Use the wording approved in `../review-and-referral-compliance/SKILL.md`.
5. Ask the minimum qualifying questions: address, roof age if known, what happened, insured claim or not, decision-maker, best time.
6. Offer inspection times. Book the appointment; send confirmation (draft).
7. If the caller mentions insurance, say the homeowner files the claim and the office documents damage. Do not discuss deductibles beyond "the homeowner is responsible for the deductible."
8. Compute `minutes_to_first_response` from timestamps and record it.

## Outputs
Lead record, response draft, appointment or follow-up task, KPI data for `../../templates/weekly-kpi-dashboard.md`.

## Gates
- Automated replies must offer a human and never quote prices, coverage or timelines the office has not approved.
- A text or call needs consent (VERIFY counsel guidance, `../../knowledge/rules.md`).
- Run `../deductible-and-inducement-gate/SKILL.md` on any message that mentions money or claims.
- Human reviews any lead flagged storm-surge, legal threat, or complaint within {{ESCALATION_MINUTES}} minutes.
- Vendor speed-to-lead statistics are unverified. Do not quote them.

Workflow: `../../workflows/01-lead-to-appointment.md`.
