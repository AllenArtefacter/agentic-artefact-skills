# Template catalog

All templates stay inside the skill. They define headings, fields, empty table headers, file slots and formatting; they contain no example tasks, people, dates, clients, decisions or output claims. `{{FIELD}}` denotes a value to resolve from project evidence, never literal published content. Optional documents/sections are instantiated only for real records. Required unknown metadata becomes TBD; omit unused optional sections. For empty indexes publish a factual empty state after listing the folder, never a dummy table row.

- `assets/folder-layout.json`: default folder/file slots; respect an existing project's names and IDs.
- `assets/project-template/Project.md` and `STATUS.md`: core document structure.
- `assets/document-templates/project-index.md`: native project navigation.
- `assets/document-templates/materials-index.md` and `deliverables-index.md`: folder inventory headers without sample rows.
- `assets/project-plan-layout.json` and `assets/project-plan/Project Timeline Template.xlsx`: the two-tab Project Timeline schema and blank portable workbook. Follow [timeline.md](timeline.md) for setup questions, timeline updates and native conversion checks.
- `assets/tasks-layout.json` and header-only CSVs in assets/control-seed are legacy layouts for existing trackers only; do not seed a new Project Timeline from them.
- `assets/document-templates/02_Meetings/`: note and running brief structures. Render each brief as the native four-row card described in meeting-notes.md; template headings are structural slots, not instructions to publish nested headings. Preserve date/person/file chips and bold labels.
- Remaining document-templates subfolders: optional workstream, task detail, deliverable, decision/risk, sprint and report structures; historical directory numbering does not create project folders.

Use folder guides and task/meeting references for workflow, permissions, merges and verification; keep those explanations out of content templates. These are source templates for native Google authoring, not already-installed native Docs/Sheets templates. The local initializer may render project-specific drafts in code; cloud creation must map the same fields, fill only verified facts and verify native output. Do not upload empty Markdown templates or layout JSON to the team folder.

Apply the project-wide [native chip convention](smart-chips.md) to people, dates/times and supported file references.
