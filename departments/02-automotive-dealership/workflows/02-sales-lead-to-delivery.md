# 02 Sales: Lead to Delivery

Owner: Sales agent (`../agents/02-sales-agent.md`). Human owner: {{SALES_MANAGER}}. Skills: `../skills/sales-lead-response/SKILL.md`, `sales-lead-retention`.

## Deal pipeline state machine
LEAD -> APPOINTMENT -> WRITE_UP -> CREDIT_SUBMITTED -> APPROVED -> DELIVERED -> FUNDED. Side states: LOST, UNWOUND, REPO. Only valid transitions are recorded; each transition logs actor, notes and timestamp. A deal idle 3 or more days is flagged.

## Steps
1. **Capture.** Log the lead from site form, social message, portal email, phone-up log or walk-in log. Dedupe against contacts. Start the speed-to-lead timer.
2. **Reply.** Draft an acknowledgment that names the actual vehicle and price (`../templates/sales-lead-acknowledgment.md`). Voice check, then outbound gate (`02-sales-outbound-message.md`). A human sends.
3. **Appointment.** `../templates/sales-appointment-confirmation.md`. Confirm the unit is on the ground and front-line ready.
4. **Demo and promises.** Every promise made goes on the we-owe the same day (`05-service-recon-and-we-owe.md`). Not recorded = escalate, copy Service/Recon.
5. **Trade.** `../templates/sales-trade-appraisal-request.md`. No written trade guarantee.
6. **Write-up and desk.** Hand to F&I (`03-fi-desking-and-submission.md`). {{OWNER}} owns the number.
7. **Delivery.** Jacket complete (`04-title-deal-jacket-and-deadlines.md`), we-owe signed, buyer acknowledgment of disclosed defects collected.
8. **Funding action chain.** Record the deal internally, run the compliance checklist, queue the review request (`../templates/reputation-review-request.md`), queue anniversary follow-up and the 30-day check-in (`../templates/service-30-day-checkin.md`).

## KPIs and escalation
Speed-to-lead per channel, show rate, lead-to-write-up rate, promises made not on the we-owe. Lead unanswered past target: tell {{SALES_MANAGER}}.

## Sign-off
Human sends every message. Owner approves price and deal.
