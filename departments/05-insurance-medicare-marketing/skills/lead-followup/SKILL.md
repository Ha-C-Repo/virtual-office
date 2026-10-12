---
name: lead-followup
description: Consent-gated, TCPA-safe lead follow-up cadence that drafts per channel or issues a named refusal.
---
# Lead follow-up

## When to use
For each batch of new or aging leads.

## Inputs
Lead batch, consent register (`../consent-register/SKILL.md`).

## Steps
0. Consent check per lead and per channel. No row, expired, revoked, wrong channel, or low-confidence evidence: no draft; return a refusal naming what would cure it.
1. Cadence by channel:
   - Call: within 24 hours, day 3, day 7, then monthly. Call hours 8am to 9pm local; respect do-not-call.
   - Text: scoped consent only; at most one per week; opt-out instruction in every message.
   - Email: welcome within 24 hours, then at most one per week; working unsubscribe.
2. Each draft names its consent basis and expiry in the `-INT` note.
3. Expiry sweep at 30 days.
4. Transfers require disclosure and prior written consent for data sharing; log in the correspondence register.

## Outputs
Drafts or named refusals; internal note; register updates.

## Gates
Drafts only; {{PRINCIPAL_ROLE}} approves before anything is sent. Opt-outs update the register the same day. Voice rules in `../voice-check/SKILL.md`.
