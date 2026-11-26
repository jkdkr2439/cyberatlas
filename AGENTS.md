# Machine-first cybersecurity concept graph

The user explicitly wants a node graph that AI can read, load selectively, update and test. **Do not build or launch a visual interface unless asked.** No background services are needed.

Node titles and metric titles must be **English**. Stable IDs must not change when renaming. Previous Vietnamese titles are retained as `aliases` for retrieval. Descriptive content remains Vietnamese unless the user requests its translation. Source-document titles are citations, not node labels, and retain their original wording.

## Repository boundary

This is a standalone Git repository for the atlas, tooling and tests. Do not copy the source security PDF or other full source books into it. Source URNs/hashes/heading indexes are provenance metadata, not runtime dependencies. Never serialize personal filesystem paths or credentials. Optional external documents are resolved only through `source_config.py` and environment variables. `.gitattributes` disables line-ending conversion for checksum-bound snapshot files; preserve that rule. The one external-book hash test skips explicitly when the source is unavailable; do not skip graph validation to compensate for missing source documents.

## Entry and canonical state

1. Read `AI_ENTRYPOINT.json` and `graph/CURRENT`.
2. The canonical snapshot is `graph/revisions/<CURRENT>/`. Its `manifest.json` lists canonical and derived records, checksums and parent revision.
3. `nodes/<id>.json` is one concept/phenomenon-analysis record. `edges.jsonl` carries typed conditional relations. `metrics.json` contains detailed contracts; `sources.json` records what was actually read. `observations.json` is empty until real evidence is supplied.
4. `index.json` is for search/selection, not a separate source of truth. Do not load all large records just to choose a node. Use `graph.py search` then `graph.py get`.
5. `data/`, `ATLAS.md`, `vault/`, `content.py`, `refinements.py`, and `deepdives.py` are the initial authored seed/import or test artifacts. **Do not overwrite current graph changes by rerunning the seed builder/import.** `exports/` is a portable snapshot with a pinned revision, never an edit target.

## Read commands (PowerShell, from this directory)

```powershell
python graph.py revision
python graph.py stats
python graph.py search "thu hoi" --type mechanism --limit 10
python graph.py get revoke-cas --max-chars 22000
python graph.py children ses-revoke
python graph.py metric M01
python graph.py source metric
python graph.py search "" --type frontier --limit 40
```

`get` preserves the full selected node and the parent frame/invariant context. It returns conditional edges and neighbor summaries within the requested **character** budget. Omitted context is explicitly counted. Too small a budget is an error, not a silently truncated definition. Read neighbors separately when the relation matters.

## Decompose before measuring

Use NMF for the observer's naming/meaning/frame. Use IPOD, conditional invariants/variables and resources for the system under analysis. A process step is not a hierarchy level; an analogy is not an identity of mechanisms. Keep constants relative to frame; record uncertainty and outdated assumptions.

Before adding nodes, inspect the parent, adjacent mechanism, existing crosslinks and sources. Reuse a mechanism if changing conditions, ordering or data binding is enough. New children need a distinct operational meaning, a changed decision/test, and a reason they cannot be represented by an existing node. Branch count is not fixed. Keep contrastive routes plus OPEN where useful.

Do not create a security score from node count, paper count, generic severity, or arbitrary weights. Candidate metrics need goal, population, conditions, baseline, scale, time and data. Preserve unknown, unrun, unresolved and censored cases. A zero denominator is undefined. Distinguish control presence, behavior in a test and production consequence.

## Patch protocol

Do **not** edit immutable revision files or `CURRENT` manually. Prepare a UTF-8 JSON patch containing:

```json
{
  "expected_revision": "<the exact CURRENT read before editing>",
  "reason": "Concrete reason and scope for this change",
  "upsert_nodes": ["<complete node objects, not string placeholders>"],
  "delete_node_ids": [],
  "upsert_edges": [],
  "delete_edge_ids": [],
  "upsert_metrics": [],
  "delete_metric_ids": [],
  "upsert_sources": [],
  "upsert_observations": []
}
```

The example placeholders are explanatory and not executable. Retrieve a complete existing node through `get` to prepare an update. Keep its ID. For a new mechanism use the required fields in `node.schema.json` and the existing local conventions. For a changed frame, also update the metric sketch's domain/conditions/question and review affected dependents. `test_graph.py` exercises update/reject behavior in isolated temporary stores.

`parent` is the single containment source; containment edges are derived. Crosslinks require source, target, relation, layer and a condition/limitation. Compute their deterministic ID with `python graph.py edge-id <edge-record.json>` (the initial record may omit `id`); put the returned ID into the edge record. A condition-only edit preserves the edge ID. Changing endpoints/relation requires deleting the old edge ID and inserting the new one.

```powershell
python graph.py apply patch.json --dry-run
python graph.py apply patch.json
python graph.py validate
python test_graph.py
```

On stale revision: reload and rebase; do not force overwrite. On a writer lock: inspect the owner and running process; never blindly remove someone else's lock. If a process dies before pointer swap, old CURRENT remains committed and an orphan revision may remain. Inspect it before recovery; do not claim power-loss durability or hostile-tamper protection from this mechanism.

## Evidence discipline

Source context, proposed tests, synthetic results and organization observations are different. Tests passing on graph tooling do not prove a security control works. Reading a source overview is not an audit of every requirement. Never label an authored hypothesis as a production observation.

Promoting a mechanism to observed/contradicted requires matching observation records, exact frame, method, time, limitations and artifact/hash. The tool checks record structure and linkage; a human/domain reviewer must still assess the evidence. A hash does not prove an event happened. A synthetic result cannot serve as an organization observation.

## Exports and tests

```powershell
python graph.py export --output exports/cybersecurity.nodes.jsonl
python synthetic_examples.py
python validate.py
python test_graph.py
```

`validate.py` checks the seed and synthetic arithmetic. `test_graph.py` checks the canonical graph protocol in copied temporary stores. For ongoing content edits, `graph.py validate` checks CURRENT; the original seed's cardinality is not the acceptance criterion for new graph revisions. After updates, refresh exported snapshots and report the current revision, changed IDs, test results and unresolved frontiers.
