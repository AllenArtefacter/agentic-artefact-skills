#!/usr/bin/env python3
"""Build or verify the Codex distribution from the canonical root skills."""
import argparse
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / 'plugins/agentic-artefact-project-collaboration'


def files(root):
    return {p.relative_to(root): p.read_bytes() for p in root.rglob('*')
            if p.is_file() and '__pycache__' not in p.parts
            and p.suffix != '.pyc' and p.name != '.DS_Store'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    source = files(ROOT / 'skills')
    target = PLUGIN / 'skills'
    if args.check:
        if files(target) != source:
            raise SystemExit('Codex skills are stale. Run python3 scripts/build_codex_plugin.py')
    else:
        if target.exists():
            shutil.rmtree(target)
        for name, content in source.items():
            path = target / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)
        shutil.copyfile(ROOT / 'LICENSE', PLUGIN / 'LICENSE')
    manifest = json.loads((PLUGIN / '.codex-plugin/plugin.json').read_text())
    claude = json.loads((ROOT / '.claude-plugin/plugin.json').read_text())
    if manifest['version'] != claude['version']:
        raise SystemExit('Keep Claude and Codex plugin versions aligned before releasing.')
    print(f'Codex package {"verified" if args.check else "built"}: {len(source)} skill files')


if __name__ == '__main__':
    main()
