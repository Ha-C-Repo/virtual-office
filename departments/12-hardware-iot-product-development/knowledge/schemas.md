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
