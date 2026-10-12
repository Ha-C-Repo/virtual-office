# Schemas (field names only)

## Design lock
lock_number, title, date, owner_role, status, areas_affected, question, constraints, options[name, pros, cons, cost, risk], decision, reasons, consequences, revisit_triggers, supersedes, ip_copy_sent

## Launch phase record
phase, date, criteria[criterion, measure, target, actual, evidence, met], reviews_done, gaps, approver_role, approved_date

## Product area status
area, week, owner_role, state, done, next, blockers, interface_changes[interface, change, areas_affected, lock_needed], risks, decisions_needed

## Risk register
risk_id, area, description, likelihood, impact, mitigation, owner_role, status

## Investor log
date, recipient_role, nda_date, materials, questions, follow_up_due, approved_by

## Product folder layout
architecture (adr, diagrams, specs); business (investor, market, model, partnerships); ip (assignment, counsel, patent, trademark); ops (confidentiality, domain); product (cloud, firmware, hardware, mobile, website); templates; skills; admin

## BOM line
line, item, part_ref, supplier_role, qty_per_unit, price_tiers, lead_time_weeks, moq, quote_date, quote_expiry, single_source, status

## Supplier scorecard
supplier_role, scope, criterion, weight, score, evidence, gap, recommendation

## Test record
test_id, requirement_id, method, sample_size, pass_criterion, result, date, hw_rev, fw_version, unit_ids, finding_id

## Pilot plan
questions, participants, duration, sites, success_criteria, stop_criteria, data_handling, support_plan, exit_plan, approvals

## OTA release
version, hash, test_ids, stage_plan, stop_criteria, stage_log, approver, issues
