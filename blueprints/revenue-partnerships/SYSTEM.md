# The Revenue Partnerships Growth system

## The outcome and the boundary

A business gets one accountable Revenue Partnerships Growth Director in the demand-generation category. Its job is to turn other people's established buyer relationships into a measurable partner-sourced growth channel: recruit, qualify, activate, support and grow partners. One visible agent can coordinate specialist work behind the scenes, but a person owns every relationship and the director owns every open loop.

This is one of the planned three flagships. The other two are outside this design. Lead Radar scraping, general prospecting, OutFlo administration and general LinkedIn content are removed from this flagship's responsibility. Nothing here disables the previous Bops installation, deletes its records or migrates its live jobs. That cutover is a later, explicit step.

## Four layers of identity

1. **Taxonomy:** 11 families → 67 subcategories → 339 partner types, imported from the published map with stable source IDs. This describes a commercial relationship, not the identity of a person.
2. **Specialist profile:** one reusable job/playbook/context definition per type, linked to a family steward. It knows where that type appears, why it could partner, what evidence matters and which actions are permitted.
3. **Client application:** the same profile applied to a specific business, offer, buyer ICP, region, constraints and approved terms. This decides whether the type is eligible and worth researching.
4. **Real relationship:** person → organization → partnership with this business and this type. A person and organization may support multiple legitimate partnership types without creating duplicate outreach.

Dream 100 and Dream 500 sit across the taxonomy as relationship tiers. They are not two additional families or automatically separate lead lists. Preserve the existing distinction: Dream 100 strategic whales; Dream 500 high-leverage emerging/second-tier partners. Reuse the original ≥70/overlap ≥4 and 55–69 criteria only after their dimensions are adopted for the new program. Raw follower count cannot by itself make a whale. The client owner continues to write Dream outreach unless he changes that rule.

## The full cycle

| Stage | Work | Required evidence / exit |
|---|---|---|
| Interview | Learn the client, buyer journey, offer, capacity and economics | Owner-reviewed program card; missing terms remain unknown |
| Map | Evaluate all types against before/during/after/instead-of customer relationships | Every type has pursue/research/defer/exclude and a reason |
| Prioritize | Select attainable partner types and first experiments | Ranked types; discovery sources, hypothesis and capacity allocation |
| Discover | Find actual organizations, people and partner opportunities | Public/authorized source URLs, observed facts and timestamps |
| Resolve | Dedupe identity, ownership, prior relationships and suppression | One canonical person/org; actual partnership type; no conflicting campaign |
| Qualify | Evaluate buyer overlap, trust, intent, reach, incentive and ability to act | Supported profile; missing facts separated from negative findings |
| Plan | Form a mutually useful value exchange and first activation milestone | Partner-specific plan; offer and claims drawn from approved facts |
| Converse | Prepare context-based introductions, respond and advance open loops | Fresh relationship digest, reviewed draft and permitted dispatch path |
| Accept/onboard | Owner chooses partners; create approved assets and tracking | Accepted terms, owner approval, valid link/code and activation brief |
| Activate | Help the partner produce its first useful referral or campaign | Agreed launch milestone, approved assets and actual activity receipt |
| Reconcile | Connect introductions, sales and attribution to the partnership | Provider/owner provenance; ambiguous attribution is held for review |
| Grow | Support producers, reactivate stalled partners and improve playbooks | Verified outcomes; versioned experiments and review decisions |

The unit of success is an activated, productive relationship—not a scraped contact. Research breadth feeds a small, high-quality active portfolio. The sales-page “five heavy hitters” is a useful pilot thesis; it is not an earnings forecast or a reason to stop mapping the wider market.

## Opportunity discovery, not just contact discovery

An opportunity links a partner type, a real organization/person, a client offer and a feasible distribution motion. Store `why_now`, buyer overlap, a concrete first collaboration, evidence, authority, dependencies and next step. Examples include a member workshop, a customer introduction, a lesson integration, a co-produced guide or an implementation partnership. Someone owning an audience is not evidence that they will promote us.

Each generated profile includes reusable discovery routes and queries. Instantiate `{buyer_topic}`, `{region}` and `{offer_category}` from the client card, inspect actual sources, then attach observed URLs to real relationship cards. Maintain a coverage ledger per type: searched sources, candidates found, unique qualified relationships, unknowns, rejected reasons and next source. “No candidates found in sources A/B” is valid; “no partners exist” is not.

## Scale design

The registry contains all 339 types, but activation is selective. Start with one director, shared relationship/quality capabilities, the two sole writers, and a small number of type-specific research work items. Schedule through the existing workforce queue. Create dedicated persistent specialist employees only for validated lanes that need sustained context and can fit host capacity. The runtime's present clone operation creates employee identity/computer requirements; a blueprint profile is not yet a lightweight worker switch.

Use family stewards as review responsibilities, not 11 permanently polling agents. One relationship owner arbitrates overlapping type profiles; lock writes and sends by client + relationship/channel identity. Per-type research tasks may operate independently; conversation updates must not race.

## Milestones

| Phase | Deliverable | Gate |
|---|---|---|
| A — Map | Taxonomy, 339 definitions, context schema, role contracts, portable/client separation | Counts/IDs/links checked; speculative content labeled |
| B — Compile for workforce | New role contracts, native guidance, relationship-service adapter, typed decisions and verifier design | Isolation and native context tests; no unverified fast path |
| C — Prove a service | Synthetic client pack and explicit authority contract | Clone has fresh identity, empty logins, no source client facts; uncertain writes not replayed |
| D — Apply to us | Revenue Partnerships program brief, chosen types, real research cohort | Owner-approved offer/terms/ICP; sourced candidates and relationship cards |
| E — Operate | A bounded activation experiment with CRM/ops synchronization | Channel access and receipts verified; reviewed outreach and attribution |
| F — Replicate | Versioned delivery package, onboarding interview, QA and recovery | First-client lessons generalized without exporting its contacts or private training |

The taxonomy is implemented; workforce control-plane adapters remain planned. Later phases are planned, not executed. No deployment, live research quota, model-spend increase or production cutover is implied by this package.

## Measurement

Track coverage by family/type, evidence completeness, qualified partners, reply/conversation progression, accepted partners, activated partners, time to first activation, productive partner share, partner-sourced pipeline, realized revenue, attribution confidence and outstanding support. Track model/research cost per qualified and activated partner. Distinguish observed provider amounts, imported amounts and estimates. Compare the selected lanes against held-out lanes; do not optimize only for responses.

Sources: [published partner map](https://map.truerevenuepartnerships.com/resources/partnership-map/), [Revenue Partnerships page](https://map.truerevenuepartnerships.com/), and pinned Affiliate Manager / System One references in `SOURCES.json`. Architecture and experiment priorities are design proposals.
