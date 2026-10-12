# 08 Backup and Change Discipline

Owner: studio-lead | Approver: {{OWNER}}

## Steps
1. Before any overwrite or delete, snapshot the file to a timestamped backup folder.
2. Make the smallest change that solves the problem.
3. Append an entry to the change log: date, file, reason, backup reference.
4. For files watched by sync tools, write through the safe-write script (backup, write, verify).
5. Nothing is deleted. Retire to an archive with per-batch owner approval.
6. Protected files (constitution, locked config) change only by amendment.
7. Run the release-output validator and the pre-commit hook. Non-zero exit blocks.
8. Never store credentials in the workspace; secrets live outside it.

## Outputs
Backup folder entry, change log entry.
