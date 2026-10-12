---
name: safe-write-and-backup
description: Back up before any overwrite, append a changelog line, never delete, and write protected or sync-watched files atomically. Use before editing any governance file, register, FINAL or DELIVERED document.
---

# Safe write and backup

## When to use
Before overwriting or retiring any file that is protected (constitution, rules, registers), final or delivered, or watched by a sync tool.

## Steps
1. Snapshot the file to `_handoff/backups/<UTC timestamp>/` keeping its relative path.
2. Write the new content to a temporary file in the same folder. Write in binary mode so line endings are preserved.
3. Let the sync tool settle, then re-read the temporary file and verify byte count and content.
4. Replace the original atomically.
5. Re-verify the replaced file.
6. Append one line to the changelog: UTC timestamp, change, approver, backup path.
7. Never delete. Retire files to an `archive/` folder with per-batch approval and a log line.
8. Corrections to a register append; they do not overwrite.

## Inputs
File path, new content, approver role.

## Outputs
Backup path, verification result, changelog line.

## Gates
- No overwrite of a FINAL or DELIVERED file without a backup.
- Protected files require the amendment protocol in `../constitution/SKILL.md`.
- A failed verification restores from the backup and reports.

## Anti-patterns
Editing a sync-watched file in place. Overwriting then "remembering" what it said. A changelog entry written before the write succeeded.
