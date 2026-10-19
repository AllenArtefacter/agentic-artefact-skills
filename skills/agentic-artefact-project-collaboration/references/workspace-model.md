# Workspace and information model

## Three spaces

| Space | Location | Meaning | Shared authority? |
|---|---|---|---|
| local_personal | Employee device | Context cache, work, draft, outbox, local sync state | No |
| online_personal | Employee My Drive project folder | Optional private working material and drafts | No |
| online_team | Project Shared Drive root | Shared inputs, plans, work and deliverables | Yes, per canonical source |

ALL offline/local space is personal. Material originating from a team file remains a personal cache locally. Only explicit publication changes its shared status. Actual visibility depends on ACL, not labels. A team root's `personal/alice` directory is not assumed private. Customer publication uses a separately configured access boundary.

Do not automatically scan unrelated personal Drive content. Keep personal root IDs, credential references, per-user cursors and read receipts only in local connection config. Credentials themselves remain outside the project.

## Recommended team structure and canonical owners

Operational guidance lives in this skill, including references/folder-guides/. Blank record templates live in assets/document-templates/ and table headers in assets/control-seed/. Never publish these reusable files into a project. scaffold.py creates only project-specific seeds and empty working folders. The default structure is:

```
Project             native Google Doc: purpose, scope, roster and responsibilities
STATUS              native Google Doc: dated overview
00_Start_Here/      project index with canonical links
01_Management/      Tasks Sheet (Tasks / Backlog) and decisions
02_Meetings/        internal/client/catchup records
03_Deliverables/    outputs and reports
04_Materials/       inputs and references
90_Archive/         superseded records
```

Local Markdown/JSON templates are draft inputs, not the cloud format. Workstreams, sprints and detailed risks can use management records; add optional folders only when needed. Existing layouts take precedence. Native Project/STATUS docs satisfy all context requirements below.


Do not create a full folder hierarchy for every task. A lightweight task is a Tasks row; a complex task links a detail document in its workstream. Create subfolders only when actual materials justify them. Do not partition shared work into four disconnected consultant/DS/DA/DE silos.

## Default task register

Follow [task-tracking.md](task-tracking.md). Use Tasks / Backlog tabs with the specified eight columns and five status values. Do not create a separate Work Plan. Task IDs use taskId.stepId text; the legacy ID/status conventions below do not apply to the new task register.

## Optional and legacy Project Control records

| Optional tab/record | Owns | Linked content |
|---|---|---|
| People | Optional derived view of Project.md; no independent membership authority | Project.md source ID/version |
| Workstreams | Workstream IDs, owner and folder URL | Workstream README |
| Milestones | Target, acceptance criteria, status | Deliverable IDs |
| Sprints | Window, goal, owner, status | Sprint brief |
| Tasks | Owner, reviewer, priority, status, deadline, dependencies | Source IDs, optional details, evidence |
| Deliverables folder / Deliverables Doc | Output index, owner, review/acceptance state, canonical file ID, task links | Deliverable content and submission evidence |
| Materials folder / Materials Doc | Input index, source, version, owner, usage notes | Original files or controlled external links |
| Meetings | Meeting IDs, date, type, notes URL | Calendar event and task/decision IDs |
| Decisions | Confirmed/proposed/superseded state and decision owner | Rationale and source |
| Risks | Owner, open/mitigating/closed state, response | Analysis and affected IDs |

Prefer a native Sheet for structured tracking; use a native Docs table if Sheets is unavailable. Do not create every optional tab for a small project. The CSVs under skill assets/control-seed are initialization headers only. Once the Google Sheet is registered, retire them as live records. Text documents do not duplicate live status. A report or sprint review may contain historical status but must label its as_of time.

Use prefix + UUID for IDs; human-friendly titles may change. Multi-ID seed cells use semicolon separators; a future database migration can normalize these relationships. Example relationship (illustrative, not a live project):

MS-pilot → DEL-evaluation → TASK-evaluate
TASK-evaluate → WS-model, SPRINT-02, MAT-labeled-data
MEET-client-review → DEC-metric-definition → TASK-evaluate
Calendar event → MEET-client-review
Report → MS-pilot + DEL-evaluation + evidence URL

A task can serve multiple deliverables; sprint may be empty. Long-lived workstreams persist across many sprints. A report section is a heading or link to a deliverable; do not make `section/` a competing storage axis unless the project has genuinely independent deliverable sections.

## Status and editing responsibilities

Current Tasks: TODO / DOING / PENDING / DONE / PARTIALLY DONE; approval is represented by Tasks versus Backlog. Record blockers and cancellation evidence in notes. Reopen with evidence and preserve why. Deliverables: draft → in_review → approved_internal → submitted → accepted; changes_requested returns to draft. Decisions: proposed → confirmed → superseded. Meeting draft is not confirmed evidence of agreement.

Person doing the work proposes progress and evidence; the designated Control steward serializes accepted sheet changes. Reviewer checks technical/quality completion; customer acceptance has an explicit source. This is a workflow ownership convention, not a technical mutex. Local preparation scripts do not access Google; check host connector capabilities separately.

Separate local/publication state: local_only → pending_publish → published; conflict or stale needs re-read/reconciliation. A published document may still be a business draft. A locally completed task is not marked done in the shared table until that update actually succeeds.

## Editing / publishing transaction checklist

Resolve record ID and canonical file → read current version → prepare targeted modification → write via authorized supported connector → verify actual result → update Control fields and evidence → publish semantic event if implemented. If content succeeds but status/event update fails, report partial success and recover that missing step only.

For current read-only installations: prepare `outbox/publish-request-template.md`; a human/steward or separate connector can execute it. No automatic bidirectional synchronization between personal and team spaces.

## Mandatory agent context

Personal ME.md establishes identity and individual focus; team Project.md / STATUS.md establish shared context. Read them every session or reuse only after verifying unchanged versions. See [identity-and-tasks.md](identity-and-tasks.md). The roster owns formal assignments; a person's self-description cannot grant project decision authority or change task ownership.

## Meeting layout

Use 02_Meetings/raw and 02_Meetings/note. Follow [meeting-notes.md](meeting-notes.md) for source-linked notes and the single running Meeting Briefs document. Create the brief when there is real meeting content; do not publish blank templates.
