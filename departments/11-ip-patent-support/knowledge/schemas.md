# Schemas (field names only)

## Invention disclosure
disclosure_id, title, inventor_roles, assignment_signed, product_area, problem, solution, differences, features, alternatives, conception_date, conception_evidence, first_written_date, first_public_disclosure, planned_disclosures

## Prior-art item
identifier, title, date, status, features_touched, discloses, difference, closeness

## IP register
asset_id, type (patent application, patent, mark, domain-neutral asset), title_or_mark, status, owner_entity, counsel_ref, filing_date, next_deadline, deadline_type

## Trademark worksheet
candidate, type, goods_services, classes, basis, first_use_date, search_log, risk_notes, counsel_opinion_date, serial_number

## Disclosure log
date, recipient_role, nda_date, documents, detail_level, approved_by

## Counsel briefing
topic, decision_requested, facts, attachments, timeline, questions, deadlines, budget_note

## IP register (additional fields)
source_doc, recorded_on, verified (yes/no), review_date

## Third-party license inventory
component, version, source_url, license_id, license_file_path, category, where_used, distribution, notice_required, flag_for_counsel, checked_on, checked_by

## Trade secret register
item_id, description_only, location, access_roles, protection_measures, agreements_on_file, last_reviewed, owner_role

## Assignment gap check
contributor_role, contribution, agreement_type, signed_date, first_contribution_date, covers_prior_work, file_location, gap, next_step

## Deadline entry
asset_id, deadline_type, date, source_doc, recorded_on, warning_stage, acknowledged_by_counsel, outcome
