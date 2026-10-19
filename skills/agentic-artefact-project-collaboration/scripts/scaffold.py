#!/usr/bin/env python3
"""Generate a local project template. No Google calls or credentials required."""
import argparse
import json
from pathlib import Path
import shutil
import tempfile
import uuid


def scaffold(output, name, folder, space="team"):
    output = Path(output).expanduser().absolute()
    if output.exists():
        raise FileExistsError(f'Refusing to overwrite existing path: {output}')
    if not name.strip() or not folder.strip():
        raise ValueError('Project name and folder must be nonempty')
    templates = {'team': 'project-template', 'online-personal': 'personal-template', 'local-personal': 'local-template'}
    source = Path(__file__).resolve().parents[1] / 'assets' / templates[space]
    values = {'{{PROJECT_NAME}}': name, '{{PROJECT_FOLDER}}': folder,
              '{{PROJECT_ID}}': str(uuid.uuid4())}
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.project-template-', dir=output.parent) as tmp:
        stage = Path(tmp) / 'project'
        shutil.copytree(source, stage)
        if space == 'team':
            # Only project-specific seed files belong in the publication tree.
            # Reusable guides and blank object templates stay inside the skill.
            for folder_name in ('00_Start_Here', '01_Management', '02_Meetings',
                                '03_Deliverables', '04_Materials', '90_Archive'):
                (stage / folder_name).mkdir(exist_ok=True)
            for subfolder in ('raw', 'note'):
                (stage / '02_Meetings' / subfolder).mkdir(exist_ok=True)
        for path in stage.rglob('*'):
            if not path.is_file():
                continue
            if path.suffix == '.json':
                def replace(value):
                    if isinstance(value, str):
                        return values.get(value, value)
                    if isinstance(value, dict):
                        return {k: replace(v) for k, v in value.items()}
                    if isinstance(value, list):
                        return [replace(v) for v in value]
                    return value
                content = json.dumps(replace(json.loads(path.read_text())), ensure_ascii=False, indent=2) + '\n'
            else:
                content = path.read_text()
                for key, value in values.items():
                    # Keep template YAML quoted scalars valid for names/URLs containing quotes.
                    content = content.replace(chr(34) + key + chr(34), json.dumps(value, ensure_ascii=False))
                    content = content.replace(key, value)
            path.write_text(content)
        # Exclusive mkdir prevents concurrent invocations from overwriting a project.
        output.mkdir()
        try:
            for item in stage.iterdir():
                shutil.move(str(item), str(output / item.name))
        except Exception:
            # Retain partially created output for inspection; never remove user files.
            raise RuntimeError(f'Partial local output retained at {output}')
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    parser.add_argument('--name', required=True)
    parser.add_argument('--space', choices=['team', 'online-personal', 'local-personal'], default='team')
    parser.add_argument('--folder', required=True, help='Google folder ID or URL; not a credential')
    args = parser.parse_args()
    try:
        result = scaffold(args.output, args.name, args.folder, args.space)
    except (OSError, ValueError, RuntimeError) as error:
        parser.exit(1, f'{error}\n')
    print(f'Local template created: {result}\nNo Google files were created or updated.')


if __name__ == '__main__':
    main()
