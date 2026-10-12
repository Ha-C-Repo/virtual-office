# Schemas: AI Video and Creative Production (field names only)

- **Script JSON:** project (name, client, brand_style, duration_seconds, aspect_ratio, platform, engine, approval_required, created); scenes (scene_id, timecode, visual_hook, generation_prompt, reference_image, composition_layers, voiceover_text, voiceover_file, music_note, captions).
- **Timing memory / observed durations:** node_type, samples, mean, stddev, last_updated.
- **Session resume:** project, platform_canvas_ref, drive_mode, preflight (check, status), steps (step, node_type, node_id, status, notes), edges (edge_id, source, target), next_action.
- **Run state:** wave, pending_nodes, running_nodes (node_id, started, expected_finish), completed_nodes, failures (node_id, time, error, retries, action).
- **Brand tokens:** name, version, status, sources, identity (company, positioning_line, signature_line, retired_lines), logo (rule, lockups, pairing), surfaces (video, document, website), donts (banned_strings, warn_strings, rules).
- **Creative brief:** overview, objective, audience, key_messages, production_specs, visual_direction, must_include, must_avoid, assets_provided, approach, revision_process, credit_budget (item, clips, attempts, cost_units).
- **Cost-gate record:** project, batch_scope, quoted_total, approver, approved_at, actual_total, variance.
- **Production log entry:** stage, date, human, human_input, ai_role, gate.
- **AI disclosure register (video):** date, asset, surface, ai_generated (video/voice/music/image), human_work_summary, disclosure_filed_where, copyright_status.
- **Audio rights table:** item, type, rights_holder, status, license_scope, credit_required.
- **Frame review record:** project, cut_version, reviewer, check, result, timecode, action.
- **IP screen record:** item, six_point_results, evidence, decision, signed_by, date.
- **Scheduled task:** id, label, hour, minute, days, enabled, description.
- **Environment cache:** gpu_present, vram, free_disk, tools_found, mode, detected_at.
