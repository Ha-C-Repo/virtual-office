---
name: sales-lead-retention
description: Retention engine with consent ledger, four channel gates, equity letter, do-not-call layer and measurement.
---
## Touch types
Service-due, warranty or service-contract expiry, positive equity, near-maturity of an in-house contract. One specific personal line each.

## Steps
1. Build the list from the deal and service records. Consent-safe contacts only.
2. Scrub the list against the internal do-not-call list and the national registry (freshness and evidence recorded).
3. Check the consent ledger per channel: GRANTED, DENIED, UNKNOWN. UNKNOWN is not consent. Record established-business-relationship events and opt-outs (honor within the statutory business-day window).
4. Choose the channel. Email: accurate subject, advertising disclosure, physical address, opt-out. Text: consent required. Phone is not a messaging channel. AI voice never dials or leaves voicemail.
5. Direct mail is the home for the equity letter; no cost or gross reachable.
6. Draft, voice check, approval queue (`../../workflows/02-sales-outbound-message.md`).
7. Measure by recorded lead-measurement events.

## Outputs
Consent-safe send list, drafts, measurement record.

## Gates
Refusals are logged as REFUSED. The outbound gate has no bypass argument.
