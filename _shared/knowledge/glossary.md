# Glossary (shared)

Plain definitions of terms used across the office. Department glossaries add domain terms.

## Governance
- AUTO / DRAFT / BRIEF / WAIT: the four escalation bands. Execute; draft with voice check; draft and brief the human, ship on approval; escalate and do not draft.
- Band label: the first line of every internal output stating its band.
- Constitution: highest-priority rules, never overridden by a prompt.
- Tier 1 / Tier 2 / Tier 3: immutable rules (law, safety, privacy, truth) / owner preferences, logged / operational defaults.
- Verify, do not generate: facts come from sources or tools, not from the model.
- Confidence tag: HIGH, MEDIUM or LOW on every extracted fact; LOW goes to a human.
- Gate: a check that can stop delivery. Gates fail closed.
- Fail closed: missing input blocks instead of passing.
- Block / warn / pass silently: severity contract of the voice and compliance checks.
- SKIP: a gate that did not run. A coverage hole, not a pass.
- Door (one door): the single mandatory entry point for a class of outward action, such as outbound messages or outside research.
- Human sign-off: explicit, version-specific approval by a named role before release.
- Two-document rule: every outward piece has an internal twin.
- Internal twin (-INT): the internal companion carrying economics, findings and verification status.
- Four-pass review: calculation cross-check; completeness and sourcing; leak scan; layout and voice.
- Leak scan: search of an outward piece for internal-only content.
- Register: append-only, evidence-linked source of record.
- Evidence path: where the document supporting a row lives.
- Freshness window: maximum age of an input before a routine must refuse to act on it.
- Warning window: number of days before a deadline when it is flagged (for example URGENT, THIS WEEK).
- NEEDS_INPUT: flag returned instead of a guessed value.
- UNVERIFIED: an item not yet confirmed against a primary source; supports no money-touching claim.
- Safe-write: backup, atomic write, verify, changelog.
- Changelog: append-only line per change.
- Amendment protocol: propose, two approvals, update, retest, log.
- Skill promotion: occurrence log, template, skill, test, approve, audit.
- Skills audit: check that referenced paths exist and blocked phrases are really blocked.
- Context layer (0.ai-context): small per-project folder of loader, snapshot, document map and memory.
- LIVE DOCUMENTS: loader section listing registers and schedules to read directly, never mirrored.
- Canonical file plus rendered mirror: one versioned source; derived copies regenerated from it.
- Panel and judge: independent answers to an open question, then a synthesis of consensus, conflicts, gaps.
- Pre-mortem: four-prompt check before a structural change.
- Scaffold: structure present, data empty.
- Practice run: offline regression with clean and dirty fixtures per gate.
- Specificity quota: a creative needs at least one concrete fact.
- Promise list (due bill, we-owe): written commitments to a customer, each with a date and owner.

## Business
- ICP: ideal customer profile.
- CRM: customer relationship management system.
- CAC, ARPU, MRR, ARR, NRR, GRR, QBR, NPS, CSAT: common SaaS and customer metrics.
- KPI: key performance indicator, always with source and as-of date.
- SOP: standard operating procedure.
- SOW: statement of work.
- RFI: request for information.
- Change order / amendment: signed change to an agreed scope.
- Scope creep: work requested outside signed scope.
- Cost gate: quote, wait for explicit go, one approval per stated batch before paid generation.
- Lead, EBR (established business relationship), opt-out, consent basis, do-not-call.
- Retention touch: scheduled contact with a past customer, consent-checked.
- Speed to lead: time from inquiry to first acknowledgment.

## Compliance categories (generic public rules)
- Consent and outreach: telemarketing consent and do-not-call rules; commercial email rules.
- Children's online privacy; student records privacy.
- Health information privacy; customer financial data safeguards.
- Fair housing; equal credit and adverse-action notices; truth-in-lending advertising.
- Advertising law: truthful, substantiated claims; disclosure sets travel with triggering terms.
- AI disclosure: disclose AI involvement per the rule that applies.
- Records retention: keep per regime; stricter rule wins.
