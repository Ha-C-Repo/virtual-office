# 06 Publishing

## Purpose
An AI-assisted small publisher run as one virtual office for {{IMPRINT}}. Two product lines live here:

1. **Children's books** (board books, picture books, early readers, chapter books), digital-first. Print is dormant but fully specified.
2. **Client life stories** (autobiography or memoir as a paid service): data intake, voice profiling, interviews, drafting, legal clearance.

Animated and commercial video is handled by `07-ai-video-creative-production`. This department hands off to it for series episodes, read-along video and promo shorts.

## Operating philosophy
AI generates and drafts. Humans write, review, decide and sign off. Every step is numbered, blocking gates need a logged human PASS, thresholds are measured and never asserted, and every published asset gets a production-log entry and an AI-disclosure register row.

## When to use
- Starting, editing, illustrating, formatting or publishing a children's title.
- Taking on, running or delivering a client life-story project.
- Deciding what to disclose to a retail platform or copyright office about AI involvement.
- Auditing a draft for readability, meter, voice fidelity or factual support.

## Contents
**Agents** (`agents/`)
- `publishing-director.md` (lead)
- `book-editor.md`
- `art-director.md`
- `production-manager.md`
- `memoir-archivist-editor.md`
- `rights-compliance-manager.md`

**Skills** (`skills/<name>/SKILL.md`): manuscript-drafting, readability-gate, rhyme-meter-gate, character-bible, illustration-prompts, layout-and-print-spec, quality-bar, retail-disclosure-gate, copyright-filing, read-along, memoir-intake-and-scope, memoir-consent-pack, memoir-ingest-and-privacy, memoir-voice-profile, memoir-interview-protocol, memoir-drafting-and-assertion-audit, memoir-anti-slop, persons-and-clearance.

**Templates** (`templates/`): concept-record, spread-map, board-book-skeleton, picture-book-skeleton, early-reader-and-chapter-book-skeleton, character-bible, location-bible, readability-report, ai-disclosure-record, production-log, back-matter, permissions-log, persons-clearance-register, memoir-chapter-brief, memoir-deliverable-agreement.

**Workflows** (`workflows/`): book-pipeline, character-consistency, memoir-pipeline, memoir-drafting-loop, release-and-disclosure, policy-recheck-cycle, session-handoff.

**Knowledge** (`knowledge/`): glossary, rules, schemas.

## Hard rules (repeat in every sub-folder instruction)
1. Verify, do not generate: readability measured, meter scanned by a human, voice fidelity measured, every factual claim diffed to source.
2. A threshold is measured or it is not a threshold. Never move a number because a draft failed it.
3. Back up before overwrite. Never delete; move to archive. Append a changelog line.
4. Nothing leaves the office (upload, filing, client delivery) without human sign-off logged in the production log.
5. Never fabricate policy claims, publication status or sales figures. Say when uncertain.
6. No detail in a life story originates with the system.
7. No filler language, no em-dashes in business output.

## Handoffs
- To `07-ai-video-creative-production`: episode adaptations, read-along video, promo shorts, book trailers.
- To `11-ip-patent-support`: trademark clearance for imprint or series names, copyright counsel questions.
- To `09-business-admin-finance-compliance`: contracts, retention schedules, vendor registers, tax.
- From `08-ai-services-software`: tooling for stylometry scripts and the egress gate.
