# Workflow: Skill Promotion

Skill: `../skills/skill-promotion-pipeline/SKILL.md`. Templates: `../templates/skill-definition.md`, `../templates/pre-mortem.md`.

| # | Step | Who | Gate / sign-off |
|---|---|---|---|
| 1 | Log each occurrence of the repeated task. | Any agent | |
| 2 | At three occurrences, extract a template. | Author agent | Templates load on demand |
| 3 | Pre-mortem for the proposed skill. | Coordinator | `pre-mortem.md` |
| 4 | Draft `SKILL.md` from `skill-definition.md`. | Author agent | Has at least one gate that can fail |
| 5 | Test on two real past cases and one bad case. | QA editor | Must fail the bad case correctly |
| 6 | Compliance review of gates and claims. | Compliance reviewer | |
| 7 | HUMAN SIGN-OFF to add the skill. | Owner role | Governance changes use the amendment protocol |
| 8 | Add to the department README, routing table if it needs a trigger. | Records keeper | |
| 9 | Skills audit: referenced paths exist; "blocked" phrases are blocked somewhere; no unstated overlap. | QA editor | |
| 10 | Changelog line. Archive any skill it replaces. | Records keeper | Never delete |
