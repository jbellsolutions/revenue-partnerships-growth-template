# Install on an existing Hermes computer

This release is an isolated profile overlay, not the upstream full-machine installer. It requires an already working, reviewed Hermes installation. New computers, software dependencies, runtime upgrades and new spend require separate authorization.

1. Read AGENTS.md, CAPABILITIES.md and OPERATIONS.md. Inspect the intended computer, runtime version, free disk and existing profile/services. Preserve all existing state.
2. Clone a private client project; materialize its pinned public template as `template/`. Do not place GitHub credentials in clone URLs or files.
3. Run `python3 template/scripts/verify.py` and `python3 -m unittest discover -s template/tests`.
4. Create a fresh profile with native `hermes profile create revenue-partnerships-growth --no-skills --no-alias`. Do not use clone/clone-all.
5. Install using `python3 template/scripts/install_profile.py --profile <fresh-profile-path> --client <private-project-path> --preserve-native-seed`. It refuses an existing installation or client session state, and backs up native bootstrap identity/skills before installing. It copies reviewed skills, AGENTS/SOUL and program context, registers only the private drafts-only relationship MCP and sets manual approvals. It does not copy credentials, provider settings or create schedules.
6. Complete native private provider authentication or bind only the already authorized model credential locally. Do not copy the source profile's complete .env, connectors, memory, channels or sessions.
7. Verify native skills discovery, MCP initialize/tools/list/status and synthetic workflow. Test one harmless native reply using the permitted tools and record provider/usage evidence.
8. Verify each selected real connection from this profile before enabling its scoped writer. Keep missing integrations pending. Capture private entrypoint, revision, recovery and stop instructions.

Installation-ready means the package checks pass. Native-answer-ready means an actual model response and selected owner entrypoint are verified. Research-ready requires approved program/buyer/source authority. CRM/operations-ready requires actual Attio/ClickUp readback and adapter receipts. Sales-operation-ready also requires approved terms, attribution and a bounded reviewed activation experiment. Do not conflate these statuses.

Rollback: stop only this named profile's processes; retain private receipts/backups; revert the package to the recorded pinned revision. Do not alter the original default Hermes profile or gateway. Never replay uncertain actions after rollback.
