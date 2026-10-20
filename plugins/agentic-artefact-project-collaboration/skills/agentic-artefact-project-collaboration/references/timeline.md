# Timeline in Project Timeline

Read for creating, reviewing or updating a project timeline. Follow the project boundary and write-approval rules in SKILL.md. A timeline request does not authorize Calendar edits, invitations, scope expansion or publication to a client.

## One workbook, two views

Use one native Google Sheets file **Project Timeline** in Management, with **Timeline** and **Backlog**. Timeline owns the agreed schedule, confirmed execution status and outputs; Backlog owns unvalidated work. STATUS summarizes these records. Calendar owns scheduled event times. Resolve actual file/tab IDs before writing; a renamed file keeps its ID. Preserve existing tabs and legacy schemas unless migration is explicitly approved.

Use `assets/project-plan/Project Timeline Template.xlsx` for a blank local workbook and `assets/project-plan-layout.json` for its schema. The XLSX is a portable layout, not proof of Google-native chips. Convert to native Sheets through the current connected tools when authorized, then verify static calendar fills, validation, merges and chips. Do not publish a raw XLSX as if it were already native Sheets. Keep reusable guidance and template masters in the skill.

### Approved layout

Use the compact Predictive Buy-style layout. Start immediately with two header rows: week groups in row 1, column headers and date values in row 2. No large title, subtitle, introduction, legend or setup block. Keep necessary assumptions concise in the affected row's Description; keep detailed usage guidance in the skill.

Hierarchy: **major phase (full-width separator row) → Module → Task**. Insert phase rows only for actual project phases. Use a continuous dark navy fill across the entire used width, including the calendar and Deliverables. Merge the left and right portions separately at the freeze boundary. Merge Module only over real contiguous task groups; keep Task and record IDs distinct.

Timeline columns, in order:

| Columns | Contents |
|---|---|
| A | Module |
| B | # — stable work-package/event ID |
| C | Task |
| D | Description (not Comment) |
| E | Owner — internal accountable owner, not participant list |
| F–G | Start, End — typed dates |
| H | Status — uppercase dropdown |
| I | Dependency |
| J onward | Week groups and daily calendar |
| Last used column | Deliverables — native file chips when actual files exist |

- Group **D–I**, collapsed by default; freeze **A–I** and the top two rows. Never merge across the frozen-column boundary. Verify grouping/collapse and freezing after inserting or moving columns; column letters must match the final layout.
- Do not create Timeline `Task IDs`, `Type` or `Participants` columns, including hidden helper columns. Retain stable IDs in `#`. Preserve task associations through existing IDs, links or local manifest mappings; do not renumber existing tasks. Backlog keeps its own schema; promoted IDs remain stable in Timeline’s # column.
- Meeting rows have blank Owner. Other rows use a confirmed internal owner or TBD; participation alone is not an assignment. Event rows may use their event ID/name to distinguish meetings and milestones without a Type column.
- **Weeks are natural calendar weeks, Monday through Sunday**, in the project timezone. Align the first displayed week to the Monday containing the project start; a Wednesday start remains in that calendar week. In a working-day view, show Monday–Friday within each week; include weekends when relevant work/events require them. Holidays stay in their original date slots and do not shift week boundaries. Label populated week groups with their Monday start date; W1/W2 may remain as display-order labels only, never rolling seven-day periods from kickoff. Preserve actual task dates when changing week grouping. Across months/years, show enough date/year information to avoid ambiguity.
- **Calendar cells contain no formulas or formula-based conditional formatting.** Use direct fills for task spans and literal meeting/milestone markers. Date headers are literal typed dates, with concise day-number display and week labels showing the week start. A change to Start/End does not automatically redraw the calendar: update the affected static fills/markers in the same authorized edit.
- Major phases use navy `#0E2340`, meetings pale blue `#EEF5FC`, milestones pale pink `#FFF0F6`. These fills span **A through the final Deliverables column**, including Dependency and the entire calendar, not just the left table. Ordinary task rows remain white outside their grey `#D9D9D9` schedule bars.
- Border hierarchy: thick phase separators, medium week/module boundaries, thin light-grey daily/task grid. Reapply after column moves and horizon changes. Use compact, readable row heights and widths; avoid clipping chips, dates and descriptions.
- Status options: TODO, DOING, PENDING, DONE, PARTIALLY DONE. Prefer native colored dropdown chips. An XLSX dropdown or colored text does not prove native chip styling; verify after conversion and disclose any limitation.
- Blank template: headers, empty formatted record slots, empty date slots and dropdown choices only. No people, project-specific names, actual dates, sample tasks, phase content or mock bars. The supplied calendar reserves four five-day workweeks (20 empty date slots); this is capacity, not a project commitment or holiday calendar. Confirm the actual calendar and extend it when needed.
- Planned span is not effort or completion. Keep unknown dates blank; do not infer today or zero duration. Split intermittent work into agreed segments rather than implying continuous effort. Respect each person's availability cutoff.
- Backlog starts directly with its own header row, without titles/subtitles. Follow [task-tracking.md](task-tracking.md) for their columns, approval rules and merges.

### Existing files and TEST copies

Use the confirmed canonical file ID, not the default name, to identify a live workbook. Never rename or modify another person's Project Plan merely to match this convention. When the user requests a separate test, create **Project Timeline — TEST** in the authorized project folder and keep original files untouched. Include existing Timeline/Backlog only within the approved scope; preserve IDs, owner/status values, original meeting/deliverable links and person/file chips. Do not add an original-task-link column when copying. A test is a snapshot, not automatic synchronization or a replacement authority. Do not promote Backlog merely because it appears on the timeline.

## Creating a timeline: resolve these questions

Read existing Project, STATUS, Project Timeline and relevant agreements first. Reuse verified answers; ask only for consequential gaps, in a small grouped question. Separate plan drafting from approval to publish it.

| Decision | What to establish | If unknown |
|---|---|---|
| Destination and audience | Authorized project root, existing Project Timeline ID, internal working plan or client-facing plan | Ask for the destination; do not create a second plan or change sharing |
| Scope and breakdown | Agreed outcomes, modules/phases, work packages, actual deliverables, excluded work | Draft only evidence-backed structure; candidate work stays Backlog |
| Time anchor and horizon | Confirmed start, target end or duration; daily/weekly display; project timezone (weeks always Monday–Sunday) | Leave missing dates blank; a duration estimate is not a promised deadline |
| Calendar and effort | Workweek, holidays, part-time availability, parallel work, elapsed span versus working effort | Use a disclosed draft assumption only; never silently assume all people are full-time |
| Fixed commitments | Client reviews, acceptance gates, contractual dates, scheduled events; which dates are immovable | Mark proposed dates as unconfirmed, outside the agreed live schedule |
| Ownership and dependencies | Internal accountable owner, client/vendor inputs, preceding IDs and dependency meaning | Keep owner TBD; external contributor is a dependency, not an internal owner |
| Task mapping and planning level | Which confirmed tasks map to each package; detail appropriate for timeline; unapproved Backlog candidates | Do not turn every small step into a timeline row or silently promote Backlog |
| Approval and baseline | Who validates scope/dates, whether an approved baseline already exists, what change history is needed | Publish only the approved portion; retain unresolved items in Backlog/draft |

Offer a compact proposal: scope/work-package outline, major dates, proposed checkpoints and meetings, dependencies, unresolved assumptions and the exact file/tab changes. Ask for confirmation once the proposal is reviewable. A user-approved plan or previously confirmed answers need not be approved again. A request for an empty template does not require project facts and does not authorize a live schedule.

If the user requests a recommended schedule, derive a local draft using explicitly labeled assumptions. Do not write estimates into the confirmed Timeline as commitments before validation. Creating a plan does not send calendar invitations or notify participants.

## Propose checkpoints and meetings proactively

When asked to create a project timeline, propose suitable checkpoints and meetings as part of the first draft, even if the user supplied only tasks and dates. Derive them from phase outcomes, decisions needed, dependencies, delivery risks and team availability. Reuse existing booked events and agreed gates before proposing additions; do not insert a fixed meeting cadence or every event below by default.

- **Checkpoint:** a measurable readiness or decision gate, such as data readiness, agreed requirements, evaluation results, handoff readiness or delivery acceptance. State what must be available and what decision or next step it enables. A checkpoint may be asynchronous; it does not automatically require a meeting.
- **Meeting:** a conversation needed to gather information, resolve a decision or coordinate people, such as kickoff, business interviews, solution review, blocker resolution, handoff or final presentation. State its purpose and expected output. A held meeting does not prove its checkpoint passed.
- Suggest cadence only when justified by project duration, uncertainty or coordination needs. Combine a meeting with its checkpoint in one linked event when appropriate rather than duplicating it. Schedule handoff/review before a person's availability ends and allow preparation/follow-up time.

Present a compact proposal alongside the work plan:

| Proposed event | Meeting or checkpoint | Suggested date/window | Purpose / expected decision or evidence | Related task/dependency |
|---|---|---|---|---|

Use relative timing when dates are unknown (for example, after interviews and before solution design). Label estimates and tentative dates as proposed; do not describe them as booked or agreed. Suggest required participant roles only when useful and distinguish them from confirmed attendees; do not add a Participants column or assign meeting owners. Keep meeting Owner blank. Checkpoint owners must be confirmed internal members or TBD.

For a local draft or an explicitly requested TEST proposal, include proposed events visibly marked [PROPOSED] with concise assumptions. In a live agreed Timeline, put unconfirmed events in Backlog until approved; approval moves them into Timeline with stable IDs and the specified meeting/milestone colors. Status is progress, not proposal approval. Ask the user to confirm or adjust the proposed events together with the rest of the draft, rather than making them invent the meeting plan from scratch. A request for a blank template leaves all event rows empty. Calendar event creation and invitations remain a separate explicit authorization.

## Updating: classify the request before editing

Cases can overlap. Prepare one combined change proposal, including affected IDs, old/new dates or values, reason/source and downstream impact. Ask only for answers not already established. Report no-op requests without rewriting the sheet.

| Case and suitable scenario | Confirm or establish | Permitted change and boundary |
|---|---|---|
| **Progress / actuals** — weekly update, work started/completed, output delivered | Exact ID, evidence, status; actual date versus planned date; completion versus acceptance | Update Timeline status/output evidence and reconcile the linked package. Preserve planned dates and approved baseline. Partial child completion does not make the package DONE |
| **Local reschedule** — one task slips, starts early or waits for input | Which ID, new start/end or duration, reason; calendar or working days; whether effort or scope changed | Show dependent tasks and milestones affected. Change approved rows only; propose dependent changes rather than shifting them automatically |
| **Whole-plan shift** — kickoff moves, project pauses/restarts | Shifted range, anchor, delta versus new dates, calendar versus working days, fixed dates, already-completed work and external commitments | Preserve actual history and fixed commitments. Moving the display window alone is not rescheduling; move task dates only with explicit plan approval |
| **Scope / work breakdown** — new requirement, canceled work, task split/merge | Addition/removal and acceptance criteria, approval state, owner, IDs, effort and schedule implications | Unconfirmed items go to Backlog. Preserve traceability and old IDs; split/merge with mapping. Do not silently delete work or renumber unrelated tasks |
| **Capacity / ownership / dependencies** — unavailable colleague, client data delay, changed vendor handoff | Internal owner acceptance, capacity/availability, predecessor and what it gates, lag or parallelism, impacted dates | Change agreed ownership/dependencies; estimate schedule effects separately. A dependency ID is not an automatic date-offset formula or authorization to move dates |
| **Meeting / milestone change** — review, kickoff, sign-off or go-live changes | Exact event, planned versus booked date, timezone, Calendar source, acceptance criteria; whether invitations should change | Update the plan within authorization. Calendar changes/invitations need explicit authorization. Meeting held is not deliverable accepted or project complete |
| **Rolling detail / view change** — detail next two weeks, extend visible horizon, regroup modules | Display-only versus schedule change, horizon/granularity, required detail and links to existing packages | Extend formatting and static calendar cells or add confirmed breakdown without changing existing dates/IDs. Keep distant estimates and new proposals explicit |
| **Rebaseline / recovery plan** — approved scope or schedule materially changes | Original approved baseline, reason, proposed new baseline/version, validator, fixed commitments and impacted outputs | Preserve original commitments in an authorized snapshot or dated baseline fields before replacement. Do not label a draft as approved or erase slippage/history |
| **Correction / reconciliation** — wrong date/ID, imported plan, Timeline/Calendar mismatch | Correct source, affected ranges, source-of-truth for each field, expected format; most recent edit and any conflict | Fix only confirmed errors. Surface competing facts; newer is not automatically more authoritative. Correcting one view must not silently overwrite the owning source |

Do not add baseline columns, history tabs or archival copies to every project by default. For a requested rebaseline, agree the preservation mechanism and location first. Store small approved change histories in existing Notes/cell notes with evidence and prior values; do not replace actual history with a newly generated plan.

## Read, propose, write, verify

1. Resolve Project Timeline and actual sheet IDs within the authorized project. Read the changed work packages, linked Timeline/Backlog groups, dates, dependencies, merges and relevant Calendar/meeting evidence. Follow only authorized source links.
2. Distinguish planned span, actual progress, client acceptance and approval. Dependency cycles, missing IDs and ambiguous mappings are gaps to resolve; do not invent a critical path from incomplete data. External blockers stay visible.
3. Present a concise before/after proposal for the requested changes and any dependent recommendations. Preserve completed work, fixed milestones, outputs and unrelated edits. Obtain missing confirmation under the parent skill; existing explicit approval is sufficient for the same concrete changes.
4. Re-read affected ranges immediately before writing, check for concurrent changes, then use a guarded write if available. If no revision/conditional write exists, serialize through the plan steward and disclose that read-compare is not an atomic lock. On conflict, reconcile at most twice, then retain the proposal without overwriting.
5. Update by IDs, preserving merges, chips, validations and links; update static schedule fills when dates change. Work-package status is a confirmed summary, not an unweighted average of child statuses. With mixed child progress, propose the appropriate summary; never infer percent completion or acceptance. The current template links by IDs but does not automatically synchronize status or dates between tabs.
6. Verify the changed data and rendered schedule: row coverage, unique record IDs, parent/task references, start ≤ end, planned dates unchanged on status-only edits, markers, full-width phase/event fills, border hierarchy, D–I collapsed group, A–I freeze, no calendar formulas, final-column Deliverables, holiday rules actually configured, and no accidental inclusion of Backlog proposals. Distinguish linked event representations from duplicate execution records.
7. Summarize the change, impacted milestones, outstanding questions and canonical Project Timeline link. Propose a STATUS update only when project-level facts change and publish it only within the authorized scope. Never claim client notification or Calendar synchronization without completing the authorized action.

## Explain usage briefly

Introduce Project Timeline as one file: Timeline holds the agreed schedule, confirmed execution status and outputs, Backlog holds pending proposals from people or agents. Examples: “Create a timeline for this project”, “Move WP-… by three working days and show the impact first”, “Update progress without moving planned dates”, “Show the next four weeks without rescheduling”, and “把 Backlog 中的 XX 加入 Timeline”. Resolve IDs and unknown facts; examples are not permission to mutate records.
