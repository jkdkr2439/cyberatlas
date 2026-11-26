"""Refresh small reading indexes and validation report from CURRENT; no UI."""
from pathlib import Path
import json
import graph

ROOT=Path(__file__).resolve().parent
revision,a=graph.load(graph.DEFAULT_STORE)
result=graph.validate(a)
lookup={n['id']:n for n in a['nodes']}
rows=['# English node index\n',f'Revision: `{revision}`. Canonical pointer: `graph/CURRENT`. Descriptions remain Vietnamese; previous labels are aliases.\n',
      '| ID | English title | Type | Parent |\n|---|---|---|---|']
for n in sorted(a['nodes'],key=lambda n:n['id']):
    rows.append(f'| `{n["id"]}` | {n["title"]} | {n["type"]} | `{n["parent"] or "—"}` |')
(ROOT/'NODE_INDEX.md').write_text('\n'.join(rows)+'\n',encoding='utf-8')
tests=json.loads((ROOT/'data/graph_test_results.json').read_text(encoding='utf-8'))
seed=json.loads((ROOT/'data/validation.json').read_text(encoding='utf-8'))
examples=json.loads((ROOT/'data/synthetic_examples.json').read_text(encoding='utf-8'))
assert tests['revision']==revision and tests['status']=='pass', 'Need passing tests for CURRENT before publishing report'
assert seed['status']=='pass'
report=f'''# Validation record

Current graph revision: `{revision}`.

- **{tests['tests']} graph/update tests passed.** Covers selective reads, complete parent context, explicit context budgets, adding/updating nodes, derived containment/IO, concurrent writers, stale revisions, failed commit rollback, dangling edges, cycles, unknown sources, metric/frame drift, unsupported evidence promotion, snapshot checksums, UTF-8 under a legacy Windows code page, bilingual search, portable export, and English-label migration integrity.
- **{seed['checks_run']} seed/integrity/arithmetic tests passed.** Includes malformed-reference/cycle mutations, source-book hashes and heading anchors, recursive parent chain, IO/evidence separation and missing denominator/overlapping interval handling.
- **{len(examples)} synthetic measurement examples ran.** They demonstrate base-rate changes, missing observation coverage, misleading patch ratios, censored revocation times, overlapping exposure intervals, business recovery versus server uptime, MFA fallback gaps, proposed versus executed agent actions, and signer checks versus deployment policy.
- CURRENT contains **{len(a['nodes'])} nodes, {len(a['edges'])} edges, {len(a['metrics'])} detailed metric contracts**, and **{len(a['observations'])} organization observations**. All node and metric titles are English; stable IDs, semantic content and graph relations were preserved during renaming.
- English renaming was committed through the same revision-checked patch API, from revision 1 to revision 2. Update/concurrency/failure tests ran only in temporary copies and did not add test nodes to CURRENT.

## What these tests do not establish

They check the machine-readable artifact, update protocol, retrieval behavior and arithmetic of toy examples. They do not test a real firewall, IAM deployment, security agent, clinical device, production incident response or every technical statement in the map. No real security scans or exploitation were performed. Source-document overview reads remain distinguished from detailed technical review in SOURCES.md.

## Reproduce

```powershell
python graph.py validate
python test_graph.py
python validate.py
python synthetic_examples.py
```

Runtime used: CPython 3.12.10 and jsonschema 4.23.0. The original source book remains unchanged. No visual interface or background server is required.

Machine-readable reports: `data/graph_test_results.json`, `data/validation.json`, `data/synthetic_examples.json`.
'''
(ROOT/'VALIDATION.md').write_text(report,encoding='utf-8')
print(json.dumps({'revision':revision,'published':['NODE_INDEX.md','VALIDATION.md'],'graph_tests':tests['tests'],'seed_tests':seed['checks_run'],'synthetic_examples':len(examples)}))
