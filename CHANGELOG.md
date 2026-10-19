# Changelog

## 0.10.1 — 2026-10-19

- Classify Tasks and Backlog by confirmation state, not author. Both people and AI can record Backlog entries.
- Use neutral titles: Tasks — Confirmed and Backlog — Pending confirmation.

## 0.10.0 — 2026-10-19

- Replace the default Work Plan with a Tasks Google Sheet: human-validated Tasks and AI-proposed Backlog.
- Add eight shared columns, stable text step IDs, explicit promotion rules, person/file chips and five status options.
- Define task/step/deliverable merges and update initialization, identity lookup and local seeds.

## 0.9.5 — 2026-10-19

- Add native meeting cards with blue headers, six bold summary labels, optional yellow open checks and file-chip sources.
- Specify editable table styling and safe updates by meeting ID.

## 0.9.4 — 2026-10-19

- Flatten Project metadata team chips without titles and use native chips for known dates.

## 0.9.3 — 2026-10-19

- Keep Meeting Briefs compact with six inline summaries and short open checks; link detailed evidence from notes.

## 0.9.2 — 2026-10-19

- Use native file chips for meeting source and related-document links; preserve useful deep links.

## 0.9.1 — 2026-10-19

- Preserve native meeting headers: bold title, date chip and labeled person chips.
- Keep reference invitees distinct from confirmed attendance; verify native chip readback.

## 0.9.0 — 2026-10-19

- Add raw/note meeting layout, source-linked notes and running Meeting Briefs.
- Add six-field summaries, cross-meeting conflict tracking and source-discrepancy handling.
- Generate meeting subfolders without publishing empty note templates.

## 0.8.3 — 2026-10-19

- Standardize six required Project metadata fields and native person-chip publishing.
- Add optional start date, project status and client contacts to initialization briefs; preserve unknown values as TBD.

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
