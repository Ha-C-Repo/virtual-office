---
name: consent-register
description: Permission-to-contact and marketing consent tracking with exact language, expiry, channel and seller scope.
---
# Consent register

## When to use
Whenever a lead or client gives, narrows or revokes permission to be contacted, and as step 0 of every lead workflow.

## Steps
1. Record: masked consumer ID, source, exact consent language, date, expiry (permission to contact is valid 12 months), channel scope (call, text, email), seller scope, evidence path, status (active, expired, revoked), confidence.
2. For purchased leads, the vendor's consent documentation (language, date, source) must be on file before any dial.
3. On opt-out, STOP or unsubscribe, set status revoked the same day.
4. Answer consent queries from the register only: "may we contact X by channel Y today" returns yes only with an active, in-scope, high or medium confidence row.

## Outputs
Register row; yes/no answers with the row cited; named refusals stating what would cure the gap.

## Gates
Low-confidence evidence is treated as no consent. Re-verify the current one-to-one consent rule each season. No deletion before retention end.
