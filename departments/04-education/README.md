# 04 Education (Homework Help and Virtual Tutor App Studio)

## Purpose
An app-studio office that designs, builds, verifies and ships a mobile homework-help and virtual-tutor product for all grade levels (preschool through college). Core idea: **the language model explains, a deterministic solver certifies, and nothing wrong ships.** The product is offline-first, has no accounts, and treats children's privacy and academic integrity as design constraints, not afterthoughts.

## Scope
1. Product management: MVP cut, user stories, numbered acceptance criteria, open questions, scope control
2. Tutoring content: step-by-step explanation, practice variant, explain-it-back prompt, confidence tagging
3. Answer verification and content QA (deterministic solver, audit trail, fact-base plan for non-math subjects)
4. Privacy and compliance (children's data, age gate, data minimization, store data-safety groundwork)
5. Monetization planning (tier options, metering scaffold, unit economics with UNMEASURED inputs)
6. Release engineering (build conventions, dependency ledger, release train, two-artifact release)
7. Marketing and store presence (listing, keywords, release notes, brand voice)
8. Competitive research
9. Studio governance (constitution, amendments, protected files, backups, change log)

## When to use
Any task about the learner-facing app, its specs, its verification rules, its compliance posture, its pricing, or its releases. For classroom or curriculum-publishing products see `../06-publishing/`.

## Agents (`agents/`)
- `studio-lead.md` (lead): governance, routing, owner approvals
- `product-manager.md`: specs, acceptance criteria, scope control
- `tutor-content-qa.md`: pedagogy and correctness QA
- `verification-engineer.md`: solver contract, check plans, test vectors, parity
- `privacy-compliance-officer.md`: children's privacy, data minimization, release compliance
- `release-manager.md`: build discipline, release train, release pair
- `store-marketing-lead.md`: listing, keywords, notes, public copy, competitor research

## Skills (`skills/`)
tutor-content-qa, answer-verification, edtech-compliance, release-compliance, public-copy-scrubber, release-notes-format, store-listing-format, aso-listing, release-pair-check, staged-release-train, pricing-config, pricing-sanity-check, scope-creep-detector, spec-completeness-check, spec-maturity-classifier, competitor-teardown, photo-intake-rd, mobile-build, integrity-coaching

## Templates (`templates/`)
product-spec, design-spec-answer-verification, design-spec-privacy, design-spec-monetization, competitor-teardown, release-notes, store-listing, release-pair-build-report, postmortem-note, release-compliance-table, business-config, solver-test-vectors, phase-handoff, domain-translation-map, release-context-loader

## Workflows (`workflows/`)
01-learner-problem-flow, 02-tutor-content-qa, 03-spec-driven-lifecycle, 04-release-train, 05-two-artifact-release, 06-pricing-sanity-gate, 07-competitor-teardown, 08-backup-and-change-discipline

## Knowledge (`knowledge/`)
glossary.md, rules.md, schemas.md

## Handoffs to other departments
- Software engineering beyond the app skeleton, model routing and integrations: `../08-ai-services-software/`
- Promo video and creative production: `../07-ai-video-creative-production/`
- Legal entity, store accounts, tax and finance: `../09-business-admin-finance-compliance/`
- Study guides or books derived from tutoring content: `../06-publishing/`
