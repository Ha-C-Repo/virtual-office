# _shared: Cross-Industry Layer

## Purpose
This folder holds everything that is not specific to one department: the front-desk router, the coordinator, the review agents, the governance skills, the cross-industry business skills, the common templates and workflows, and the shared knowledge files. Every department in `../departments/` inherits this layer. Where a department file and a shared file disagree, the stricter rule wins and the conflict is logged in a decision log.

## Scope
- Governance: constitution, escalation bands (AUTO / DRAFT / BRIEF / WAIT), voice firewall, verify-don't-generate, human sign-off, registers, handoffs, skill promotion, context-layer building.
- Cross-industry work: marketing, lead follow-up, document drafting, customer service, reporting, scheduling and routines.
- Routing: `routing-table.md` maps request types and keywords to the 13 departments.
- No department folders live here. Department material lives under `../departments/<folder>/`.

## When to use
- Every request starts at the front desk (`agents/front-desk-router.md`), which uses `routing-table.md`.
- Any outward deliverable passes through the review chain (QA/editor, compliance reviewer, scrubber, human sign-off) described in `workflows/outward-deliverable-chain.md`.
- Any time a department has no skill for a task, look here first before building a new one.

## Agents (`agents/`)
| File | Role |
|---|---|
| `front-desk-router.md` | Classifies each request and routes it to one of the 13 departments |
| `coordinator.md` | Runs multi-department work, tracks owners, handoffs and deadlines |
| `qa-editor.md` | Quality gate: facts, arithmetic, completeness, voice, layout |
| `compliance-reviewer.md` | Applies Tier 1 rules and regulatory checks before anything goes out |
| `anonymization-scrubber.md` | Final scrub of names, identifiers, internal economics and secrets |
| `records-keeper.md` | Maintains registers, logs and changelogs, append-only |
| `research-analyst.md` | Open-question research with panel-and-judge synthesis and source tagging |

## Skills (`skills/<name>/SKILL.md`)
Governance: `constitution`, `thinking-protocol`, `escalation-bands`, `voice-firewall`, `verify-dont-generate`, `confidence-tagging`, `human-signoff-gate`, `two-document-rule`, `registers`, `handoff-writing`, `safe-write-and-backup`, `skill-promotion-pipeline`, `project-indexer`, `request-routing`, `anonymization-scrub`.
Cross-industry: `marketing-content`, `cold-outreach`, `lead-followup`, `document-drafting`, `proposal-writing`, `customer-service`, `reporting`, `scheduling-and-routines`, `scope-creep-detector`, `competitor-analysis`, `panel-and-judge`, `meeting-notes`.

## Templates (`templates/`)
Handoff, decision log, register, meeting notes, status report, SOP, cold email, follow-up email, service recovery email, proposal, internal twin memo, creative brief, approval request, escalation note, pre-mortem, weekly report, changelog, agent definition, skill definition, department README.

## Workflows (`workflows/`)
Request intake and routing, outward deliverable chain, document drafting to sign-off, lead to follow-up, customer complaint resolution, weekly review cadence, session handoff, skill promotion, incident and escalation, register maintenance, backup before overwrite, new department context layer, anonymization pass.

## Knowledge (`knowledge/`)
`glossary.md`, `governance.md`, `schemas.md` (field names only).

## Handoffs
This layer hands work to departments, never the reverse. Departments hand back to the coordinator when work touches a second department. See `routing-table.md` section "Cross-department handoffs".

## Ground rules in one paragraph
Verify, do not generate. Humans own every number that costs money and every message that leaves the office. Anything unclear is escalated up, not guessed. Every outward piece has an internal twin that carries the economics and the verification status. Nothing is deleted; superseded material is archived and the change is logged. Real names, contacts, identifiers and secrets never enter this folder; use `{{UPPER_SNAKE_CASE}}` placeholders.
