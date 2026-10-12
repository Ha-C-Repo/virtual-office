# 09 Business Admin, Finance and Compliance

## Purpose
Administration, finance, compliance, commercial and investor support for a small owner-operated business ({{COMPANY}}) that produces and sells physical assets in a controlled environment, and bids for contract work that requires safety and insurance prequalification. The pattern is: a context layer (identity, hard rules, voice, pricing), a workflow layer, a data layer of registers, and admin layers for finance, compliance, commercial and investor work.

Core philosophy: the AI does data moves; humans do physical and biological judgment. Never fabricate a reading, count, ID, yield or policy. Missing data returns a flag, not a value.

## When to use
Weekly yield and cost audits; reserve sweeps; invoicing and purchase orders; permit, trade-document and certification tracking; intake and quarantine records; answering contractor prequalification questionnaires; investor packages, grants and reports.

## Agents (`agents/`)
admin-operations-lead, finance-controller, compliance-officer, prequalification-specialist, investor-relations-writer, records-keeper, billing-and-procurement-clerk.

## Skills (`skills/`)
verify-dont-generate, inventory-reconciler, unit-yield-audit, opex-cap-monitor, reserve-sweep, ar-milestone-billing, purchase-order-drafter, permit-tracker, trade-documentation-log, certification-register, sop-repository, prequalification-response, insurance-gap-analysis, investor-package, grant-application, investor-reporting, output-scrubber, voice-check, spreadsheet-formula-auditor, document-governance.

## Templates (`templates/`)
operating-rules, brand-voice-guide, weekly-yield-audit, reserve-sweep-log, invoice, purchase-order, permit-register, trade-documentation-log, certification-register, sop-index, safety-program-checklist, prequalification-status, prequalification-answer, insurance-gap-analysis, investor-package-outline, grant-application-outline, investor-update, changelog, buyer-guarantee-policy, occupancy-map.

## Workflows (`workflows/`)
production-cycle, weekly-yield-audit, friday-reserve-sweep, intake-quarantine, inventory-indexing, milestone-billing, purchase-order, prequalification-response, investor-reporting, routine-rollout.

## Knowledge (`knowledge/`)
glossary, rules, schemas.

## Handoffs
- 01 Construction: project billing detail, change orders, bid documents (this department keeps AR, PO and prequalification).
- 05 Insurance and Medicare marketing: agent commission and contracting registers stay there.
- 10 Management consulting: strategy and pricing work.
- 11 IP and patent support: IP assignments and filings.
- Counsel: legal, tax and securities questions through {{OWNER_ROLE}}.

## Sign-off points
{{OWNER_ROLE}} approves work plans, every external document, every invoice and PO, every submission to a platform or investor, and every money movement.
