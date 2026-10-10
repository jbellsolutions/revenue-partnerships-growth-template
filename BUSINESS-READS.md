# Native CRM and operations read connection

`scripts/business_read_mcp.py` exposes five narrowly scoped tools: verify native workspace/task binding, read configured Attio partner lists, read their schema, read bounded list entries, and read the configured ClickUp operating task. List aliases and provider identities come from a private bindings file; tool callers cannot select arbitrary endpoints or unbound lists. Attio list-entry queries use the provider's read-only POST query route. Redirects are refused, pagination is bounded, and raw authentication errors are withheld.

Register this stdio server using the existing Hermes Python executable and these environment paths (no secret values in config):

- `REVENUE_CONNECTION_BINDINGS`: private JSON with `attio.workspace_id`, `attio.lists` alias-to-ID map, `clickup.workspace_id`, and `clickup.task_id`.
- `REVENUE_CONNECTION_ENV`: private dotenv file with ATTIO_API_KEY and CLICKUP_API_TOKEN, mode 0600 under the profile's private-business directory. python-dotenv is already included in the reviewed Hermes runtime.

Run native `hermes mcp test revenue-business-reads`, then execute the identity, list/schema and task reads. Verify that a mismatched workspace, unbound list, unknown write tool and out-of-range query fail. This connector does not write CRM records, send messages, edit tasks, change attribution or run a sync worker. Production sole writers need their own reviewed diff/receipt and reconciliation gates.

Official API references: https://docs.attio.com/rest-api/endpoint-reference/meta/identify, https://docs.attio.com/rest-api/endpoint-reference/entries/list-entries, https://developer.clickup.com/reference/getauthorizeduser and https://developer.clickup.com/reference/gettask.
