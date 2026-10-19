# Changelog

## 0.8.2 — 2026-10-19

- Bundle Claude connector screenshot and host-specific sign-in guidance.
- Distinguish an already-connected UI from verified project access and Claude Code tool availability.

## 0.8.1 — 2026-10-19

- Bundle the maintainer-provided Codex Google Drive setup screenshot.
- Add explicit Settings → Plugins → Google Drive sign-in guidance and scoped verification.

## 0.8.0 — 2026-10-16

- Prefer host Google Drive/Workspace MCP and connectors across installation, initialize and work.
- Guide host installation and human OAuth consent; verify actual scoped capabilities.
- Move gws/gog and team OAuth configuration to opt-in fallback documentation.

## 0.7.4 — 2026-10-16

- Document the team OAuth project and Allen support contact.
- Require agent-guided client setup, browser consent and scoped read verification.
- Clarify that client credentials are distributed separately, not bundled.

## 0.7.3 — 2026-10-16

- Rename skill to agentic-artefact-project-collaboration.
- Scope discovery metadata and instructions to explicitly identified Artefact team projects.
- Add branded interface metadata and legacy-install migration instructions.

## 0.7.2 — 2026-10-16

- Make INSTALL.md the single agent installation procedure; remove manual ZIP instructions from README.
- Add agent-run dependency checks, confirmed installation and separate access validation.
- Use gws by default; gog is optional, not an additional dependency.

## 0.7.1 — 2026-10-16

- Add project-root access boundary and explicit confirmation before all mutations.
- Apply restrictions consistently to initialize, work and browser workflows.
- Document agent-led installation from a GitHub URL.

## 0.7.0 — 2026-10-16

- initialize / work workflows for cross-agent Google Drive projects.
- Native Google Docs, Sheets and Slides preferred for team-facing content.
- Six-folder default; shared guidance and blank templates stay inside the skill.
- Separate local personal identity, shared roster, task ownership and access permissions.
- Agent-run OAuth, gws access, browser fallback and read-only Python reader.
- Scoped reads, local change tracking and 16 unit tests.
