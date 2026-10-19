# Meeting notes and running briefs

Use for internal, client and catchup meetings within an explicitly identified Artefact project. Apply the parent skill's project boundary, source handling and confirmation-before-change rules. This workflow is part of the project skill, not a separate installation.

## Storage

```text
02_Meetings/
  raw/                 Original recordings, transcripts, chat exports and source files
  note/
    YYYY-MM-DD Topic   One native Google Doc per meeting
    Meeting Briefs     One native Google Doc covering every recorded meeting
```

Keep raw originals unchanged and in their source formats; a native Doc is acceptable if that is the received source. Do not translate, correct or overwrite raw material. Store derived notes separately. For existing projects, obtain confirmation for the concrete migration; reuse IDs and move rather than duplicate. Preserve links and unrelated parents. Retry by recorded IDs, not names alone. Never move a user-provided reference document merely because it was supplied as a style example. If an original remains outside the project boundary, use only an explicitly authorized source or link and explain the exception; never follow its parent or other links automatically.

## One note per meeting

Use assets/document-templates/02_Meetings/meeting.md as a local authoring guide, not a blank file to publish. Shared notes are concise English Google Docs. Identify a meeting by stable meeting ID plus actual event/source identity; multiple summaries or transcripts of one event are not additional meetings.

Metadata: title, meeting ID, date/time/timezone, type, review status, confirmed attendees (@person chips where supported), and original source links in raw. Unknown details are TBD. A project roster or invitation list is not attendance evidence; never infer speaker identity from a role or name similarity.

### Native meeting header

Retain the existing meeting header when simplifying or translating notes: bold meeting title, native date chip, then native person chips on the next line. For new notes, use the same compact layout before metadata and Quick notes. Preserve the title wording and existing chip identities unless the user asks to change them. Use the source date and verified emails; never turn chips into plain text or a screenshot merely to preserve appearance.

Label people as Invitees or Attendees according to the evidence. A reference used only for styling supplies no participants or dates for a different meeting. If the user explicitly requests its participant header while event identity is uncertain, label it as the reference invitee list and mark attendance unconfirmed. Do not substitute project members for meeting participants. When native chips are unavailable, disclose the limitation and use labeled text; do not claim text beginning with @ is a chip. Verify native date/person elements after publishing.

Order the document as:
1. Quick notes: Topics, Requirements, Difficulties, Options, Conclusions, Follow-up. Keep each short; use Not discussed or TBD instead of inventing content.
2. Full notes: only material discussion and evidence, with timestamps/sections linking to the raw source. Distinguish requests, proposals, approved decisions and unresolved questions.
3. Actions: action, confirmed owner or TBD, due date or TBD, task ID/link and source. Do not silently assign group actions or infer completion.
4. Conflicts / open questions: link related notes and the running brief's conflict ID.

Quick notes → Full notes → source links follows the useful structure of meeting-assistant output, but omits surveys, tips and unsupported automatic conclusions. Separate tabs are optional, not required. Do not copy example content, participants or facts into a new meeting.

## Meeting Briefs: project-wide chronology

Maintain exactly one canonical Meeting Briefs document in note. For every meeting, add or update an entry keyed by meeting ID, ordered by date. Include date, note link, raw link, review status, and all six fields: Topics, Requirements, Difficulties, Options, Conclusions, Follow-up. Corrections update the same entry; they do not create a second meeting. Do not erase earlier meetings when adding new ones. Link task IDs rather than maintaining a separate live task-status table.

For an existing project, enumerate scoped meeting records to establish coverage. If some meetings are unavailable, label missing coverage; do not claim complete history. Unknown dates go in an undated section, not an invented position in the timeline.

Keep Meeting Briefs scannable: one compact block per meeting, about 100–150 English words, with each of the six fields limited to one short sentence. Use inline bold labels rather than six section headings. Link details through file chips; do not duplicate task tables or source analysis. Show only concise conflict IDs, the opposing claims, status and clarification owner here; keep detailed evidence and resolution history in the individual note, linked from the brief. Preserve uncertainty and material commitments when shortening.

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

Prepare the concrete note, brief entry and any conflict updates for user confirmation; an explicit request to publish those prepared changes is sufficient. After approval: preserve/move the raw source as authorized, publish the individual note, then update Meeting Briefs and links. Update Tasks/Decisions/STATUS only for the approved changes. Use current revision guards for existing Docs. Preserve people chips, tables, existing content and links. Verify file parents, raw links, the meeting entry and conflict status. If only part succeeds, report it and retry the missing step without duplication. No background listener is implied.
