# Schemas (field names only)

## Customer config
legal_name, trade_name, primary_contact, title, email, phone, website, industry, classification_code, size, revenue, location, discovery_source, first_contact_date, pain_trigger, decision_maker, decision_process, budget_authority, stage, tier, mrr, trial_start, trial_end, next_step, modules_enabled, vertical_overrides, branding, integrations, custom_workflows, agreement_type, signed_date, auto_renewal, notice_period, billing_period, conversation_log[date, channel, summary, next_step], risks, open_questions

## AI call telemetry
timestamp, model, input_tokens, output_tokens, cached_tokens, cost, feature, tenant_id, department, latency

## Health score
signal_category, weight, value, delta, trigger_flags, band

## Cancellation reasons
code (C1..Cn), description, save_likelihood, offer

## Geofence domain (all org-scoped)
geofence, gps_ping, geofence_alert, time_entry, alert_recipient

## Async job
job_id, tenant_id, state (enqueued, running, done, failed), created_at, result_ref

## Contact submissions
id, name, email, phone, message, created_at

## Log line
level, message, tenant_id

## Ubiquitous-language ledger
term, code_symbols, definition_scope, constitution_constraint

## API catalog groups
authentication, organizations, users/team, customers, jobs/work orders, proposals, AI proposal builder, invoices, payments, products/catalog

## Auth model
auth_methods, session_model, org_model, rbac, tier_gating, password_reset, email_verification, calendar_oauth, customer_portal_auth

## Spec index
feature, status, depends_on, open_unknowns, last_updated
