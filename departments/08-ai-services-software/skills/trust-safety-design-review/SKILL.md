---
name: trust-safety-design-review
description: Review a feature for moderation, consent, minors, provenance, in-app currency and data-handling risks before spec approval.
---
# Trust and Safety Design Review

## When to use
Any feature involving user-generated or AI-generated content, location, biometrics, face or voice, minors, or a virtual currency.

## Steps
1. Read `../../knowledge/trust-safety-consent-currency-patterns.md`.
2. Walk the checklist: content moderation gates, consent capture, minor handling, provenance labeling, currency ledger integrity, data retention, incident severity.
3. For each gap, add a requirement to the spec and a task.
4. Identify which parts need an attorney (biometric, children's privacy, consumer-protection rules).
5. Record the review as a decision record.

## Outputs
Requirements added to the spec, list of attorney questions, residual risks.

## Gates
Features that handle biometrics or minors do not ship without recorded legal review and principal approval.
