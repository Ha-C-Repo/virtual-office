---
name: mobile-build
description: Conventions for the native mobile app: layers, variants, signing discipline, dependency rule, build gates, tests.
---
# Mobile Build

## When to use
Writing or reviewing app code or build configuration.

## Architecture
Single module, monolith-first, declarative UI. Layers: `solver/` (no platform imports, no network, no model), `tutor/` (the only place model output meets the solver), `ai/` (one provider interface: transcribe and explain; debug mock; unconfigured release default fails loudly), `data/` (repository interfaces and local implementations), `meter/`, `config/` (feature flags for pending privacy decisions), `ui/` (state holder and actions; destinations Solve, History, Profile).
Hand-wired dependency graph (no DI framework). Platform SQLite in WAL mode with parameterized queries. Preferences store for profile and meter.

## Rules
1. A version catalog is the only place versions live.
2. Every new dependency needs a ledger row: what native approach was exhausted first. Deliberately absent: ORM, DI framework, serialization library, analytics and crash SDKs.
3. Debug vs release: mock provider only in debug via build flag; release minified, no debug logging, signing keys never in the repo.
4. Permissions: network and camera only. Backup of app data disabled.
5. Offline-first: launch, history, profile, delete, meter and solver work offline; photo transcription and explanation need a connection and say so.
6. Build gates in the check task: no ad/analytics/vendor-runtime artifacts (transitive included), no dash punctuation in strings, no payment markers.

## Tests
Solver contract and vector families; pipeline with stubbed model (wrong answer must not ship; retry bounded to one); metering; repository fakes; resource sweeps; instrumented tests for airplane mode, permission denial, delete-all residue.

## Gates
Dependency-tax and premature-scaling gates require written justification. Release builds are made by the release-manager only.
