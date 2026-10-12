---
name: project-indexer
description: Builds the per-project or per-release AI context layer (a 0.ai-context folder) from static documents so later queries load a small summary instead of the full set. Lists living documents, never mirrors them. Use when starting a project, release, deal, unit, title or engagement, or when documents change.
---

# Project indexer (context-layer builder)

## When to use
Start of a new project, release, deal, engagement, unit or title; when source documents change; when the user says "index the project", "build the context" or "set up the project".

## Inputs
The project folder, its static documents (contracts, specs, drawings, manuscripts, policies), and the list of living documents (registers, schedules, pipeline databases, changelogs).

## Output structure
A folder `0.ai-context/` containing:
- `CLAUDE.md`: the loader. Points to the constitution, the department rules, this project's summary, the memory file, and a mandatory LIVE DOCUMENTS section.
- `project.md` (or `release.md`): dated snapshot of facts of record, parties by role, scope, key dates, money terms by reference, open questions. Every fact has a source path.
- `index.md` (or `drawings.md`, `specs.md`): map of the static documents: what each is, where, what it governs, conflicts between them.
- `memory.md`: append-only log of learnings, decisions and corrections, one or two lines each, dated.

## Steps
1. Inventory the folder read-only. Classify each document by type and completeness. Flag gaps.
2. Read each static document fully before extracting. Do not rely on its own summary.
3. Write the snapshot with confidence tags and source paths. Mark measured vs assumed.
4. Write the document map, including which document governs when two conflict (flag conflicts, never silently choose).
5. List living documents under LIVE DOCUMENTS with path and purpose. Say: always read the source file, never a mirror.
6. Create `memory.md` empty with its header.
7. Verify: every path exists; no secrets; no real names (placeholders only); loader is under a page.
8. Log a changelog line. Re-run when static documents change; living documents are never re-indexed.

## Outputs
The four files, a verification note, a changelog line.

## Gates
- Read-only first pass; copy or write only after approval.
- Never mirror live registers into the context layer.
- Keep skeleton folders; never delete empty ones.
- Token target: the loader plus snapshot should replace loading the whole document set.

## Anti-patterns
Copying contract text into the snapshot. Summaries without paths. Letting the context layer drift from the sources.
