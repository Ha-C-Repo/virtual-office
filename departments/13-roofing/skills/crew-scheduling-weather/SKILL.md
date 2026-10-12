---
name: crew-scheduling-weather
description: Assign crews, run the kickoff checklist and reschedule around weather without leaving a roof open.
---
# Crew Scheduling and Weather

## When to use
Daily production planning and any forecast change.

## Inputs
Backlog with delivery status, crew availability and certifications, forecast, permit status, customer constraints, safety plan status.

## Steps
1. Only schedule jobs with: signed contract, permit, confirmed delivery, color confirmation, fall protection plan on file.
2. Match crew to job: size, steep-slope experience, commercial membrane certification, manufacturer certification required for the chosen warranty tier.
3. Run `../../templates/job-kickoff-checklist.md` the day before. Issue `../../templates/crew-work-order.md` to the lead.
4. Weather rule: check the forecast the evening before and at start. Do not tear off more than the crew can dry-in that day. Do not start on a day with rain forecast during the work window unless the owner approves a contingency (tarps, partial scope).
5. Wind, lightning, heat and cold limits come from the manufacturer instructions and the safety program (VERIFY). Heat: schedule early starts and breaks.
6. When rescheduling, notify the customer with a draft message for approval, move the delivery if needed, and re-sequence the backlog by urgency (open roofs first).
7. For piecework crews record the squares installed and expected quality spot checks (`../qc-checklists/SKILL.md`).
8. Log weather delays on the project record.

## Outputs
Daily schedule, work orders, customer delay messages (drafts), backlog view.

## Gates
- No crew dispatch without a signed fall protection plan.
- A sub with an expired COI does not start (`../subcontractor-vetting-and-payments/SKILL.md`).
- Owner approves schedule changes that affect a customer deadline or an insurance completion deadline.

Workflow: `../../workflows/07-production-day-and-weather.md`.
