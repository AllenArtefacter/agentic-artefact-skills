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

r = module('drive_reader')
s = module('scaffold')

def item(fid, mime='text/plain', parents=None, version='1'):
    return {'id': fid, 'name': fid, 'mimeType': mime, 'parents': parents or [], 'version': version, 'driveId': 'shared'}

class FakeGoogle:
    def __init__(self, token='unused'):
        self.items = {'root': item('root', r.FOLDER), 'sub': item('sub', r.FOLDER, ['root']),
                      'doc': item('doc', 'application/vnd.google-apps.document', ['sub']),
                      'outside': item('outside'), 'shortcut': item('shortcut', r.SHORTCUT, ['root'])}
        self.principal = 'person-A'
        self.fail = False
        self.requests = []

    def identity(self):
        return self.principal

    def metadata(self, fid):
        if self.fail:
            raise r.ReaderError('simulated access failure')
        if fid not in self.items:
            raise r.ReaderError('not accessible')
        return copy.deepcopy(self.items[fid])

    def children(self, fid, drive_id):
        if self.fail:
            raise r.ReaderError('simulated scan failure')
        yield from [copy.deepcopy(v) for v in self.items.values() if fid in v.get('parents', [])]

    def get(self, path, params=None, base=None, binary=False):
        self.requests.append((path, params, base, binary))
        if base and 'sheets.googleapis.com' in base:
            return {'sheets': [{'properties': {'title': 'Tasks'}}, {'properties': {'title': 'Deliverables'}}]}
        return b'Current project content'

class ReaderTests(unittest.TestCase):
    def test_folder_url_and_validation(self):
        self.assertEqual(r.file_id('https://drive.google.com/drive/u/0/folders/abc_123?usp=sharing'), 'abc_123')
        for bad in ('https://evil.test/folders/root', "x' or true", '../root'):
            with self.assertRaises(r.ReaderError): r.file_id(bad)

    def test_inventory_scope_and_shortcuts(self):
        api = FakeGoogle()
        self.assertEqual(set(r.inventory(api, 'root')), {'root','sub','doc','shortcut'})
        with self.assertRaises(r.ReaderError): r.scoped_metadata(api,'root','outside')
        with self.assertRaises(r.ReaderError): r.read_content(api,'root','shortcut')
        self.assertEqual(r.scoped_metadata(api,'root','doc')['id'],'doc')

    def test_folder_move_out_excludes_subtree(self):
        api=FakeGoogle()
        old=r.reconcile({},r.inventory(api,'root'))
        api.items['sub']['parents']=['outside']
        new=r.reconcile(old,r.inventory(api,'root'))
        unavailable=[e for e in new['inbox'] if e['kind']=='unavailable_or_moved_out']
        self.assertEqual({e['file_id'] for e in unavailable},{'sub','doc'})
        self.assertTrue(all('name' not in e for e in unavailable))
        again=r.reconcile(new,r.inventory(api,'root'))
        self.assertEqual(again['inbox'],new['inbox'])
        with self.assertRaises(r.ReaderError): r.read_content(api,'root','doc')

    def test_delta_no_repeat_and_ack_separate(self):
        api=FakeGoogle(); first=r.reconcile({},r.inventory(api,'root'))
        second=r.reconcile(first,r.inventory(api,'root'))
        self.assertEqual(first['inbox'],second['inbox'])
        second['inbox']=[]
        self.assertEqual(r.reconcile(second,r.inventory(api,'root'))['inbox'],[])
        api.items['doc']['version']='2'
        update=r.reconcile(second,r.inventory(api,'root'))
        self.assertEqual([(e['file_id'],e['kind']) for e in update['inbox']],[('doc','updated')])

    def test_paginated_shared_drive(self):
        api=r.Google('fake'); calls=[]
        pages=[{'files':[item('a')],'nextPageToken':'page2'}, {'files':[item('b')]}]
        def fake_get(path,params):
            calls.append(dict(params));return pages.pop(0)
        api.get=fake_get
        self.assertEqual([x['id'] for x in api.children('root','shared')],['a','b'])
        self.assertEqual(calls[1]['pageToken'],'page2')
        self.assertEqual(calls[0]['corpora'],'drive')
        self.assertEqual(calls[0]['supportsAllDrives'],'true')

    def test_incomplete_and_repeating_pagination_fail(self):
        api=r.Google('fake')
        api.get=lambda *a:{'incompleteSearch':True}
        with self.assertRaises(r.ReaderError):list(api.children('root','shared'))
        api.get=lambda *a:{'files':[],'nextPageToken':'same'}
        with self.assertRaises(r.ReaderError):list(api.children('root','shared'))

    def test_reads_docs_and_all_sheet_tabs(self):
        api=FakeGoogle()
        self.assertEqual(r.read_content(api,'root','doc')['text'],'Current project content')
        api.items['doc']['mimeType']='application/vnd.google-apps.spreadsheet'
        out=r.read_content(api,'root','doc')
        self.assertEqual(len(out['sheets']),2)
        self.assertEqual(api.requests[-1][1]['includeGridData'],'true')
        self.assertNotIn('ranges',api.requests[-1][1])

    def test_concurrent_read_change_fails(self):
        api=FakeGoogle(); original=api.get
        def get(*a,**kw):
            api.items['doc']['version']='2';return original(*a,**kw)
        api.get=get
        with self.assertRaises(r.ReaderError):r.read_content(api,'root','doc')

    def test_whoami_uses_authenticated_account_not_role(self):
        api=r.Google('fake-token')
        api.get=lambda path, params: {'user': {'permissionId': 'principal-A', 'emailAddress': 'member@example.test', 'displayName': 'Member'}}
        self.assertEqual(api.identity(),'principal-A')
        self.assertEqual(api.current_user()['emailAddress'],'member@example.test')
        self.assertNotIn('roles',api.current_user())

    def test_missing_token(self):
        with patch.dict(os.environ,{},clear=True):
            with self.assertRaises(r.ReaderError):r.get_token({'token_env':'MISSING_TEST_TOKEN'})

    def test_refresh_uses_fixed_google_endpoint(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'creds.json'
            path.write_text(json.dumps({'type':'authorized_user','client_id':'test','client_secret':'secret',
                                        'refresh_token':'refresh','token_uri':'https://evil.test'}))
            with patch.object(r,'http',return_value=b'{"access_token":"test-access"}') as call:
                self.assertEqual(r.get_token({'credentials_file':str(path)}),'test-access')
                self.assertEqual(call.call_args.args[0],'https://oauth2.googleapis.com/token')

    def test_lock_exclusion(self):
        with tempfile.TemporaryDirectory() as tmp:
            with r.workspace_lock(Path(tmp)):
                with self.assertRaises(r.ReaderError):
                    with r.workspace_lock(Path(tmp)):pass
            self.assertFalse((Path(tmp)/'.collab/reader.lock').exists())

    def test_workflow_failure_preserves_snapshot_and_account_boundary(self):
        with tempfile.TemporaryDirectory() as tmp:
            api=FakeGoogle()
            args=types.SimpleNamespace(command='join',workspace=tmp,folder='root',token_env='TEST_TOKEN',
                                       personal_folder='personal',credentials_file=None)
            with patch.object(r,'Google',return_value=api), patch.dict(os.environ,{'TEST_TOKEN':'never-store-this'}):
                r.run(args)
                stored=(Path(tmp)/'.collab/config.json').read_text()
                self.assertNotIn('never-store-this',stored)
                self.assertIn('personal',stored)
                before=(Path(tmp)/'.collab/state.json').read_bytes()
                args.command='sync';api.fail=True
                with self.assertRaises(r.ReaderError):r.run(args)
                self.assertEqual((Path(tmp)/'.collab/state.json').read_bytes(),before)
                api.fail=False;api.principal='person-B'
                with self.assertRaises(r.ReaderError):r.run(args)
                self.assertEqual((Path(tmp)/'.collab/state.json').read_bytes(),before)
                api.principal='person-A';api.items['doc']['version']='2'
                result=r.run(args)
                change=next(e for e in result['pending_changes'] if e['file_id']=='doc' and e['kind']=='updated')
                args.command='ack';args.change_id=change['change_id'];r.run(args)
                args.command='sync'
                self.assertFalse(any(e['change_id']==change['change_id'] for e in r.run(args)['pending_changes']))

class TemplateTests(unittest.TestCase):
    def test_all_spaces_and_json_escape(self):
        with tempfile.TemporaryDirectory() as tmp:
            for space in ('team','online-personal','local-personal'):
                out=Path(tmp)/space;s.scaffold(out,'客户 "AI"','root',space)
                self.assertEqual((out/'README.md').exists(), space != 'team')
                with self.assertRaises(FileExistsError):s.scaffold(out,'wrong','other',space)
            manifest=json.loads((Path(tmp)/'team/00_Start_Here/project.manifest.json').read_text())
            self.assertEqual(manifest['project_name'],'客户 "AI"')
            self.assertEqual(manifest['authority']['task_status'],'Project Control/Tasks')
            team = Path(tmp)/'team'
            self.assertEqual({str(p.relative_to(team)) for p in team.rglob('*') if p.is_file()},
                {'Project.md', 'STATUS.md', '01_Management/working-plan.md', '00_Start_Here/project.manifest.json'})
            self.assertFalse(list(team.rglob('_templates')))
            self.assertIn('个人',(Path(tmp)/'local-personal/README.md').read_text())

if __name__=='__main__':unittest.main()

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
            self.assertIn(data['context'],project);self.assertIn(data['vision'],project)
            self.assertIn(data['project_name'],project)
            self.assertIn('| P-existing | 项目经理 | pm@example.test |',project)
            self.assertFalse(list(out.rglob('README.md')))
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
