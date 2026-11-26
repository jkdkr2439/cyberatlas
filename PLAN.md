# Cybersecurity Concept Atlas — decision and goal record

Date: 2026-11-26 (Asia/Bangkok). Authoring: assistant, at Kevin T.N.'s request.

## Decision D01
Use Kevin's security book as the seed ontology and Lens Metric Generation as the decomposition method. Preserve source files. Build a new, offline, Vietnamese atlas here. Reuse the idea of navigable concept cards from the PNP atlas, without importing its claims or its runtime. Separate containment, conditional causal flows, hypotheses, evidence and candidate measures. A large graph is not proof of completeness or security.

Selected: domain map + mechanism cards + deeply decomposed journeys + explicit measurement contracts + synthetic counterexamples + offline explorer.
Deferred: production integrations, actual vulnerability scans, legal compliance certification, calibrated risk prediction, universal security score. No organization data was supplied.

## Goal map (assistant-proposed execution structure)

| ID | Parent | Predecessors | A -> Z | Frame/invariants | Acceptance evidence | Output -> successor | Status / reopen |
|---|---|---|---|---|---|---|---|
| G0 | User's cybersecurity understanding | Existing book and Metric Generation | Book-level concepts -> inspectable deep map | Educational; source preserved; no invented observations | Linked concepts, mechanisms, conditions, missing evidence, tests and usable viewer | Atlas -> user-selected investigations | Active; reopen with new domain or contradictions |
| G1 | G0 | Supplied source locations | Discovered sources -> indexed source inventory | Hash source; distinguish read passages from whole-document indexing | Source anchors resolve; overview sources version-pinned | Inventory -> G2 | Active; reopen on source change |
| G2 | G0 | G1 | Seed ontology -> multi-domain mechanism map | NMF is observer lens; IPOD/CV/resources describe object system | Each mechanism has scope, inputs, state change, control limits and OPEN frontier | Mechanisms -> G3 | Proposed; reopen when frame changes |
| G3 | G0 | G2 | Mechanism map -> conditional metric contracts | No score without goal, denominator and missing-data rule | Quantitative/structural contracts and discriminating synthetic cases | Contracts -> G4 | Proposed; reopen with actual telemetry |
| G4 | G0 | G2,G3 | Data -> offline atlas and documents | Stable IDs; separate canonical I_TO_O from process/evidence | Integrity checks; browser search/navigation; rendered review | Artifacts -> G5 | Proposed; reopen with UI or data failure |
| G5 | G0 | G4 | Checked artifacts -> delivered map | State actual breadth and limitations | Paths, counts, tests and next frontier recorded | User's next question consumes atlas + context | Proposed; reopen on new request |

Stop locally when a node supports an explicit decision/test and its remaining uncertainties are recorded; deeper unknowns stay OPEN. This does not close the whole cybersecurity domain.

## Decision D02 — user steering overrides D01 presentation choice

The user explicitly requested a machine-readable node graph for AI to load/update and test, and asked to remove the visual windows. Stop visualization work. The test browser has been closed and the temporary HTTP process stopped. Generated HTML/screenshots are not deliverables. No further UI is required.

G4's revised Z is a canonical versioned graph with per-node JSON, typed edges, selective context packets, schema/reference validation, optimistic revision checks and an atomic CURRENT commit pointer. G5 delivers the AI entry point, portable JSONL and test results. The primary output is no longer an explorer.

Additional decomposition: 24 child mechanisms were added in nonuniform branches around revocation/cache/version races, tenant context/async delivery, build trust, agent approval/execution and recovery consistency. These are distinct mechanisms, not mechanically multiplied lens fields.

## Decision D03 — English node names

User requested English node names. Rename all 233 node titles and 8 metric-contract titles, retaining IDs, relationships and descriptive content. Preserve prior labels as search aliases. Commit through the same revision-checked patch path used for future updates, and regression-test that only naming metadata changed.

## Local completion record

- G1: complete for this scope. Original book hash retained, 502 heading anchors indexed; source-reading levels recorded in SOURCES.md. The source book was not modified.
- G2: complete as a bounded authored map: 26 domains, 102 mechanisms including 24 recursive refinements, 8 journeys with 64 steps, 32 unresolved frontiers, one root. These are 233 primary nodes and 432 typed relations; not an exhaustive cybersecurity ontology.
- G3: complete as measurement design: 102 sketches, 8 detailed contracts and 9 executed synthetic examples. No organization measurements or calibrated security scores were invented.
- G4: complete under D02. Canonical per-node records, selective context loading, JSONL export, version-checked atomic updates and schema/reference validation are implemented. The UI files were removed; the test browser and temporary server were stopped.
- G5: delivered through AI_ENTRYPOINT.json, AGENTS.md, README.md, NODE_INDEX.md, exports/cybersecurity.nodes.jsonl and VALIDATION.md. Current revision: r000002-fc8033e2e4fc67f3.
- Verification: 26 graph/update tests and 10 seed/integrity/arithmetic tests passed. Three changed assertions were rerun after making the historical rename audit compatible with future node additions. No test-only nodes entered CURRENT. UTF-8 CLI output and word-fragment search failures found during smoke testing were fixed and regression-tested.
- Reopen: user-selected frontier, new evidence, changed system frame, new control mechanism or actual organizational data. Future edits consume CURRENT rather than the original seed.

## Decision D04 — standalone repository hygiene

User requested removal of personal paths, credentials and clutter. Regenerated both snapshots using source URNs, preserving node/edge/metric content, and refreshed revision references/checksums. The unpublished initial Git import will be replaced after clean-checkout validation; private paths must not remain in publishable history. Optional source files resolve through environment variables only. Added redacted offline scanning and regression tests; no source book is bundled.
