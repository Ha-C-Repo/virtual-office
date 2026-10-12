# 07 Reputation: Review Response

Owner: Reputation agent (`../agents/07-reputation-agent.md`). Skill: `../skills/reputation-response/SKILL.md`. Runs daily as the reputation harvester. Reply only after the business profile is claimed.

## Steps
1. **Collect** new reviews from every surface into `../templates/reputation-review-queue.md`.
2. **Classify.**
   1. Concealment, safety or title allegation.
   2. Service or follow-up complaint without concealment claim.
   3. Positive review naming a specific staff action.
   4. Generic positive or negative.
3. **Class 1.** Never auto-answered. No public draft. Send `../templates/reputation-escalation-note.md` to {{OWNER}} the same business day. When in doubt, escalate. Pull the records first.
4. **Classes 2 to 4.** Draft from `../templates/reputation-response-by-class.md`.
5. **Checks.** Owner voice check on every reply. Compliance check in marketing context on any reply that touches a vehicle fact or financing claim.
6. **Approval.** A human approves and posts.
7. **Follow up.** Class 2: contact the customer directly, record the resolution. A posted reply is not a resolved complaint.
8. **Review requests.** After funding and delivery, ask every customer (`../templates/reputation-review-request.md`).
9. **Weekly digest.** `../templates/reputation-weekly-sentiment-digest.md`.
10. **Risk feed.** Concealment-flavored reviews plus universal-approval ad language is the pattern behind a base off-limits designation; report counts to Compliance monthly.

## Never
Claim reviews were removed. Promise a rating. Offer anything for a review or for removal. Re-litigate in public. Reuse a review as an ad testimonial without permission.

## KPIs
Response rate and time per surface. Class 1 escalated same business day, 100 percent.
