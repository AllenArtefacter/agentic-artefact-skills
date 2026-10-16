# Adapter contract and synchronization protocol

Future incremental synchronization and write-adapter specification. The current package includes a read-only recursive-inventory reader; it does not implement the Changes API, write/outbox recovery, semantic event publication or background watcher described below. See google-reader.md for actual commands.

## Required capabilities

`connect`: obtain personal identity through configured OAuth without exposing secrets.
`inspect`: validate root MIME type, drive ID, permissions and manifest.
`inventory`: recursively enumerate accessible descendants, all pages; stable file IDs, parent IDs, MIME type, version/modifiedTime and trash state.
`sync`: write durable local inbox entries and return relevant changed file IDs.
`read`: fetch current content with revision/version and source links.
`patch_doc`: guarded Docs write; never claim Sheets or ordinary files share its concurrency contract.
`publish_event`: append separate immutable event object with a stable operation/event ID.
`ack`: record handled inbox items only after the agent has incorporated them.

These are interface names, not runnable CLI commands. Implement via Google SDK, gws or an available MCP connector. Verify endpoint schema and installed tool version before constructing calls.

## Local state

Key state by authenticated principal + project root ID + adapter schema version. Persist observed cursor, parent graph, file metadata, pending inbox, acknowledgements and mutation outbox in a local transactional store. OAuth credentials belong in secure credential storage, not this store. Account changes must not reuse another user's cache.

## Initial scan and deltas

1. Resolve folderId and its Shared Drive driveId. Fetch a start page token BEFORE initial inventory so scan-time edits can be replayed.
2. Recursively list project descendants with pagination, excluding trashed objects. Do not follow shortcuts outside root implicitly. Record incomplete/denied scans and do not claim completeness.
3. Replay changes from the saved token, with Shared Drive flags. Apply every page to a staging state; atomically persist inbox records and the next cursor only after durable processing. At the end use newStartPageToken for the next pass.
4. Changes feeds are drive/user scoped, not recursive project-folder subscriptions. Filter using the cached parent graph plus current metadata. Folder moves require subtree reconciliation: moving a folder changes membership of descendants even without per-child changes. Moving into the project requires subtree inventory; moving out removes all affected cached membership.
5. For removed/inaccessible entries use prior membership to invalidate local content and mark unavailable; do not call every removal a deletion. Revalidate permissions before resurfacing cached contents. A revoked root stops processing and makes cached content unavailable to the agent.
6. Deduplicate by provider change identity where available, otherwise file ID + version/state fingerprint. Distinguish same-file new versions from retries. Updates of identical metadata should not produce repeated inbox items.
7. Keep detection cursor separate from agent acknowledgements. A worker fetching an item does not mean an agent has read it. Replay after crash must be harmless.
8. On invalid cursor, rebuild with token-before-scan and reconcile old/new membership. Authentication and API failures preserve the last good state. Use bounded retry with backoff for transient errors; access denial requires revalidation, not blind retries.
9. Periodic full reconciliation catches drift; Changes is current-state detection, not a guaranteed business edit history.

Do not write a shared event for a read, polling heartbeat or notification receipt. Event creation is itself a Drive change: classify `_collab/events` as event input, never as a reason to produce another event. Deduplicate an event and its corresponding file update; human edits without events must still surface.

## Writes and recovery

Keep operation_id stable across retries. Locally serialize each user's outbox per operation; shared uniqueness cannot be guaranteed by Drive filenames. Resolve ambiguous outcomes with the returned file ID or lookup plus readback. For content writes whose outcome cannot be proven, stop and reconcile instead of replaying non-idempotent updates.

Write source first, then immutable event. They are not a distributed transaction. Record source success locally before event publication; retry publication separately. Consumers deduplicate event_id even if duplicate event files exist. A centralized coordinator with unique keys is needed if strict global exactly-once effects are required.

Suggested semantic event fields:

```json
{
  "schema_version": 1,
  "event_id": "UUID",
  "operation_id": "UUID",
  "project_id": "stable-project-id",
  "actor_subject": "authenticated-identity",
  "occurred_at": "RFC3339-UTC",
  "kind": "artifact.updated",
  "file_id": "verified-drive-file-id",
  "source_version": "provider-version-if-available",
  "task_ids": ["TASK-UUID"],
  "summary": "What changed and why",
  "visibility": "internal"
}
```

Event identity is descriptive; for stronger audit requirements use authenticated server-side logs. `visibility` is a routing hint, never an ACL. Store events in the same or narrower access boundary as their sources. Avoid copying sensitive content into shared summaries.

## Trigger integration

On-demand calls work only when the agent invokes the skill. Session hooks and scheduled workers are host-specific adapters and must be installed explicitly. A worker may populate an inbox without being able to wake the host. Webhooks need verified channel routing, renewal, durable queues and reconciliation polling. Notify only for meaningful changes; report a stale sync honestly.

## Integration acceptance cases

Two users with different ACLs; edit during initial scan; multiple pages; process crash before/after cursor commit; folder move in/out; deletion and revoked access; shortcut outside root; manual edits with no event; repeated event delivery; content success/event failure; ambiguous write timeout; simultaneous Docs writes; expired login; offline recovery; no-change polling without an event loop.
