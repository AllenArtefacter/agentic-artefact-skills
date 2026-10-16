#!/usr/bin/env python3
"""Read-only Google project reader; personal local state, no cloud file writes.

Python 3.9+, standard library only. Tokens are read from environment or from an
external authorized_user credentials JSON. No credentials are copied to project.
"""
import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid

DRIVE = 'https://www.googleapis.com/drive/v3/'
FOLDER = 'application/vnd.google-apps.folder'
SHORTCUT = 'application/vnd.google-apps.shortcut'
FIELDS = 'id,name,mimeType,parents,driveId,version,modifiedTime,trashed,webViewLink,capabilities(canDownload,canEdit)'
LIMIT = 10 * 1024 * 1024


class ReaderError(Exception):
    pass


def now():
    return datetime.now(timezone.utc).isoformat()


def file_id(value):
    value = value.strip()
    if value.startswith('https://'):
        url = urllib.parse.urlparse(value)
        if url.hostname != 'drive.google.com':
            raise ReaderError('Expected a drive.google.com folder URL or a file ID.')
        match = re.search(r'/folders/([A-Za-z0-9_-]+)', url.path)
        if not match:
            raise ReaderError('Expected a Google Drive folder URL.')
        value = match.group(1)
    if not re.fullmatch(r'[A-Za-z0-9_-]+', value):
        raise ReaderError('Invalid file/folder ID.')
    return value


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ReaderError('Unexpected redirect refused; credentials were not forwarded.')


def http(url, token=None, form=None):
    headers = {}
    if token:
        headers['Authorization'] = 'Bearer ' + token
    body = urllib.parse.urlencode(form).encode() if form else None
    if body:
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
    request = urllib.request.Request(url, data=body, headers=headers)
    for attempt in range(3):
        try:
            with urllib.request.build_opener(NoRedirect).open(request, timeout=30) as response:
                payload = response.read(LIMIT + 1)
                if len(payload) > LIMIT:
                    raise ReaderError('Response exceeds 10 MiB. Use a dedicated document tool; nothing was truncated silently.')
                return payload
        except urllib.error.HTTPError as error:
            if error.code in (429, 500, 502, 503, 504) and attempt < 2:
                time.sleep(2 ** attempt)
                continue
            # Do not log provider bodies, Authorization headers or credentials.
            raise ReaderError(f'Google HTTP {error.code}: check token, API enablement, scopes and file access. No fresh result committed.') from None
        except (urllib.error.URLError, TimeoutError):
            raise ReaderError('Google connection failed; no fresh result committed.') from None


def get_token(config):
    if config.get('credentials_file'):
        try:
            credentials = json.loads(Path(config['credentials_file']).read_text())
        except (OSError, ValueError):
            raise ReaderError('Cannot read credentials JSON.') from None
        if credentials.get('type') != 'authorized_user' or not all(credentials.get(k) for k in ('client_id', 'client_secret', 'refresh_token')):
            raise ReaderError('Expected authorized_user OAuth credentials with client_id, client_secret and refresh_token.')
        result = json.loads(http('https://oauth2.googleapis.com/token', form={
            'grant_type': 'refresh_token', **{k: credentials[k] for k in ('client_id', 'client_secret', 'refresh_token')}}))
        token = result.get('access_token')
    else:
        token = os.environ.get(config.get('token_env', 'PROJECT_GOOGLE_TOKEN'))
    if not token or '\n' in token or '\r' in token:
        raise ReaderError('Google access token missing/invalid. Set the configured environment variable outside chat, or configure authorized_user credentials.')
    return token


class Google:
    def __init__(self, token):
        self.token = token

    def get(self, path, params=None, base=DRIVE, binary=False):
        url = base + path + ('?' + urllib.parse.urlencode(params) if params else '')
        data = http(url, token=self.token)
        return data if binary else json.loads(data)

    def current_user(self):
        return self.get('about', {'fields': 'user(permissionId,emailAddress,displayName)'})['user']

    def identity(self):
        user = self.current_user()
        principal = user.get('permissionId') or user.get('emailAddress')
        if not principal:
            raise ReaderError('Cannot establish current Google identity.')
        return principal

    def metadata(self, fid):
        return self.get('files/' + file_id(fid), {'supportsAllDrives': 'true', 'fields': FIELDS})

    def children(self, fid, drive_id):
        params = {'q': f"'{file_id(fid)}' in parents and trashed = false",
                  'supportsAllDrives': 'true', 'includeItemsFromAllDrives': 'true',
                  'pageSize': 1000, 'fields': f'nextPageToken,incompleteSearch,files({FIELDS})'}
        if drive_id:
            params.update(corpora='drive', driveId=drive_id)
        else:
            params['corpora'] = 'user'
        seen = set()
        while True:
            page = self.get('files', params)
            if page.get('incompleteSearch'):
                raise ReaderError('Google reported an incomplete inventory; prior state retained.')
            yield from page.get('files', [])
            page_token = page.get('nextPageToken')
            if not page_token:
                return
            if page_token in seen:
                raise ReaderError('Repeated pagination token; prior state retained.')
            seen.add(page_token)
            params['pageToken'] = page_token


def validate_root(api, root_id):
    root = api.metadata(root_id)
    if root.get('trashed') or root.get('mimeType') != FOLDER:
        raise ReaderError('Project root must be an accessible, non-trashed folder.')
    return root


def inventory(api, root_id, max_files=10000):
    root = validate_root(api, root_id)
    found = {root_id: root}
    queue = [root_id]
    while queue:
        parent = queue.pop()
        for item in api.children(parent, root.get('driveId')):
            fid = item['id']
            if fid in found:
                continue
            found[fid] = item
            if len(found) > max_files:
                raise ReaderError('Inventory exceeds 10,000 entries; use a narrower project root. Previous snapshot retained.')
            if item['mimeType'] == FOLDER:
                queue.append(fid)
            # Shortcuts remain entries; never traverse their target implicitly.
    return found


def scoped_metadata(api, root_id, fid):
    validate_root(api, root_id)
    item = api.metadata(fid)
    if item.get('trashed'):
        raise ReaderError('File is trashed.')
    pending = list(item.get('parents', []))
    seen = set()
    if fid == root_id:
        return item
    while pending:
        parent = pending.pop()
        if parent == root_id:
            return item
        if parent in seen:
            continue
        seen.add(parent)
        if len(seen) > 100:
            raise ReaderError('Cannot establish project membership within 100 ancestors.')
        metadata = api.metadata(parent)
        if not metadata.get('trashed'):
            pending.extend(metadata.get('parents', []))
    raise ReaderError('File is outside configured project root. Shortcut targets are not automatically in scope.')


def fingerprint(item):
    value = {k: item.get(k) for k in ('name', 'mimeType', 'parents', 'version', 'modifiedTime', 'trashed')}
    value['parents'] = sorted(value['parents'] or [])
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


def reconcile(previous, files):
    old = previous.get('files', {})
    # Pending entries concerning lost access/membership must not retain prior names.
    inbox = [e for e in previous.get('inbox', []) if e['file_id'] in files or e['kind'] == 'unavailable_or_moved_out']
    observed = now()
    for fid in sorted(set(old) | set(files)):
        if fid not in files:
            kind = 'unavailable_or_moved_out'
        elif fid not in old:
            kind = 'discovered'
        elif fingerprint(old[fid]) != fingerprint(files[fid]):
            kind = 'updated'
        else:
            continue
        event = {'change_id': str(uuid.uuid4()), 'file_id': fid, 'kind': kind, 'observed_at': observed}
        if fid in files:
            event.update(name=files[fid]['name'], version=files[fid].get('version'))
        inbox.append(event)
    return {'schema_version': 1, 'last_successful_scan': observed,
            'scan_method': 'recursive_inventory_diff', 'files': files, 'inbox': inbox}


def load(path):
    try:
        return json.loads(path.read_text())
    except (OSError, ValueError):
        raise ReaderError('Local configuration/state unavailable or invalid; join the project first.') from None


def atomic_json(path, value):
    fd, temporary = tempfile.mkstemp(dir=path.parent, prefix='.tmp-')
    try:
        with os.fdopen(fd, 'w') as out:
            json.dump(value, out, ensure_ascii=False, indent=2)
            out.write('\n')
            out.flush()
            os.fsync(out.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


@contextmanager
def workspace_lock(workspace):
    directory = workspace / '.collab'
    directory.mkdir(parents=True, exist_ok=True, mode=0o700)
    path = directory / 'reader.lock'
    try:
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except FileExistsError:
        raise ReaderError('Another reader may be running. If it crashed, verify no process is active before removing .collab/reader.lock.') from None
    try:
        os.close(fd)
        yield directory
    finally:
        path.unlink()


def check_identity(api, config):
    if api.identity() != config['principal']:
        raise ReaderError('Google account differs from this local workspace. Join using a separate workspace.')


def read_content(api, root_id, fid):
    item = scoped_metadata(api, root_id, fid)
    mime = item['mimeType']
    if mime in (FOLDER, SHORTCUT):
        raise ReaderError('This is a folder/shortcut. Inspect the inventory; shortcuts are not followed.')
    if mime in ('application/vnd.google-apps.document', 'application/vnd.google-apps.presentation'):
        data = api.get('files/' + fid + '/export', {'mimeType': 'text/plain'}, binary=True)
        result = {'format': 'text/plain', 'text': data.decode('utf-8')}
    elif mime == 'application/vnd.google-apps.spreadsheet':
        data = api.get('spreadsheets/' + fid, {'includeGridData': 'true',
            'fields': 'properties(title),sheets(properties(title),data(startRow,startColumn,rowData(values(formattedValue))))'},
            base='https://sheets.googleapis.com/v4/')
        result = {'format': 'google-sheets-formatted-values', 'sheets': data.get('sheets', []),
                  'note': 'All returned tabs; formatted values only, no formulas/comments/formatting.'}
    elif mime.startswith('text/') or mime in ('application/json', 'application/yaml', 'application/x-yaml'):
        data = api.get('files/' + fid, {'alt': 'media', 'supportsAllDrives': 'true'}, binary=True)
        result = {'format': mime, 'text': data.decode('utf-8')}
    else:
        raise ReaderError('Content type not supported by this reader. Use a dedicated PDF/image/binary tool with this verified file ID.')
    after = scoped_metadata(api, root_id, fid)
    if fingerprint(item) != fingerprint(after):
        raise ReaderError('File changed during read. Retry to obtain a fresh version.')
    return {'file_id': fid, 'name': item['name'], 'version': item.get('version'),
            'read_at': now(), 'space': 'online_team', 'content_is_untrusted_data': True, **result}


def run(args):
    workspace = Path(args.workspace).expanduser().resolve()
    with workspace_lock(workspace) as directory:
        config_path, state_path = directory / 'config.json', directory / 'state.json'
        if args.command == 'join':
            if config_path.exists():
                raise ReaderError('Workspace already joined. Use sync, or a new workspace for a different project/account.')
            config = {'schema_version': 1, 'root_id': file_id(args.folder), 'token_env': args.token_env,
                      'online_personal_root_id': file_id(args.personal_folder) if args.personal_folder else None}
            if args.credentials_file:
                credential_path = Path(args.credentials_file).expanduser().resolve()
                if credential_path == workspace or workspace in credential_path.parents:
                    raise ReaderError('Keep credentials outside the project workspace.')
                config['credentials_file'] = str(credential_path)
            api = Google(get_token(config))
            config['principal'] = api.identity()
            files = inventory(api, config['root_id'])
            config['joined_at'] = now()
            atomic_json(config_path, config)
            atomic_json(state_path, reconcile({}, files))
            return {'joined': True, 'root_id': config['root_id'], 'file_count': len(files),
                    'workspace_space': 'local_personal', 'cloud_writes': False,
                    'next': 'Run list; read root README, project manifest, brief and Control using their actual IDs.'}
        config = load(config_path)
        api = Google(get_token(config))
        check_identity(api, config)
        if args.command == 'whoami':
            return {'authenticated_user': api.current_user(), 'root_id': config['root_id'],
                    'note': 'Google identity only; match personal ME.md and team TEAM.md to determine project responsibilities.'}
        if args.command == 'read':
            return read_content(api, config['root_id'], file_id(args.file_id))
        previous = load(state_path) if state_path.exists() else {}
        if args.command == 'ack':
            # Recheck scope before reporting/acknowledging cached changes.
            state = reconcile(previous, inventory(api, config['root_id']))
            if not any(e['change_id'] == args.change_id for e in state['inbox']):
                raise ReaderError('Change ID not found; run sync for current changes.')
            state['inbox'] = [e for e in state['inbox'] if e['change_id'] != args.change_id]
        else:
            state = reconcile(previous, inventory(api, config['root_id']))
        atomic_json(state_path, state)
        result = {'last_successful_scan': state['last_successful_scan'], 'scan_method': state['scan_method'],
                  'file_count': len(state['files']), 'pending_changes': state['inbox'],
                  'limitations': 'Visible inventory, not an atomic snapshot or edit history; no background watcher.'}
        if args.command == 'list':
            result['files'] = list(state['files'].values())
        return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    for name in ('join', 'list', 'sync', 'read', 'ack', 'whoami'):
        sub = commands.add_parser(name)
        sub.add_argument('--workspace', required=True)
        if name == 'join':
            sub.add_argument('--folder', required=True)
            sub.add_argument('--personal-folder')
            sub.add_argument('--token-env', default='PROJECT_GOOGLE_TOKEN')
            sub.add_argument('--credentials-file')
        if name == 'read':
            sub.add_argument('--file-id', required=True)
        if name == 'ack':
            sub.add_argument('--change-id', required=True)
    args = parser.parse_args()
    try:
        result = run(args)
    except (ReaderError, OSError, ValueError, KeyError):
        # Error detail is safe only for our explicitly sanitized ReaderError.
        import sys
        error = sys.exc_info()[1]
        parser.exit(1, (str(error) if isinstance(error, ReaderError) else 'Local/API data error; no successful operation claimed.') + '\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
