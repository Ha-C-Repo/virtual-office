# 12 - Hardware and IoT Product Development

## Purpose
Run a hardware and connected-product startup (device, firmware, cloud, mobile app, website) through architecture decisions, phased launch, and investor and partner communications for {{COMPANY}}. The source material is a connected-vehicle access platform; this department generalizes it.

## Scope note
The original source material was thin (folder structure and skill outlines). This department was expanded with BOM and cost rollup, supplier qualification, EVT/DVT/PVT test planning, pilot design and OTA release control. Technical content beyond the source is generic, widely known practice and is labeled as such. Counts: 5 agents, 11 skills, 11 templates, 8 workflows, 4 knowledge files, 1 harness.

## When to use
- Recording an architecture decision ("design lock") for hardware, firmware, cloud or mobile.
- Planning or gating a launch phase (pre-launch, pilot, commercial, scale).
- Preparing investor one-pagers, decks or follow-ups.
- Defining market strategy and brand for a connected product.
- Coordinating across product areas and with IP counsel.

## Product area layout
architecture (adr, diagrams, specs); business (investor, market, model, partnerships); ip (assignment, counsel, patent, trademark); ops (confidentiality, domain); product (cloud, firmware, hardware, mobile, website); templates; skills; admin.

## Agents (`agents/`)
- `product-development-lead` - lead; roadmap, cross-area coordination, gates
- `systems-architect` - design locks, interfaces, security architecture
- `launch-and-investor-manager` - launch phases, market strategy, investor materials
- `supply-chain-manager` - BOM, quotes, supplier qualification, unit cost
- `test-and-certification-coordinator` - test plans, build-phase evidence, certification prep

## Skills (`skills/`)
design-lock-adr, launch-phase-gating, investor-communications, market-strategy-brief, connected-product-risk-review, product-area-handoff, bom-cost-rollup, supplier-qualification, pilot-program-design, ota-update-plan, build-phase-test-plan

## Templates (`templates/`)
design-lock, launch-phase-checklist, investor-one-pager, investor-deck-outline, investor-followup-email, product-area-status, bom, supplier-scorecard, test-plan, pilot-plan, ota-release-checklist

## Workflows (`workflows/`)
design-lock-process, launch-phase-gate, investor-outreach, certification-and-compliance-prep, build-phase-gate, supplier-qualification, pilot-execution, ota-release

## Knowledge (`knowledge/`)
glossary, rules, schemas, regulatory-map-generic

## Harnesses (`harnesses/`)
Stdlib Python 3 with self-tests: `bom_rollup.py` (unit cost by volume tier, margin, stale-quote check). Run `python bom_rollup.py --selftest` after any change.

## Handoffs
- 11-ip-patent-support: disclosures, pre-disclosure check, FTO before pilot.
- 08-ai-services-software: cloud and mobile software practice (specs, environment promotion, security).
- 10-management-consulting: business model, pricing, investor strategy.
- 09-business-admin-finance-compliance: entity, insurance, regulatory filings.
