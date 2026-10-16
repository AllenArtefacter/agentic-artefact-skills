#!/usr/bin/env python3
"""Run Workspace API commands with existing gws OAuth, without an explicit quota project.

Compatibility path for gws 0.22.5's automatic x-goog-user-project behavior.
Does not grant permissions, enable APIs, log in, or change persistent config.
"""
import os
from pathlib import Path
import subprocess
import sys
import tempfile


def run(arguments):
    if not arguments or arguments[0] in ('-h', '--help'):
        print('Usage: python3 gws_workspace.py <drive|sheets|docs|slides> <gws API arguments>')
        print('Uses existing encrypted gws OAuth credentials. Login separately with gws auth login.')
        return 0
    if arguments[0] not in ('drive', 'sheets', 'docs', 'slides'):
        raise ValueError('Only Workspace Drive/Sheets/Docs/Slides calls are supported; auth commands are not forwarded.')
    for name in ('GOOGLE_WORKSPACE_CLI_TOKEN', 'GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE'):
        if os.environ.get(name):
            raise ValueError('An explicit credential override is active. Resolve the intended identity before using this OAuth-only wrapper.')
    source = Path(os.environ.get('GOOGLE_WORKSPACE_CLI_CONFIG_DIR', str(Path.home()/'.config/gws'))).expanduser().resolve()
    if not (source/'credentials.enc').is_file():
        raise ValueError('No existing encrypted gws OAuth credentials found; use the normal agent-run gws login flow first.')
    with tempfile.TemporaryDirectory(prefix='gws-workspace-oauth-') as temp:
        target=Path(temp)
        for name in ('credentials.enc', '.encryption_key'):
            original=source/name
            if original.is_file():
                (target/name).symlink_to(original)
        env=os.environ.copy()
        env['GOOGLE_WORKSPACE_CLI_CONFIG_DIR']=temp
        # No client_secret.json => no implicit quota project from its project_id.
        # /dev/null prevents unrelated ambient ADC from supplying a quota project.
        # Authentication still uses the same user's existing encrypted credentials.
        env['GOOGLE_APPLICATION_CREDENTIALS']=os.devnull
        env.pop('GOOGLE_WORKSPACE_PROJECT_ID', None)
        return subprocess.run(['gws', *arguments], env=env).returncode


if __name__ == '__main__':
    try:
        sys.exit(run(sys.argv[1:]))
    except (ValueError, OSError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(2)
