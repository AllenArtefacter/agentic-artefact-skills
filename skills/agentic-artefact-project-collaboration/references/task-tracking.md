# Project Timeline and Backlog

Use one native Google Sheets file, Project Timeline, with two tabs: Timeline and Backlog. Timeline holds the agreed schedule, confirmed tasks, execution status and outputs. Backlog holds unconfirmed proposals from people or agents. Do not create a separate Tasks tab or Work Plan. The legacy manifest key tasks_sheet_id identifies this workbook. STATUS summarizes it; substantive decisions belong in meeting notes and Meeting Briefs, with matching source links.

## Timeline

Follow [timeline.md](timeline.md): major phase rows → modules → tasks, A:I = Module, #, Task, Description, Owner, Start, End, Status, Dependency; calendar from J and Deliverables last. Keep stable text IDs in #, including promoted task.step IDs. Do not renumber existing items. Use one short description and preserve source meeting links; detailed evidence and approval history can live in cell notes. Timeline is the execution register, not a second summary requiring a separate Tasks tab.

## Backlog layout

Start at row 1 with these headers, without a title or subtitle:

Task | Step | ID | Description | Owner | Deadline | Status | Deliverables

Do not add an original-task-link column. Format IDs as text: 4.10 differs from 4.1. Description is one short sentence plus a source meeting/document link where available. Keep approval/evidence history in cell notes. Resolve columns from actual headers before editing a legacy tracker.

Use Arial 10, a bold white header on navy #0E2340, white task rows and body text #243247. Column widths in pixels: 150, 210, 85, 380, 155, 95, 135, 230. Freeze the header and first three columns. Use thin horizontal separators #E4E9EF and stronger task-group separators #AAB8C8, without heavy vertical gridlines. Header height 34px; fit wrapped body text, using 76px as a starting point rather than clipping content. Do not insert empty spacer rows between actual tasks.

Merge Task (A) only across contiguous steps of the same task. For a step with multiple output rows, merge identical B:G fields individually over those rows, leaving H Deliverables unmerged. A belongs to the whole task group and must not overlap step merges. Never merge differing owners, dates, status or descriptions. Blank templates contain no example records or record merges. Read merge metadata to inherit values only within known ranges; count distinct IDs, not physical output rows. Reorder whole groups; do not enable sorting/filtering that splits merged groups. Preserve current edits by rereading affected cells/merges immediately before mutation.

## Ownership, dates and status

Owner must be a verified internal team member, represented by a native person chip. Use TBD when unassigned. Never infer ownership from attendance, role, speaker number or roster order; client/vendor inputs belong in Description or Dependency. Meeting owners stay blank unless explicitly assigned. Match personal tasks using confirmed chip email/aliases.

Dates must reflect confirmed plans; an event date is not automatically a related task deadline. Leave unknown dates empty and record TBD in a cell note. Apply the [native chip convention](smart-chips.md) where supported, preserving usable date values and disclosing connector limitations.

Strict uppercase status dropdown options:

| Option | Meaning | Chip color |
|---|---|---|
| TODO | Not started | Gray #e6e6e6 |
| DOING | In progress | Blue #bfe1f6 |
| PENDING | Waiting/blocked; explain why | Yellow #ffe5a0 |
| DONE | Completed with evidence | Green #d4edbc |
| PARTIALLY DONE | Some work exists; unfinished | Purple #e6cff2 |

Approval and progress are different: DONE does not imply approval or client acceptance. Use native colored dropdown chips, not status-driven row/cell backgrounds. If the API cannot configure option colors, use supported native UI or disclose the fallback; colored text is not a colored dropdown chip.

Use pale blue #EEF5FC for meetings and pale pink #FFF0F6 for milestones across the full record width, including Deliverables. Ordinary tasks stay white. Prefix event labels with [MEETING] or [MILESTONE]; do not require a Type column. Preserve existing IDs when reclassifying a kickoff as a milestone and avoid duplicate event rows.

## Confirmation and promotion

Human entry alone does not validate a proposal. Meeting mentions, agent interpretations and existing drafts default to Backlog unless explicitly confirmed. A direct request to perform a concrete task validates that task. Confirm ambiguous IDs/names before moving anything; unknown owner/date may remain unknown.

On explicit approval, move only the approved Backlog steps into Timeline, retaining IDs, source links, owners, dates, status and deliverables. Map ID → #, Step → Task, Description → Description, Deadline → End when it is a planned end/deadline; retain the parent task context in the appropriate Module or cell note. Do not invent Start dates or collapse multiple confirmed steps into an untraceable summary. Record approval evidence when known. Verify the destination before removing source rows, preserving unapproved siblings and avoiding two active copies. Repaint the static calendar only for known dates under the same approved scope.

Maintain actual output chips and the Deliverables folder index together, following [folder-indexes.md](folder-indexes.md). TEST snapshots do not become the authority automatically.

## Migration and checks

Existing Tasks tabs and other people's Project Plan files remain unchanged unless migration/removal is explicitly authorized. Before removing a Tasks tab, reconcile every confirmed record into Timeline or another explicitly agreed retained source, including historical status, links and output evidence; report unresolved mappings. Do not lose confirmed work merely to achieve two tabs. Preserve existing workbook IDs and deep links where possible and update canonical links only after verified migration.

Verify tab names, actual headers, stable IDs, record coverage, owners, dates, status validation, native chips, merges and links. For Timeline also verify freeze, D–I grouping, static calendar and full-width fills. Test real multi-step/multi-output groups when present; never insert mock project content to demonstrate formatting.

## Explain to users

At first use, briefly explain: Timeline contains confirmed tasks and the delivery schedule; Backlog contains pending proposals from people or AI. Explain status changes and attaching outputs. Say in the user's language:

> 如果希望把 Backlog 中的任务放进 Timeline，可以直接和我说：“把 Backlog 中的 XX 加入 Timeline。”XX 可以是任务名称或 ID。

For older projects still using Tasks, adapt this wording to the actual confirmed register. Examples are guidance, not blanket mutation permission. Do not repeat the full explanation on every update.
