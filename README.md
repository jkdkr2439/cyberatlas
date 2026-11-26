![CyberAtlas — The Mechanics of Cybersecurity. v0.1 research preview. Kevin T.N., Epistemologist.](assets/cyberatlas-banner.png)

# CyberAtlas

**The Mechanics of Cybersecurity**

A machine-readable knowledge graph for exploring cybersecurity mechanisms: how systems behave, where controls fail, what conditions matter, and what evidence would change an assessment.

**v0.1 · Initial research preview** · Python CLI · JSON / JSONL · Offline graph operations

[Quick start](#quick-start) · [Explore](#explore-the-graph) · [Roadmap](ROADMAP.md) · [Contributing](CONTRIBUTING.md) · [Changelog](CHANGELOG.md)

## Why this atlas exists

Knowing the name of a security control does not explain how it works. CyberAtlas connects concepts to their inputs, processes, outputs, constraints, failure conditions, possible tests, and measurement requirements. It is designed for people and AI assistants that need to follow a mechanism across multiple systems, inspect its assumptions, and revise the map as understanding improves.

Retrieve one node with its parent context and nearby relationships instead of loading the entire atlas into a model's context window. Updates are validated and recorded as new snapshots.

## Status: v0.1

This is a starting research map, not a finished taxonomy or a validated model of every cybersecurity system. Future revisions will expand coverage, refine definitions, revisit proposed causal relationships, qualify their conditions, and incorporate supporting or contradictory evidence.

A graph link is **not automatically a demonstrated causal relationship**. Read its relation type, condition, scope, and evidence status. Structural membership, dependencies, and proposed explanations must not be treated as interchangeable.

**Language:** node and metric titles are English; much of the analytical content is Vietnamese. Previous Vietnamese titles remain as search aliases. This README is English; the atlas has not yet been fully translated.

## What is included

| Component | v0.1 scope |
| --- | ---: |
| Primary nodes | 233 |
| Typed relationships | 432 |
| Security domains | 26 |
| Mechanism cards | 102, including 24 deeper refinements |
| Journeys | 8, with 64 process steps |
| Open research frontiers | 32 |
| Candidate measurement sketches | 102 |
| Detailed metric contracts | 8 |
| Synthetic measurement examples | 9 |
| Organization observations | 0 |

These counts describe the v0.1 artifact's scope, not its security coverage or effectiveness. Use `python graph.py stats` for the current working graph.

## Quick start

Use Python 3.12, the tested runtime. From the repository directory:

```sh
python -m pip install -r requirements.txt
python graph.py validate
python graph.py search "revocation" --type mechanism --limit 5
python graph.py get revoke-cas --max-chars 22000
```

The graph is already initialized. No API key, source-book PDF, server, or model subscription is required to read it. Dependency installation may require internet access; graph operations run locally.

Do not run `build.py` or `graph.py init` over the existing atlas. `build.py` is a historical seed-generation tool, not the normal entry point.

## Explore the graph

```sh
python graph.py stats
python graph.py children ses-revoke
python graph.py metric M01
python graph.py source book
python graph.py search "" --type frontier --limit 40
```

For example, a session-control branch follows revocation through caching, versioning, and race conditions:

```text
root
└─ session
   └─ ses-revoke
      ├─ revoke-fanout
      ├─ revoke-offline
      └─ revoke-cache
         ├─ revoke-version
         └─ revoke-race
            └─ revoke-cas
```

`get` returns the selected node, required parent context, and bounded related records. The budget is in **characters**, not tokens; omitted neighboring context is reported explicitly.

**For AI assistants:** start with [AGENTS.md](AGENTS.md) and [AI_ENTRYPOINT.json](AI_ENTRYPOINT.json). Use [NODE_INDEX.md](NODE_INDEX.md) for navigation or the [JSONL export](exports/cybersecurity.nodes.jsonl) for bulk ingestion.

## Data and update model

[graph/CURRENT](graph/CURRENT) points to the canonical snapshot. Each revision contains individual node files, typed edges, metric contracts, sources, observations, derived indexes, and a checksum manifest.

Changes use a revision-checked patch. Schema and relationship checks run before a new snapshot is written; the current pointer is then replaced. Stale edits are rejected, and earlier snapshots remain available.

```sh
# Prepare a patch using the schema and procedure in AGENTS.md.
python graph.py apply patch.json --dry-run
python graph.py apply patch.json
python graph.py validate
python graph.py export --output exports/cybersecurity.nodes.jsonl
```

`patch.json` is a file you prepare, not a bundled runnable example. Do not edit immutable snapshots or exported records directly. See [AGENTS.md](AGENTS.md) for the full protocol, evidence requirements, and failure recovery.

Project releases and graph revisions serve different purposes: **v0.1** identifies the project preview; `graph/CURRENT` identifies the exact dataset revision.

## Repository guide

| Path | Purpose |
| --- | --- |
| `graph.py` | Query, validation, patch, and export CLI |
| `graph/` | Canonical versioned graph and checksum manifests |
| `exports/` | Portable derived snapshot pinned to a revision |
| `data/`, `vault/` | Initial seed data, explanations, validation artifacts |
| `test_graph.py`, `validate.py`, `test_hygiene.py` | Graph, seed, arithmetic, and hygiene checks |
| `scripts/` | Staged-checkout verification and hygiene scanning |
| `assets/` | Repository banner and generation provenance |
| `AGENTS.md`, `AI_ENTRYPOINT.json` | AI entry and operating instructions |

Historical seed documents are explanatory material. Where they differ from a later graph update, `graph/CURRENT` takes precedence.

## Validation

```sh
python -m unittest test_graph validate test_hygiene -v
python scripts/audit_repository.py --history
```

After staging changes, `python scripts/verify_checkout.py` checks the staged files in a temporary checkout, runs the tests without external books, and rejects bundled PDF/DOCX files.

The latest full verification ran **44 tests: 43 passed, 1 skipped** because the original external book was intentionally unavailable. Tests check the artifact and tooling; they do not demonstrate production security effectiveness. See [VALIDATION.md](VALIDATION.md).

## Method, sources, and boundaries

- [METHOD.md](METHOD.md): decomposition and measurement design.
- [DATA_DICTIONARY.md](DATA_DICTIONARY.md): record meanings and conventions.
- [SOURCES.md](SOURCES.md): source inventory and actual review scope.
- [METRIC_PROFILES.md](METRIC_PROFILES.md): measurement contracts.
- [FRONTIERS.md](FRONTIERS.md): unresolved branches.
- [REPOSITORY_HYGIENE.md](REPOSITORY_HYGIENE.md): local source configuration and checks.

The initial map draws on *Hệ miễn dịch của thế giới số* and *A Fractal Model for Metric Generation*, alongside cited technical references. Source books are not bundled. External local documents use URNs and hashes, with optional environment-based resolution; personal filesystem paths are not stored in the atlas.

The map contains authored analyses, candidate tests, and synthetic examples. It does not contain production observations, a universal security score, a compliance certification, or a complete technical audit of every cited source.

## Development direction

Upcoming work includes deeper decomposition, clearer definitions and system boundaries, review of causal hypotheses and alternative explanations, evidence-backed corrections, and improved English documentation. Revisions may split, merge, qualify, or remove claims as the map develops. See [ROADMAP.md](ROADMAP.md) and [CONTRIBUTING.md](CONTRIBUTING.md).

## Author and licensing

**Kevin T.N. · Epistemologist**

A reuse license has not yet been selected. This preview does not declare an open-source license. Third-party sources remain separately attributed; citing them does not grant rights to redistribute their full contents.
