# Repository hygiene

This repository contains the authored concept atlas, source citations, heading metadata, CLI and tests. Full source books, credentials and machine-specific paths do not belong in it.

## External sources

Local references use `urn:cyber-atlas:source:book`, `urn:cyber-atlas:source:metric` and `urn:cyber-atlas:source:lens`. These identify documents; they are not download URLs. Content hashes and heading anchors remain available for provenance.

Graph operations require none of these documents. To explicitly verify the original book, set `CYBER_ATLAS_SOURCE_BOOK` in your own environment. The legacy seed builder additionally requires `CYBER_ATLAS_SOURCE_METRIC` and `CYBER_ATLAS_SOURCE_LENS`. It resolves paths in memory and writes only source URNs. Do not commit environment values or rerun the seed builder over an existing graph.

## Checks

```powershell
python scripts/audit_repository.py --history
python scripts/audit_repository.py --staged
python scripts/verify_checkout.py
```

The offline scanner checks tracked and nonignored new files, optionally staged content and all reachable Git blobs, for absolute personal paths, recognizable provider tokens, private-key headers, JWTs, credential-bearing URLs and literal credential assignments. It also rejects source documents and key-store file extensions. Reports contain rule names and locations, never matched values. This is a heuristic scan, not a guarantee that every possible secret format will be detected; it makes no network calls to validate credentials.

## Cleanup record — 2026-11-26

Personal source paths were found in provenance metadata, exports and both original graph snapshots. No recognizable credential was found by the scanner. Both snapshots were regenerated with source URNs, fresh revision IDs and matching checksums; node IDs, node content, metrics and graph relations were preserved. Revision references and rename receipts were updated together. The single unpublished Git import is replaced by the sanitized import, so the old paths are not retained in publishable history.

The portable export is `exports/cybersecurity.nodes.jsonl`; the old `.txt` copy was removed. Bootstrap receipts, retired browser output and Python caches are local generated files, not deliverables. Existing authorship attribution is retained; Git's configured noreply author address is not a credential.
