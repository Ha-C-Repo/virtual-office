# 03 Real Estate (Residential Brokerage Office)

## Purpose
A virtual office for a residential brokerage run by a principal agent/broker ({{OWNER}}) with a small team. The AI layer drafts, extracts, checks and organizes. Humans own every number that costs money and every message that leaves the office. Core rule: **verify, do not generate**.

## Scope
1. Listing presentation and CMA (comparative market analysis) production
2. Pricing strategy (three scenarios, comp corridor check, internal net sheets)
3. Listing intake and document classification
4. 3D / virtual tour production and staging imagery
5. Buyer consultation and offer support
6. Transaction coordination (deadlines, amendments, repair requests, closing checklist)
7. Open house kits
8. Social media (draft, screen, approve, publish, measure, learn)
9. Lead retention over past clients and sphere; outbound gating
10. Video and advertising production (see handoffs)
11. Compliance and governance (fair housing, MLS terms, advertising disclosure, consent, do-not-call)
12. Brand voice and client onboarding intake

## When to use
Use this department for any task touching a listing, a buyer, a contract-to-close timeline, a client-facing document, or an outbound message to a past client or lead. Do not use it for legal advice, appraisals, or tax advice: it produces opinions of value and organized drafts for licensed humans to decide.

## Agents (`agents/`)
- `office-manager.md` (lead): routes work, enforces gates, owns the approval queue view
- `listing-cma-analyst.md`: intake, GLA sourcing, comps, adjustment grid, price scenarios
- `transaction-coordinator.md`: contract dates, deadline calendar, amendments, closing checklist
- `marketing-coordinator.md`: open house, social, flyers, video briefs
- `compliance-reviewer.md`: fair housing, advertising, consent, disclosure; four-pass review
- `lead-retention-manager.md`: sphere touches, consent ledger, equity letter, outbound gate
- `tour-producer.md`: floor plan reading, tour build, completeness check

## Skills (`skills/`)
cma-pricing, cma-sanity-check, listing-doc-classifier, listing-compliance, client-doc-scrubber, two-pdf-pair-check, floorplan-reading, tour-build-and-check, transaction-timeline, deadline-risk-detector, amendment-generator, buyer-consult, open-house-kit, social-media-loop, lead-retention, research-gate, portal-listing-intake, brand-voice-check

## Templates (`templates/`)
office-rules, commission-and-fees-internal, brand-voice-guide, company-details, listing-presentation-client, listing-presentation-internal, cma-report, net-sheet-internal, open-house-signin-sheet, open-house-flyer-and-feature-sheet, followup-sequence, amendment-and-repair-request, annual-equity-letter, fair-housing-rewrite-table, client-intake-pack, video-script-brief, handoff-note, lead-stub

## Workflows (`workflows/`)
01-cma-listing-presentation, 02-listing-intake, 03-tour-build, 04-transaction-timeline, 05-open-house, 06-social-media, 07-outbound-and-lead-retention, 08-video-production, 09-change-control

## Knowledge (`knowledge/`)
glossary.md, rules.md, schemas.md

## Harnesses (`harnesses/`)
Stdlib Python 3 with self-tests: `net_sheet.py`. See `harnesses/README.md`. Run `python net_sheet.py --selftest` after any change.

## Handoffs to other departments
- Video/ad production: to `../07-ai-video-creative-production/` (scripts must pass the script screen here first).
- Contracts, commission bookkeeping, entity filings: to `../09-business-admin-finance-compliance/`.
- Website builds, tour engine software, integrations: to `../08-ai-services-software/`.
- Long-form publishing for the brokerage: to `../06-publishing/`.
