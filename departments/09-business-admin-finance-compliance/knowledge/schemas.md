# Schemas (field names only)

## Production registers
- chemistry (readings): sample_date, unit_id, chamber, parameter_1 ... parameter_n, temp, ph, tech_id, confidence
- creation sessions: session_date, session_id, unit_id, source_asset_id, type_name, variant_name, count, asset_tags, medium_type, target_grid, hold_until, tech_id
- husbandry: timestamp, unit_id, grid_address, entry_type, observation, tech_id, notes
- incidents: incident_date, incident_id, unit_id, type, severity, symptoms, protocol_applied, assets_affected, outcome, logged_by
- intake: intake_date, asset_id, type_name, variant_name, source_ref, trade_doc_ref, tier, treatment_1, treatment_2, treatment_3, qt_system, qt_days_required, qt_release_date, released_on, inspector_id
- opex: month, unit_id, utilities, consumables, chemicals_media, substrates, lab_testing, total, cap_min, cap_max, within_cap
- sales: event_date, asset_tag, event_type, grid_address, list_price, sale_price, lifecycle_day, buyer_ref, order_id, notes
- yield: audit_week, unit_id, active_count, gross_sales_7d, opex_spent, net_yield, count_status, pct_of_target, escalation_flag

## Finance and billing
- Project: name, client, contact, contract_sum, signed_date, milestones_paid, material_arrived, sov_pct_complete, notes
- Invoice: invoice_number, project_name, client, date, due_date, milestone, amount, status, sent_date, paid_date, reminder_count
- PurchaseOrder: po_number, project_name, vendor, date, line_items[description, quantity, unit, unit_price, total], subtotal, status
- Reserve sweep: week, gross, percent, amount, balance_after, cap_reached, status, approved_by

## Compliance
- Permit register: authority, permit, number, cost, term, issued, expires, status
- Trade documentation log: date, direction, asset_ids, type, origin, destination, permit_number, sanitary_certificate_number, customs_ref, status
- Certification register: level, role, scope, pay_tier
- Staff matrix: staff_id, level, sop_signoffs, ppe_issued, boot_camp_complete
- SOP index: doc_number, title, effective_date, file_present
- Prequalification program: id, title, questionnaire_file, written_program_file, alt_written_file, standard_questions[]
- Prequalification status: platform, status, outstanding_items[]

## Folder schema
Per unit: _unit_context/{unit, readings, grid, lineage, memory}; logs/{sessions, incidents, watch}; photos.
Top level: units, register, commercial/{listings, orders, wholesale, policy}, finance/{capital, opex, reserve, yield}, compliance/{trade-docs, permits, sops, training}, investor/{grants, packages, reporting}, skills, workflows, _handoff/{backups, changelog}.
