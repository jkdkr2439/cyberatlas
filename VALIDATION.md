# Validation record

Current graph revision: `r000002-fc8033e2e4fc67f3`.

## CyberAtlas v0.1 presentation verification — 2026-11-26

The staged release-preparation checkout passed graph validation and **44 tests: 43 passed, 1 skipped** (external-book comparison). The three additional hygiene tests distinguish PNG pixel data from text metadata, inspect compressed metadata, and reject unreadable metadata. The generated 2172 × 724 PNG banner was visually reviewed, decoded successfully, and contains no embedded metadata fields. README local links, navigation anchors and version metadata were checked. Staged-file and reachable-history scans reported no findings. No graph content changed, and no remote publication was performed.

## Sanitized repository verification — 2026-11-26

Both graph snapshots were regenerated with portable source URNs, preserving all node/edge/metric content and updating revision IDs and checksums. A staged clean checkout passed graph validation and **41 tests: 40 passed, 1 skipped** (external-book comparison). Four hygiene regression tests cover redacted findings, credential/path patterns, opt-in source resolution and source metadata across both snapshots. The staged repository contains 636 files with no PDF/DOCX payloads. Pattern scanning and a separate high-entropy quoted-string review found no credential candidates. Full Git-history scanning is part of the final sanitized-import check; scan limitations are documented in REPOSITORY_HYGIENE.md.

## Standalone repository verification — 2026-11-26

`python scripts/verify_checkout.py` checked the staged Git files in a clean temporary checkout. Graph validation passed with the immutable snapshot checksums intact. The combined suite ran **37 tests: 36 passed, 1 explicitly skipped** (comparison against the external original book, disabled to verify portability). The added metadata test checks source-heading anchors and hash structure without needing the original book.

The checkout contained **0 PDF and 0 DOCX files**; a file-signature scan also found no PDF payload under another extension. Source references and heading indexes remain provenance metadata only. No source book was copied into this repository.

## Earlier graph and source verification

- **26 graph/update tests passed.** Covers selective reads, complete parent context, explicit context budgets, adding/updating nodes, derived containment/IO, concurrent writers, stale revisions, failed commit rollback, dangling edges, cycles, unknown sources, metric/frame drift, unsupported evidence promotion, snapshot checksums, UTF-8 under a legacy Windows code page, bilingual search, portable export, and English-label migration integrity.
- **10 seed/integrity/arithmetic tests passed.** Includes malformed-reference/cycle mutations, source-book hashes and heading anchors, recursive parent chain, IO/evidence separation and missing denominator/overlapping interval handling.
- **9 synthetic measurement examples ran.** They demonstrate base-rate changes, missing observation coverage, misleading patch ratios, censored revocation times, overlapping exposure intervals, business recovery versus server uptime, MFA fallback gaps, proposed versus executed agent actions, and signer checks versus deployment policy.
- CURRENT contains **233 nodes, 432 edges, 8 detailed metric contracts**, and **0 organization observations**. All node and metric titles are English; stable IDs, semantic content and graph relations were preserved during renaming.
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
