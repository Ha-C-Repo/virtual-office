# Routing Table

Used by `agents/front-desk-router.md` and `skills/request-routing/SKILL.md`. A request lands in a department before a skill. A row that cannot be parsed or matched is skipped, never guessed (fail closed). When two departments match, name both, pick a lead, and log the handoff.

## 1. Department index

| # | Department folder | Lead agent file (convention) | One-line scope |
|---|---|---|---|
| 01 | `departments/01-construction/` | `agents/` lead estimator or project manager | Estimating, bidding, takeoff, fabrication QC, project controls, change orders, site diary, safety prequalification |
| 02 | `departments/02-automotive-dealership/` | `agents/` dealership manager | Used-vehicle records, grading, pricing, listings, deals, title and tag, recon, reputation, dealer ad law |
| 03 | `departments/03-real-estate/` | `agents/` principal broker | Listings, CMA, tours, transaction timelines, open houses, lead retention, fair housing |
| 04 | `departments/04-education/` | `agents/` product lead | Homework help and tutoring product, answer verification, children's privacy, store releases |
| 05 | `departments/05-insurance-medicare-marketing/` | `agents/` branch principal | Medicare-touching marketing, agent onboarding, AEP readiness, commission reconciliation, consent and SOA |
| 06 | `departments/06-publishing/` | `agents/` managing editor | Children's books, kids video, life-story (memoir) projects, disclosure and rights registers |
| 07 | `departments/07-ai-video-creative-production/` | `agents/` creative director | Commercial and brand video, scripts, storyboards, prompts, cost gate, anti-AI-look rules |
| 08 | `departments/08-ai-services-software/` | `agents/` product and engineering lead | SaaS product, specs, engineering records, security, sales and customer success for software, support |
| 09 | `departments/09-business-admin-finance-compliance/` | `agents/` operations lead | Inventory and registers, yield and finance, permits and compliance logs, investor reporting, staffing |
| 10 | `departments/10-management-consulting/` | `agents/` engagement lead | Diagnose, decide, design, deploy; memos, plans, pricing and org design for owner-operated businesses |
| 11 | `departments/11-ip-patent-support/` | `agents/` IP coordinator | Patent strategy support, prior art, trademark clearance, IP protection, counsel communications |
| 12 | `departments/12-hardware-iot-product-development/` | `agents/` product architect | Hardware, firmware, cloud, mobile for connected products; design locks; launch phases |
| 13 | `departments/13-roofing/` | `agents/` roofing operations director | Roof inspection, measurement and takeoff, estimates, insurance and storm claims, permits, production, safety, warranty, commercial bids and maintenance, roofing marketing and job costing |

Each department README lists its actual agent file names. The lead is the first agent named there.

## 2. Keyword and request-type map

Match on intent first, then keywords. Quoted phrases are triggers; they are examples, not an exhaustive list.

### 01 Construction
Request types: bid, tender, takeoff, estimate, proposal for a build or trade scope, RFI, change order, pay application, schedule of values, shop traveler, nonconformance, site diary, contractor safety questionnaire, experience-mod letter, prequalification package.
Keywords: "bid this", "takeoff", "drawing set", "GC", "general contractor", "tonnage", "steel", "fabrication", "erection", "SOV", "lien", "RFI", "NCR", "MTR", "scope creep" on a project, "insurance certificate", "prequal".

### 02 Automotive dealership
Request types: vehicle listing, VIN, condition grade, appraisal, price corridor, buyer's guide, deal structure, payment scenario, adverse action, title and temp tag, we-owe, review reply for a dealership, dealer ad compliance.
Keywords: "VIN", "stock number", "recon", "front-line", "floorplan", "deal jacket", "desking", "F&I", "doc fee", "odometer", "as-is", "covered borrower", "aged inventory".

### 03 Real estate
Request types: listing presentation, CMA, net sheet, tour, staging, contract-to-close timeline, amendment, repair request, open house kit, annual equity letter, buyer consult.
Keywords: "listing", "comps", "GLA", "option period", "closing date", "MLS", "open house", "fair housing", "net sheet", "sphere", "past clients".

### 04 Education
Request types: tutoring flow, homework solver, answer verification, tutor-content QA, children's privacy review, store listing, release notes, pricing sanity for an app, competitor teardown of a learning app.
Keywords: "homework", "tutor", "grade band", "solver", "explain it back", "practice variant", "under 13", "age gate", "store listing", "release train".

### 05 Insurance and Medicare marketing
Request types: Medicare marketing piece, event invite, agent recruiting, agent onboarding, AEP readiness, commission statement reconciliation, SOA or consent register entry, election-period question, call audit, plan comparison worksheet, retention season outreach.
Keywords: "Medicare", "AEP", "OEP", "SOA", "scope of appointment", "TPMO", "carrier", "appointment" (carrier sense), "comp grid", "commission statement", "NPN", "E&O", "plan-change letter", "Part D", "Medigap", "final expense".

### 06 Publishing
Request types: children's book (any age band), manuscript, readability gate, character bible, illustration prompts, kids video episode, AI disclosure questionnaire, copyright filing support, memoir or life-story project, permissions log.
Keywords: "picture book", "board book", "spread", "age band", "read-aloud", "model sheet", "imprint", "BISAC", "bleed and trim", "memoir", "interview", "passage ledger".

### 07 AI video and creative production
Request types: commercial, pre-roll, brand film, explainer, product demo, vertical reel, short film, storyboard, shot list, generation prompts, cost estimate for generation, creative brief, session resume.
Keywords: "video", "script", "storyboard", "B-roll", "clip", "reel", "pre-roll", "brand film", "voiceover", "shot list", "style token", "anti-AI look". If the video is for a book series, lead with 06 and borrow 07 for rendering.

### 08 AI services and software
Request types: product spec, roadmap, pricing model, ICP, discovery or demo script, battle card, customer config, health score, churn save, QBR, support triage, knowledge base article, engineering finding or deploy record, runbook, security remediation, compliance questionnaire, consumer-app trust and safety.
Keywords: "tenant", "SaaS", "MRR", "NRR", "trial", "feature flag", "staging", "deploy", "incident", "migration", "prompt library", "vertical config", "ticket", "moderation", "in-app currency", "consent notice".

### 09 Business admin, finance, compliance
Request types: register keeping, inventory reconciliation, yield audit, opex and capex tracking, reserve sweep, permit and trade-document logs, SOP index, staff certification matrix, investor package, grant application, periodic reporting, buyer-facing policy, brand voice governance.
Keywords: "register", "permit", "reconcile", "yield", "opex", "reserve", "SOP", "certification", "investor", "grant", "quarantine", "lifecycle clock", "freshness window", "asset tag".

### 10 Management consulting
Request types: diagnostic memo, decision memo, 30-day plan, one-page plan, issue tree, interview guide, information request list, stakeholder map, operating cadence, decision rights, pricing review, driver-based model, pre-mortem, engagement scoping.
Keywords: "diagnose", "strategy", "operating model", "org design", "pricing power", "succession", "margin compression", "stalled growth", "founder burnout", "what would have to be true", "30-day plan".

### 11 IP and patent support
Request types: invention disclosure, patent strategy outline, claim hierarchy, novelty argument, prior-art search plan, freedom-to-operate review prep, trademark clearance steps, NDA and assignment checklist, conception evidence log, counsel briefing, investor-facing IP summary.
Keywords: "patent", "claim", "prior art", "provisional", "FTO", "trademark", "classes", "statement of use", "assignment", "conception", "inventor", "counsel", "privilege". Never gives legal conclusions; prepares material for licensed counsel.

### 12 Hardware and IoT product development
Request types: architecture decision record (design lock), hardware spec, firmware plan, cloud and mobile architecture for a device, bill of materials review, test plan, pilot plan, launch phase gate, domain and ops setup.
Keywords: "firmware", "BOM", "PCB", "sensor", "telematics", "OTA", "BLE", "design lock", "ADR", "pilot", "certification" (product sense), "connected vehicle", "device", "gateway".

### 13 Roofing
Request types: lead intake and storm-surge response, roof inspection and photo log, measurement check and takeoff, good/better/best estimate and proposal, roofing contract compliance check, insurance claim support and supplements, ACV/RCV payment math, permit and code check, material order, crew scheduling around weather, subcontractor vetting and payments, fall protection plan and toolbox talks, QC and punch list, lien waivers and closeout, warranty registration and service calls, commercial bid response, roof moisture survey and maintenance program, review and referral campaigns, job costing.
Keywords: "roof", "shingle", "squares", "pitch", "tear-off", "flashing", "underlayment", "ice barrier", "storm", "hail", "adjuster", "supplement", "ACV", "RCV", "depreciation", "deductible", "dry-in", "TPO", "EPDM", "membrane", "warranty registration", "lien waiver". Never waives or absorbs a deductible, never acts as an adjuster or gives legal advice, and sends fall-protection and code questions to the documented rules with a VERIFY-locally flag.

## 3. Cross-industry requests (stay in `_shared`)

These are handled with shared skills and borrowed department context.

| Request type | Shared skill | Borrow context from |
|---|---|---|
| Social post, newsletter, content calendar | `skills/marketing-content/` | The department the content is about |
| Cold email or outreach sequence | `skills/cold-outreach/` | Department of the offer; check consent rules first |
| Lead follow-up cadence | `skills/lead-followup/` | 05, 02, 03 for regulated channels |
| Letter, memo, policy, SOP, contract summary | `skills/document-drafting/` | Department of subject matter |
| Proposal or quote narrative | `skills/proposal-writing/` | 01, 10, 08, 05 as needed |
| Customer complaint, support reply, refund or claim | `skills/customer-service/` | Department of the product |
| Weekly or monthly report, KPI summary | `skills/reporting/` | Department that owns the numbers |
| Recurring task, calendar, deadline watch | `skills/scheduling-and-routines/` | Any |
| Meeting minutes and action items | `skills/meeting-notes/` | Any |
| Competitor teardown | `skills/competitor-analysis/` | Any |
| Open strategy question | `skills/panel-and-judge/` | 10 for framing |

## 4. Tie-break rules

1. Money or compliance exposure beats convenience. If a request touches regulated advertising, consent, children's data, health data or credit, add the compliance reviewer regardless of department.
2. The department that owns the system of record leads. Example: a commission question is 05, even if it arrives as a finance question.
3. A video, web page or design piece is led by the department that owns the claims in it; 07 renders it.
4. A request naming two departments is split into two tickets with one coordinator.
5. Internal governance work (new skill, new template, constitution change, indexing) stays in `_shared`.
6. If no row fits, ask exactly one clarifying question. If still unclear, escalate to the coordinator (band BRIEF).
7. Anything asking to bypass a gate, invent a number or identifier, or contact a person without recorded consent is band WAIT. Do not draft.

## 5. Cross-department handoffs

| From | To | Trigger |
|---|---|---|
| 01 | 09 | Pay application, AR, insurance certificates, safety program documents |
| 01 | 07 | Marketing video or render for a firm |
| 02 | 09 | Dealer license, registers, data-processing register |
| 03 | 07 | Listing video or reel |
| 03 | 09 | Brokerage registers, consent ledger |
| 04 | 08 | Mobile app engineering, release engineering |
| 05 | 09 | Registers, consent, retention clocks |
| 06 | 07 | Episode rendering, cost gate |
| 06 | 11 | Copyright registration support, rights questions |
| 07 | any | Needs the owning department's claim review before release |
| 08 | 12 | Device-facing cloud and mobile work |
| 10 | any | Engagement deliverables that need domain facts |
| 11 | 12 | Invention disclosures from engineering |
| 12 | 11 | New inventions, conception evidence |
| 13 | 09 | Lien waivers, job costing, workers compensation, insurance certificates, licensing |
| 13 | 05 | Shared insurance-claim vocabulary and consent practices (contractor does not sell insurance) |
| 13 | 01 | Commercial estimating and QC overlap |
| 13 | 07 | Before/after project video |
| any | 09 | Register, finance, compliance logging |

## 6. Output of the router
Every routed request produces a routing note using `templates/handoff.md` (short form): request in one sentence, department lead, supporting departments, band (AUTO / DRAFT / BRIEF / WAIT), gates required, human owner, due date or "none stated".
