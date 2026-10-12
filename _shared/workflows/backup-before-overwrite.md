# Workflow: Backup Before Overwrite

Skill: `../skills/safe-write-and-backup/SKILL.md`. Template: `../templates/changelog.md`.

| # | Step | Gate |
|---|---|---|
| 1 | Identify the file and why it changes. Protected files need the amendment protocol first. | Approval for protected files |
| 2 | Snapshot to `_handoff/backups/<UTC timestamp>/`, keeping the relative path. | Snapshot exists and opens |
| 3 | Write new content to a temporary file in the same folder, binary mode. | |
| 4 | Wait for sync tools to settle; re-read the temporary file; check bytes and content. | Mismatch: stop |
| 5 | Replace atomically. Re-read the final file. | Failed verification: restore from backup |
| 6 | Append one changelog line: UTC timestamp, change, approver role, backup path. | |
| 7 | If the file is retired instead of changed, move it to `archive/` with approval. Never delete. | Per-batch approval |

Never overwrite a FINAL or DELIVERED file without a backup. Never write a changelog line before the write has been verified.
