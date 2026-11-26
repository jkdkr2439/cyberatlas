"""Machine-first, versioned concept graph. No UI, no network, no background process.

Canonical records live in graph/revisions/<CURRENT>/; never edit revisions in place.
Only apply commits new revisions, after schema and semantic validation.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse, copy, hashlib, json, os, re, sys, tempfile, unicodedata
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parent
DEFAULT_STORE=ROOT/'graph'
ID_PATTERN=r'^[A-Za-z0-9][A-Za-z0-9_.-]*$'
SCHEMA={
 '$schema':'https://json-schema.org/draft/2020-12/schema',
 'title':'Cybersecurity concept node v1','type':'object',
 'required':['id','type','title','parent','status','provenance','frame'],
 'properties':{'id':{'type':'string','pattern':ID_PATTERN},'title':{'type':'string','minLength':1},
  'parent':{'type':['string','null']},'frame':{'type':'string','minLength':1},'status':{'type':'string','minLength':1},
  'provenance':{'type':'string','minLength':1},'type':{'enum':['root','domain','mechanism','journey','step','frontier']}},
 'allOf':[
  {'if':{'properties':{'type':{'const':'domain'}}},'then':{'required':['goal','scope','variables','resources']}},
  {'if':{'properties':{'type':{'const':'mechanism'}}},'then':{'required':['domain','condition','input','process','output','data','invariant','failure','control','measure','test','tradeoff','open','reopen','metric_sketch','source_refs','evidence_status']}},
  {'if':{'properties':{'type':{'const':'journey'}}},'then':{'required':['goal','boundary','cards','steps','branches','reopen']}},
  {'if':{'properties':{'type':{'const':'step'}}},'then':{'required':['journey','order','process','observable','goal']}},
  {'if':{'properties':{'type':{'const':'frontier'}}},'then':{'required':['question','related','reopen']}}
 ]}

def serial(obj):return json.dumps(obj,ensure_ascii=False,sort_keys=True,separators=(',',':'))
def sha(data):return hashlib.sha256(data).hexdigest()
def pretty(obj):return json.dumps(obj,ensure_ascii=False,indent=2)+'\n'
def norm(s):return ''.join(c for c in unicodedata.normalize('NFD',str(s).lower().replace('đ','d')) if not unicodedata.combining(c))
def search_index(index,query,node_type=None):
    phrase=norm(query).strip();terms=re.findall(r'\w+',phrase)
    def contains_words(text):return all(re.search(r'\b'+re.escape(t)+r'\b',text) for t in terms)
    items=[n for n in index if contains_words(n['search']) and (not node_type or n['type']==node_type)]
    # Navigation relevance only: exact title prefix, title phrase, title words, then body phrase.
    def ranking(n):
        labels=[norm(n['title'])]+[norm(alias) for alias in n.get('aliases',[])]
        return (not any(label.startswith(phrase) for label in labels),not any(phrase in label for label in labels),not any(contains_words(label) for label in labels),phrase not in n['search'],norm(n['title']))
    return sorted(items,key=ranking)
def require(ok,msg):
    if not ok:raise ValueError(msg)
def edge_id(e):return 'e-'+sha(serial([e['source'],e['relation'],e['target'],e['layer']]).encode())[:20]
def emit(obj):print(pretty(obj),end='')

def normalize(dataset):
    a=copy.deepcopy(dataset); lookup={n['id']:n for n in a['nodes']}
    for n in a['nodes']:
        n.setdefault('provenance','analyst_authored')
        n.setdefault('frame',n.get('scope') or n.get('boundary') or lookup.get(n.get('domain'),{}).get('scope') or 'Bounded educational cybersecurity model; no organization data.')
    # Containment is generated from parent; clients never maintain two competing hierarchies.
    a['edges']=[e for e in a['edges'] if e['relation']!='contains']
    for n in a['nodes']:
        if n['parent'] is not None:
            a['edges'].append(dict(source=n['parent'],target=n['id'],relation='contains',layer='containment'))
    for e in a['edges']:e['id']=edge_id(e)
    a.setdefault('observations',[])
    return a

def validate(a):
    validator=Draft202012Validator(SCHEMA)
    ids=[n.get('id') for n in a['nodes']]
    require(len(ids)==len(set(ids)),'duplicate node IDs')
    lookup={n['id']:n for n in a['nodes']}
    require('root' in lookup and lookup['root']['type']=='root','missing root')
    source_ids={s['id'] for s in a['sources']}
    require(len(source_ids)==len(a['sources']),'duplicate source IDs')
    observation_ids={o['id'] for o in a.get('observations',[])}
    require(len(observation_ids)==len(a.get('observations',[])),'duplicate observation IDs')
    for n in a['nodes']:
        errors=list(validator.iter_errors(n))
        require(not errors,f'schema {n["id"]}: '+('; '.join(e.message for e in errors)))
        require((n['parent'] is None)==(n['id']=='root'),'exactly one root must have null parent')
        seen=set();cur=n
        while cur['parent'] is not None:
            require(cur['id'] not in seen,'containment cycle at '+n['id']);seen.add(cur['id'])
            require(cur['parent'] in lookup,'dangling parent '+cur['parent']);cur=lookup[cur['parent']]
        if n.get('domain'):
            require(n['domain'] in lookup and lookup[n['domain']]['type']=='domain','invalid domain '+n['id'])
            require(n['domain'] in seen or n['parent']==n['domain'],'domain not an ancestor '+n['id'])
        require(set(n.get('source_refs',[]))<=source_ids,'unknown source reference '+n['id'])
        if n['type']=='mechanism':
            require(n['status'] in ['mapped_not_observed','observed_in_frame','contradicted_in_frame','ambiguous'],'unknown mechanism status')
            if n['status'] in ['observed_in_frame','contradicted_in_frame']:
                require(n['evidence_status'] not in ['proposed_test_not_run_on_real_system','not_observed'],'status promotes evidence without observation')
            for key in ['condition','input','process','output','data','invariant','failure','control','measure','test','tradeoff','open','reopen']:
                require(isinstance(n[key],str) and bool(n[key].strip()),'empty mechanism field '+key)
            require(n['metric_sketch'].get('domain')==n['frame'],'metric frame out of sync '+n['id'])
            require(n['metric_sketch'].get('q')==n['measure'],'metric question out of sync '+n['id'])
            require(n['metric_sketch'].get('conditions')==n['condition'],'metric conditions out of sync '+n['id'])
            if n['evidence_status'] not in ('proposed_test_not_run_on_real_system','not_observed'):
                refs=n.get('observation_refs',[])
                require(refs and set(refs)<=observation_ids,'evidence promotion needs observation records '+n['id'])
                require(all(o.get('kind')=='organization_observation' and o.get('node_id')==n['id'] and o.get('frame')==n['frame'] for o in a['observations'] if o['id'] in refs),'evidence scope/kind mismatch '+n['id'])
        if n['type']=='journey':
            require(n['cards'] and all(x in lookup and lookup[x]['type']=='mechanism' for x in n['cards']),'invalid journey cards')
            require(n['steps'] and len(set(n['steps']))==len(n['steps']),'invalid journey step list')
            for i,sid in enumerate(n['steps'],1):
                require(sid in lookup and lookup[sid]['type']=='step','dangling journey step')
                s=lookup[sid];require(s['parent']==n['id'] and s['journey']==n['id'] and s['order']==i,'journey ordering mismatch')
            require(any('OPEN' in x for x in n['branches']),'journey needs OPEN alternative')
        if n['type']=='step':
            require(n['journey'] in lookup and n['id'] in lookup[n['journey']]['steps'],'orphan step')
        if n['type']=='frontier':require(n['related'] in lookup,'frontier related node missing')
    edge_ids=set()
    for e in a['edges']:
        require(e['source'] in lookup and e['target'] in lookup,'dangling edge')
        require(e['id']==edge_id(e),'edge identity mismatch')
        require(e['id'] not in edge_ids,'duplicate edge');edge_ids.add(e['id'])
        if e['relation']=='contains':require(lookup[e['target']]['parent']==e['source'],'inconsistent containment')
        else:require(bool(e.get('condition','').strip()),'relation must state condition')
    metric_ids=set()
    for m in a['metrics']:
        require(m['id'] not in metric_ids,'duplicate metric');metric_ids.add(m['id'])
        require(m['journey'] in lookup and lookup[m['journey']]['type']=='journey','metric journey missing')
        for k in ['q','domain','conditions','goal','baseline','scale','time','data','method','missing','bias','consequence','binding','status']:
            require(isinstance(m.get(k),str) and bool(m[k].strip()),'incomplete metric '+m['id']+': '+k)
    for o in a.get('observations',[]):
        require(o.get('node_id') in lookup,'observation node missing')
        require(o.get('kind') in ['organization_observation','synthetic_result'],'unknown observation kind')
        require(o.get('frame') and o.get('method') and o.get('limitations') and o.get('observed_at'),'unqualified observation')
        require(o.get('artifact_ref') and re.fullmatch(r'[a-f0-9]{64}',o.get('artifact_sha256','')),'observation requires artifact and hash')
        # An artifact/hash binds a record, but does not by itself prove the observation is true.
    return {'valid':True,'nodes':len(ids),'edges':len(a['edges']),'metrics':len(a['metrics']),'observations':len(a.get('observations',[]))}

def project_io(a):
    io_nodes=[];edges=[];processes=[];evidence=[];lookup={n['id']:n for n in a['nodes']}
    for n in a['nodes']:
        if n['type']=='mechanism':
            src=n['id']+':I';dst=n['id']+':O';eid=n['id']+':flow'
            io_nodes += [dict(id=src,title='Input: '+n['title'],phenomenon=n['input'],frame=n['frame']),dict(id=dst,title='Output: '+n['title'],phenomenon=n['output'],frame=n['frame'])]
            edges.append(dict(id=eid,source=src,target=dst,type='I_TO_O',frame=n['frame']))
            processes.append(dict(id='P:'+n['id'],edge_id=eid,process=n['process'],invariant=n['invariant'],control=n['control'],failure=n['failure'],retained_data=n['data'],status='analyst_model'))
            evidence.append(dict(id='E:'+n['id'],mechanism_id='P:'+n['id'],source_refs=n['source_refs'],proposed_test=n['test'],status=n['evidence_status'],observation_refs=n.get('observation_refs',[])))
        if n['type']=='journey':
            src=n['id']+':S0';io_nodes.append(dict(id=src,title='Initial State: '+n['title'],phenomenon='Trạng thái đầu cho mục tiêu: '+n['goal'],frame=n['frame']))
            for i,sid in enumerate(n['steps'],1):
                s=lookup[sid];dst=n['id']+':S'+str(i);eid=n['id']+':flow'+str(i)
                io_nodes.append(dict(id=dst,title=s['title'],phenomenon=s['title'],frame=n['frame']))
                edges.append(dict(id=eid,source=src,target=dst,type='I_TO_O',frame=n['frame']))
                processes.append(dict(id='P:'+sid,edge_id=eid,process=s['process'],expected_observation=s['observable'],status='analyst_model'))
                evidence.append(dict(id='E:'+sid,mechanism_id='P:'+sid,proposed_observation=s['observable'],status='not_observed'))
                src=dst
    return {'io_map.json':{'nodes':io_nodes,'edges':edges},'mechanisms.json':processes,'evidence.json':evidence}

def current(store):
    name=(store/'CURRENT').read_text(encoding='utf-8').strip()
    require(bool(re.fullmatch(r'r[0-9]{6}-[a-f0-9]{16}',name)),'invalid CURRENT revision')
    return name

def load(store,verify_hashes=True):
    rev=current(store);folder=store/'revisions'/rev
    manifest=json.loads((folder/'manifest.json').read_text(encoding='utf-8'))
    require(manifest['revision']==rev,'manifest revision mismatch')
    if verify_hashes:
        for rel,digest in manifest['files'].items():
            p=(folder/rel).resolve()
            require(p.is_relative_to(folder.resolve()),'unsafe manifest path')
            require(p.is_file() and sha(p.read_bytes())==digest,'snapshot integrity mismatch: '+rel)
    idx=json.loads((folder/'index.json').read_text(encoding='utf-8'))
    nodes=[json.loads((folder/n['file']).read_text(encoding='utf-8')) for n in idx['nodes']]
    data={'nodes':nodes,'edges':[json.loads(line) for line in (folder/'edges.jsonl').read_text(encoding='utf-8').splitlines() if line],
          **{key:json.loads((folder/(key+'.json')).read_text(encoding='utf-8')) for key in ['metrics','sources','observations']}}
    return rev,data

def save_snapshot(store,a,parent,reason):
    a=normalize(a);validate(a)
    count=1 if parent is None else int(parent[1:7])+1
    rev=f'r{count:06}-'+sha(serial({'parent':parent,'data':a}).encode())[:16]
    folder=store/'revisions'/rev
    require(not folder.exists(),'revision already exists; inspect abandoned snapshot')
    folder.mkdir(parents=True)
    files={}
    def put(rel,data):
        p=folder/rel;p.parent.mkdir(parents=True,exist_ok=True)
        raw=data.encode('utf-8');p.write_bytes(raw);files[rel]=sha(raw)
    index=[]
    for n in sorted(a['nodes'],key=lambda x:x['id']):
        rel='nodes/'+n['id']+'.json';put(rel,pretty(n))
        index.append({**{k:n.get(k) for k in ['id','type','title','parent','domain','status']},'file':rel,'sha256':files[rel],
                      'aliases':n.get('aliases',[]),'search':norm(serial(n))})
    put('index.json',pretty({'revision':rev,'nodes':index}))
    put('edges.jsonl',''.join(serial(e)+'\n' for e in sorted(a['edges'],key=lambda x:x['id'])))
    for key in ['metrics','sources','observations']:put(key+'.json',pretty(a[key]))
    for name,data in project_io(a).items():put(name,pretty(data))
    put('node.schema.json',pretty(SCHEMA))
    # Snapshot files are immutable by convention; their hashes are checked before mutation.
    manifest=dict(schema_version='1.0',revision=rev,parent_revision=parent,reason=reason,
                  created_utc=datetime.now(timezone.utc).isoformat(),files=files,counts=validate(a),
                  canonical=['nodes/*.json','edges.jsonl','metrics.json','sources.json','observations.json'],
                  derived=['index.json','io_map.json','mechanisms.json','evidence.json'])
    (folder/'manifest.json').write_text(pretty(manifest),encoding='utf-8')
    # The tiny pointer is the only mutable commit point. A crash before this leaves old CURRENT intact.
    temp=store/('CURRENT.'+str(os.getpid())+'.tmp')
    with temp.open('w',encoding='utf-8') as f:
        f.write(rev+'\n');f.flush();os.fsync(f.fileno())
    os.replace(temp,store/'CURRENT')
    return manifest

def apply_patch(store,patch,dry_run=False):
    allowed={'expected_revision','reason','upsert_nodes','delete_node_ids','upsert_edges','delete_edge_ids','upsert_metrics','delete_metric_ids','upsert_sources','upsert_observations'}
    require(set(patch)<=allowed,'unknown patch keys: '+str(set(patch)-allowed))
    require(patch.get('expected_revision') and patch.get('reason'),'patch needs expected_revision and reason')
    lock=store/'WRITE.lock';store.mkdir(parents=True,exist_ok=True)
    try:fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
    except FileExistsError:raise ValueError('writer lock exists; inspect owner/process before manual recovery')
    try:
        os.write(fd,pretty({'pid':os.getpid(),'expected_revision':patch['expected_revision']}).encode());os.close(fd)
        rev,a=load(store)
        require(rev==patch['expected_revision'],'stale revision; reload and rebase patch')
        def merge(key,upsert,delete):
            records={x['id']:x for x in a[key]}
            for rid in patch.get(delete,[]):
                require(rid in records,'delete target missing: '+rid);del records[rid]
            values=patch.get(upsert,[])
            require(len({x['id'] for x in values})==len(values),'duplicate upsert IDs')
            for value in values:records[value['id']]=value
            a[key]=list(records.values())
        merge('nodes','upsert_nodes','delete_node_ids')
        # IDs of edges are stable on endpoints/relation/layer; a condition update preserves identity.
        for e in patch.get('upsert_edges',[]):
            require(e.get('relation')!='contains','edit parent on node; containment is derived')
            require(e.get('id')==edge_id(e),'upsert edge needs correct deterministic id')
        merge('edges','upsert_edges','delete_edge_ids');merge('metrics','upsert_metrics','delete_metric_ids')
        merge('sources','upsert_sources','_no_source_deletion');merge('observations','upsert_observations','_no_observation_deletion')
        a=normalize(a);report=validate(a)
        if dry_run:return {'dry_run':True,'current_revision':rev,**report}
        return save_snapshot(store,a,rev,patch['reason'])
    finally:
        if lock.exists():lock.unlink()

def packet(store,node_id,max_chars=22000):
    # Select via index, then load only the requested node and compact context records.
    rev=current(store);folder=store/'revisions'/rev
    idx=json.loads((folder/'index.json').read_text(encoding='utf-8'));items={n['id']:n for n in idx['nodes']}
    require(node_id in items,'node not found')
    def get(nid):
        item=items[nid];raw=(folder/item['file']).read_bytes()
        require(sha(raw)==item['sha256'],'node integrity mismatch '+nid)
        return json.loads(raw)
    n=get(node_id);parents=[];p=n['parent']
    while p:
        pn=get(p);parents.append({k:pn[k] for k in ['id','title','type','frame','goal','invariant'] if k in pn});p=pn['parent']
    all_edges=[json.loads(line) for line in (folder/'edges.jsonl').read_text(encoding='utf-8').splitlines() if line]
    edges=[e for e in all_edges if node_id in (e['source'],e['target'])]
    neighbors=sorted({e['target'] if e['source']==node_id else e['source'] for e in edges})
    out={'revision':rev,'node':n,'parents_nearest_first':parents,'edges':[], 'neighbor_summaries':[],
         'omitted_edges':len(edges),'omitted_neighbors':len(neighbors),
         'next_read':'graph.py get <neighbor-id>; graph.py metric <M-id>; graph.py validate before editing. Keep frame, missing data and OPEN explicit.'}
    require(len(pretty(out))<=max_chars,'max-chars too small for full node plus mandatory parent context')
    for e in edges:
        trial=copy.deepcopy(out);trial['edges'].append(e);trial['omitted_edges']-=1
        if len(pretty(trial))<=max_chars:out=trial
    for nid in neighbors:
        item=items[nid];summary={k:item[k] for k in ['id','title','type','parent','domain','status']}
        trial=copy.deepcopy(out);trial['neighbor_summaries'].append(summary);trial['omitted_neighbors']-=1
        if len(pretty(trial))<=max_chars:out=trial
    return out

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--store',type=Path,default=DEFAULT_STORE)
    sub=parser.add_subparsers(dest='command',required=True)
    sub.add_parser('init');sub.add_parser('validate');sub.add_parser('stats');sub.add_parser('revision')
    p=sub.add_parser('get');p.add_argument('id');p.add_argument('--max-chars',type=int,default=22000)
    p=sub.add_parser('search');p.add_argument('query');p.add_argument('--type');p.add_argument('--limit',type=int,default=20)
    p=sub.add_parser('children');p.add_argument('id')
    p=sub.add_parser('metric');p.add_argument('id')
    p=sub.add_parser('source');p.add_argument('id')
    p=sub.add_parser('export');p.add_argument('--output',type=Path,required=True)
    p=sub.add_parser('apply');p.add_argument('patch',type=Path);p.add_argument('--dry-run',action='store_true')
    p=sub.add_parser('edge-id');p.add_argument('record',type=Path)
    args=parser.parse_args();store=args.store
    if args.command=='init':
        require(not (store/'CURRENT').exists(),'store already initialized; use apply')
        seed=json.loads((ROOT/'data/atlas.json').read_text(encoding='utf-8'))
        a={k:seed[k] for k in ['nodes','edges','metrics','sources']};a['observations']=[]
        emit(save_snapshot(store,a,None,'Import authored cybersecurity map; machine-first graph requested by user.'));return
    if args.command=='revision':emit({'revision':current(store)});return
    if args.command=='get':emit(packet(store,args.id,args.max_chars));return
    if args.command=='edge-id':emit({'id':edge_id(json.loads(args.record.read_text(encoding='utf-8-sig')))});return
    if args.command=='apply':emit(apply_patch(store,json.loads(args.patch.read_text(encoding='utf-8-sig')),args.dry_run));return
    if args.command in ['search','children']:
        rev=current(store);index=json.loads((store/'revisions'/rev/'index.json').read_text(encoding='utf-8'))['nodes']
        if args.command=='search':
            items=search_index(index,args.query,args.type);limit=max(0,args.limit)
        else:items=[n for n in index if n['parent']==args.id];limit=len(items)
        emit({'revision':rev,'total':len(items),'returned':min(limit,len(items)),'nodes':[{k:n[k] for k in ['id','title','type','parent','domain','status']} for n in items[:limit]]});return
    rev,a=load(store)
    if args.command=='validate':emit({'revision':rev,'snapshot_hashes':'verified',**validate(a)})
    elif args.command=='metric':
        m=next((m for m in a['metrics'] if m['id']==args.id),None);require(m is not None,'metric not found');emit({'revision':rev,'metric':m})
    elif args.command=='source':
        s=next((s for s in a['sources'] if s['id']==args.id),None);require(s is not None,'source not found');emit({'revision':rev,'source':s})
    elif args.command=='export':
        records=[{'record_type':'metadata','revision':rev,'schema_version':'1.0','canonical':False,'note':'Portable snapshot; edit through revision-checked patches, not this export.'}]
        for key,kind in [('nodes','node'),('edges','edge'),('metrics','metric'),('sources','source'),('observations','observation')]:
            records.extend({'record_type':kind,'revision':rev,'record':record} for record in a[key])
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(''.join(serial(r)+'\n' for r in records),encoding='utf-8')
        emit({'revision':rev,'path':str(args.output.resolve()),'records':len(records),'sha256':sha(args.output.read_bytes())})
    elif args.command=='stats':
        counts={};lookup={n['id']:n for n in a['nodes']};depth=0
        for n in a['nodes']:
            counts[n['type']]=counts.get(n['type'],0)+1;d=0;p=n['parent']
            while p:d+=1;p=lookup[p]['parent']
            depth=max(depth,d)
        emit({'revision':rev,'nodes_by_type':counts,'edges':len(a['edges']),'detailed_metrics':len(a['metrics']),'max_containment_edges_from_root':depth,'organization_observations':len(a['observations'])})

if __name__=='__main__':
    # Windows pipes may default to a legacy code page; the machine contract is UTF-8 JSON.
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
    try:main()
    except (ValueError,OSError,KeyError,TypeError) as e:
        emit({'error':str(e),'command_failed':True});raise SystemExit(2)
