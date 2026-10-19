# Tasks and Backlog

In 01_Management, use one native Google Sheets file named Tasks with exactly two default tabs: Tasks and Backlog. Do not create a separate Work Plan. Record substantive decisions in the corresponding meeting note and summarize them in Meeting Briefs with matching decision IDs. Preserve existing decisions during migration; any separate Decisions Doc is an optional index, not an independent authority.

## Shared columns

Task / Meeting / Milestone | Step | ID | Description | Owner | Deadline | Status | Deliverables

- Task is the parent work item; Step is a concrete action.
- ID is a stable text identifier in taskId.stepId form, e.g. 3.1, 3.4, 4.15. Never store it as a decimal: 4.10 and 4.1 differ. Keep IDs unique across both tabs; retain IDs when promoting, moving or reordering. Preserve legacy ID mappings in Description or a cell note.
- Description is one short sentence stating the work, with a source link when available. Put approval history, migration details and detailed progress evidence in cell notes. Use native file chips for supported sources, descriptive hyperlinks otherwise. Preserve proposal/confirmation and evidence dates.
- Owner uses a native person chip from a confirmed email; TBD when unassigned. Do not infer an owner from a role, speaker number or roster order. Plain @email is only a disclosed fallback.
- Deadline is a confirmed date with date formatting; TBD when unknown. A meeting date or completion date is not automatically a deadline.
- Status is a strict dropdown with exactly: TODO, DOING, PENDING, DONE, PARTIALLY DONE. Pending includes waiting for input/verification, explained in Description. Completion requires evidence. Status does not represent human approval.
- Deliverables contains actual output links/chips, one per physical row. Use TBD when an output does not exist; never invent links.

## Approval boundary

Tasks contains confirmed work. Backlog contains tasks awaiting confirmation, recorded by people or AI from meetings, chats or planning. Classify by confirmation state, never by author. Use titles Tasks — Confirmed and Backlog — Pending confirmation. Human entry alone does not constitute approval. An AI interpretation, a meeting mention, an existing draft, or a done status does not prove human validation. Record who approved, when and the source in Description or an ordinary cell note where known; do not invent attribution or approval dates. An explicit user request to do a concrete task is validation of that task.

Promote only explicitly approved IDs/steps from Backlog to Tasks, preserving IDs, source links, ownership, status and deliverables. Verify destination rows before removing the source entry, and do not leave two active copies. Resolve duplicate IDs or concurrent edits before writing. Unapproved steps stay in Backlog even when another step of the same Task is approved. New unconfirmed items from people or AI default to Backlog. Owner's tasks are matched by exact chip email/confirmed aliases, with Backlog suggestions reported separately from assignments.

## Merged layout

For one Task with multiple Steps, merge column A vertically across that Task's contiguous rows within each tab. For one Step with multiple Deliverables, use one row per deliverable and merge each of B:G vertically across that step's rows. Column A spans the full Task group, so do not apply overlapping step merges to A. H remains unmerged. A single-step Task with several outputs therefore has A:G merged individually across its output rows.

Keep one step's values in the top-left cell of each merged range. When reading, use merge metadata to inherit these values only inside that range, not arbitrary fill-down. Count distinct IDs rather than output rows. Never merge different owners, deadlines or statuses into one step. Split the step or ask when these differ.

Use a plain formatted grid with cell-level status dropdowns because the requested vertical merges conflict with sortable native table semantics. Do not force native Sheets tables, filters or row-level sorting over these merges. Freeze header rows; do not freeze part of a horizontal merged title. Reorder whole task/step groups. For insertions, read affected merges and cells, preserve content, unmerge only the affected group, write the new rows and reapply its merges. Do not overwrite another user's edit from stale row numbers.

## Migration and verification

Read existing task/plan/decision records before migrating. Separate confirmed tasks from unconfirmed entries regardless of author, retain historical status caveats and preserve decisions. After the new Sheet is verified, update canonical links in Project/index/meeting records. Remove or archive superseded files only within the user's explicit authorization; prefer recoverable deletion. Do not create a second authoritative task register.

Verify both tab names, eight headers, text IDs, dropdown values/strictness, person/file chips, deadline types, merged ranges and source-to-destination row coverage. Check a multi-step Task and a multi-output Step where real records exist; do not add fake project rows just to demonstrate formatting. Preserve unknowns. Keep reusable seeds and this guide inside the skill.

## Key meetings and milestones

Include key meetings and milestones in the same eight-column grid, using [MEETING] and [MILESTONE] prefixes in column A. Use stable MEET-... and MS-... IDs; task IDs remain taskId.stepId. Step states the event or acceptance action. Description links the source and records confirmation evidence. Confirmed events belong in Tasks; proposals or unverified schedules belong in Backlog regardless of author. Do not invent milestone dates, acceptance criteria or owners. Deadline may hold a confirmed scheduled event date for meeting/milestone rows; explain its meaning in Description. An event date is not a deadline for a related task. Actual historical dates can remain in Description.

Use white rows for ordinary tasks, pale blue (#EAF3FC) for [MEETING] rows and pale purple (#F2ECFA) for [MILESTONE] rows, across A:H. Keep the native colored status dropdown chips; do not add status-driven cell background rules. A key meeting such as client kickoff may be a milestone: record it once as [MILESTONE], link its meeting note, and preserve its existing ID on reclassification. Status chip colors: TODO gray (#e6e6e6), DOING blue (#bfe1f6), PENDING yellow (#ffe5a0), DONE green (#d4edbc), PARTIALLY DONE purple (#e6cff2). Configure option colors and Chip display using the native UI when the connector cannot expose them; cell background formatting is not a substitute. Preserve colored validation when extending rows or copying between tabs. Verify uppercase values, option colors and display style after writes; disclose unsupported UI work rather than claiming chips were configured.

Maintain output links and the project Deliverables folder index together under [folder-indexes.md](folder-indexes.md).

Apply the project-wide [native chip convention](smart-chips.md) to people, dates/times and supported file references.

## Explain the tracker to users

When creating the tracker, introducing an existing tracker to a new teammate, or first showing their tasks, proactively give a short explanation in the user's language. Do not repeat it on every status update. Explain that this is one Google Sheets file with two tabs, separated by confirmation state, not author or progress:

- Tasks: human-confirmed work and key events; these are the agreed items to track.
- Backlog: ideas/actions awaiting confirmation, recorded by people or AI. Human entry alone does not make an item approved.

Explain the practical flow: add a suggestion to Backlog → human confirms scope/owner/date where known → move the approved item to Tasks with the same ID and links → update Status as work progresses → attach actual output chips in Deliverables. Do not leave an active duplicate in Backlog. Unknown owner/date stays TBD. A partially completed draft may still await approval in Backlog; approval and completion are different.

Introduce columns briefly: Task is the grouped item, Step the action, ID the stable taskId.stepId identifier, Description a short explanation/source link, Owner a verified person chip, Deadline the confirmed date, Status the uppercase colored dropdown, Deliverables the actual output links. Key meetings/milestones use the same grid. Multiple steps share a merged Task cell; multiple outputs use separate rows with the step cells merged. Do not sort individual rows across merged groups.

Status meanings: TODO = not started; DOING = in progress; PENDING = waiting/blocked, with reason in notes; DONE = completed with evidence; PARTIALLY DONE = some work/output exists but the item is unfinished. DONE is not automatically client acceptance. Colors follow the specified dropdown palette.

Offer simple examples: “把这条加入 Backlog”, “确认这两项由我负责”, “把我的任务改为 DOING”, “把这份产出关联到任务 2.1”. Examples are guidance, not authorization to mutate data. Keep full reusable guidance in the skill, not a third instructions tab; the existing short tab subtitles may explain their purpose.
