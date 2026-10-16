# Working practices

## Meetings

Create one record per meeting, identified by a stable meeting ID, date/time with timezone and source URL. Classify internal, client or catchup; audience is separate from meeting type. Include attendees, purpose, factual notes, confirmed decisions, proposed decisions, actions, open questions and source references/timestamps.

Do not treat an inferred action as assigned or an utterance as an approved scope change. Create proposed tasks when owner or due date is unknown. Deduplicate imports by source meeting/conference ID and artifact ID. Meet artifacts may be in the organizer's personal Drive; record a link or authorized copy, never assume they already live in the project root. Missing transcript means work from supplied notes, not invented meeting content.

## Plans and tasks

A working plan explains approach, phases and dependencies; live dates/status are in Project Control. Tasks tab owns task state, responsibility, dependencies and acceptance evidence. Deliverables tab owns output state and acceptance; actual content lives at its canonical file URL. A task detail document is optional and must not duplicate live status. The Control steward serializes table edits until a tested coordinating writer exists. The bundled reader cannot write these updates.

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
