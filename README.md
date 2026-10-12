# Virtual Office

A generic, reusable, all-in-one virtual office for Claude. It has thirteen industry departments and a shared layer. Nothing in it identifies any person or company: every specific is a `{{PLACEHOLDER}}` you fill in for your own business.

## Layout

```
CLAUDE.md          routing and rules Claude follows in this folder
PLACEHOLDERS.md    every placeholder token and what it means
_shared/           front desk, governance, cross-industry skills, templates, workflows
departments/
  01-construction                    07-ai-video-creative-production
  02-automotive-dealership           08-ai-services-software
  03-real-estate                     09-business-admin-finance-compliance
  04-education                       10-management-consulting
  05-insurance-medicare-marketing    11-ip-patent-support
  06-publishing                      12-hardware-iot-product-development
  13-roofing
_work/             analysis notes used to build the office (anonymized; safe to delete)
```

Each department has: `README.md`, `agents/`, `skills/<name>/SKILL.md`, `templates/`, `workflows/`, `knowledge/` (glossary, rules, schemas).

## How to use it

1. Open Claude Code in this folder. `CLAUDE.md` loads automatically and makes the front-desk agent route your request.
2. Or go straight to a department: read its `README.md`, then use its lead agent or a skill.
3. Fill placeholders as you go. Keep your real details in a private file outside this folder, not in these templates.
4. To start for a specific business, copy the relevant department folder and replace the tokens listed in `PLACEHOLDERS.md`.

## Principles carried through every department
- Verify, do not generate: facts, numbers and citations come from a source or are flagged.
- Gates before anything leaves the office, with logged human sign-off.
- Escalation bands: AUTO, DRAFT, BRIEF, WAIT (see `_shared/skills`).
- Generic public regulations (HIPAA, TCPA, FTC, fair housing, COPPA, and similar) appear as compliance rules. They are starting points, not legal advice: confirm with a qualified professional.

## Authored, not extracted
Most content was distilled from earlier project work. Some rule sets and example thresholds were written fresh to fill gaps (notably in `07-ai-video-creative-production`). Review those before relying on them.
