# Schemas (field names only)

## Approval queue item
id, kind, title, summary, preview, risk, status, transaction_id, artifact_path, recipient, payload, gate_report, gates_passed, produced_by, session_id, decided_at, decided_by, decision_note, sent_at, created_at, updated_at

## Audit
id, ts, actor, action, detail, content_hash, provider, model, metadata

## Contact
id, name, company, role, email, phone, last_contact, notes, tags, relationship, source, source_detail, mailing_street, mailing_city, mailing_state, mailing_zip, property_address, schema_version

## Consent
Channel consent: contact_id, channel, state, basis, recorded_by, recorded_at
Consent events: contact_id, channel, action, occurred_on, recorded_by
Opt-outs: contact_id, scope, identifier, identifier_kind, reason, recorded_at
Internal DNC: identifier, identifier_kind, reason, recorded_at
EBR events: contact_id, kind, occurred_on
Contact-transaction link: contact_id, transaction_id, role

## Outbound
outbound: id, contact_id, channel, kind, campaign, subject, body, status, gate_report, approval_item_id, sent_at, sent_by
outbound_events: outbound_id, status, detail, occurred_at
outcomes: contact_id, kind, source, campaign, channel, occurred_on, value, detail

## DNC evidence
registry files: registry, area_code, published_on, downloaded_on, file_name, hash, row_count
scrubs: performed_on, numbers_in, numbers_removed, freshness
training records, violation reports (occurred_on, description, root_cause, remediation), seller-assertion records

## Social
accounts: platform, account_type, role, active
profile_checks: broker_name_present, broker_name_prominent, disclosure_links, passed, evidence
posts: platform, status, title, caption, first_comment, hashtags, media_paths, listing_dir, language, promoted, scheduled_for, published_at, permalink
post_dimensions: dimension, level
metrics_post: reach, impressions, engagements, likes, comments, shares, saves, profile_taps, video_views, missing_fields, series_break
lead_events: kind, associated_post, window_hours, confidence
posteriors: dimension, level, alpha, beta, trials, successes
driver_halts: reason, occurred_at

## Hash chain document log
doc_type, doc_name, file_hash, prev_hash, chain_hash, metadata, created_by

## Lead scan
subject, sender, received_at, score, tier, reasons, project_signals, actioned

## Retention calendar
readme, counties[] with dated entries and verified_on

## Brand tokens
name, version, status, fill_state, sources, identity, logo, palette, typography

## Lead stub (file per lead)
Lead ID, Name, Phone, Email, Property interest, Source, Consent, Notes

## Config template (slots only, no values)
AI provider key slots, project_root, routing notes, messaging gateway host/port/credential slot, MLS feed key slot, county data key slot, walkability data key slot, capture service key slot

## Social export CSV
banner line, then metric columns per platform
