from pathlib import Path
import json, copy, hashlib, unittest, os
from synthetic_examples import run, ratio, duration_union
from source_config import external_source

ROOT=Path(__file__).resolve().parent
def read(name):return json.loads((ROOT/name).read_text(encoding='utf-8'))

def validate_atlas(a):
    ns=a['nodes']; ids=[n['id'] for n in ns]
    assert len(ids)==len(set(ids)), 'duplicate node'
    lookup={n['id']:n for n in ns}
    assert lookup['root']['parent'] is None
    for n in ns:
        if n['parent'] is not None: assert n['parent'] in lookup,'missing parent'
        seen=set(); cur=n
        while cur['parent'] is not None:
            assert cur['id'] not in seen,'containment cycle'
            seen.add(cur['id']);cur=lookup[cur['parent']]
        assert cur['id']=='root','unreachable'
        if n['type']=='mechanism':
            for k in ['frame','input','process','output','data','invariant','failure','control','measure','test','tradeoff','open','reopen']:
                assert n.get(k),'missing mechanism field '+k
            assert n['metric_sketch']['status']=='candidate_missing_data'
            assert len(n['six_regions'])==6
            assert n['book_anchor']['line']<=n['book_anchor']['end_line']
        if n['type']=='journey':
            assert len(n['steps'])==8
            assert all(x in lookup for x in n['cards']+n['steps'])
            assert len(n['branches'])>=3 and any('OPEN' in b for b in n['branches'])
    for e in a['edges']:
        assert e['source'] in lookup and e['target'] in lookup,'dangling edge'
        if e['relation']!='contains':assert e.get('condition'),'missing relation condition'
    for m in a['metrics']:
        for k in ['q','domain','conditions','goal','baseline','scale','time','data','method','missing','bias','consequence','binding']:
            assert m.get(k),'missing metric contract '+k
        assert m['journey'] in lookup
    return True

class Checks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.a=read('data/atlas.json')
    def test_actual_graph(self):self.assertTrue(validate_atlas(self.a))
    def test_reject_dangling_link(self):
        a=copy.deepcopy(self.a);a['edges'][0]['target']='missing-node'
        with self.assertRaisesRegex(AssertionError,'dangling'):validate_atlas(a)
    def test_reject_containment_cycle(self):
        a=copy.deepcopy(self.a);a['nodes'][1]['parent']=a['nodes'][1]['id']
        with self.assertRaisesRegex(AssertionError,'cycle'):validate_atlas(a)
    def test_reject_unqualified_metric(self):
        a=copy.deepcopy(self.a);a['metrics'][0]['conditions']=''
        with self.assertRaisesRegex(AssertionError,'metric contract'):validate_atlas(a)
    def test_io_separation(self):
        io=read('data/io_map.json');ids={n['id'] for n in io['nodes']}
        self.assertEqual(len(ids),len(io['nodes']))
        for e in io['edges']:
            self.assertEqual(e['type'],'I_TO_O');self.assertIn(e['source'],ids);self.assertIn(e['target'],ids)
            self.assertEqual(set(e),{'id','source','target','type','frame'})
        edges={e['id'] for e in io['edges']}
        processes=read('data/mechanisms.json');pids={p['id'] for p in processes}
        self.assertEqual(len(edges),len(processes))
        for p in processes:self.assertIn(p['edge_id'],edges)
        for e in read('data/evidence.json'):self.assertIn(e['mechanism_id'],pids)
    def test_source_hash_unchanged(self):
        s=read('data/source_index.json')
        if os.environ.get('CYBER_ATLAS_EXTERNAL_SOURCE_CHECKS')=='0':
            self.skipTest('External source verification disabled; source books are not bundled')
        book=external_source('book')
        if book is None:
            self.skipTest('Original external book not available; graph tests do not require it')
        self.assertEqual(hashlib.sha256(book.read_bytes()).hexdigest(),s['sha256'])
        lines=book.read_text(encoding='utf-8-sig').splitlines()
        for h in s['headings']:self.assertIn(h['title'],lines[h['line']-1])
    def test_source_index_is_self_contained_metadata(self):
        s=read('data/source_index.json')
        self.assertEqual(len(s['sha256']),64)
        int(s['sha256'],16)
        self.assertTrue(s['headings'])
        self.assertEqual(len({h['id'] for h in s['headings']}),len(s['headings']))
        for h in s['headings']:
            self.assertTrue(h['title']);self.assertGreaterEqual(h['line'],1)
            self.assertGreaterEqual(h['end_line'],h['line'])
    def test_synthetic_counterexamples(self):self.assertEqual(len(run()),9)
    def test_denominator_missing_not_success(self):
        self.assertIsNone(ratio(0,0))
        with self.assertRaises(ValueError):ratio(11,10)
    def test_interval_overlap_clipping(self):
        self.assertEqual(duration_union([(0,5),(2,7),(-10,1),(9,20)],0,10),8)
        self.assertEqual(duration_union([],0,10),0)
    def test_recursive_refinements_have_parent_context(self):
        nodes={n['id']:n for n in self.a['nodes']}
        node=nodes['revoke-cas']
        chain=[]
        while node['parent']:
            chain.append(node['parent']);node=nodes[node['parent']]
        self.assertEqual(chain,['revoke-race','revoke-cache','ses-revoke','session','root'])

if __name__=='__main__':
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(Checks)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    report={'checks_run':result.testsRun,'skipped':len(result.skipped),'failures':len(result.failures),'errors':len(result.errors),
            'status':'pass' if result.wasSuccessful() else 'fail','scope':'Artifact integrity and synthetic metric logic only; no production security validation.'}
    (ROOT/'data/validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    raise SystemExit(0 if result.wasSuccessful() else 1)
