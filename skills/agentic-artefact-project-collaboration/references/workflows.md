# Working practices

## Meetings

Follow [meeting-notes.md](meeting-notes.md): raw originals → linked individual notes → running Meeting Briefs with six-field summaries and cross-meeting conflict tracking. Keep source evidence and decisions distinct; confirm writes before publishing.

## Plans and tasks

Use [task-tracking.md](task-tracking.md): Tasks contains human-validated work and Backlog contains AI suggestions. Do not create Work Plan. Keep actual outputs at their canonical URLs and link them in Deliverables cells. A task detail document is optional and does not duplicate live status. Serialize accepted edits and verify them; the bundled reader cannot write cloud updates.

Calendar owns real meeting schedule and attendance; notes own discussion and action evidence. Sprint briefs describe goals/review/retro and link tasks via sprint_id. Workstream folders persist across sprints. Materials are inputs; workstream files contain analysis; managed output content belongs in Deliverables. See [workspace-model.md](workspace-model.md) and the skill folder guides before placing new work.

## Role handoffs

| Role | Typical evidence handed to the next person |
|---|---|
| Consultant | Scope, stakeholder needs, success criteria, decisions and client-ready narrative |
| DA | Metric definitions, queries, data caveats, analysis and reproducible results |
| DS | Hypotheses, baselines, experiment settings, evaluation and model limitations |
| DE | Contracts, pipelines, data quality, environment/version and operations evidence |

Roles may overlap. Record dependencies and accepted inputs instead of enforcing a fixed sequence. A DS result depending on a changed metric becomes potentially stale until reviewed, not automatically invalid.

## Deliverables and reports

Each artifact records linked tasks, owner, reviewer, version, source inputs, validation, status and audience. A weekly report distinguishes completed and accepted work, work in progress, blockers, decisions needed and next period commitments. Cite source links and as-of time. Do not turn local execution success into deployment success or client acceptance.

A release to a customer uses the approved external location and authorized content. Internal notes, credentials and unrestricted event logs do not travel with the release. Existing user authorization applies; do not invent additional approval ceremonies for routine internal work.
