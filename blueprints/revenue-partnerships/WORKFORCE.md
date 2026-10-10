# Applying the system to System One Workforce / Hermes Trial

## What exists and what must be built

The tagged project was renamed from `jev-workforce-hermes-trial` to `system-one-hermes-trial`. The reviewed baseline is `746655f`. It already has persistent employees, native Hermes homes, jobs, training, authority scopes, browser profiles, assignments, routines, role-copy/transfer logic, typed decision contracts, a shared budget and evidence verification. Use that control plane; do not add a separate scheduler.

The Affiliate Manager source is pinned to `1329a2b`. Reuse its mission, partner lifecycle, relationship-card model, `rel_context`/draft digest, restrictions, private data handling and draft-only outbox. Its Orgo setup contract is a source reference, not a command to replace the workforce runtime or install another Hermes version. Preserve the trial's pinned runtime until its release policy approves a change.

| Existing seam | Proposed application | Gap / acceptance requirement |
|---|---|---|
| `system_one/roles.py` | Add Growth Director, shared affiliate capabilities, Attio and ClickUp roles | Roles currently contain broker/crm/funding/admin; generated partner profiles are not recognized runtime roles yet |
| `JobDescription` / workforce training | Compile reviewed program and type charter into mission, business brief, authority and success criteria | Validate lengths; private program overlay resolved before activation |
| `provision_home` / `worker_home.py` | Seed SOUL, AGENTS and pointers to the authorized card reader | New workers preserve persistent identity and do not inherit another client's memory |
| `relcore` in Affiliate Manager | Private per-client relationship service and generated Obsidian views | Add an authenticated workforce adapter; prove state isolation, stale-digest refusal and schema compatibility |
| `workforce.assign` / employee work queue | Bounded research, qualification, onboarding and support jobs | Read declared family/type/relationship context, record next owner and completed artifacts |
| `Contracts` / `models.decide` | Draft classification and qualification choices | ≤50 options per contract; calibrate with labeled examples; no new backend API assumed |
| `Authority` / employee gateway | Existing safe research/private work; reviewed external action scopes | Reject self-expanded authority, changed payloads and expired approvals |
| `procedures.py` / procedure receipts | Deterministic verified routines for repeatable reads and writes | Current CRM adapter is synthetic; existing visible-browser verifier is not proof of production CRM correctness |
| `Portability.role/clone` | Clean service-client role templates | Inspect free-text training for client facts; redaction is not a substitute for a clean-room template |
| `Portability` encrypted transfer | Explicit same-owner recovery | Uncertain work remains awaiting reconciliation; never replay sends |
| Cost/isolation controls | Existing lifetime metering and host capacity | Keep the $10 lifetime trial cap; do not borrow original credentials, homes or containers |

## How a profile becomes work

The 339 registry entries are definition records, each with a unique type ID, job, avatar, discovery channels, qualification evidence and reference-card path. A client overlay supplies the business/customer ICP and status. The director selects work from eligible types. The queue schedules a bounded assignment under an authorized persistent employee. Its task carries the selected profile ID and immutable dossier/program versions.

This design does not yet implement switching native Hermes identities within one employee. If a lane needs its own persistent specialist, create a reviewed template and provision it through the existing workforce controls. If it only needs a bounded type lens, provide the dossier as assignment context. Both approaches preserve a single relationship owner and client-wide deduplication. Profile count, employee count, browser-profile count and simultaneous worker count are separate capacity measures.

## System One versus Hermes versus deterministic code

| Decision/work | Owner |
|---|---|
| Exact IDs, dedupe, source freshness, locks, approvals, stage ordering, budgets and receipt reconciliation | Deterministic control plane |
| Which family best fits a stated commercial relationship? | Bounded System One Choice with no-match/insufficient-evidence |
| Which subcategory/type fits within candidate branches? | Hierarchical candidate routing; never a flat 339-option call |
| Does supplied evidence support buyer overlap or activation readiness? | Bounded typed judgments with evidence spans and review cases |
| Research a new partner, form an unfamiliar value exchange, write a tailored brief, explain ambiguity | Hermes using the trial's configured reasoning provider |
| Verify a completed external action | Provider/readback/committed receipt, not model prose |
| Accept partners, negotiate terms, resolve disputes and release payouts | Human owner |

For ambiguous identities, return possible matches for human/entity-resolution review. For overlapping relationships, keep one primary type per partnership and allow additional evidence-backed partnership records; do not force an organization into only one family. Insufficient evidence is an explicit result, not a low-scoring rejection.

The initial contract files cover 11-family routing and partner-fit disposition. They use the existing Choice schema. Noul/Score ideas from TypeSafe remain future adapter work because the trial's current `models.decide` interface is a bounded choice. The 0.85 threshold in draft contracts matches the trial convention; it is uncalibrated for this domain and not permission to dispatch messages. Contracts stay draft until passing a completed live evaluation and owner-reviewed promotion.

## Integration order

1. Validate the map, private/public separation, program/schema and profile definitions offline.
2. Add recognized roles and training pointers without altering existing employees.
3. Wire the relationship reader/writer and prove isolation, freshness and context-before-draft with synthetic data.
4. Run native Hermes synthetic partner assignments using the existing metered gateway. Keep paid quality/cost results pending until run.
5. Bind Attio and ClickUp read scopes; verify schemas, identities and sole writers before any write experiment.
6. Add a permitted channel executor only after the sender/approval boundary is proven. Preserve the source's draft-only behavior until then.
7. Evaluate selected type dossiers and partner-fit judgments on labeled examples, then promote only versions supported by receipts.
8. Activate a first-client cohort through the existing queue. No idle polling fleet; each routine must have a concrete due portfolio or event.

This package is a workforce integration specification. It does not authorize provisioning, change Phase 0, choose a winner, increase trial spending, run a soak test or deploy the application.

References: [workforce repo](https://github.com/jbellsolutions/system-one-hermes-trial), [TypeSafe building guide](https://docs.typesafe.ai/concepts/how-to-build-with-system-one), [hierarchical classification](https://docs.typesafe.ai/cookbooks/hierarchical_classification), [confidence](https://docs.typesafe.ai/confidence). The proposed worker decomposition follows these sources but has not been measured live.
