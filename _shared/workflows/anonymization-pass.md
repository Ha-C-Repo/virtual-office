# Workflow: Anonymization Pass

Skill: `../skills/anonymization-scrub/SKILL.md`. Agent: `../agents/anonymization-scrubber.md`.

| # | Step | Gate |
|---|---|---|
| 1 | List the target files. Work on copies of source material; never edit the original in place. | |
| 2 | Pattern scan: at-signs, domains, URLs, phone-length and ID-length digit groups, currency symbols, long random strings. | |
| 3 | Manual read for capitalized multi-word names, brand names, place names, product names. | |
| 4 | Replace each hit with a consistent `{{UPPER_SNAKE_CASE}}` token or a role phrase. Software and AI vendors become categories. | |
| 5 | Secrets: do not copy. Report location only. BLOCK until a human handles them. | Secret found = BLOCK |
| 6 | Re-scan every file after edits. | Zero hits required |
| 7 | Check filenames and headings too. | |
| 8 | Log the pass (counts by type, no original values). | `changelog.md` |
| 9 | Spot-check meaning: the text must still be usable. | QA editor |

Allowed to remain: names of generic public regulations and standards. Everything else is a placeholder.
