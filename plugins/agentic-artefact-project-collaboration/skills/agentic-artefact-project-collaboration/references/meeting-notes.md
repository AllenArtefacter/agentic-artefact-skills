# Meeting notes and running briefs

Use for internal, client and catchup meetings within an explicitly identified Artefact project. Apply the parent skill's project boundary, source handling and confirmation-before-change rules. This workflow is part of the project skill, not a separate installation.

## Storage

```text
02_Meetings/
  raw/                 Original recordings, transcripts, chat exports and source files
  note/
    YYYY-MM-DD Topic   One native Google Doc per meeting
  Meeting Briefs       One native Google Doc covering every recorded meeting
```

Keep raw originals unchanged and in their source formats; a native Doc is acceptable if that is the received source. Do not translate, correct or overwrite raw material. Store derived notes separately. For existing projects, obtain confirmation for the concrete migration; reuse IDs and move rather than duplicate. Preserve links and unrelated parents. Retry by recorded IDs, not names alone. Never move a user-provided reference document merely because it was supplied as a style example. If an original remains outside the project boundary, use only an explicitly authorized source or link and explain the exception; never follow its parent or other links automatically.

## One note per meeting

Use assets/document-templates/02_Meetings/meeting.md as a local authoring guide, not a blank file to publish. Shared notes are concise native Google Docs. Follow the requested language; Chinese is appropriate for Chinese meetings when requested. Local review drafts use document format (for example Word), not HTML, unless requested. Identify a meeting by stable meeting ID plus actual event/source identity; multiple summaries or transcripts of one event are not additional meetings.

Metadata: title, meeting ID, date/time/timezone, type, review status, confirmed attendees (@person chips where supported), and original source links in raw. Unknown details are TBD. A project roster or invitation list is not attendance evidence; never infer speaker identity from a role or name similarity.

### Native meeting header

Retain the existing meeting header when simplifying or translating notes: bold meeting title, native date chip, then native person chips on the next line. For new notes, use the same compact layout before metadata and Core arguments. Preserve the title wording and existing chip identities unless the user asks to change them. Use the source date and verified emails; never turn chips into plain text or a screenshot merely to preserve appearance.

Label people as Invitees or Attendees according to the evidence. A reference used only for styling supplies no participants or dates for a different meeting. If the user explicitly requests its participant header while event identity is uncertain, label it as the reference invitee list and mark attendance unconfirmed. Do not substitute project members for meeting participants. When native chips are unavailable, disclose the limitation and use labeled text; do not claim text beginning with @ is a chip. Verify native date/person elements after publishing.

Order the document as:
1. **Core arguments:** lead with the few central positions and implications supported by the meeting. Attribute contested positions; a synthesis is not automatically a confirmed agreement.
2. **Requirements and viewpoints:** identify stakeholders first, then topics. Use a compact Topic / Stakeholder viewpoints table to capture each party's core view and concern. Separate requests, proposals, confirmations and unknowns. Use confirmed speaker mappings; do not infer speakers from invitation lists. Summarize by stakeholder or topic only when it adds information, rather than duplicating the matrix.
3. **Meeting agreements:** preserve material agreements, decision IDs, evidence/timestamps and confirmation scope. Do not promote opinions into decisions when shortening.
4. **Actions and task links:** use a native table with Proposed task / Proposed owner / Related task IDs or links / Expected output or dependencies. Suggested owners must be internal team members and explicitly marked proposed; use TBD when unknown. Client contributors are dependencies, not internal task owners. Preserve already-confirmed ownership as confirmed. Suggestions do not change task assignments; keep unvalidated actions in Backlog.
5. **Items to verify:** place unresolved requirements, evidence gaps, scope, ownership, dates and cross-meeting conflicts at the end. Retain conflict IDs and source links; remove resolved speaker ambiguity once the user confirms a mapping.

Keep each point short and avoid chronological transcript retelling or repeating the same content in an executive summary, matrix and full notes. Bold the key claim or label, not whole paragraphs. Link original sources and the running brief with native file chips. Templates contain structure and placeholders only, never project-specific names, assignments or mock findings.

### Actionable drivers in requirements discussions

When the meeting raises business levers or actions, treat **Actionable drivers** as its own topic, alongside accuracy, gap explanation and scenario planning where relevant. Do not force these forecasting topics into unrelated meetings.

- Accuracy asks what will happen; gap explanation asks why a gap exists; actionable drivers ask what the business can change; scenario planning compares outcomes under candidate actions.
- Record which stakeholder wants which decision or action, and their concern. Distinguish controllable actions, intermediate outcomes and external conditions. A predictive feature or model contribution is not automatically an actionable lever.
- Capture the decision owner, execution level, timing, feasible range, cost/constraints and evidence of impact only where discussed; otherwise mark the material questions for review. Do not invent feasible actions or causal effects.
- Keep predictive association, what-if output and causal incremental impact distinct. Feature importance alone does not establish that changing the feature will change sales.
- For an assessment, a candidate-driver inventory with evidence, data needs and limitations can be a proposed output. It does not commit the team to building a simulator or quantifying causal uplift. Label new analyst suggestions separately from meeting requests or agreements.
- Reflect this topic in the same meeting's brief and verification items. Updating minutes does not authorize new task assignments or expanded project scope.

## Meeting Briefs: project-wide chronology

Maintain exactly one canonical Meeting Briefs document directly in 02_Meetings, alongside raw/ and note/, never inside note/. For every meeting, add or update an entry keyed by meeting ID, ordered by date. Include date, note link, raw link, review status, and all six fields: Topics, Requirements, Difficulties, Options, Conclusions, Follow-up. Corrections update the same entry; they do not create a second meeting. Do not erase earlier meetings when adding new ones. Link task IDs rather than maintaining a separate live task-status table.

For an existing project, enumerate scoped meeting records to establish coverage. If some meetings are unavailable, label missing coverage; do not claim complete history. Unknown dates go in an undated section, not an invented position in the timeline.

Keep Meeting Briefs scannable: one compact block per meeting, about 100–150 words in English or a similarly compact block in the requested language, with each of the six fields limited to one short sentence. Use inline bold labels rather than six section headings. Link details through file chips; do not duplicate task tables or source analysis. Show only concise conflict IDs, the opposing claims, status and clarification owner here; keep detailed evidence and resolution history in the individual note, linked from the brief. Preserve uncertainty and material commitments when shortening.

### Meeting Briefs card layout

Render each meeting as its own native Google Docs single-column table, separated from other cards by a blank paragraph. Use assets/document-templates/02_Meetings/meeting-briefs.md as the content guide. This card layout applies to Meeting Briefs; individual full notes keep their own structure.

- Header row: bold meeting title, then native date chip, review status and stable meeting ID. Add person chips only when useful and supported by confirmed meeting evidence; never copy a project roster or template invitees.
- Summary row: a short Core argument first, then the six inline bold labels, one short sentence each, with normal-weight values. Include distinct material topics such as Actionable drivers when supported; do not repeat the full notes.
- Optional open-check row: pale yellow; one concise line per conflict ID with status and owner/TBD. Omit the row when there are no open checks. Keep full evidence and resolution history in the linked individual note.
- Sources row: native file chips for the note and raw source, plus relevant tasks or conflict detail. Add a reference only when actually used; retain useful deep links as descriptive hyperlinks.

Default appearance: light-blue header (#E6F0FA), white summary/source rows, pale-yellow checks (#FFFAED), 0.5 pt light-gray-blue borders (#D1DBE6), 12 pt horizontal and 7 pt vertical cell padding. Use a bold 14 pt card title and 10 pt body, 110% line spacing and 3 pt paragraph spacing. Preserve chips as native editable elements; do not render the card as an image. Avoid fixed row heights that clip text.

When using the Docs API, insert the table, read its actual cell paragraph indexes, then fill cells from highest index to lowest. Style returned text ranges, not structural boundaries. Use revision guards; verify native table rows, chip destinations and formatting after publishing. Locate updates by meeting ID and edit the existing card rather than appending duplicates or rebuilding the entire document. Inspect a rendered preview when available before claiming visual fidelity. If table styling is unavailable, disclose the limitation and keep a compact editable block.

## Cross-meeting conflicts

Before publishing new notes, compare relevant earlier briefs and source notes for changes in requirements, scope, definitions, targets, dates, ownership, methods, decisions and completion claims. Search only within the authorized project.

Record detailed conflicts in the relevant individual note and link a one-line summary from Meeting Briefs. The detailed record contains:
- Stable conflict ID and topic.
- Meeting A and B IDs/dates, both source links and precise statements or timestamps.
- Impact, status (unverified / confirmed conflict / resolved / superseded), clarification owner or TBD and question to resolve.
- Resolution evidence, date and affected records once explicitly confirmed.

Do not treat a later statement as an automatic override. An approved scope change is recorded as superseding an earlier decision; preserve the earlier record and link the resolution. Distinguish real cross-meeting conflicts from transcript/summary discrepancies, different definitions, invitation-versus-attendance differences and legitimate updates. If the identity of a reference meeting is unclear, flag a source discrepancy and do not count it as another meeting. With only one verified meeting, say cross-meeting comparison is not yet possible.

Automatic summaries are unverified evidence. When summary and transcript disagree, retain the conflict for human review; do not change Project, mark tasks done, or promise new scope without confirmation. Contacting participants or sending notes requires explicit authorization.

## File links

In shared Google Docs, render source files, notes, Meeting Briefs and task documents as native file smart chips, not bare URLs. Use insertRichLink with the verified resource URL and confirm richLink elements on readback. Preserve existing chips. Keep useful tab/section deep links separately as descriptive hyperlinks alongside the file chip. For unsupported resources or connectors, use descriptive linked text and disclose the limitation; never claim an ordinary hyperlink is a chip.

## Publish and verify

Prepare the concrete note, brief entry and any conflict updates for user confirmation; an explicit request to publish those prepared changes is sufficient. After approval: preserve/move the raw source as authorized, publish the individual note, then update Meeting Briefs and links. Route unconfirmed actions recorded by people or AI to Backlog; promote only human-validated actions to Timeline under [task-tracking.md](task-tracking.md). Update STATUS only for approved project-level changes; do not create or maintain a separate Decisions document. Use current revision guards for existing Docs. Preserve people chips, tables, existing content and links. Verify file parents, raw links, the meeting entry and conflict status. If only part succeeds, report it and retry the missing step without duplication. No background listener is implied.

## Decision recording

For each substantive decision, record a stable DEC-... ID, concise statement, source/timestamp, and confirmation scope in the individual meeting note. Summarize the same decision IDs under Conclusions / Decisions in that meeting's brief card. Distinguish proposals, internal directions, pending team review and client approval. Link affected task IDs where known; do not create action assignments merely because a decision exists. Preserve conflicts and superseded decisions with their resolution history. Do not create a separate Decisions document, tab or index. For legacy records, preserve unique decisions and their source/history in the relevant meeting note and Meeting Briefs before any authorized removal; never invent a meeting for a decision made elsewhere. Record non-meeting decisions as clearly dated source-linked updates in Meeting Briefs.
