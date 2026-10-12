# Schemas (shared, field names only)

No values. Department `schemas.md` files extend these. Dates are ISO strings; identities are masked.

## Routing note
request, lead_department, support_departments, band, gates, human_owner, due_date, open_question

## Handoff
project, date, from_role, to_role, status, closed_items[item, evidence, date], remaining[item, owner_role, blocker, unblocks], decisions_made, decisions_pending, read_first[], living_documents[path, purpose], non_negotiables[], measured_vs_assumed[fact, tag, as_of, source], definition_of_done

## Decision log entry
id, date, decision, decided_by_role, reason, alternatives, replaces, band, evidence_path

## Changelog entry
utc_timestamp, change, approver_role, backup_path

## Generic register row
id, date_recorded, subject_masked, type, status, confidence, evidence_path, valid_from, valid_until, retention_end, owner_role, recorded_by_role, notes

## Consent register
id, contact_masked, source, consent_language, date, expiry, channel_scope, seller_scope, evidence_path, status (active, expired, revoked), confidence

## Opt-out
contact_id, scope, occurred_at, source, detail, recorded_by

## Contact
id, name_placeholder, company_placeholder, role, email_placeholder, phone_placeholder, last_contact, notes, tags, relationship, source, created_at, updated_at

## Lead
id, contact_id, source, channel, received_at, interest_item, speed_to_lead_target, first_touch_at, status, next_touch_at, outcome

## Outbound message
id, contact_id, channel, kind, campaign, subject, body, status (draft, gated, approved, sent, refused), gate_report, approval_item_id, sent_at, sent_by

## Approval queue item
id, kind, title, summary, preview, risk (internal, customer_facing, money, legal), status, artifact_path, recipient_role, gate_report, gates_passed, produced_by, decided_at, decided_by, decision_note

## Promise list entry (due bill)
id, account_masked, description, owner_role, promise_date, status (draft, approved, open, fulfilled, canceled), fulfilled_date, notes

## Obligation
id, source_clause, obligation, type (deliverable, signature_gate, money_moment, notice), owner_role, due_or_trigger, status, evidence_link, notes

## Correspondence entry
id, date, direction, from_role, to_role, medium, subject, reference, action_required, response_due, status, link

## Audit log entry
id, ts, actor, action, detail, content_hash, provider_category, model_tier, metadata

## Data processing entry
project, source, received, files, bytes, manifest_hash, storage_location, retention_expiry, destroyed, certificate_ref, sub_processors

## Claim object (structured numeric output)
value, unit, confidence, source_or_derivation, as_of

## Platform policy entry
platform_or_body, rule, source, checked, recheck

## AI disclosure entry
date, asset_or_surface, ai_generated (text, image, narration, music, video), ai_touched_only, human_work_summary, disclosure_filed_where

## Production log entry
stage, date, human_role, human_input, ai_role, gate (pass or fail, sign_off)

## Scheduled routine
id, label, schedule (day, hour, minute, timezone), enabled, inputs[], freshness_window, never_list[], output, owner_role, last_run, last_result

## Skill promotion record
skill_name, first_occurrence_date, occurrence_count, template_path, test_cases[good, good, bad], approvals[role, date], audit_result
