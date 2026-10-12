# Schemas (field names only)

- Comp grid: carrier, product, level, basis, rate, first_year_comp, renewal_comp, notes.
- Lead economics: item, cost_per_lead_per_vendor, coop_available, target_acquisition_cost_per_issued_policy.
- Margin targets: override_margin_target, per_agent_production_target, persistency_target.
- Statement (normalized): carrier, product, record_reference_masked, writing_agent, comp_level, basis, paid_amount, statement_period.
- Reconciliation line: line_id, matched_grid_row, expected, paid, variance, status, confidence, reason, flags.
- SOA register: id, beneficiary_masked, products_scoped, date_agreed, method, appointment_date, validity_end, retention_end, evidence_path, status (active/expired/consumed), confidence, notes.
- Consent register: id, consumer_masked, source, consent_language, date, expiry, channel_scope, seller_scope, evidence_path, status (active/expired/revoked), confidence.
- Contracting tracker: agent, carrier, plan_year, status (not started/submitted/appointed/certified/RTS/terminated), evidence, writing_number, updated.
- Roster: agent, resident_state, producer_number, certification_status, carrier_certs, eo_through, rts_notices_on_file, book_review.
- Obligations register: id, source_clause, obligation, type (deliverable/signature gate/money moment/notice), owner, due_or_trigger, status (TEMPLATE/OPEN/IN PROGRESS/DONE/AT RISK/MISSED), evidence_link, notes.
- Correspondence register: id, date, direction, from, to, medium, subject, reference, action_required, response_due, status, link.
- Onboarding checklist: step_number, step, status, evidence_on_file.
- Compliance registrations: licenses, certifications, eo, appointments (placeholders in shared docs).
- Call audit log: call_date, regime, retention_end, storage_location, format, findings, confidence.
- Brand tokens: banned_strings, warn_strings.
- Changelog entry: utc_timestamp, change, approver, backup_path.
- Document header: type, year, abbreviation, sequence, internal_suffix.
