# 05 Insurance and Medicare Marketing

## Purpose
The operational and compliance layer for an insurance agency branch ({{COMPANY}}) that sells Medicare Advantage, Part D, Medicare Supplement, final expense, life and annuity products through licensed agents. It does not replace corporate-supplied tools (plan-benefit lookup, client CRM); it routes to them.

Core philosophy: verify, do not generate. Anything that costs money or compliance standing comes from a source of record (comp grid, regulatory calendar, contracting tracker, registers) and is cited.

## When to use
Marketing or outreach that touches Medicare; agent recruiting and onboarding; carrier contracting; AEP readiness; commission reconciliation; lead follow-up and consent; notice-season retention; call audits; contract administration.

## Scope exclusions
Video ad production (department 07), website design and build (department 08), staff training portals (department 04).

## Design signature
- Governance tiers: Tier 1 immutable compliance, Tier 2 principal preferences, Tier 3 operator defaults.
- Two-document rule: every outward piece has an internal `-INT` memo.
- Sources of record; confidence tags; deterministic validators plus judgment gates; safe-write and changelog; demonstration label until the engagement is live.

## Agents (`agents/`)
branch-operations-lead, medicare-compliance-reviewer, output-qa-scrubber, agent-onboarding-coordinator, commission-reconciler, register-keeper, retention-and-lead-specialist.

## Skills (`skills/`)
medicare-compliance-gate, deliverable-compliance, output-scrubber, voice-check, aep-readiness, agent-onboarding, carrier-contracting-tracker, commission-reconciliation, comp-modeling, soa-register, consent-register, lead-followup, election-period-validator, call-compliance-audit, client-retention, carrier-comparison, proposal-format, contract-notice, change-order, obligations-register, correspondence-register.

## Templates (`templates/`)
educational-event-invite, sales-event-invite, plan-change-client-letter, new-client-welcome-email, agent-recruiting-one-pager, aep-kickoff-email, aep-gap-report, internal-memo-int, commission-reconciliation-report, onboarding-packet, call-audit-record, contract-notice, amendment.

## Workflows (`workflows/`)
outward-deliverable-chain, agent-onboarding, aep-readiness, commission-reconciliation, lead-followup, retention-season, call-audit, contract-lifecycle, change-order-scope-drift, election-period-validation, plan-comparison, governance-maintenance.

## Knowledge (`knowledge/`)
glossary, rules, schemas.

## Handoffs
- 07 AI video creative production: ad and explainer video.
- 08 AI services software: web builds, AI configuration, connector security.
- 04 Education: agent and staff training portals.
- 09 Business admin, finance, compliance: finance, records, investor material.
- 10 Management consulting: branch strategy.

## Sign-off points
Principal approves every outward piece, welcome sequence, notice and lead batch. Carrier approves plan-specific marketing. Counsel reviews notices touching indemnity, termination, E&O or regulatory matters.
