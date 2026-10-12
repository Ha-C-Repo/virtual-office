# Workflow: Build Phase Gate (EVT to DVT to PVT)

1. Confirm the hardware revision under test matches the current design lock. Mismatch: stop and reconcile.
2. Compile the test matrix (`../templates/test-plan.md`). List requirements with no test.
3. Summarize pass rate and open findings by severity.
4. List changes made since the last phase and which tests they re-open.
5. Review supply status: BOM costs, lead times, single-source parts (`supply-chain-manager`).
6. Review IP status: new inventions, third-party licenses, pre-disclosure check (`11-ip-patent-support`).
7. **Gate (sign-off):** principal approves moving to the next phase, with the open-findings list attached. No open safety finding passes.
8. Record the decision as a design lock if it freezes the design.
