---
name: attio-partner-crm
description: Prepare or verify Attio partner CRM synchronization; use for actual partner pipeline changes.
---

# Attio Partner Crm

Use only the designated sole writer. First verify workspace, schema, list bindings and canonical IDs. Packet must include client, relationship, source event, exact field diff, idempotency identity and expected readback. Upsert by stable provider IDs, preserve owner-confirmed values and prevent stage regression. Dispatch only through a reviewed scoped adapter. On uncertainty reread provider and reconcile; no blind retry. Complete only with provider ID and matching readback; otherwise mark pending_sync.

Read AGENTS.md, the private program card and OPERATIONS.md for authority and receipt requirements. Secrets stay in the client secret store. Stop affected work when context, authority or connection evidence is missing. Report prepared versus completed work accurately.
