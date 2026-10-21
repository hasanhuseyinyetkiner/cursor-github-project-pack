# Audit · Implement · Verify — HR Policy Copilot

> **Scope:** Local edit/verify only. Apply `00-SYSTEM.md`. No push, no visibility change, no deploy, no LICENSE creation.

Repo: `../hr-policy-copilot`  
Ports: API **8101**, web **5101**, compose postgres **5401**, qdrant **6301**  
Read first: `docs/REVIEW_AMENDMENTS.md` (binding), then `docs/PRODUCT_SPEC.md` (**historical** development brief), `.cursor/rules/*.mdc`, README shipped/planned table.

### Infrastructure
- Compose: web, api, postgres, qdrant with healthchecks; CI compose-smoke. Local: SQLite + Qdrant local mode + CPU torch embeddings.
- Models: Document, DocumentVersion, Chunk, IngestionJob, Conversation, Message, Citation, Category + Alembic.
- Default offline extractive answers; optional Ollama behind a flag (**planned ≠ shipped** — check README).

### RAG engine
- Parsers: pypdf≥6.20.1, python-docx, BeautifulSoup, TXT; section/page-aware chunking; hostile upload sandbox/timeout.
- Versioning: supersede old version, remove stale vectors, citations keep snippet snapshot (HR-4).
- Hybrid: dense (sentence-transformers) + sparse + RRF; PG/SQLite is source of truth (HR-1); corpus_version for BM25 (HR-2).
- Abstention, contradiction display with dates, prompt-injection defense.

### Demo & evaluation
- ≥5 synthetic HR policies + conflicting/obsolete version; seed/reset.
- Eval set (answerable/ambiguous/conflicting/unanswerable); measure Recall@K, MRR, citation precision — report only real numbers.

### Frontend
Wire Dashboard, Library, Chat (citations), Source Viewer, Versions, Settings to real API via TanStack Query.

### Verify
pytest (parsers, chunking, versioning, RRF, citations, abstention), Playwright upload→index→query→citation, README + `docs/GITHUB_METADATA.md`. Local commit only if owner asks; **do not push**.
