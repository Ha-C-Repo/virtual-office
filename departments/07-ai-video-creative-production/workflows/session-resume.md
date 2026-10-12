# Session Resume

Use after any interruption (timeout, crash, handoff, end of day).

1. Read the session resume file and run state (`../templates/session-resume.md`, `../templates/run-state.md`).
2. Re-run environment detection.
3. Re-verify pre-flight: references, wiring, mode toggles, approved batch scope.
4. Confirm the cost-gate go still covers the remaining work. If not, quote again.
5. Identify the first incomplete step; check partial outputs before rerunning anything.
6. Continue; update the progress table after each step.
7. At end of session, write the next action into the resume file.

Gate: never rerun completed paid nodes without a reason logged.
