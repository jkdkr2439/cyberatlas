# Graph data dictionary

## Identity, naming, and scope

`id` is stable identity. `title` is the current English label. `aliases` preserves earlier labels for search; it is not a list of equivalent concepts. `title_language` describes the label and `content_language` describes the analysis body. `frame` defines where the claim applies. Source titles and quoted source headings retain their original language.

`parent` expresses containment/decomposition, not temporal order or causation. `domain` must be an ancestor. The deepest current branch has five containment edges from root. Eight-step journeys describe a process and must not be reported as eight ontology levels.

## Node types

| type | Meaning | Distinctive fields |
|---|---|---|
| root | Bounded purpose of this map | frame |
| domain | A cybersecurity scope and ownership lens | scope, goal, variables, resources |
| mechanism | A conditioned transformation and its possible failure/control | input, process, output, data, condition, invariant, failure, control, test, tradeoff, open |
| journey | A process model connecting several mechanisms | boundary, goal, cards, ordered steps, branches, reopen |
| step | A proposed transformation inside a journey | journey, order, process, observable |
| frontier | An unresolved research question | question, related, reopen |

Mechanism records also include a metric sketch and six review regions. Those fields are analytical views of the same mechanism, not six additional mechanisms. `resources` and `variables` may be inherited from the domain; binding them to a specific organization remains work to do.

## Relations

Every edge has a deterministic ID derived from source, relation, target and layer. A change to its condition preserves its identity. A change to endpoints or relation creates a different edge.

| Layer / relation family | Interpretation |
|---|---|
| containment / contains | Derived exclusively from node.parent; not a causal assertion |
| process_navigation / enables_next | Proposed order in a journey; preceding state requires appropriate evidence |
| crosslink / uses_mechanism | A journey draws on a mechanism; not parent-child identity |
| crosslink / requires, depends_on, depends_for_recovery | Conditional dependency; read the condition before inferring necessity |
| crosslink / constrains, conditions, compensates_conditionally | A condition or control changes reachable behavior in a stated frame |
| crosslink / feeds, informs, supports, enables, feedback | An output/information relationship; check consumer and return path |
| crosslink / does_not_imply, tradeoff | Explicit limit on an inference or a competing consequence |
| crosslink / same_*_pattern, analogy_only, specializes | An analytical mapping; does not prove identical implementation or causal mechanism |
| crosslink / can_affect, can_be_bypassed_by, drives_load | A proposed conditional influence; no unconditional probability is attached |
| crosslink / opens_question | Connects an authored mechanism to an unresolved frontier |

The authoritative qualification for each edge is its `condition`, not the relation label alone. New relation types should have a precise operational meaning, rather than introducing synonyms without a distinction. A crosslink is assistant-authored analysis unless separate evidence establishes more.

## Canonical records and derived IO projection

Canonical snapshot: node files, edges.jsonl, metrics.json, sources.json, observations.json. The manifest binds files to hashes and a revision. `CURRENT` points to the committed snapshot. Hashes detect unintended file changes; this is not a hostile-tamper-proof database.

The derived IO map has 276 phenomenon nodes and 166 conditional I_TO_O edges at the initial English-label revision. `title` is the English phenomenon label; `phenomenon` and `frame` retain explanatory content. Process explanations are in mechanisms.json and evidence/test plans are in evidence.json. Do not add a process or evidence claim directly to an IO edge. Rebuild projections through a graph commit rather than editing them independently.

## Metrics and evidence

A metric sketch is a candidate question attached to a mechanism. Its frame, question and conditions must remain consistent with the mechanism when edited. Eight detailed metric records additionally specify baseline, scale, time, required data, method, missing-data rule, bias, consequences and execution binding. They are not production observations.

An organization observation needs node identity, exact frame, method, observed_at, limitations, artifact reference and hash. Synthetic results use a different kind and cannot promote a mechanism to an observed organization state. The updater validates record linkage, not the truth of a supplied account or the validity of a scientific claim.

Unknown, unrun, unresolved and time-censored cases must remain visible. A missing source is not a benign event; an empty denominator is not a perfect score. No overall security score is defined by this graph.

## Version and failure behavior

Patches use whole-record upserts and the exact expected_revision. Validation precedes writing a new immutable snapshot. An exclusive writer lock prevents simultaneous writers; the final atomic pointer replacement is the commit point. A stale patch must be rebased. Old snapshots remain available.

If a write fails before pointer replacement, CURRENT still references the previous revision. An uncommitted directory/temp pointer can remain for inspection. The tool does not automatically steal a lock, delete an orphan revision, guarantee power-loss durability, or silently reconcile conflicting semantic edits.

Search uses whole normalized words, prioritizing exact title/alias phrases. Ranking is for retrieval convenience, not a risk score or a judgment of concept importance. Context packets preserve the complete requested node and its parent frames, report omitted neighbors/edges, and reject budgets too small for mandatory context.
