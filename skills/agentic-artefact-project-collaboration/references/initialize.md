# Initialize a project from zero

Follow the global restrictions in SKILL.md and [dependencies.md](dependencies.md). Use the host Google integration first; custom OAuth and CLI tools are optional. Existing membership never authorizes invitations or permission changes.

## Inputs and destination

Use supplied brief, SOW or meeting evidence for name, context, vision, scope, success criteria, PM and member emails/responsibilities. Start date, client contacts and unconfirmed facts remain TBD. Ask for a missing destination before cloud creation.

Two valid entry paths:
- **Existing project folder:** verify the exact authorized root. Reconcile existing files; initialize an empty folder or resume missing pieces without overwriting work.
- **No project folder yet:** obtain an explicitly authorized creation container and desired project name. Create one project root in that container, record its returned ID, then work only inside that root. This does not permit discovering or traversing a supplied project's parent. If folder creation is unsupported, ask the user to create the root and provide its link; finish a local draft meanwhile.

## Build and publish

1. Inspect integration capabilities for folder creation, native Docs, Sheets, chips and moves. Read the authorized destination; record existing IDs and unfinished setup. Tool availability is not proof of access.
2. Create six default folders: 00_Start_Here, 01_Management, 02_Meetings, 03_Deliverables, 04_Materials, 90_Archive. Create raw and note within Meetings. Preserve existing names/numbering. Optional workstreams, sprints and reporting folders require actual need.
3. Publish native **Project** and **STATUS** Docs at root. Apply [project-metadata.md](project-metadata.md). Project holds background, vision, scope, success criteria and confirmed team responsibilities; STATUS is a dated progress/blocker/next-step summary. Shared prose is English, while source quotations and names may retain their language.
4. Create **Tasks** in Management using [task-tracking.md](task-tracking.md): Tasks and Backlog tabs, approved versus unconfirmed work, text IDs, uppercase colored status dropdowns, owner/file chips and required merges. Do not invent rows for a blank project. Do not create Work Plan or a duplicate task register. Disclose unsupported native styling rather than claiming it exists.
5. Create **Deliverables** and **Materials** native index Docs inside their respective folders per [folder-indexes.md](folder-indexes.md), including empty-state text where appropriate. Publish meeting notes and Meeting Briefs only when actual meeting evidence exists, following [meeting-notes.md](meeting-notes.md).
6. Create a project-specific **Project Index** Doc in Start Here with canonical core, tracker, folder and index links. Keep machine manifest and checkpoints in the local personal workspace; never publish generic READMEs, template files, credentials or CSV header seeds. Record all created folder/file IDs immediately for recovery.
7. Read back the required files and confirm their parents, project-specific content, IDs, links, tab schema and indexing. Update STATUS with actual initialization outcome. Mark ready only after this succeeds.

## Local preparation

`python3 scripts/initialize.py --brief /absolute/brief.json --output /absolute/new-draft`

This generates personal local drafts and folders only: Project, STATUS, Project Index, Materials/Deliverables indexes and a manifest. It does not provision Google resources or a live Sheet. Use a real folder URL if available; for a not-yet-created root, use an explicit pending destination description. A missing brief may use scaffold.py, then fill confirmed facts. Do not present placeholders as ready.

## Acceptance and recovery

**draft_ready:** local artifacts exist, with unknowns identified and cloud IDs unset. **ready:** root and six folders exist; Project, STATUS, Project Index, Tasks Sheet and both folder indexes are readable and correctly located; canonical IDs resolve; task schema/links verified. Optional meeting records are required only when real meetings were supplied. Distinguish content verification from unverified styling or teammate access. Only claim access for tested identities.

On partial failure, preserve successful IDs, report missing steps and resume those steps only. Find existing candidates within the authorized root before creation; resolve duplicate names rather than guessing. Never recreate the project to fix a failed file. Return project entry, files, remaining gaps and a short work-mode example.

Folder-by-folder procedures: [folder-guides/README.md](folder-guides/README.md).
