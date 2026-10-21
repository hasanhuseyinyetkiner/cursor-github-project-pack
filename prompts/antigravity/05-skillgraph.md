# Audit · Implement · Verify — SkillGraph

> **Scope:** Local edit/verify only. Apply `00-SYSTEM.md`. No push, no visibility change, no deploy, no LICENSE creation.

Repo: `../skillgraph`  
Ports: API **8105**, web **5105**, compose postgres **5405**  
Read first: `docs/REVIEW_AMENDMENTS.md` (SKG-1 graph_version; **embeddings optional / off by default**), then `docs/PRODUCT_SPEC.md` (**historical**), README shipped table.

### Ontology
Skill/Relation/Role/Requirement/Profile/LearningResource/RecommendationTrace. Seed ≥80 skills, ≥20 roles, ≥30 resources; career clusters. Local SQLite / Compose+CI PostgreSQL.

### Algorithms
Alias normalization; **deterministic baseline without embeddings** (demo/eval with `EMBEDDINGS_ENABLED=false`); mandatory requirements never hidden; named score components + RecommendationTrace; cycle-safe learning paths; versioned NetworkX cache. Do not list sentence-transformers as a hard required runtime unless README says so.

### Frontend
Dashboard, My Skills, Graph Explorer (Cytoscape), Role Explorer, Path Builder, Methodology — real API; profile export/erase/reset.

### Verify
Precision@K / nDCG@K on gold fixtures (measured only); Playwright demo→graph→role→path; ALGORITHM.md + README + GITHUB_METADATA. Local commit only if owner asks; **do not push**.
