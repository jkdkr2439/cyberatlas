from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from unittest.mock import patch as mock_patch
import copy, json, shutil, tempfile, unittest, subprocess, sys, os
import graph as g

ROOT=Path(__file__).resolve().parent

class GraphTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='cyber-map-tests-')
        self.store=Path(self.temp.name)/'graph'
        shutil.copytree(g.DEFAULT_STORE,self.store)
        self.rev,self.data=g.load(self.store)
    def tearDown(self):self.temp.cleanup()
    def node(self,nid='revoke-cas'):
        return copy.deepcopy(next(n for n in self.data['nodes'] if n['id']==nid))
    def proposal(self,node):
        return {'expected_revision':self.rev,'reason':'Test-only candidate mutation','upsert_nodes':[node]}
    def test_current_schema_and_hashes(self):
        self.assertEqual(g.validate(self.data)['nodes'],len(self.data['nodes']))
        self.assertEqual(g.validate(self.data)['observations'],len(self.data['observations']))
    def test_context_includes_ancestry_not_only_keyword(self):
        packet=g.packet(self.store,'revoke-cas')
        self.assertEqual([n['id'] for n in packet['parents_nearest_first']],['revoke-race','revoke-cache','ses-revoke','session','root'])
        self.assertIn('policy epoch',packet['node']['test'])
    def test_context_reads_only_selected_and_parent_node_files(self):
        original=Path.read_bytes; seen=[]
        def read(path):
            if path.parent.name=='nodes':seen.append(path.name)
            return original(path)
        with mock_patch.object(Path,'read_bytes',read):g.packet(self.store,'revoke-cas')
        self.assertEqual(set(seen),{'revoke-cas.json','revoke-race.json','revoke-cache.json','ses-revoke.json','session.json','root.json'})
    def test_budget_is_explicit_not_silent_truncation(self):
        p=g.packet(self.store,'root',1600)
        self.assertLessEqual(len(g.pretty(p)),1600)
        self.assertGreater(p['omitted_edges'],0)
        with self.assertRaisesRegex(ValueError,'too small'):g.packet(self.store,'revoke-cas',100)
    def test_update_preserves_other_nodes_and_changes_projection(self):
        n=self.node();n['control']+='; verified-version fixture for test only'
        result=g.apply_patch(self.store,self.proposal(n));newrev,new=g.load(self.store)
        self.assertNotEqual(newrev,self.rev);self.assertEqual(result['parent_revision'],self.rev)
        old={n['id']:n for n in self.data['nodes']};after={n['id']:n for n in new['nodes']}
        self.assertEqual([i for i in old if old[i]!=after[i]],['revoke-cas'])
        projected=json.loads((self.store/'revisions'/newrev/'mechanisms.json').read_text(encoding='utf-8'))
        self.assertIn('fixture',next(p['control'] for p in projected if p['id']=='P:revoke-cas'))
        self.assertTrue((self.store/'revisions'/self.rev).exists())
    def test_dry_run_does_not_commit(self):
        n=self.node();n['open']+=' Test-only extra question.'
        before=list((self.store/'revisions').iterdir())
        result=g.apply_patch(self.store,self.proposal(n),dry_run=True)
        self.assertTrue(result['dry_run']);self.assertEqual(g.current(self.store),self.rev)
        self.assertEqual(before,list((self.store/'revisions').iterdir()))
    def test_stale_revision_rejected_without_lost_update(self):
        n=self.node();n['open']+=' first'
        g.apply_patch(self.store,self.proposal(n));second=self.node();second['open']+=' second'
        with self.assertRaisesRegex(ValueError,'stale revision'):g.apply_patch(self.store,self.proposal(second))
        _,a=g.load(self.store)
        self.assertTrue(next(n for n in a['nodes'] if n['id']=='revoke-cas')['open'].endswith('first'))
    def test_concurrent_writers_do_not_both_overwrite(self):
        n1=self.node();n1['open']+=' writer1';n2=self.node('tenant-cache');n2['open']+=' writer2'
        def apply(node):
            try:g.apply_patch(self.store,self.proposal(node));return 'committed'
            except ValueError as e:return str(e)
        with ThreadPoolExecutor(max_workers=2) as ex:results=list(ex.map(apply,[n1,n2]))
        self.assertEqual(results.count('committed'),1)
        self.assertTrue(any('lock exists' in r or 'stale revision' in r for r in results))
        self.assertTrue(g.validate(g.load(self.store)[1])['valid'])
    def test_dangling_edge_blocks_whole_patch(self):
        n=self.node();n['open']+=' should not commit'
        edge={'source':n['id'],'target':'nonexistent','relation':'requires','layer':'crosslink','condition':'test'};edge['id']=g.edge_id(edge)
        proposal=self.proposal(n);proposal['upsert_edges']=[edge]
        with self.assertRaisesRegex(ValueError,'dangling edge'):g.apply_patch(self.store,proposal)
        self.assertEqual(g.current(self.store),self.rev);self.assertFalse((self.store/'WRITE.lock').exists())
    def test_cycle_rejected(self):
        n=self.node('ses-revoke');n['parent']='revoke-cas'
        with self.assertRaisesRegex(ValueError,'cycle'):g.apply_patch(self.store,self.proposal(n))
    def test_unknown_source_rejected(self):
        n=self.node();n['source_refs'].append('invented-source')
        with self.assertRaisesRegex(ValueError,'source reference'):g.apply_patch(self.store,self.proposal(n))
    def test_metric_frame_drift_rejected(self):
        n=self.node();n['frame']='new system but old denominator'
        with self.assertRaisesRegex(ValueError,'metric frame out of sync'):g.apply_patch(self.store,self.proposal(n))
    def test_missing_required_mechanism_rejected(self):
        n=self.node();del n['invariant']
        with self.assertRaisesRegex(ValueError,'schema'):g.apply_patch(self.store,self.proposal(n))
    def test_metric_contract_without_missing_rule_rejected(self):
        m=copy.deepcopy(self.data['metrics'][0]);m['missing']=''
        proposal={'expected_revision':self.rev,'reason':'test','upsert_metrics':[m]}
        with self.assertRaisesRegex(ValueError,'incomplete metric'):g.apply_patch(self.store,proposal)
    def test_deleting_referenced_node_requires_refactor(self):
        p={'expected_revision':self.rev,'reason':'test','delete_node_ids':['ses-revoke']}
        with self.assertRaises(ValueError):g.apply_patch(self.store,p)
        self.assertEqual(g.current(self.store),self.rev)
    def test_synthetic_or_unbacked_claim_cannot_be_promoted(self):
        n=self.node();n['status']='observed_in_frame'
        with self.assertRaisesRegex(ValueError,'promotes evidence'):g.apply_patch(self.store,self.proposal(n))
        n['evidence_status']='observed'
        with self.assertRaisesRegex(ValueError,'needs observation'):g.apply_patch(self.store,self.proposal(n))
    def test_snapshot_tampering_detected(self):
        f=self.store/'revisions'/self.rev/'nodes/revoke-cas.json'
        f.write_text(f.read_text(encoding='utf-8')+' ',encoding='utf-8')
        with self.assertRaisesRegex(ValueError,'integrity mismatch'):g.load(self.store)
    def test_failure_before_pointer_swap_keeps_old_revision(self):
        n=self.node();n['open']+=' uncommitted'
        with mock_patch.object(g.os,'replace',side_effect=OSError('simulated pointer-write failure')):
            with self.assertRaises(OSError):g.apply_patch(self.store,self.proposal(n))
        self.assertEqual(g.current(self.store),self.rev)
        self.assertEqual(g.load(self.store)[1],self.data)
        self.assertFalse((self.store/'WRITE.lock').exists())
    def test_existing_lock_is_not_stolen(self):
        lock=self.store/'WRITE.lock';lock.write_text('another writer',encoding='utf-8')
        with self.assertRaisesRegex(ValueError,'lock exists'):g.apply_patch(self.store,self.proposal(self.node()))
        self.assertEqual(lock.read_text(encoding='utf-8'),'another writer')
    def test_canonical_io_excludes_process_and_evidence(self):
        io=g.project_io(self.data)['io_map.json']
        self.assertEqual(len(io['edges']),sum(n['type'] in ['mechanism','step'] for n in self.data['nodes']))
        for e in io['edges']:self.assertEqual(set(e),{'id','source','target','type','frame'})
    def test_search_normalization_vietnamese(self):
        self.assertIn('thu hoi quyen',g.norm('Thu hồi quyền có độ trễ'))
        self.assertEqual(g.norm('ĐỊNH DANH'),'dinh danh')
    def test_add_child_with_derived_containment(self):
        n=self.node();n.update(id='test-child-only',title='Test-only child',parent='revoke-cas')
        n['metric_sketch']['binding']='test-child-only → test fixture'
        g.apply_patch(self.store,self.proposal(n));_,a=g.load(self.store)
        self.assertEqual(len(a['nodes']),len(self.data['nodes'])+1)
        edge=next(e for e in a['edges'] if e['relation']=='contains' and e['target']=='test-child-only')
        self.assertEqual(edge['source'],'revoke-cas')
        self.assertEqual(g.packet(self.store,'test-child-only')['parents_nearest_first'][0]['id'],'revoke-cas')
    def test_portable_export_roundtrip_records(self):
        out=Path(self.temp.name)/'export.jsonl'
        result=subprocess.run([sys.executable,str(ROOT/'graph.py'),'--store',str(self.store),'export','--output',str(out)],capture_output=True,text=True,encoding='utf-8')
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)
        rows=[json.loads(line) for line in out.read_text(encoding='utf-8').splitlines()]
        self.assertTrue(all(row['revision']==self.rev for row in rows))
        exported={r['record']['id']:r['record'] for r in rows if r['record_type']=='node'}
        self.assertEqual(exported,{n['id']:n for n in self.data['nodes']})
        self.assertEqual(len([r for r in rows if r['record_type']=='edge']),len(self.data['edges']))
    def test_cli_vietnamese_utf8_under_legacy_windows_encoding(self):
        env={**os.environ,'PYTHONIOENCODING':'cp1252'}
        result=subprocess.run([sys.executable,str(ROOT/'graph.py'),'--store',str(self.store),'get','revoke-cas'],capture_output=True,env=env)
        self.assertEqual(result.returncode,0,result.stdout.decode('utf-8',errors='replace'))
        packet=json.loads(result.stdout.decode('utf-8'))
        self.assertEqual(packet['node']['title'],self.node()['title'])
        self.assertIn('Conditional write ở điểm commit',packet['node']['aliases'])
        self.assertIn('Giữ cache-entry version nhưng tăng policy epoch',packet['node']['test'])
    def test_search_ranks_actual_phrase_not_word_fragments(self):
        idx=json.loads((self.store/'revisions'/self.rev/'index.json').read_text(encoding='utf-8'))['nodes']
        matches=g.search_index(idx,'thu hoi','mechanism')
        self.assertEqual(matches[0]['id'],'ses-revoke')
        fake=[{'id':'fake','title':'Không phù hợp','type':'mechanism','search':'thuoc thoi gian'}]
        self.assertEqual(g.search_index(fake,'thu hoi'),[])
    def test_english_names_preserve_ids_edges_and_content(self):
        from english_names import NAMES, METRIC_NAMES
        labels=dict(line.split('|') for line in NAMES.splitlines())
        # Audit the rename commit itself; later legitimate graph expansions must remain possible.
        rename_revision=json.loads((ROOT/'rename_receipt.json').read_text(encoding='utf-8-sig'))['revision']
        renamed_folder=self.store/'revisions'/rename_revision
        renamed_nodes=[json.loads(p.read_text(encoding='utf-8')) for p in (renamed_folder/'nodes').glob('*.json')]
        self.assertEqual(set(labels),{n['id'] for n in renamed_nodes})
        for n in self.data['nodes']:self.assertEqual(n['title_language'],'en')
        manifest=json.loads((renamed_folder/'manifest.json').read_text(encoding='utf-8'))
        old_folder=self.store/'revisions'/manifest['parent_revision']
        for n in renamed_nodes:
            self.assertEqual(n['title'],labels[n['id']]);self.assertEqual(n['title_language'],'en')
            old=json.loads((old_folder/'nodes'/f'{n["id"]}.json').read_text(encoding='utf-8'))
            if old['title']!=n['title']:self.assertIn(old['title'],n['aliases'])
            ignore={'title','aliases','title_language','content_language'}
            self.assertEqual({k:v for k,v in n.items() if k not in ignore},{k:v for k,v in old.items() if k not in ignore})
        old_edges=[json.loads(line) for line in (old_folder/'edges.jsonl').read_text(encoding='utf-8').splitlines()]
        renamed_edges=[json.loads(line) for line in (renamed_folder/'edges.jsonl').read_text(encoding='utf-8').splitlines()]
        self.assertEqual(sorted(renamed_edges,key=lambda e:e['id']),sorted(old_edges,key=lambda e:e['id']))
        for m in json.loads((renamed_folder/'metrics.json').read_text(encoding='utf-8')):self.assertEqual(m['title'],METRIC_NAMES[m['id']])

if __name__=='__main__':
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(GraphTests))
    out={'revision':g.current(g.DEFAULT_STORE),'tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'status':'pass' if result.wasSuccessful() else 'fail',
         'scope':'Versioned graph, partial loading, schema, atomic update protocol, reference integrity; no production security claim.'}
    (ROOT/'data/graph_test_results.json').write_text(g.pretty(out),encoding='utf-8')
    raise SystemExit(0 if result.wasSuccessful() else 1)
