# Audit · Implement · Verify — SkillGraph

Repo: `C:\Users\Hasan Hsey\Desktop\hr-portfolio\skillgraph`  
Ports: API **8105**, web **5105**, compose postgres **5405**  
Read first: `docs/PRODUCT_SPEC.md`, `docs/REVIEW_AMENDMENTS.md` (SKG-1 graph_version; embeddings optional)

### Ontology
Skill/Relation/Role/Requirement/Profile/LearningResource/RecommendationTrace. Seed ≥80 skills, ≥20 roles, ≥30 resources; career clusters.

### Algorithms
Alias normalization; deterministic baseline without embeddings; mandatory requirements never hidden; named score components + RecommendationTrace; cycle-safe learning paths; versioned NetworkX cache.

### Frontend
Dashboard, My Skills, Graph Explorer (Cytoscape), Role Explorer, Path Builder, Methodology — real API; profile export/erase/reset.

### Verify
Precision@K / nDCG@K on gold fixtures (measured only); Playwright demo→graph→role→path; ALGORITHM.md + README + GITHUB_METADATA; commit & push.
