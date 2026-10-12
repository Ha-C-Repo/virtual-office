# Generative Platform Run (browser-driven)

Precondition: cost-gate go on file for this batch.

1. Open or create the session resume file (`../templates/session-resume.md`). If one exists, resume from it.
2. Pre-flight: references uploaded, prompts match the script version, plan or mode known.
3. Build the graph: reference image nodes, clip nodes wired to prompt and first-frame inputs.
4. **Verify the unlimited or credit mode toggle on every node.** Record it.
5. Run wave 1 in the stated order. Never "run all" on a cached canvas.
6. Wait per timing memory (`../skills/timing-memory-and-persistence/SKILL.md`); update `../templates/run-state.md`.
7. Review outputs as they land. Failed or artifact-heavy clips are rerun only inside the approved batch.
8. Stitch, add text-to-speech and audio nodes if used, download.
9. Update build-progress table and edge ledger; log actual versus quoted cost.
10. Hand clips to assembly (`local-render-hybrid.md`).

Failure handling: retry once; on second failure trip the circuit breaker and ask a human. Never exceed the batch. Never handle credentials.
