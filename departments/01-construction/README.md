# 01 Construction

## Purpose
Estimating, bidding, contract administration, project controls, shop quality control, field reporting and contractor compliance for {{COMPANY}}, a specialty trade contractor (default trade pack: structural steel fabrication and erection, working as a subcontractor to general contractors). The department is trade-agnostic by design: a company profile plus a swappable trade pack (item classes, assemblies, benchmarks, scope checklist) adapts it to other trades.

## Governing philosophy
**Verify, do not generate.** AI checks, reformats and drafts. It never produces a system-of-record number (price, quantity, rate, weight). Locked rate tables and the reference shape database own the numbers; deterministic calculators do the arithmetic. Every extracted item carries a confidence tag (HIGH / MED / LOW); LOW items go to a human. Nothing leaves the office until the approver role signs off.

## When to use
- A bid invitation, drawing set or scope of works arrives.
- A contract is awarded and needs a budget, registers and a project folder.
- A client asks for extra work (change order) or causes delay (notice).
- Milestone invoices, purchase orders or pay applications are due.
- Material arrives at the shop, or a piece moves through fabrication and release.
- Field messages or voice notes need turning into a daily log and a weekly digest.
- A contractor-qualification questionnaire or prequalification package is requested.

## Contents

### Agents (`agents/`)
| File | Role |
|---|---|
| `construction-lead.md` | Department manager and router; owns gates and hand-offs |
| `estimator-takeoff.md` | Scout: reads drawings, builds takeoff and pricing inputs |
| `bid-reviewer.md` | Independent verifier: sanity gates, reconciliation, four-pass review |
| `proposal-composer.md` | Composer: proposal, margin report, RFIs, bid emails in the executive voice |
| `contract-administrator.md` | Registers, change orders, notices, billing, purchase orders |
| `shop-qc-inspector.md` | Receiving, traveler, NCR, release |
| `field-reporting-clerk.md` | Site diary, delivery and delay logs, weekly digest |
| `safety-prequal-coordinator.md` | Safety questionnaires, injury rates, prequalification package |

### Skills (`skills/<name>/SKILL.md`)
drawing-reading, drawing-stage-classifier, takeoff, takeoff-completeness-check, bid-pricing, bid-sanity-check, tender-ingest, requirement-register, contract-risk-review, inclusions-exclusions, bid-reconciliation, bid-output-scrubber, two-document-pair-check, scope-creep-detector, change-order, contract-notice, award-to-budget, milestone-billing, steel-purchase-order, supplier-quote-tracker, site-diary, shop-traveler-gates, prequal-tracker, safety-questionnaire-responder, executive-voice-check, competitor-analysis.

### Templates (`templates/`)
client-proposal, internal-margin-report, bid-intel-report, statement-of-qualifications, value-engineering-alternate, clarification-register, returnable-pricing-schedule, rfi-form, sf-confirmation-rfi, bid-follow-up-email, change-order, contract-notice, milestone-invoice, pay-application-seed, purchase-order, obligations-register, correspondence-register, contract-risk-register, project-budget-workbook, project-folder-skeleton, project-loader, site-diary-log, weekly-owner-digest, shop-traveler, ncr, receiving-inspection-report, release-certificate, pre-flight-checklist, prequalification-checklist, experience-mod-letter.

### Workflows (`workflows/`)
01 bid pipeline, 02 four-pass review, 03 tender ingest to reconciliation, 04 drawing indexing, 05 award to project controls, 06 scope creep to change order, 07 contract notice, 08 milestone billing and receivables, 09 steel procurement, 10 shop QC three-gate, 11 site diary daily routine, 12 prequalification package.

### Knowledge (`knowledge/`)
`glossary.md`, `rules.md`, `schemas.md`.

## Hand-offs to other departments
- **Business admin, finance and compliance (09):** invoices, receivables, insurance certificates, tax and registration documents, accounting entries.
- **Management consulting (10):** pricing strategy or business-model questions beyond a single bid.
- **AI services and software (08):** tooling, scheduled routines, connectors, self-test harness.
- **AI video and creative production (07):** marketing video and render work (brief from this department, approval stays here).
- **IP and patent support (11):** proprietary connection or process details being published.
- **Hardware / IoT product development (12):** embedded tracking of pieces or equipment.

## Standing gates
1. Intake gate before takeoff (drawings, GC, deadline, stage, scope confirmed; never assume).
2. Rates are locked; no session-level overrides.
3. Two independent calculation paths must agree before a price is released.
4. Output scrub and two-document pair check before anything leaves.
5. The approver role signs before send. Notices and change orders are DRAFT ONLY until then.
