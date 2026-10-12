# Generic Patterns: Trust and Safety, Consent, In-App Currency

A reusable note for any consumer or prosumer product that generates or hosts content, captures personal data, or sells a virtual currency. Patterns only; legal requirements vary by jurisdiction and need counsel.

## 1. Moderation
- Three mandatory gates for generated or user-submitted content: (a) input gate before generation (prompt and uploads), (b) output gate before storage, (c) delivery gate before anyone else can see it.
- Log every decision in a moderation events table: content id, gate, rule, action, reviewer, timestamp.
- Human review queue for borderline and appeals. Severity levels with response times.
- Block minors from content classes that require adult access; do not rely on self-declared age alone for high-risk features.

## 2. Consent
- Separate consent for each sensitive use: location, biometrics (face, voice), contacts, training use of content.
- Consent is a record: user id, purpose, notice version, timestamp, choice, withdrawal time.
- Disclose before the system permission prompt, in plain language, on its own screen (see `../templates/location-consent-notice.md`).
- Easy withdrawal; withdrawal deletes or stops use within a stated time.
- Biometric features: written policy, retention schedule, ephemeral handling where possible, jurisdiction-specific rules (state biometric statutes, EU data protection rules).
- Children's data: children's online privacy law (COPPA and equivalents) applies; default to blocking under-age users.

## 3. Isolation and privacy of user captures
- User-provided likeness, voice or private captures stay private to that user: never pooled, never reused for other users or for training without separate consent.
- Per-user isolation is enforced in storage paths, caches and indexes.
- Ephemeral processing for raw biometric inputs; store only what the feature needs.

## 4. Provenance and labeling
- Label AI-generated media in the product and embed provenance metadata in exports.
- Keep a record linking each generated asset to its inputs, model configuration and moderation outcome.
- Obtain rights for any real person's likeness; no impersonation.

## 5. In-app currency (coins, credits, tokens)
- Treat the balance as a ledger, not a number: append-only entries (id, user, delta, reason, reference, timestamp); balance derived or reconciled.
- Idempotency keys on every purchase and spend call; signed webhooks from the payment processor.
- Entitlements are separate from balance (what the user may access, with expiry).
- Clear pricing display: cost in currency units shown before spend; real-money equivalence disclosed where the law requires.
- Refund and chargeback handling: reverse entries, never delete; flag abuse patterns.
- Spending controls and limits for minors and optionally for all users; no dark patterns, no pressure countdowns.
- Store policies (app marketplaces) restrict how digital goods are sold; review them during design.
- Consumer-protection and unfair-practices rules (FTC and state equivalents) apply to pricing and disclosures; sweepstakes, loot-box and gambling rules may apply to randomized rewards.
- Cost control: track generation cost per unit of revenue; cache reusable generated assets (semantic cache: filter by state, score similarity, serve or adapt or generate, always write back).

## 6. Incident handling
- Severity levels: SEV1 (harmful content published, data exposure), SEV2, SEV3, SEV4.
- Takedown path with a target time; evidence preserved; postmortem with follow-ups.
- Report channel for users; response commitments published.

## 7. Threat-model starters
Prompt injection into generation, upload abuse, account takeover, wallet fraud, replay of purchase calls, scraping of private captures, insider access to private content.

## Review hook
Use `../skills/trust-safety-design-review/SKILL.md` before approving any spec touching these areas.
