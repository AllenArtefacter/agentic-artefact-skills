# Tasks and Backlog

In 01_Management, use one native Google Sheets file named Tasks with exactly two default tabs: Tasks and Backlog. Do not create a separate Work Plan. Keep substantive decisions in their existing source or a concise Decisions Doc; a task migration must not discard them.

## Shared columns

Task | Step | ID | Description | Owner | Deadline | Status | Deliverables

- Task is the parent work item; Step is a concrete action.
- ID is a stable text identifier in taskId.stepId form, e.g. 3.1, 3.4, 4.15. Never store it as a decimal: 4.10 and 4.1 differ. Keep IDs unique across both tabs; retain IDs when promoting, moving or reordering. Preserve legacy ID mappings in Description or a cell note.
- Description states the work and links the originating meeting, chat or plan when available. Use native file chips for supported sources, descriptive hyperlinks otherwise. Preserve proposal/confirmation and evidence dates.
- Owner uses a native person chip from a confirmed email; TBD when unassigned. Do not infer an owner from a role, speaker number or roster order. Plain @email is only a disclosed fallback.
- Deadline is a confirmed date with date formatting; TBD when unknown. A meeting date or completion date is not automatically a deadline.
- Status is a strict dropdown with exactly: todo, doing, pending, done, partially done. Pending includes waiting for input/verification, explained in Description. Completion requires evidence. Status does not represent human approval.
- Deliverables contains actual output links/chips, one per physical row. Use TBD when an output does not exist; never invent links.

## Approval boundary

Tasks contains only human-validated work. Backlog contains agent/AI suggestions extracted from meetings, chats and planning. An AI interpretation, a meeting mention, an existing draft, or a done status does not prove human validation. Record who approved, when and the source in Description or an ordinary cell note where known; do not invent attribution or approval dates. An explicit user request to do a concrete task is validation of that task.

Promote only explicitly approved IDs/steps from Backlog to Tasks, preserving IDs, source links, ownership, status and deliverables. Verify destination rows before removing the source entry, and do not leave two active copies. Resolve duplicate IDs or concurrent edits before writing. Unapproved steps stay in Backlog even when another step of the same Task is approved. New AI suggestions default to Backlog. Owner's tasks are matched by exact chip email/confirmed aliases, with Backlog suggestions reported separately from assignments.

## Merged layout

For one Task with multiple Steps, merge column A vertically across that Task's contiguous rows within each tab. For one Step with multiple Deliverables, use one row per deliverable and merge each of B:G vertically across that step's rows. Column A spans the full Task group, so do not apply overlapping step merges to A. H remains unmerged. A single-step Task with several outputs therefore has A:G merged individually across its output rows.

Keep one step's values in the top-left cell of each merged range. When reading, use merge metadata to inherit these values only inside that range, not arbitrary fill-down. Count distinct IDs rather than output rows. Never merge different owners, deadlines or statuses into one step. Split the step or ask when these differ.

Use a plain formatted grid with cell-level status dropdowns because the requested vertical merges conflict with sortable native table semantics. Do not force native Sheets tables, filters or row-level sorting over these merges. Freeze header rows; do not freeze part of a horizontal merged title. Reorder whole task/step groups. For insertions, read affected merges and cells, preserve content, unmerge only the affected group, write the new rows and reapply its merges. Do not overwrite another user's edit from stale row numbers.

## Migration and verification

Read existing task/plan/decision records before migrating. Separate proven human requests from AI suggestions, retain historical status caveats and preserve decisions. After the new Sheet is verified, update canonical links in Project/index/meeting records. Remove or archive superseded files only within the user's explicit authorization; prefer recoverable deletion. Do not create a second authoritative task register.

Verify both tab names, eight headers, text IDs, dropdown values/strictness, person/file chips, deadline types, merged ranges and source-to-destination row coverage. Check a multi-step Task and a multi-output Step where real records exist; do not add fake project rows just to demonstrate formatting. Preserve unknowns. Keep reusable seeds and this guide inside the skill.
