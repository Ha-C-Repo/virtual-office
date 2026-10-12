# Schemas: Automotive Dealership (field names only)

Sections are prefixed by function number. Types and values are left to the implementation.

## 00 Shared
- **dealer_profile:** legal_name, dba, license_number, license_expiry, address_line1, city, county, state, zip, phone, sms_number, email_domain, website, sales_hours, service_hours, has_service_dept, lenders[], has_inhouse_paper, warranty{administrator, term, miles, coverage, deductible}, doc_fee, default_down_tier[], price_band{low, high}, social{page_url, place_id, handles}, market{metro, counties_served[], nearby_installations[]}
- **audit:** id, ts, actor, action, detail, content_hash, provider, model, metadata
- **approval queue:** queue_items (kind, title, summary, preview, risk, status, transaction_id, artifact_path, recipient, payload, gate_report, gates_passed, produced_by, session_id); review_sessions (label, status, opened_at, closed_at, opened_by, item_count)
- **calculator_audit:** ts, function, inputs, output, caller

## 01 Inventory
- **units:** id, vin, stock_number, year, make, model, trim, vin_reconciled, grade, status, created_at
- **unit_facts:** id, unit_id, field, value, confidence, source, recorded_at
- **unit_documents:** id, unit_id, doc_type, confidence, file_path, file_hash, notes, recorded_at. doc_type: title, odometer_statement, inspection_sheet, auction_condition_report, service_record, recall_notice, buyers_guide_prior, warranty_paperwork, seller_statement, photo
- **defects:** id, unit_id, category (structural/mechanical/cosmetic/wear), severity (critical/major/minor), description, disclosed, recon_closed, source, recorded_at
- **recalls:** id, unit_id, campaign_number, component, summary, checked_at
- **syndication:** id, unit_id, channel, external_ref, status, last_confirmed_at
- **photo entry:** tag (front_3q, rear_3q, driver_side, passenger_side, interior_front, vin_plate, odometer, defect:<id>), is_generated; minimum 8
- **comps:** unit_id, source, pulled_on, year, trim, mileage, asking_price, market

## 02 Sales
- **deals:** id, name, vin, stock_number, price, state, score, source, deadline, created_at, updated_at
- **transitions:** id, deal_id, from_state, to_state, actor, notes, ts
- **contacts:** id, name, company, role, email, phone, last_contact, notes, tags, relationship, source, source_detail, created_at, updated_at
- **channel_consent:** contact_id, channel, state (GRANTED/DENIED/UNKNOWN), basis, recorded_at, recorded_by
- **consent_events (append-only):** contact_id, channel, action, state, detail, source, recorded_by, occurred_at, recorded_at
- **opt_outs:** contact_id, scope, occurred_at, source, detail, recorded_by
- **internal_dnc:** identifier, identifier_kind, contact_id, reason, added_by, added_at
- **ebr_events:** contact_id, kind, occurred_on, detail
- **contact_transactions:** contact_id, transaction_id, role, linked_at
- **outbound:** contact_id, channel, kind, campaign, subject, body, status, gate_report, approval_item_id, sent_at, sent_by
- **outbound_events:** outbound_id, status, detail, occurred_at
- **dnc registry:** registry_files (registry, area_code, published_on, downloaded_on, source_note, file_name, sha256, row_count); registry_numbers (registry, number, file_id); scrubs (label, performed_on, numbers_in, numbers_removed, freshness, detail, performed_by); training_records (person, trained_on, procedures_document); violation_reports (occurred_on, number, description, root_cause, remediation)
- **lead measurement:** contact_id, kind, source, campaign, channel, occurred_on, value, detail, recorded_by

## 03 Finance and Insurance
- **deal_economics (owner-locked):** pack, recon_budget_by_grade, floorplan_rate, floorplan_lender, front_gross_target, back_gross_target, reserve, min_down_by_tier, doc_fee, markdown_schedule, corridor_tolerance
- **covered_borrower_check:** deal_id, checked_at, checked_by, result (COVERED/NOT_COVERED/INDETERMINATE), basis
- **credit_decision:** deal_id, lender, decision, terms, stipulations[], adverse_action_sent_at
- **stipulations:** deal_id, text, requested_on, due_on, received_on, verified_by, status

## 04 Title and Admin
- **transactions (deal jacket):** id, ref, unit_ref, status, price, price_source, sale_date, funded_date, title_office, facts_source, listing_folder, terminated_reason, notes, created_at, updated_at
- **parties:** transaction_id, role, name, company, email, phone, license_number, notes
- **deadlines:** key, label, due_date, due_time, status, basis, offset_days, source, confidence, completed_date, notes
- **money lines:** kind, amount, due_date, received_date, held_by, status, internal_only, source, notes
- **documents:** doc_type, form_number, form_version, path, status, executed_date, source, notes
- **events:** kind, detail, actor, ts
- **temp_tags:** tag_id, issued_on, expires_on, deal_id, unit_ref, issued_by, filed_on, status
- **liens:** deal_id, lienholder, filed_on, method, deadline, recorded_on, confirmed, status
- **certificates:** cert_type, holder_name, issuer, cert_number, issue_date, expiry_date, file_path, status, alerted_30, alerted_15, alerted_3

## 05 Service and Recon
- **we_owes:** id, wo_number, unit_ref, description, line_items, direct_cost, markup_pct, total_cost, promise_date, status (DRAFT/APPROVED/OPEN/FULFILLED/CANCELED), fulfilled_date, notes, created_at
- **recon_items:** unit_id, defect_id, repair, assigned_to, estimate, actual, opened_on, closed_on, photo_id, we_owe_ref
- **checkins:** deal_id, due_on, done_on, reached, issues, routed_to

## 06 Marketing
- **accounts:** platform, handle, account_type, profile_url, active, note
- **profile_checks:** account_id, checked_at, checked_by, passed, evidence, findings
- **posts:** account_id, platform, status, title, caption, first_comment, hashtags, media_paths, language, promoted, approval_item_id, gate_report, gates_passed, scheduled_for, published_at, permalink, external_id, drafted_by
- **post_dimensions:** post_id, dimension (format/hook/topic/media/length/cta), level
- **post_events:** post_id, at, from_status, to_status, detail
- **raw_imports:** platform, source_file, imported_at, row_index, external_id, permalink, published_at, payload, matched_post_id, unmatched_reason
- **metrics:** post_id, as_of, source_file, reach, impressions, engagements, likes, comments, shares, saves, profile_taps, video_views, missing_fields, series_break
- **lead_events:** kind, occurred_at, detail, associated_post_id, window_hours, confidence
- **posteriors:** dimension, level, alpha, beta, trials, successes, posts_counted, updated_at
- **weekly_updates:** week_ending, dimension, level, added_successes, added_trials, posts, applied_at
- **video storyboard:** project{name, brand_style, duration_seconds, aspect_ratio, platform, approval_required, created}, scenes[]{scene_id, timecode{start,end}, source_photo, treatment, voiceover{text,file}, on_screen_text}

## 07 Reputation
- **reviews:** id, date, surface, source_ref, rating, class, issue_category, owner_role, next_action, reply_draft_ref, approved_by, posted_on, resolution_documented, status
- **review_baseline:** captured_on, surface, rating, count, unanswered

## 08 Compliance
- **programs:** category, title, authority, program_file, status, last_reviewed, score, notes
- **ad_substantiation:** first_ran_on, claim, surface, evidence, source, approved_by, status, reverify_on
- **ai_disclosure_surfaces:** surface, live, disclosure_template_id, fires_at, verified_against_statute, verified_on
- **ai_disclosure_assets:** date, asset, surface, ai_generated_types, ai_touched_only, human_review, disclosure_filed_at
- **data_processing:** deal_or_stock, doc_type, received_on, has_ssn, has_dob, has_income, storage_location, retention_expiry, destroyed_on, certificate_ref, subprocessors
- **condition_disclosure:** stock_vin, grade, defects_disclosed, disclosed_in, date, buyer_ack, title_status_disclosed, odometer_statement_on_file
- **platform_policy:** platform, rule, source, checked_on, recheck_on, status
- **gate_run:** gate, target, exit_code, skip_count, run_at, run_by
