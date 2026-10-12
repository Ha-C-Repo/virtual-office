---
name: hosted-layer-design-spec
description: Design spec for a hosted, license-keyed layer that serves the virtual office to clients who plug in their own AI, so clients never receive the folders and the licensor carries no client token cost. Spec only; nothing is built.
status: draft-spec
date: 2026-10-12
related: [README.md, LICENSE, CLAUDE.md]
---
# Hosted Layer Design Spec

## 1. Summary
Serve the virtual office as a hosted service. The client connects their own AI assistant to it. The service returns only the department material needed for each request. The client's AI runs on the client's account, so the licensor pays no client token cost. This is a design for review. No code exists.

## 2. Why
| Problem with shipping folders | Hosted layer answer |
|---|---|
| Markdown is copyable once delivered | Content stays on the server; clients get small pieces per request |
| Updates need re-delivery | One live version; clients always get current content |
| No usage signal | Per-tenant, per-department usage records |
| Clients fill placeholders in files that then drift | Tenant profile stored per client; placeholders resolved at request time |
| Calculators run only if the client has Python | Harnesses run server-side and return results |

Honest limit: anything the service returns to a client's AI can be copied by that client one request at a time. The design reduces bulk copying and adds contractual and technical friction. It does not make the content uncopyable.

## 3. Non-goals
- Not hosting the client's AI model or paying for its tokens.
- Not a replacement for professional advice (see `LICENSE` Section 5).
- No client data used to train any model.
- No code in this repo until this spec is approved.

## 4. Architecture
```
Client AI assistant
   | (MCP or equivalent connector, license key)
   v
Gateway: auth, rate limit, tenant lookup, usage log
   |-- Router tool: front-desk routing (routing-table)
   |-- Content tools: get_department, get_skill, get_template, get_workflow
   |-- Harness tools: run_calculation (server-side, allowlisted scripts)
   |-- Tenant profile store: placeholder values per tenant
   `-- Gate log: sign-offs recorded per tenant
Content store (this repo, built into a read-only bundle per release)
```

## 5. Interfaces (proposed tools)
| Tool | Input | Returns | Notes |
|---|---|---|---|
| `route_request` | free text | department id, lead agent, suggested skills | Uses `_shared/routing-table.md` rules; fail closed |
| `get_department` | department id | README and agent list | Metadata only |
| `get_item` | kind (agent/skill/template/workflow/knowledge), department, name | the file text with tenant placeholders filled | Rate limited; watermarked per tenant |
| `run_calculation` | harness name, args | JSON result | Allowlist of the `harnesses/*.py` tools; no arbitrary code |
| `set_profile_value` | placeholder token, value | ok | Stored per tenant; never returned to other tenants |
| `log_gate` | gate id, approver role, decision | ok | Human sign-off record |

## 6. Tenancy and data
| Item | Rule |
|---|---|
| Isolation | Every record keyed by tenant id; no cross-tenant query path |
| Client data | Only placeholder values and gate logs; no client documents stored by default |
| Secrets | Never stored in the profile; tokens that look like credentials are rejected |
| Retention | Gate logs and usage kept per contract; deletion on termination |
| Content versioning | Each release is an immutable bundle with a version id; requests record the version served |

## 7. Licensing and metering
- License key per client with limits: departments included, seats, request budget.
- Meter by request count and departments touched; no token metering because the client pays their own AI.
- Watermark: item text carries a per-tenant marker so leaks can be traced. Disclose this in the contract.
- Keys are revocable; expiry returns a clear message.

## 8. Security
| Risk | Control |
|---|---|
| Prompt injection via tool output | Content is first-party and read-only; the service never relays third-party text |
| Bulk scraping | Per-key rate limits, request-pattern alerts, watermarks |
| Harness abuse | Allowlisted scripts, fixed argument schemas, size and time limits, no file system or network access |
| Key theft | Short-lived tokens, rotation, revocation |
| Tenant leakage | Row-level tenant filter on every query; tests for cross-tenant reads |
| Supply chain | Pin dependencies; harnesses are stdlib-only today |

## 9. Compatibility
Target one open connector standard first (the Model Context Protocol), then adapters for other assistants. A thin adapter per platform maps its tool format to the same gateway. Confirm each platform's current connector support before committing (VERIFY).

## 10. Build plan (if approved)
| Phase | Deliverable | Exit test |
|---|---|---|
| 0 | Release bundler: repo to read-only versioned bundle, placeholder map | Bundle hash reproducible |
| 1 | Gateway + `route_request` + `get_item` for 2 departments | Pilot client completes 5 real tasks with their own AI |
| 2 | Tenant profile + harness tools | Cross-tenant test suite passes |
| 3 | Licensing, metering, watermark, admin console | Key revocation works within one minute |
| 4 | Remaining departments, other connectors | Per-platform smoke tests |

## 11. Open questions for the owner
1. Price model: per department, per seat, or flat; what does "less than one employee's monthly salary" mean in numbers?
2. Which assistant platform is first?
3. Is a client allowed to export their filled-in templates? (Proposed: yes, outputs are theirs.)
4. Who is the licensor entity named in `LICENSE`?
5. Is watermarking acceptable to the first clients?
6. Hosting location and data-residency promises, if any.
