---
name: lead-followup
description: Consent-gated lead follow-up cadence across call, text and email. Step 0 is a consent check per lead per channel; no consent row means no draft and a named refusal. Use for any lead, inquiry or past-client touch.
---

# Lead follow-up

## When to use
New inbound lead, web form, phone-up, walk-in, event sign-in, referral, past-client retention touch.

## Inputs
Lead record, consent register rows per channel, opt-out and do-not-call lists, the offer, owner voice profile, department rules.

## Step 0: consent check (every lead, every channel)
No row, expired, revoked, wrong channel, wrong seller scope, or low-confidence evidence means no draft. Write a refusal that names exactly what would cure it (for example: obtain written consent for text). Direct mail is an open channel unless the department says otherwise.

## Cadence defaults (override with department rules)
- Call: within 24 hours, day 3, day 7, then monthly. Local calling hours only. Recording and disclosure per department.
- Text: scoped consent only, at most one per week, opt-out instruction in every message.
- Email: welcome within 24 hours, then at most one per week, working unsubscribe.
- Speed to lead: acknowledge inside the target window with a reply that names the actual item inquired about and its actual price or status, taken from the record.

## Steps
1. Log the lead once; dedupe against existing records.
2. Consent check per channel.
3. Choose channel by consent, not by preference.
4. Draft naming the consent basis and expiry in the internal note.
5. Voice firewall and compliance review. BRIEF band until the owner trusts the voice, then DRAFT for low-risk replies.
6. Human sends. Log the touch and outcome.
7. Expiry sweep at 30 days. Opt-outs recorded the same day.
8. Transfers or data sharing need disclosure and prior written consent, logged.

## Outputs
Draft per allowed channel or a named refusal, cadence calendar, register updates, outcome log.

## Gates
- AI never auto-replies, auto-dials or leaves voicemail.
- Any conversational surface discloses it is AI in its first message.
- No promise made in a reply that is not recorded on the owner's promise list.

## Anti-patterns
Following up on the channel that is easiest. Treating a form submission as blanket consent. Dropping the lead without logging the reason.
