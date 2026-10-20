# Implementation status (sibling product repos)

**Purpose:** Snapshot of **shipped vs planned** facts for the five portfolio apps, so pack prompts and READMEs do not drift into outdated stack claims.  
**Source of truth:** each product’s root `README.md` + `docs/REVIEW_AMENDMENTS.md` + code. Re-verify before publication.  
**Date of pack alignment:** 2026-10-20 (local filesystem inspection).

> Product `docs/PRODUCT_SPEC.md` files and pack `prompts/01–05-*.md` are **historical development briefs**. Prefer this file + product READMEs for “what exists now.”

## Shared delivery model

| Concern | Current practice |
| --- | --- |
| Local native path | `uv` + `pnpm`; **SQLite** common for demos |
| Compose / PostgreSQL | Present; verified primarily via **CI** `compose-smoke` when Docker absent locally |
| Git | Remotes exist under `hasanhuseyinyetkiner/*`; pack policy = **no push / no visibility change** without fresh owner approval |
| License | Pending owner decision (dev amendments forbade silent `LICENSE` creation) |

## Per product

| Product | Shipped core (high level) | Stack corrections vs older pack text | Planned / optional (not default) |
| --- | --- | --- | --- |
| **hr-policy-copilot** | Hybrid RAG (DB BM25 + dense + RRF), versioning, citations, abstention, extractive demo | SQLite local / Postgres Compose; extractive MVP | Ollama/cloud LLM grounding |
| **hiring-process-miner** | CSV import, pandas DFG/variants/funnel/rework, rule-based conformance, React Flow | **Core = pandas/NumPy**; PM4Py **optional extra** (AGPL) | XES import; multi-user auth; PM4Py token-replay when extra installed |
| **workforce-optimizer** | CP-SAT solve, independent validator, scenarios, CSV/ICS | **Custom employee×day roster grid** shipped; **not** FullCalendar Premium / not “FullCalendar shipped” | Manual drag-edit; labor-law certification |
| **fairhire-audit** | Import, Fairlearn metrics, CIs, threshold lab, reports | SQLite local / Postgres CI | Side-by-side two-model comparison **UI** (domain may exist; UI planned) |
| **skillgraph** | Ontology, Cytoscape graph, role fit, learning paths, traces | **Embeddings optional / off by default** (`EMBEDDINGS_ENABLED=false`) | Embedding-enhanced similarity when explicitly enabled |

## Remotes (inspected locally)

All five product folders report `origin` → `https://github.com/hasanhuseyinyetkiner/<repo>.git`. Publish via [`templates/GITHUB_PUBLISH.md`](../templates/GITHUB_PUBLISH.md); never `gh repo create --public --push` on these checkouts.
