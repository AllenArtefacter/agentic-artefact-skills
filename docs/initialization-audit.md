# Initialization and folder workflow audit — 2026-10-19

Version: 0.13.0

## Verified locally

- 16 tests pass, including populated initialize from a brief, required six-folder layout, raw/note, project-specific index drafts, unset cloud IDs, invalid roster rejection and non-overwrite on repeated invocation.
- Skill frontmatter validation passes; 27 routing/guide files have no broken relative links.
- General guides/templates remain inside the skill; initialize outputs no generic README or CSV seeds.

## Workflow coverage

| Area | Documented workflow |
|---|---|
| New root / empty root / partial setup | references/initialize.md: authorization, creation, native publishing, checkpoint IDs, recovery, readback |
| Project and STATUS | Context/membership versus dated progress; project-metadata.md and workspace-model.md |
| Start Here | Project Index navigation; local-only machine manifest |
| Management | Backlog approval, task ownership, statuses, evidence, merged layout |
| Meetings raw / note | Original preservation; note/brief; conflicts; tasks and decisions |
| Deliverables | Output/review/acceptance, folder index and task links |
| Materials | Receipt/provenance, original preservation, folder index and use links |
| Archive | Authorized archival, successor/history, active-link preservation |

## Limits

This audit did not create a test project in Google Drive. Local tests do not prove every host connector can create folders, write Sheets or set chip colors. Cloud ready requires the per-project native readback checklist; unsupported UI styling and teammate access remain explicitly unverified. The Python initializer prepares personal local drafts, not cloud resources. Existing live project folders were not changed by this audit.
