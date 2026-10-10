# Skills, plugins and software inventory

## Installed skills

Twelve reviewed skills in `skills/` cover intake, complete taxonomy mapping, actual opportunity research, fit review, canonical relationship context, Dream portfolio, conversation drafts, activation/support, attribution review, Attio CRM, ClickUp operations and daily/weekly portfolio review. Their charters are in `blueprints/revenue-partnerships/GOVERNANCE.md`. Skill text is operating guidance; it does not implement external adapters or authorize writes.

## Connections and plugins

| Capability | Requirement | Access / acceptance gate |
|---|---|---|
| Hermes native skills, memory and file tools | Required | Isolated profile, skill discovery and rule injection verified |
| relcore relationship MCP (included) | Required | Private SQLite/vault, no network credential; init/list/context/draft and stale-digest/suppression tests |
| Attio official API or reviewed MCP | Required before CRM operation | Client workspace, schema/list mapping, read test, sole writer, exact diff and readback receipts |
| ClickUp official API or reviewed MCP | Required before delivery sync | Client workspace/list/task mapping, read test, sole writer and readback |
| Browser/public research | Required before actual sourcing | Authorized public sources; private browser sessions isolated per client |
| System One workforce integration | Required for workforce scheduling/typed routing | Role/queue/gateway adapters and live metering/evaluation receipts; currently specification only |
| Affiliate tracking platform | Required before tracked conversions | Client-selected provider, approved terms, actual link/event readback; never invent a platform |
| Email/calendar or messaging | Optional | Read/draft scopes first; owner allowlist; human send remains default |
| Obsidian desktop | Optional | Markdown vault works without desktop software; graph views contain private relationships |
| GitHub | Release/updates only | Clean template history, private client repo, pinned revision and no secrets |
| Composio | Optional connection broker | Explicit tool allowlist; do not expose full account capabilities; private OAuth/sign-in |
| Orgo computer control | Deployment only | Existing authorized computer; no new billable resource |

No LinkedIn, OutFlo or Lead Radar plugin is required for this flagship. Existing shared services remain an inventory/cutover concern, not permission for this profile to use them. Avoid installing an omnibus agent-team plugin or inheriting another profile's connectors.

A chat application's connected Attio/ClickUp account is not proof that the remote Hermes computer has those connections. Verify native profile access independently. Provider names and official docs must be recorded in the private connection registry; no tokens or browser cookies enter Git.

## Software

| Software | Baseline / check |
|---|---|
| Linux Orgo computer | Reuse existing host; check free disk, ownership and existing services before install |
| Hermes | Existing reviewed v0.21.0 / v2026.8.31 for this release; never silently update |
| Python | 3.10+ for stdlib generator/relcore and tests; use existing Hermes venv for native runtime |
| SQLite | Python stdlib sqlite3; private DB, permissions and recoverable backup |
| Git | Clone/update pinned revisions; no force pushes or credential URLs |
| PyYAML | Already in Hermes runtime; installer config only, not a new package dependency |
| Browser | Optional for offline taxonomy explorer; needed for authorized browser research/login flows |
| Node/Docker/Obsidian | Not required for this standalone profile; workforce host dependencies remain in its upstream repo |

The upstream Affiliate Manager's old Orgo sizing/template pin is historical provenance. Current Orgo docs list `system/hermes-agent@1.1.13` on 1 vCPU/8 GB RAM; this overlay reuses the existing computer and does not upgrade or create it. See https://docs.orgo.ai/guides/hermes.

Official integration references: https://docs.attio.com/rest-api/guides/webhooks and https://developer.clickup.com/docs/authentication. An Orgo computer has no public inbound webhook hostname; use authorized outbound polling or a separately reviewed HTTPS receiver. Attio webhook consumers must verify signatures and deduplicate at-least-once deliveries.
