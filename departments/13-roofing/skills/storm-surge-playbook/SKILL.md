---
name: storm-surge-playbook
description: Triage and capacity plan for a surge of leads after a hail, wind or flood event, with honest messaging and no prohibited inducements.
---
# Storm Surge Playbook

## When to use
When an event in {{SERVICE_AREA}} is expected or has occurred and inbound volume spikes.

## Inputs
Event date, affected area, current crew capacity, inspection capacity per day, tarp supply, staff available to answer.

## Steps
1. Open an event record and a lead log (`../../templates/storm-response-lead-log.md`). Assign `event_id`.
2. Triage every lead into: active leak or open roof (tarp first), damage suspected (inspection), information. Order by urgency, then by arrival time.
3. Set a daily capacity: inspections per day, tarp jobs per day. Tell leads the real wait; never promise a date the schedule cannot hold.
4. Send a short honest status message to the waiting list (draft for approval): who we are, that we are local and licensed ({{LICENSE_NUMBER}}), the wait, what to do now (photos from the ground, move belongings, call the carrier to open a claim).
5. For tarps use `../service-call-leak-triage/SKILL.md` and `../../templates/tarp-authorization.md`. A tarp is mitigation; keep photos and receipts for the claim.
6. Inspections follow `../roof-inspection-protocol/SKILL.md`. Insurance leads move to `../insurance-claim-support/SKILL.md` only after the homeowner decides to file.
7. Flag price-gouging risk: use the normal price book ({{PRICE_BOOK}}); any surge pricing is an owner decision and may be restricted by law (VERIFY {{STATE}}).
8. Check capacity daily; stop taking new inspection slots when the backlog exceeds {{MAX_BACKLOG_DAYS}} days and say so.

## Outputs
Event lead log, daily capacity plan, status message draft, tarp queue, KPI snapshot.

## Gates
- No door knocking without permits and posted-sign compliance (`../review-and-referral-compliance/SKILL.md`).
- No mention of deductibles in any canvass or message (`../deductible-and-inducement-gate/SKILL.md`).
- Owner approves outbound status messages and any pricing change.
- Out-of-area crews or subcontractors are vetted first (`../subcontractor-vetting-and-payments/SKILL.md`).

Workflow: `../../workflows/13-storm-surge-response.md`.
