# Workflow: Sandbox Software Factory

Background workers that draft code in isolation.

1. Define one microscopic task with acceptance criteria and a stop condition.
2. Run in a sandbox with **synthetic tenant data only**. Never production data or credentials.
3. Worker produces a diff and a short record; it does not merge or deploy.
4. Supervised only: never unattended overnight.
5. `engineering-reviewer` reviews cold.
6. **Gate (sign-off):** technical owner decides whether the diff enters the normal lifecycle.
7. Scratch experiments stay in a marked scratch area and are cleaned up at handoff.
