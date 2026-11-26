# Contributing to CyberAtlas

Useful contributions improve a definition, explain a mechanism, identify an omitted condition, challenge a relationship, provide scoped evidence, or repair the graph tools.

## Propose a bounded change

Start with the node ID and parent context. Explain the current claim, proposed replacement, why it matters, and affected relationships or metrics. Distinguish a hypothesis, a synthetic demonstration, and an observed result. Include sources and what was actually checked.

A disagreement is most useful when it identifies a concrete condition under which an explanation fails. Adding a citation alone does not establish that every claim in a node is supported.

## Edit through patches

Read [AGENTS.md](AGENTS.md). Retrieve the current revision, load relevant nodes, and follow the full-record patch protocol. Preserve IDs for changes that preserve identity. Keep titles English and retain meaningful prior labels as aliases. Do not modify immutable revision files directly.

Run a dry run before applying a patch, validate the graph, and refresh the export. Never use the initial seed builder to overwrite current work.

## Check the change

```sh
python graph.py validate
python -m unittest test_graph validate test_hygiene -v
python scripts/audit_repository.py --history
```

After staging, use `python scripts/verify_checkout.py` to check staged files in isolation. Report what was checked, which revision it applies to, and unresolved limitations.

## Keep private data out

Do not include credentials, personal paths, private incident records, production logs, source-book PDFs, or full third-party publications. Use sanitized examples and references. Optional source files belong outside the repository; see [REPOSITORY_HYGIENE.md](REPOSITORY_HYGIENE.md).

## Rights status

A reuse license has not yet been selected. No contributor license agreement or automatic ownership transfer is implied here. Resolve publication and reuse terms with the maintainer before incorporating third-party material.
