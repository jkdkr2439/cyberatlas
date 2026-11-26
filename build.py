from pathlib import Path
import json, hashlib, re, html
from content import DOMAINS, CARDS, DOMAIN_ORDER, CROSS
from deepdives import JOURNEYS, METRICS
from sources import SOURCES, FRONTIERS
from refinements import expand
from source_config import external_source, source_ref

ROOT = Path(__file__).resolve().parent
BOOK = external_source('book', required=True)
DATE = '2026-11-26'

def dump(path, value):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding='utf-8')

def write(path, text):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding='utf-8')

def link(path):
    return path

book_bytes = BOOK.read_bytes()
book_lines = book_bytes.decode('utf-8-sig').splitlines()
headings = []
for lineno, line in enumerate(book_lines, 1):
    m = re.match(r'^(#{1,6})\s+(.+)', line)
    if m:
        headings.append({'id':f'B{lineno}', 'line':lineno, 'level':len(m[1]), 'title':m[2]})
for i,h in enumerate(headings):
    h['end_line'] = next((n['line']-1 for n in headings[i+1:] if n['level']<=h['level']),len(book_lines))
parts = {}
for h in headings:
    m = re.match(r'Phần\s+(\d+)',h['title'])
    if m and h['level']==2:
        parts[int(m[1])] = h
assert len(parts)==12, parts

sources=[]
for sid,title,url,scope in SOURCES:
    s={'id':sid,'title':title,'url':link(url),'location':url,'checked':DATE,'read_scope':scope}
    if not url.startswith('http'):
        p=external_source(sid, required=True)
        s['sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
    sources.append(s)
dump('data/source_index.json',{'book':source_ref('book'),'sha256':hashlib.sha256(book_bytes).hexdigest(),'headings':headings,'sources':sources})

domains=[]
for row in DOMAINS.splitlines():
    did,title,scope,goal,variables,resources,part,refs=row.split('|')
    domains.append(dict(id=did,title=title,type='domain',parent='root',scope=scope,goal=goal,variables=variables,
                        resources=resources,book_part=int(part),book_anchor=parts[int(part)],source_refs=refs.split(','),
                        status='mapped',provenance='analyst_expansion_from_book'))
by_domain={d['id']:d for d in domains}
keys=['id','title','condition','input','process','output','data','invariant','failure','control','measure','test','tradeoff','open']
cards=[]
for i,row in enumerate(CARDS.splitlines()):
    values=row.split('|')
    assert len(values)==len(keys),(i,len(values))
    c=dict(zip(keys,values)); d=by_domain[DOMAIN_ORDER[i//3]]
    c.update(type='mechanism', parent=d['id'], domain=d['id'], status='mapped_not_observed',
             provenance='analyst_expansion', frame=d['scope']+'; '+c['condition'], goal=d['goal'],
             variables=d['variables'],resources=d['resources'],book_anchor=d['book_anchor'],
             source_refs=['book']+d['source_refs'],
             source_relation='Book: conceptual seed only; primary references: domain context unless SOURCES states a specific inspected passage.',
             reopen=c['open']+' Mở lại khi đổi frame, có counterexample hoặc nguồn mới.',
             evidence_status='proposed_test_not_run_on_real_system')
    c['metric_sketch']={
        'status':'candidate_missing_data','region':'owner_selects_from_six_regions',
        'q':c['measure'],'domain':c['frame'],'conditions':c['condition'], 'goal':c['goal'],
        'baseline':'Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.',
        'scale':'Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.',
        'time':'Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.',
        'data':c['data']+'; bằng chứng test: '+c['test'],
        'method':'Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.',
        'missing':'Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.',
        'limitation':c['tradeoff']+'; '+c['open'],
        'binding':c['id']+' → điểm thực thi: '+c['process']}
    c['six_regions']={
        'meaning':'Phân biệt trạng thái mong muốn với failure: '+c['output']+' / '+c['failure'],
        'domain':'Chốt population và giới hạn: '+c['frame'],
        'mechanism':'Control có giữ invariant này không? '+c['invariant'],
        'evidence':'Quan sát nào có thể bác bỏ kết luận? '+c['test'],
        'operational':'Nguồn lực có đủ và điều kiện nào đổi? '+c['resources']+'; '+c['variables'],
        'consequence':'Đạt '+c['goal']+' nhưng phải theo dõi '+c['tradeoff']}
    cards.append(c)
assert len(cards)==len(domains)*3
cards.extend(expand(cards))
by_card={c['id']:c for c in cards}

nodes=[{'id':'root','type':'root','title':'Cybersecurity · bản đồ cơ chế','parent':None,'status':'bounded_map'}]+domains+cards
edges=[]
for row in CROSS.splitlines():
    a,b,relation,condition=row.split('|')
    edges.append({'source':a,'target':b,'relation':relation,'condition':condition,'layer':'crosslink','provenance':'analyst_proposed'})
frontiers=[]
for i,row in enumerate(FRONTIERS.splitlines(),1):
    did,title,question,related=row.split('|')
    f=dict(id=f'F{i:02}',title=title,type='frontier',parent=did,domain=did,status='OPEN',question=question,
           related=related,reopen='Chọn scope cụ thể và nguồn chuyên ngành; trả lời câu hỏi trước khi sinh metric.',provenance='research_question')
    frontiers.append(f); nodes.append(f)
    edges.append(dict(source=related,target=f['id'],relation='opens_question',condition=question,layer='crosslink'))

io_nodes=[]; io_edges=[]; mechanisms=[]; evidence=[]
for c in cards:
    sid,tid=c['id']+':I',c['id']+':O'
    io_nodes.extend([dict(id=sid,phenomenon=c['input'],frame=c['frame']),dict(id=tid,phenomenon=c['output'],frame=c['frame'])])
    eid=c['id']+':flow'
    io_edges.append(dict(id=eid,source=sid,target=tid,type='I_TO_O',frame=c['frame']))
    mechanisms.append(dict(id='P:'+c['id'],edge_id=eid,process=c['process'],control=c['control'],failure=c['failure'],invariant=c['invariant'],retained_data=c['data'],status='analyst_model'))
    evidence.append(dict(id='E:'+c['id'],mechanism_id='P:'+c['id'],source_refs=c['source_refs'],source_relation=c['source_relation'],proposed_test=c['test'],status='not_tested_in_organization'))

journeys=[]
for j in JOURNEYS:
    card_ids=j['cards']; domain=by_card[card_ids[0]]['domain']
    jj={k:v for k,v in j.items() if k!='steps'}
    jj.update(type='journey',parent=domain,domain=domain,status='analyst_process_model',provenance='analyst_expansion',steps=[])
    nodes.append(jj); journeys.append(jj)
    for card_id in card_ids:
        edges.append(dict(source=j['id'],target=card_id,relation='uses_mechanism',condition=j['goal'],layer='crosslink'))
    before=j['id']+':S0'
    io_nodes.append(dict(id=before,phenomenon='Trạng thái đầu: cần đạt mục tiêu — '+j['goal'],frame=j['boundary']))
    for i,(title,process,observable) in enumerate(j['steps'],1):
        nid=f'{j["id"]}.{i}'; after=j['id']+f':S{i}'; eid=f'{j["id"]}:flow{i}'
        step=dict(id=nid,title=title,type='step',parent=j['id'],domain=domain,journey=j['id'],order=i,
                  process=process,observable=observable,frame=j['boundary'],goal=j['goal'],status='proposed_process_step',provenance='analyst_expansion')
        jj['steps'].append(nid); nodes.append(step)
        io_nodes.append(dict(id=after,phenomenon=title,frame=j['boundary']))
        io_edges.append(dict(id=eid,source=before,target=after,type='I_TO_O',frame=j['boundary']))
        mechanisms.append(dict(id='P:'+nid,edge_id=eid,process=process,expected_observation=observable,status='analyst_model'))
        evidence.append(dict(id='E:'+nid,mechanism_id='P:'+nid,proposed_observation=observable,status='not_observed'))
        if i>1:
            edges.append(dict(source=f'{j["id"]}.{i-1}',target=nid,relation='enables_next',condition='Chỉ tiếp khi trạng thái trước có bằng chứng phù hợp; nếu không giữ unresolved.',layer='process_navigation'))
        before=after

for n in nodes:
    if n['parent']:
        edges.append(dict(source=n['parent'],target=n['id'],relation='contains',layer='containment'))
for m in METRICS:
    m.update(status='candidate_missing_organization_data',provenance='analyst_proposed_metric_contract')

stats={'domains':len(domains),'mechanism_cards':len(cards),'journeys':len(journeys),'process_steps':sum(len(j['steps']) for j in journeys),
       'base_mechanism_cards':78,'recursive_refinements':len(cards)-78,
       'frontiers':len(frontiers),'concept_nodes_including_root':len(nodes),'atlas_edges':len(edges),
       'authored_mechanism_crosslinks':len(CROSS.splitlines()),'metric_sketches':len(cards),'detailed_metric_contracts':len(METRICS),
       'io_phenomena':len(io_nodes),'conditional_io_edges':len(io_edges),'book_headings_indexed':len(headings)}
atlas=dict(meta=dict(title='Cybersecurity · Atlas of Mechanisms',subtitle='Từ ontology đến cơ chế, bằng chứng và phép đo',
                    authoring='Assistant-authored expansion for Kevin T.N.',method='Lens Metric Generation + Pete framing',date=DATE,
                    observed_organization_data=False,stats=stats),nodes=nodes,edges=edges,metrics=METRICS,sources=sources,book_parts=parts)
dump('data/atlas.json',atlas)
dump('data/io_map.json',dict(schema='phenomena-and-conditional-I_TO_O/v1',nodes=io_nodes,edges=io_edges))
dump('data/mechanisms.json',mechanisms)
dump('data/evidence.json',evidence)
dump('data/metrics.json',METRICS)

out=['# Cybersecurity — bản đồ cơ chế\n', 'Biên soạn cho Kevin T.N. · '+DATE+'\n',
     'Đọc [METHOD.md](METHOD.md) để biết frame và mức bằng chứng; dùng [AGENTS.md](AGENTS.md) và graph.py để load/update node. Đây là tài liệu của seed import; graph/CURRENT mới là phiên bản dữ liệu hiện hành. Các test dưới đây là đề xuất, chưa chạy trên hệ thật.\n',
     f'**{len(domains)} miền · {len(cards)} thẻ cơ chế · {len(journeys)} hành trình · {len(frontiers)} frontier OPEN.** Số lượng chỉ mô tả artifact, không đo mức an toàn.\n']
for d in domains:
    out += [f'## {d["title"]}\n',f'**Frame / owner:** {d["scope"]}. **Mục tiêu:** {d["goal"]}.\n',
            f'**Biến:** {d["variables"]}. **Nguồn lực:** {d["resources"]}.\n',
            f'**Nguồn ý tưởng trong sách:** {d["book_anchor"]["title"]}, dòng {d["book_anchor"]["line"]}–{d["book_anchor"]["end_line"]}. Tham chiếu bối cảnh: '+', '.join(d['source_refs'])+'.\n']
    for c in [c for c in cards if c['domain']==d['id']]:
        section=[f'### {c["id"]} — {c["title"]}\n',f'**Điều kiện:** {c["condition"]}.\n',
                 f'- **I:** {c["input"]}\n- **P:** {c["process"]}\n- **O:** {c["output"]}\n- **D:** {c["data"]}\n',
                 f'**Hằng trong frame:** {c["invariant"]}.\n\n**Đường hỏng:** {c["failure"]}. **Điểm can thiệp:** {c["control"]}.\n',
                 f'**Phép đo ứng viên:** {c["measure"]}.\n\n**Test phân biệt / bằng chứng cần:** {c["test"]}.\n',
                 f'**Đánh đổi:** {c["tradeoff"]}.\n\n**OPEN:** {c["open"]}\n']
        related=[e for e in edges if e['layer']=='crosslink' and e['source']==c['id']]
        if related:
            section.append('**Liên hệ có điều kiện:**\n\n'+'\n'.join('- `'+e['target']+'` — '+e['condition'] for e in related)+'\n')
        out.extend(section)
        write('vault/'+c['id']+'.md','\n'.join(section)+'\n\n## Sáu miền review\n\n'+'\n'.join('- **'+k+':** '+v for k,v in c['six_regions'].items())+'\n\n## Metric sketch\n\n'+'\n'.join('- **'+k+':** '+v for k,v in c['metric_sketch'].items())+'\n')
    fs=[f for f in frontiers if f['domain']==d['id']]
    if fs:
        out.append('**Nhánh nghiên cứu chưa mở đủ:**\n\n'+'\n'.join('- '+f['title']+': '+f['question'] for f in fs)+'\n')
write('ATLAS.md','\n'.join(out))

out=['# Tám hành trình đào sâu\n','Các bước là mô hình quá trình có điều kiện do assistant biên soạn; không phải dữ liệu incident thật. Quan hệ thứ tự không được dùng làm độ sâu ontology.\n']
for j in JOURNEYS:
    out += [f'## {j["id"]} — {j["title"]}\n',f'**Mục tiêu:** {j["goal"]}\n\n**Biên:** {j["boundary"]}\n']
    for i,(title,process,obs) in enumerate(j['steps'],1):
        out += [f'### {i}. {title}\n',process+'\n', '**Observable cần có:** '+obs+'\n']
    out += ['**Đối chiếu + OPEN:**\n\n'+'\n'.join('- '+x for x in j['branches'])+'\n', '**Mở lại khi:** '+j['reopen']+'\n', '**Thẻ nối:** '+', '.join(j['cards'])+'\n']
write('DEEP_DIVES.md','\n'.join(out))

out=['# Metric contracts — chưa có dữ liệu tổ chức\n','Tám contract chi tiết và 102 candidate sketches trong các thẻ cơ chế. Không có điểm tổng bảo mật. Đây là bản thuyết minh seed; dữ liệu cập nhật nằm trong graph/CURRENT.\n']
for m in METRICS:
    out += [f'## {m["id"]} — {m["title"]}\n']
    out += [f'**{k}:** {v}\n' for k,v in m.items() if k not in ['id','title']]
write('METRIC_PROFILES.md','\n'.join(out))

out=['# Nguồn và provenance\n',f'Rà ngày {DATE}, Asia/Bangkok. Tham chiếu bối cảnh không đồng nghĩa từng câu đã được nguồn xác nhận. Các thẻ/metric mở rộng do assistant biên soạn; không gán cho NIST/OWASP/Pete hoặc tác giả sách.\n']
for s in sources:
    out += [f'## {s["id"]} — {s["title"]}\n',f'[{s["title"]}]({s["location"]})\n',s['read_scope']+'\n']
    if 'sha256' in s: out.append('SHA-256: `'+s['sha256']+'`\n')
out += ['## Giới hạn truy cập\n','CISA KEV catalog trả 403 ở lượt rà. Không dùng kết quả không truy cập được làm bằng chứng. Việc tìm kiếm KEV/exploitation intelligence khi áp vào môi trường thật vẫn là frontier dữ liệu.\n',
        '## Index sách\n',f'Toàn bộ {len(headings)} heading được index bằng chương trình; việc này không đồng nghĩa đã kiểm định toàn bộ nội dung. Bản gốc không bị sửa.\n',
        '| Phần | Dòng bắt đầu | Dòng kết thúc |\n|---|---:|---:|']
for h in parts.values(): out.append(f'| {h["title"]} | {h["line"]} | {h["end_line"]} |')
write('SOURCES.md','\n'.join(out))
write('FRONTIERS.md','# Nhánh OPEN\n\nKhông được tính các câu hỏi này là cơ chế đã giải thích.\n\n'+'\n\n'.join(f'## {f["id"]} — {f["title"]}\n\n{f["question"]}\n\nNối từ `{f["related"]}`. Mở lại: {f["reopen"]}' for f in frontiers)+'\n')

dump('data/stats.json',stats)
print(json.dumps(stats,ensure_ascii=False))
