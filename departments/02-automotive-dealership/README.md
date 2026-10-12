# 02 Automotive Dealership

## Purpose
A virtual back office for {{DEALERSHIP}}, a small independent used-vehicle retailer where one person often wears several hats. The office drafts, checks and organizes. A human owns every number and posts or sends everything. It runs eight clearly separated functions, each with its own agent, skills, templates, workflows and knowledge files, coordinated by one lead.

## Core ideas
1. **Verify, do not generate.** The VIN and the title are the controlling inputs. Every vehicle fact comes from a sourced record tagged HIGH / MED / LOW. The model never sets mileage, price, VIN or title status and never does arithmetic; a deterministic calculator owns payments, totals and markdowns.
2. **The condition grade gates the adjective.** Grade A Inspected, B Declared, C As-Is Unverified decide what copy may claim.
3. **Two-document rule.** Every unit or deal yields a client document and an internal `-INT` twin carrying cost, pack, recon spend, floorplan interest, reserve and gross. A client document without its twin is a defect.
4. **One home per fact.** Registers are the source of truth; other files link by path.
5. **Gates with exit-code contract.** 0 clean, 1 blocked, 2 usage or input error (2 is not a pass). SKIP is a coverage hole. No override on Tier 1 gates.
6. **Tiered governance.** Tier 1 immutable (law), Tier 2 owner preferences (logged), Tier 3 defaults.
7. **Human approval queue.** Nothing auto-posts, auto-replies or auto-dials.
8. **Placeholders fail closed.** An unfilled token in an outward document is a blocked defect.

## Sub-areas (the eight functions)
Each function owns files carrying its prefix in `agents/`, `skills/`, `templates/` and `workflows/`. The three knowledge files are sectioned by the same function numbers.

| # | Function | Agent | Workflows |
|---|---|---|---|
| 01 | Inventory | `agents/01-inventory-agent.md` | `workflows/01-inventory-*.md` |
| 02 | Sales | `agents/02-sales-agent.md` | `workflows/02-sales-*.md` |
| 03 | Finance and Insurance | `agents/03-fi-agent.md` | `workflows/03-fi-*.md` |
| 04 | Title and Admin | `agents/04-title-admin-agent.md` | `workflows/04-title-*.md` |
| 05 | Service and Recon | `agents/05-service-recon-agent.md` | `workflows/05-service-*.md` |
| 06 | Marketing | `agents/06-marketing-agent.md` | `workflows/06-marketing-*.md` |
| 07 | Reputation | `agents/07-reputation-agent.md` | `workflows/07-reputation-*.md` |
| 08 | Compliance | `agents/08-compliance-agent.md` | `workflows/08-compliance-*.md` |

Lead: `agents/00-dealership-lead.md`. Cross-function: `workflows/00-morning-briefing.md`, `workflows/00-unit-to-listing-gate-order.md`. Knowledge (sections prefixed 00 to 08): `knowledge/glossary.md`, `knowledge/rules.md`, `knowledge/schemas.md`.

Skills are named `<function>-<skill>` (for example `inventory-condition-grading`). Templates are named `<function>-<document>`.

## Each function's charter in one line
- **Inventory:** the spine. Nothing else works until a unit record is correct.
- **Sales:** speed-to-lead and a clean deal pipeline; every promise recorded.
- **F&I:** transparent structures, covered-borrower check on every deal, adverse-action on every decline.
- **Title and Admin:** deal jackets complete, deadlines never missed, licenses current.
- **Service and Recon:** a unit is not listed until recon is closed; a we-owe is never late.
- **Marketing:** truthful, substantiated, specific ads; no generated vehicles, buildings or people.
- **Reputation:** answer every review the right way; escalate allegations the same day.
- **Compliance:** owns Tier 1, the five registers and the gates; can stop any department.

## When to use
Any request touching a vehicle, a lead, a deal, a title, a repair promise, an ad or post, a review, or a compliance question.

## Hand-offs to other departments
- **Business admin, finance and compliance (09):** accounting, payroll, insurance policies, tax, general licenses.
- **AI video and creative production (07):** video work beyond walkaround clips (brief from Marketing; hard rules still apply).
- **AI services and software (08):** routines, connectors, gate code, practice-run harness.
- **Publishing (06):** long-form content.
- **Real estate (03):** lot or facility transactions.

## Human roles referenced
{{OWNER}}, {{GM}}, {{SALES_MANAGER}}, {{FI_MANAGER}}, {{RECON_LEAD}}, {{TITLE_CLERK}}, {{IT_DIRECTOR}}. In a one-person store the owner holds all of them.

## Go-live gates
License on file, county set, warranty terms stated, doc fee set, lender (or an explicit in-house-only declaration) recorded, ad substantiation register seeded or explicitly empty, and a compliance check passing on a sample ad built from the filled profile. See `workflows/08-compliance-onboarding-and-go-live.md`.

## File index

**agents/**
- `agents/00-dealership-lead.md`
- `agents/01-inventory-agent.md`
- `agents/02-sales-agent.md`
- `agents/03-fi-agent.md`
- `agents/04-title-admin-agent.md`
- `agents/05-service-recon-agent.md`
- `agents/06-marketing-agent.md`
- `agents/07-reputation-agent.md`
- `agents/08-compliance-agent.md`

**skills/**
- `skills/compliance-buyers-guide/SKILL.md`
- `skills/compliance-registers-audit/SKILL.md`
- `skills/compliance-safeguards-program/SKILL.md`
- `skills/compliance-verification-before-completion/SKILL.md`
- `skills/fi-client-doc-scrubber/SKILL.md`
- `skills/fi-desking/SKILL.md`
- `skills/fi-military-lending/SKILL.md`
- `skills/inventory-condition-grading/SKILL.md`
- `skills/inventory-condition-report-reading/SKILL.md`
- `skills/inventory-document-classifier/SKILL.md`
- `skills/inventory-listing-completeness-check/SKILL.md`
- `skills/inventory-photo-standard/SKILL.md`
- `skills/inventory-pricing-appraisal/SKILL.md`
- `skills/inventory-pricing-sanity-check/SKILL.md`
- `skills/inventory-vehicle-record-intake/SKILL.md`
- `skills/marketing-owner-voice-check/SKILL.md`
- `skills/marketing-social-media/SKILL.md`
- `skills/marketing-vehicle-ad-compliance/SKILL.md`
- `skills/marketing-video-walkaround/SKILL.md`
- `skills/reputation-response/SKILL.md`
- `skills/sales-lead-response/SKILL.md`
- `skills/sales-lead-retention/SKILL.md`
- `skills/service-we-owe-generator/SKILL.md`
- `skills/title-deadline-risk-detector/SKILL.md`
- `skills/title-deal-jacket-checklist/SKILL.md`
- `skills/title-title-and-tag/SKILL.md`

**templates/**
- `templates/compliance-ad-substantiation-register.md`
- `templates/compliance-ai-disclosure-register.md`
- `templates/compliance-data-processing-register.md`
- `templates/compliance-disclosure-register.md`
- `templates/compliance-platform-policy-register.md`
- `templates/compliance-scorecard.md`
- `templates/fi-adverse-action-notice.md`
- `templates/fi-deal-recap-int.md`
- `templates/fi-deal-recap.md`
- `templates/fi-lender-packet-checklist.md`
- `templates/fi-product-menu.md`
- `templates/fi-stipulation-tracker.md`
- `templates/inventory-comp-grid.md`
- `templates/inventory-disclosure-set.md`
- `templates/inventory-photo-manifest.md`
- `templates/inventory-recon-work-order.md`
- `templates/inventory-unit-record.md`
- `templates/marketing-social-caption.md`
- `templates/marketing-video-brief.md`
- `templates/reputation-escalation-note.md`
- `templates/reputation-response-by-class.md`
- `templates/reputation-review-queue.md`
- `templates/reputation-review-request.md`
- `templates/reputation-weekly-sentiment-digest.md`
- `templates/sales-appointment-confirmation.md`
- `templates/sales-lead-acknowledgment.md`
- `templates/sales-trade-appraisal-request.md`
- `templates/service-30-day-checkin.md`
- `templates/service-recon-log.md`
- `templates/service-we-owe-int.md`
- `templates/service-we-owe.md`
- `templates/title-deadline-timeline.md`
- `templates/title-deal-jacket-checklist.md`
- `templates/title-lien-filing-tracker.md`
- `templates/title-temp-tag-log.md`

**workflows/**
- `workflows/00-morning-briefing.md`
- `workflows/00-unit-to-listing-gate-order.md`
- `workflows/01-inventory-aged-unit-review.md`
- `workflows/01-inventory-vehicle-record-to-listing.md`
- `workflows/02-sales-lead-to-delivery.md`
- `workflows/02-sales-outbound-message.md`
- `workflows/03-fi-desking-and-submission.md`
- `workflows/04-title-deal-jacket-and-deadlines.md`
- `workflows/05-service-recon-and-we-owe.md`
- `workflows/06-marketing-ad-and-social-publishing.md`
- `workflows/07-reputation-digital-footprint.md`
- `workflows/07-reputation-review-response.md`
- `workflows/08-compliance-four-pass-review.md`
- `workflows/08-compliance-onboarding-and-go-live.md`

**knowledge/**
- `knowledge/glossary.md`
- `knowledge/rules.md`
- `knowledge/schemas.md`
