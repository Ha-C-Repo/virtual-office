# 01 Lead to Appointment

Owner: sales-estimator | Approver: {{OWNER}} (for scripts and automated replies)

## Steps
1. Lead arrives (call, form, message, referral, canvass). Log it with source (`../skills/lead-intake-triage/SKILL.md`).
2. First response within {{SPEED_TO_LEAD_TARGET}}. Missed call: send the approved text-back and queue a human callback.
3. Classify service type and urgency. Active leak: go to `../skills/service-call-leak-triage/SKILL.md`. Storm surge: `13-storm-surge-response.md`.
4. Ask the qualifying questions; note insured claim or not, decision-maker, roof age, and what happened.
5. GATE: any message that mentions money, claims or deductibles passes `../skills/deductible-and-inducement-gate/SKILL.md`.
6. Offer appointment times; book the inspection; send the confirmation draft.
7. GATE (human): owner reviews the automated-reply scripts before first use and monthly after; a person answers any escalation within {{ESCALATION_MINUTES}} minutes.
8. Reminder the day before; on the day, confirm the inspector is en route.
9. Record `minutes_to_first_response` and source; feed `../templates/weekly-kpi-dashboard.md`.
10. Unbooked leads enter a follow-up cadence limited by consent rules (`../skills/review-and-referral-compliance/SKILL.md`).

## Outputs
Lead record, appointment, response-time data, follow-up task.
