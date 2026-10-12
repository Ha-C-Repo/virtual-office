# Workflow: New Project or Department Context Layer

Skill: `../skills/project-indexer/SKILL.md`. Template: `../templates/department-readme.md`.

| # | Step | Who | Gate |
|---|---|---|---|
| 1 | Create the folder skeleton (numbered folders as the department defines). Skeleton folders are never deleted, even if empty. | Records keeper | |
| 2 | Read-only inventory of source documents; classify and flag gaps. | Indexer | Read-only first pass |
| 3 | Read each static document fully. | Indexer | |
| 4 | Write `0.ai-context/` files: `CLAUDE.md` loader, `project.md` snapshot, document map, `memory.md`. | Indexer | Facts have source paths and confidence tags |
| 5 | List living documents under LIVE DOCUMENTS; never mirror them. | Indexer | |
| 6 | Anonymization pass on the context files. | Scrubber | `anonymization-pass.md` |
| 7 | Verify: paths exist; no secrets; loader is short; conflicts flagged, not resolved silently. | QA editor | |
| 8 | Owner reviews the snapshot. | Owner role | Sign-off |
| 9 | Changelog line. Schedule re-index when static documents change. | Records keeper | |
