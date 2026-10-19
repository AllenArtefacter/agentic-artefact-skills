# Project metadata

Every Project document starts with these six fields, in this order. Use English for shared project documents. Preserve existing file IDs and unrelated content when updating.

| Field | Required content |
|---|---|
| Project name | Confirmed project name |
| Team | A flat inline row of Google Docs @person chips resolved from confirmed emails; no job titles or role labels |
| Start date | Confirmed project start date as a native date chip; otherwise TBD |
| Status | Current confirmed project phase; use TBD if unknown, or label the last confirmed phase and its evidence date |
| Last updated | Date of the actual Project edit as a native date chip (project timezone); include time and timezone if useful |
| Client contacts | @person chips from confirmed client emails, with roles if known; otherwise explicitly TBD |

Unknown values must say TBD (待补充), never be blank or inferred. A kickoff date, first meeting date or folder creation date is not automatically the project start date. Editing metadata does not establish new business progress. Last updated changes only after a real edit, not on reads. STATUS remains the detailed progress summary; Project status is a concise phase.

For native Google Docs, use the connector's supported person-chip insertion with the verified email and read back person elements to verify. Literal @email text or a mailto link is not a native person chip. Local Markdown drafts use @email placeholders; convert these to chips on publication. If chip creation is unsupported, retain @email text and explicitly report the limitation. Never guess client emails from names. Known names without emails may be retained with email: TBD.

People chips do not grant access or authorize notifications/invitations. Never change sharing or send messages merely because a person is listed. Preserve existing chips and roster IDs. Metadata is the identity summary; keep detailed responsibilities in the roster without conflicting duplicates.

Use native date chips for known dates in Project, including evidence dates. Preserve time/timezone and tentative-date qualifiers. Do not invent a timestamp precision or replace TBD with today. Verify dateElement values after publication. Local draft dates can use YYYY-MM-DD placeholders.
