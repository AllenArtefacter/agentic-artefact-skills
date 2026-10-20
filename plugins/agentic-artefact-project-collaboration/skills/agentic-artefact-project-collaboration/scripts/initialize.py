#!/usr/bin/env python3
"""Prepare a populated local project draft from a PM brief; no cloud writes."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import uuid
from scaffold import scaffold


def nonempty(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f'{label} must be a nonempty string')
    return value.strip()


def strings(value, label, required=False):
    if not isinstance(value, list):
        raise ValueError(f'{label} must be a list')
    result = [nonempty(v, label) for v in value]
    if required and not result:
        raise ValueError(f'{label} must contain at least one entry')
    return result


def validate(brief):
    if not isinstance(brief, dict):
        raise ValueError('Brief must be a JSON object')
    result = {k: nonempty(brief.get(k), k) for k in
              ('project_name', 'team_folder', 'context', 'vision', 'project_manager_email')}
    for key in ('in_scope', 'out_of_scope', 'success_criteria', 'open_questions'):
        result[key] = strings(brief.get(key, []), key, required=key in ('in_scope', 'success_criteria'))
    members = brief.get('members')
    if not isinstance(members, list) or not members:
        raise ValueError('members must include real named members with email, roles and responsibilities')
    result['members'] = []
    seen_ids, seen_emails = set(), set()
    for raw in members:
        if not isinstance(raw, dict):
            raise ValueError('Each member must be an object')
        person = {k: nonempty(raw.get(k), 'member.' + k) for k in ('name', 'email')}
        person['person_id'] = nonempty(raw.get('person_id', 'P-' + str(uuid.uuid4())), 'person_id')
        if person['person_id'] in seen_ids:
            raise ValueError('Duplicate member person_id')
        seen_ids.add(person['person_id'])
        for key in ('roles', 'responsibilities', 'email_aliases', 'workstream_ids'):
            person[key] = strings(raw.get(key, []), key, required=key in ('roles', 'responsibilities'))
        for email in [person['email'], *person['email_aliases']]:
            if email.count('@') != 1 or any(c.isspace() for c in email) or not all(email.split('@')):
                raise ValueError('Members must have valid complete email addresses')
            if email.lower() in seen_emails:
                raise ValueError('Duplicate or ambiguous email/alias in roster')
            seen_emails.add(email.lower())
        person['membership_status'] = 'active'
        result['members'].append(person)
    matches = [m for m in result['members'] if m['email'] == result['project_manager_email']]
    if len(matches) != 1:
        raise ValueError('project_manager_email must exactly match one member primary email')
    result['start_date'] = brief.get('start_date') or 'TBD'
    if result['start_date'] != 'TBD':
        value = nonempty(result['start_date'], 'start_date')
        if datetime.strptime(value, '%Y-%m-%d').strftime('%Y-%m-%d') != value:
            raise ValueError('start_date must be YYYY-MM-DD')
        result['start_date'] = value
    result['project_status'] = nonempty(brief.get('project_status') or 'TBD', 'project_status')
    contacts = brief.get('client_contacts', [])
    if not isinstance(contacts, list):
        raise ValueError('client_contacts must be a list')
    result['client_contacts'] = []
    for contact in contacts:
        if not isinstance(contact, dict):
            raise ValueError('client contact must be an object')
        email = contact.get('email') or ''
        if not isinstance(email, str) or (email and (email.count('@') != 1 or any(c.isspace() for c in email) or not all(email.split('@')))):
            raise ValueError('client contact requires a complete email or no email')
        result['client_contacts'].append({'name': str(contact.get('name') or 'TBD'), 'email': email})
    result['maintainer_person_id'] = matches[0]['person_id']
    return result


def frontmatter(data):
    # JSON values are valid YAML values; avoids unsafe string interpolation.
    return '---\n' + '\n'.join(f'{k}: {json.dumps(v, ensure_ascii=False)}' for k, v in data.items()) + '\n---\n'


def bullets(values):
    return '\n'.join('- ' + v.replace('\n', '\n  ') for v in values) if values else '未提供；不自动补充假设。'


def initialize(brief, output):
    b = validate(brief)  # Validate before creating output or allocating a project.
    out = scaffold(output, b['project_name'], b['team_folder'], 'team')
    timestamp = datetime.now(timezone.utc).isoformat()
    manifest_path = out / '00_Start_Here/project.manifest.json'
    manifest = json.loads(manifest_path.read_text())
    def cell(value):
        return str(value).replace('|', r'\|').replace('\n', ' ')
    roster = '\n'.join('| ' + ' | '.join(cell(v) for v in (
        m['person_id'], m['name'], '@' + m['email'],
        '; '.join(m['email_aliases']) or '—',
        '; '.join(m['roles'] + m['responsibilities']))) + ' |'
        for m in b['members'])
    team_mentions = ' '.join('@' + m['email'] for m in b['members'])
    client_mentions = '; '.join(('@' + c['email']) if c['email'] else c['name'] + ' (email: TBD)' for c in b['client_contacts']) or 'TBD'
    (out / 'Project.md').write_text(f"""# {b['project_name']}

## Metadata

| Field | Value |
|---|---|
| Project name | {cell(b['project_name'])} |
| Team | {cell(team_mentions)} |
| Start date | {b['start_date']} |
| Status | {cell(b['project_status'])} |
| Last updated | {timestamp} |
| Client contacts | {cell(client_mentions)} |

Project ID: {manifest['project_id']}

## 项目目标

{b['context']}

{b['vision']}

## 范围与验收

{bullets(b['in_scope'])}

成功标准：
{bullets(b['success_criteria'])}

非范围：
{bullets(b['out_of_scope'])}

## 人员

| 成员 ID | 姓名 | 邮箱 | 已确认别名 | 职责 |
|---|---|---|---|---|
{roster}

PM：{b['maintainer_person_id']}。人员以此表为准；任务归属以 Timeline 表为准。

## 项目入口

团队目录：{b['team_folder']}
当前进展：STATUS.md；任务：01_Management/Project Timeline（Google Sheets，Timeline / Backlog）；正式文件 ID：00_Start_Here/project.manifest.json。

## 待确认

{bullets(b['open_questions'])}
""")
    (out / 'STATUS.md').write_text(f"""# {b['project_name']} 当前状态

更新：{timestamp} · 汇总依据：项目 brief 与 Project.md

初始化草稿已准备（draft_ready）。云端部署与回读尚未完成。

已填写项目目标、范围、验收标准和 {len(b['members'])} 位成员。
待办：发布核心文件，配置 Project Timeline、目录索引与真实文件 ID，然后回读验收。

{bullets(b['open_questions'])}
""")
    for directory, title in [('03_Deliverables', 'Deliverables'), ('04_Materials', 'Materials')]:
        (out / directory / (title + '.md')).write_text(
            f'# {title}\n\nProject: {b["project_name"]}\nUpdated: {timestamp}\n\n'
            'Local initialization draft. No folder files registered yet; verify cloud inventory before publishing.\n')
    (out / '00_Start_Here/Project Index.md').write_text(
        f'# Project Index\n\nProject: {b["project_name"]}\nFolder: {b["team_folder"]}\n\n'
        'Local draft: cloud links pending. Publish Project, STATUS, Project Timeline, Materials and Deliverables, then register verified links here.\n')
    manifest['initialization_status'] = 'draft_ready'
    manifest['project_manager_person_id'] = b['maintainer_person_id']
    manifest['control_steward'] = None  # PM does not silently become an assigned table steward.
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    return {'output': str(out), 'mode': 'initialize', 'initialization_status': 'draft_ready',
            'member_count': len(b['members']), 'cloud_writes': False,
            'remaining': 'Cloud deployment, canonical IDs and readback; verify Project Timeline and folder indexes.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--brief', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    try:
        brief = json.loads(Path(args.brief).expanduser().read_text())
        result = initialize(brief, args.output)
    except (ValueError, OSError, RuntimeError) as error:
        parser.exit(1, f'Initialization not completed: {error}\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
