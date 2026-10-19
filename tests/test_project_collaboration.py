import copy
import importlib.util
import json
import os
from pathlib import Path
import tempfile
import types
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / 'skills/agentic-artefact-project-collaboration/scripts'

def module(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / (name + '.py'))
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result

s = module('scaffold')

class TemplateTests(unittest.TestCase):
    def test_all_spaces_and_json_escape(self):
        with tempfile.TemporaryDirectory() as tmp:
            for space in ('team','online-personal','local-personal'):
                out=Path(tmp)/space;s.scaffold(out,'客户 "AI"','root',space)
                self.assertEqual((out/'README.md').exists(), space != 'team')
                with self.assertRaises(FileExistsError):s.scaffold(out,'wrong','other',space)
            manifest=json.loads((Path(tmp)/'team/00_Start_Here/project.manifest.json').read_text())
            self.assertEqual(manifest['project_name'],'客户 "AI"')
            self.assertEqual(manifest['authority']['task_status'],'Tasks/Tasks')
            team = Path(tmp)/'team'
            self.assertEqual({str(p.relative_to(team)) for p in team.rglob('*') if p.is_file()},
                {'Project.md', 'STATUS.md', '00_Start_Here/project.manifest.json'})
            self.assertFalse(list(team.rglob('_templates')))
            self.assertEqual({p.name for p in (team/'02_Meetings').iterdir()}, {'raw', 'note'})
            self.assertFalse(list((team/'02_Meetings').rglob('*.*')))
            self.assertIn('个人',(Path(tmp)/'local-personal/README.md').read_text())

class InitializeTests(unittest.TestCase):
    def test_initialize_populates_context_and_preserves_draft_boundary(self):
        import subprocess
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'project'; brief=Path(tmp)/'brief.json'
            data={'project_name':'客户 "AI" 试点','team_folder':'folder-id',
                  'context':'客服响应较慢，需要验证 AI 辅助方案。','vision':'让客服更快获得可信答复。',
                  'in_scope':['评估试点'],'success_criteria':['完成可复核的试点评估'],
                  'project_manager_email':'pm@example.test',
                  'members':[{'person_id':'P-existing','name':'项目经理','email':'pm@example.test',
                              'roles':['PM','consultant'],'responsibilities':['项目范围与协调']}],
                  'open_questions':['上线日期未确认']}
            brief.write_text(json.dumps(data,ensure_ascii=False))
            command=['python3',str(SCRIPTS/'initialize.py'),'--brief',str(brief),'--output',str(out)]
            result=subprocess.run(command,capture_output=True,text=True)
            self.assertEqual(result.returncode,0,result.stderr)
            self.assertEqual(json.loads(result.stdout)['initialization_status'],'draft_ready')
            manifest=json.loads((out/'00_Start_Here/project.manifest.json').read_text())
            self.assertEqual(manifest['project_manager_person_id'],'P-existing')
            self.assertTrue(all(v is None for v in manifest['canonical_files'].values()))
            project=(out/'Project.md').read_text()
            self.assertIn('| Start date | TBD |', project)
            self.assertIn('| Status | TBD |', project)
            self.assertIn('| Client contacts | TBD |', project)
            self.assertIn('| Team | @pm@example.test |', project)
            self.assertIn(data['context'],project);self.assertIn(data['vision'],project)
            self.assertIn(data['project_name'],project)
            self.assertIn('| P-existing | 项目经理 | @pm@example.test |',project)
            self.assertFalse(list(out.rglob('README.md')))
            expected_dirs = {'00_Start_Here', '01_Management', '02_Meetings',
                             '03_Deliverables', '04_Materials', '90_Archive'}
            self.assertEqual({x.name for x in out.iterdir() if x.is_dir()}, expected_dirs)
            for relative in ('00_Start_Here/Project Index.md',
                             '03_Deliverables/Deliverables.md', '04_Materials/Materials.md'):
                draft = (out / relative).read_text()
                self.assertIn(data['project_name'], draft)
                self.assertNotIn('{{', draft)
            self.assertIsNone(manifest['canonical_files']['materials_index_id'])
            self.assertIsNone(manifest['canonical_files']['deliverables_index_id'])
            self.assertFalse(list(out.rglob('*.csv')))

            self.assertIn('云端部署与回读尚未完成',(out/'STATUS.md').read_text())
            before=(out/'Project.md').read_bytes()
            self.assertNotEqual(subprocess.run(command,capture_output=True).returncode,0)
            self.assertEqual((out/'Project.md').read_bytes(),before)

    def test_initialize_rejects_ambiguous_roster_before_creating_folder(self):
        import subprocess
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'project';brief=Path(tmp)/'brief.json'
            member={'name':'A','email':'same@example.test','roles':['PM'],'responsibilities':['Coordination']}
            brief.write_text(json.dumps({'project_name':'Test','team_folder':'root','context':'Context','vision':'Vision',
                'in_scope':['Scope'],'success_criteria':['Evidence'],'project_manager_email':'same@example.test',
                'members':[member,dict(member,name='B')]}))
            result=subprocess.run(['python3',str(SCRIPTS/'initialize.py'),'--brief',str(brief),'--output',str(out)],capture_output=True,text=True)
            self.assertNotEqual(result.returncode,0)
            self.assertIn('ambiguous',result.stderr)
            self.assertFalse(out.exists())

if __name__=='__main__': unittest.main()
