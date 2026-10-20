# Audit · Implement · Verify — FairHire Audit

> **Scope:** Local edit/verify only. Apply `00-SYSTEM.md`. No push, no visibility change, no deploy, no LICENSE creation.

Repo: `C:\Users\Hasan Hsey\Desktop\hr-portfolio\fairhire-audit`  
Ports: API **8104**, web **5104**, compose postgres **5404**  
Read first: `docs/REVIEW_AMENDMENTS.md` (FHA-1 score gate, FHA-2 cascade delete, FHA-3 pyarrow if Parquet), then `docs/PRODUCT_SPEC.md` (**historical**), README shipped vs planned table.

### Models & ingest
Dataset, ColumnMapping, AuditRun, metrics, CI, ThresholdScenario, AuditReport. CSV/Parquet validation; no silent zeros for undefined rates. Local SQLite / Compose+CI PostgreSQL.

### Stats engine
Fairlearn MetricFrame; DP/EO/EqOdds differences with formulas; seeded bootstrap CIs; small-cell suppression; Threshold Lab only with declared score semantics; optional model comparison; HTML+JSON report (no bias-free certificate).

### Frontend
Import → Quality → Groups → Threshold → Report; show n beside every rate. Do not claim planned UI (e.g. side-by-side two-model compare) as shipped.

### Verify
Golden fixtures, Playwright import→groups→export; METRICS.md + README + GITHUB_METADATA. Local commit only if owner asks; **do not push**.
