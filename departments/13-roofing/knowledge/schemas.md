# Schemas (field names only)

## Lead
lead_id, created_at, source, source_detail, channel, contact_name, phone, email, property_address, property_type, service_type (repair / re-roof / storm / commercial / maintenance), storm_event_id, urgency, first_response_at, minutes_to_first_response, first_response_by, appointment_at, status, lost_reason, consent_basis, consent_recorded_at, opt_out, owner, notes

## Storm response lead log
event_id, event_date, area, lead_id, triage_class (active leak / tarp / inspection / info), assigned_to, scheduled_at, tarp_authorized, outcome

## Inspection
inspection_id, lead_id, property_address, inspected_at, inspector, access_method (roof / ladder / drone / ground), weather, roof_type, pitch, layers, decking_condition, soft_spots_count, test_square_results (slope, hits), hail_indicators, wind_indicators, flashing_condition, ventilation_notes, penetrations, safety_concerns, photo_count, recommendation, signed_off_by

## Photo log entry
photo_id, inspection_id, file_name, timestamp, geotag, slope_or_area, label, caption, original_preserved, reviewed_by

## Measurement
measurement_id, property_address, source (aerial / manual / both), report_date, footprint_sf, roof_area_sf, squares, pitch_by_plane, eave_lf, rake_lf, ridge_lf, hip_lf, valley_lf, wall_flashing_lf, penetration_count, complexity_class, verified_on_site (y/n), variance_pct, verified_by

## Estimate
estimate_id, lead_id, measurement_id, tier (good / better / best), product_line, color, ordering_squares, waste_pct, bundles_per_square, line_items (code, description, qty, unit, unit_cost_ref), labor_squares, tearoff_layers, permit_fee_ref, disposal_ref, price, local_markup_ref, margin_pct, valid_through, issued_at, sent_by, approved_by

## Contract
contract_id, estimate_id, signed_at, customer_signers, license_number, scope_ref, exclusions, price, deposit_ref, payment_schedule, permit_responsibility, warranty_refs, rescission_notice_given_at, rescission_expires_at, insurance_clause_present, change_order_clause_present

## Change order
change_order_id, contract_id, requested_by, reason, scope_delta, price_delta, schedule_delta, customer_signed_at, internal_approved_by

## Claim
claim_id, contract_id, carrier, claim_number, policy_type, date_of_loss, cause_of_loss, adjuster_name, adjuster_contact, adjuster_visit_at, deductible, rcv, depreciation_amount, depreciation_pct, acv, recoverable_flag, payments (stage, amount, received_at, check_payees, mortgagee_endorsement_status), supplements (number, submitted_at, items, amount, status), deadlines (work_completion, recoverable_depreciation_claim, proof_of_loss), appraisal_status, public_adjuster_involved

## Permit
permit_id, project_id, authority, application_at, issued_at, permit_number_ref, inspections (type, requested_at, scheduled_at, result, photo_refs), final_passed_at

## Project
project_id, contract_id, address, type (residential / commercial), system, status, kickoff_at, material_order_id, crew_id, scheduled_start, actual_start, dryin_at, completed_at, weather_delays, punch_open_count, final_invoice_at, paid_in_full_at, lien_waiver_status

## Crew
crew_id, type (employee / subcontractor), lead_name, size, trades, certifications, safety_training_dates, coi_expires_at, license_ref, pay_basis (piece / day), rate_ref, holdback_pct, quality_score, rating_notes

## Subcontractor payment milestone
sub_id, project_id, milestone (dryin / final / punch_closed), amount_ref, holdback_ref, evidence_refs, approved_by, paid_at

## Material order
order_id, project_id, supplier, takeoff_ref, line_items (sku_ref, description, qty, unit), delivery_window, delivery_confirmed_at, roof_load_plan, dumpster_ref, color_confirmed_by_customer_at, substitutions_approved_by, returns, status

## Safety record
record_id, project_id, date, toolbox_topic, attendees, fall_plan_ref, harness_inspections, ladder_inspection, hazards_found, incident_ref, signed_by

## Incident
incident_id, occurred_at, location, person_type, description, injury_class, first_aid_or_care, root_cause, corrective_action, reportable (y/n), reported_at, reviewed_by

## Warranty
warranty_id, project_id, type (workmanship / manufacturer / extended / system), term_ref, product_registration_due, registered_at, registration_ref, certified_installer_required, exclusions_noted, certificate_issued_at, inspections_log, repairs_log

## Service ticket
ticket_id, warranty_id, reported_at, caller, symptom, urgency, triage_class (emergency / urgent / routine), tarp_authorized, visit_at, findings, cause (workmanship / material / other / storm / maintenance), covered (y/n/undetermined), resolution, closed_at

## Commercial bid
bid_id, owner_ref, building_ref, bid_due_at, prewalk_at, requirements (experience_years, certifications, substitution_controls, warranty_term), system_selected, moisture_survey_ref, alternates, exclusions, submitted_at, result

## Maintenance program
program_id, building_ref, agreement_term, visits (season, date, inspector), findings (location, deficiency, photo_ref, severity), owner_authorizations, repairs_done, emergency_response_terms

## Job cost
project_id, week_ending, revenue_recognized, costs (labor, labor_taxes, materials, subcontractors, disposal, permits, commissions, transportation, warranty_reserve, workers_comp, other), billable_hours, overhead_rate_ref, gross_margin_pct, variance_to_estimate, leakage_flags

## KPI (weekly)
week_ending, leads, median_minutes_to_first_response, appointments, estimates_sent, median_days_to_estimate, closes, close_rate, avg_ticket_ref, backlog_squares, jobs_started, jobs_completed, callbacks, open_punch, receivables_over_30, safety_incidents

## Outbound / consent
contact_id, channel, basis, recorded_at, scrub_date, opt_out_scope, message_kind, approved_by, sent_at
