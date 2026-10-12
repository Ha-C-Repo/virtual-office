# Schemas (field names only)

## Learner profile
subject, grade_band (unset / early / middle / advanced)

## Problem request
text, intake (typed / photo), transcription_confirmed, transcription_edited

## Transcription
text, confidence

## Explanation request
problem_text, subject, grade_band_hint, solver_constraint

## Explanation draft
steps[], final_answer, practice_variant, explain_back_prompt, model_flagged_uncertain

## Tutor result
outcome, steps[], answer, verdict, confidence, practice_variant, explain_back_prompt, message, model_calls, counts_against_meter

## Verdict
status, detail, inputs, roots[], audited, unaudited

## Audit record
timestamp, entry_point, inputs, status, detail, implementation

## Solver status
engine, engine_available, audit_destination, verified_domain[], policy

## History table
id, problem_text, intake, steps, answer, verdict_status, verdict_detail, confidence, practice_variant, explain_back, created_at (index on created_at descending)

## Meter
state: period_start_epoch_day, count
config: limit (disabled sentinel), period_days

## Feature flags
crop_first_photo_intake, send_coarse_grade_band

## Solver test vectors
id, kind (numeric / equation / simplification), expression_or_equation, variable, proposed, expect, expect_overrides, divergence_reason

## Local analytics events (counts only, no content)
problem_submitted, transcription_confirmed, transcription_edited, verdict_recorded, confidence_tagged, practice_variant_opened, explain_back_submitted, history_opened, history_item_deleted, history_cleared, meter_incremented, meter_limit_reached, provider_error

## Business config (all unset until the owner decides)
tier_names, monthly_price, annual_price, free_tier_limit, trial_length, ai_cost_ceiling_per_user, effective_date, approval_line

## Constitution clause index
clause_id (NC-n.m), source, check_type (auto / manual)

## Assessment bank (training portal pattern, structure only)
base schema, tamper gate, answer key, module tables
