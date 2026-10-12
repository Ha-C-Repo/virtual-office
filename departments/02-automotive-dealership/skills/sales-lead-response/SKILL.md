---
name: sales-lead-response
description: Logs and dedupes a lead, starts the speed-to-lead timer and drafts a reply naming the actual vehicle and price for human approval.
---
## When to use
Any inbound lead from the site form, social marketplace, classified portal email, phone-up log or walk-in log.

## Steps
1. Dedupe against contacts (phone, email, name plus vehicle).
2. Start the speed-to-lead timer for the channel.
3. Pull the vehicle record: stock number, actual price, availability. If the unit is not on the ground, say so and offer alternatives from the record.
4. Draft from `../../templates/sales-lead-acknowledgment.md`. Include one specific line about the vehicle.
5. Do not quote a payment, rate or trade value. Route to F&I.
6. Run voice check (`../marketing-owner-voice-check/SKILL.md`) and the outbound gate (`../../workflows/02-sales-outbound-message.md`).
7. Queue for approval. Never send.
8. Log state LEAD.

## Outputs
Lead record, timer, drafted reply in the approval queue.

## Gates
Consent ledger first. Any conversational surface discloses AI in its first message using the fixed template.
