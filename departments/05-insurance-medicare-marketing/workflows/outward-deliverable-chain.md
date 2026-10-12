# Outward Deliverable Chain

Applies to any flyer, mailer, event invite, script, web copy, social post, email or PDF that leaves the office.

## Steps
1. Draft from a pre-approved template in `../templates/`. Copy; never edit the master.
2. Assign a document number: {TYPE}-{YYYY}-{ABBREV}-{NNN}, TYPE in REC, MKT, ONB, RPT, CMP. Revisions increment NNN.
3. Medicare compliance gate (judgment): `../skills/medicare-compliance-gate/SKILL.md`. Verdict PASS, FIX-AND-RERUN or BLOCK. A template pass at creation never pre-clears a filled copy.
4. Create the internal `-INT` memo (`../templates/internal-memo-int.md`).
5. Deterministic output validator on the outward document AND the `-INT` memo. Non-zero exit blocks export.
6. Four-pass review (below).
7. Output scrubber and voice check: `../skills/output-scrubber/SKILL.md`, `../skills/voice-check/SKILL.md`.
8. GATE: principal approval.
9. Plan-specific pieces: carrier submission and approval before use. Record the reference.
10. Export PDF. Visual QC. Deliver with a one-line delivery summary.

## Four-pass review
1. Calculation cross-check by two independent paths.
2. Compliance completeness: disclaimers, event type, SOA, recording, consent basis.
3. Internal-info leak scan against the forbidden-items table in `../skills/deliverable-compliance/SKILL.md`.
4. Visual QC of the final PDF: no overflow, orphan headings, leaked placeholders, wrong escapes, missing footer or label.

## Three gates that apply throughout
Number ownership (verified versus labeled ESTIMATED); source reading (read the actual document row by row before extracting); review before output.

## Sign-off points
Principal approval (step 8). Carrier approval (step 9, plan-specific only). Nothing leaves the office before both apply.
