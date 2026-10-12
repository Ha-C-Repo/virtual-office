# Schemas: Publishing (field names only)

- **AI disclosure register (books/video):** date, asset, surface, ai_generated (text/illustration/narration/music/video), human_work_summary, disclosure_filed_where, copyright_status.
- **AI disclosure register (memoir):** date, title, subject, tier, authorship_mode, passage_tier_counts, ai_generated, human_work_summary, disclosure_per_format, limitation_of_claim_text, copyright_status.
- **Production log entry:** stage, date, human, human_input, ai_role, gate.
- **Persons and clearance register:** project, person_or_id, relationship, living, disposition, consent_status, sensitive_categories, appears_in, cleared_by, date.
- **Data processing register:** project, source, received, files, bytes, manifest_sha256, storage_location, retention_expiry, destroyed, certificate_ref, sub_processors.
- **Exposure event:** what, route, archive_implicated, solicited, containment, retention, disclosed_to, lesson.
- **Voice profile register:** subject, profile_version, registers_measured, corpus_words_per_register, stage0_result, control_corpus_version, consent_on_file, date, permitted_use.
- **Permissions log:** project, item, type, rights_holder, contact, status, fee, date_cleared, license_scope.
- **Platform policy register:** platform, rule, source, checked, recheck. **Open items:** item, status.
- **Spread map:** number, pages, text, beat, illustration_note, right_page_hook.
- **Timeline record:** event_id, date, date_precision, qualifier, provenance_type, extraction_confidence, verification_status, told_at, occurred_at, sensitivity_tier, source_ref.
- **Ingest manifest:** file, size, sha256, received_utc, source_label, lawful_basis.
- **Gap matrix:** domain, era, question, purpose_class, risk_flag.
- **Stylometry outputs:** voice_targets, slop_baseline, stage0_calibration (metric, subject_value, threshold, direction).
- **Passage authorship ledger:** chapter, passage_id, tier, author_of_origin, source_ref, date.
- **Assertion audit:** claim_id, claim_text, source_ref, status, confidence.
