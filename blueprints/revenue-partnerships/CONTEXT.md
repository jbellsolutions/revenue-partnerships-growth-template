# Context cards and the relationship graph

## Reuse the working concept

Affiliate Manager's `relcore` is the base for relationship memory. Its SQLite state supplies rendered Obsidian cards; the agent reads and records through its `rel_` interface. The vault is the visible knowledge graph and owner review surface. Do not create a second independent relationship database in each specialist's memory or treat hand-edited generated Markdown as an unrestricted CRM writer.

The existing package already distinguishes people, partners and partnerships, builds a bounded context brief, rejects stale draft context and prepares outbox/CRM work. Adopt those contracts. Do not copy the old GrokBot or Bops runtime instructions into this new service. Do not merge private partner data from those installations.

## Card types

| Card | Identity / contents | Authority |
|---|---|---|
| Growth Director | Mission, delegated responsibilities, exclusions, success, escalation | Reviewed program governance |
| Affiliate Manager capability | Recruiting → onboarding → activation → reporting playbook | Pinned source skill adapted to this program |
| Apply 2 | Unresolved named concept from the owner's request | Keep a question card; do not invent its job |
| Program / client | Business, offer, buyer ICP, funnel, economics, claims, approved terms | Client owner is authoritative |
| Family | Definition, steward, subcategories, permitted commercial models | Taxonomy snapshot + reviewed eligibility |
| Partner type | Stable ID, avatar, opportunity hypotheses, discovery plan, qualification | One definition per 339 types |
| Person | Contact identity, channel preferences/consent, quoted replies, commitments | Sources and restrictions required |
| Organization | Buyer audience, products, regions, team, reach and trust evidence | Observed facts separate from model inference |
| Partnership | Client × organization × type; owner, tier, stage, agreed plan and terms | System-of-record and owner-controlled fields |
| Opportunity / plan | Specific collaboration, why now, milestones, dependencies, next ask | Proposed until mutually accepted |
| Call / review / receipt | What was actually said/approved/executed, evidence and open loops | Provenance, exact action scope and immutable receipt |

The generated `vault/00-System` notes are context-card seeds. Taxonomy notes are reusable public reference. Real People, Partners, Partnerships, Calls, Plans and Reviews remain private per client. A generic avatar is never a discovered person.

## Context before action

Assemble only the relevant slice: client program → type dossier → relationship → restrictions → prior conversation → open loops → current task. Record a digest of versions and inputs. Before drafting, use the existing `rel_context` result and its digest. Before a dispatch or CRM mutation, reread authoritative current fields and verify that the approval and payload match. New replies, changed consent or changed terms invalidate old proposed actions.

The type profile is a reusable lens. The person card is the individual truth. A type-level suggested hook must never overwrite the person's history, preferences or do-not-contact status.

## Essential fields and graph edges

All facts need `value`, `source_kind`, `source_url_or_record_id`, `observed_at`, `recorded_by` and `verification_status`; inferences need a rationale and explicit inferred status. Plans carry `client_id`, `program_version`, `type_id`, `person_id`, `organization_id`, `partnership_id`, `relationship_owner`, `next_action`, dependencies and a context digest. Activity carries a source event ID and provider/owner receipt. Terms, consent, affiliate codes, payouts and conversions are not guessed by models.

Graph links: Client has Offer; Offer serves Buyer ICP; Type belongs to Subcategory belongs to Family; Organization reaches Buyer ICP; Person represents Organization; Partnership connects Client/Organization/Type; Opportunity advances Partnership; Action produces Receipt; Receipt supports CRM stage or Attribution. Dream tier belongs to the relationship portfolio, not the type node.

## Systems of record

Attio is authoritative for agreed relationship pipeline, next action and recognized partner outcomes. Affiliate platforms/payment exports establish tracking and realized commercial outcomes. ClickUp holds service delivery, operating work, blockers and won-client work; individual prospects stay in Attio. The context graph holds supporting evidence, conversations, plans and unresolved questions. Field ownership and sync direction must be mapped before adapters can write.

No double-writing: the relationship service updates private context state; Attio Operator writes Attio; ClickUp Operator writes ClickUp. They exchange durable packets and receipts. The renderer refreshes views after committed state changes. Per-client dedupe and revision checks stop multiple profiles from racing on one person.

## Client isolation

A clean client clone copies schema, public taxonomy, reviewed SOPs and role definitions. It starts with a new identity, empty relationship state, empty authenticated browser profiles and unbound provider requirements. A same-owner transfer is a different operation: encrypted context transfer, preserved uncertain-action records and reconciliation before resume. A client template never includes commissions negotiated for another client, private contact lists, browser cookies or old approvals.

See [Affiliate Manager relationship cards](https://github.com/jbellsolutions/affiliate-manager-agent/blob/1329a2b41633ffdcf93344e17e3a3ca3069487ec/docs/RELATIONSHIP-CARDS.md). The worker/program/type-card extensions in this document are proposed integration work.
