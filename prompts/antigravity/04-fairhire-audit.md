# Audit · Implement · Verify — FairHire Audit

Repo: `C:\Users\Hasan Hsey\Desktop\hr-portfolio\fairhire-audit`  
Ports: API **8104**, web **5104**, compose postgres **5404**  
Read first: `docs/PRODUCT_SPEC.md`, `docs/REVIEW_AMENDMENTS.md` (FHA-1 score gate, FHA-2 cascade delete, FHA-3 pyarrow if Parquet)

### Models & ingest
Dataset, ColumnMapping, AuditRun, metrics, CI, ThresholdScenario, AuditReport. CSV/Parquet validation; no silent zeros for undefined rates.

### Stats engine
Fairlearn MetricFrame; DP/EO/EqOdds differences with formulas; seeded bootstrap CIs; small-cell suppression; Threshold Lab only with declared score semantics; optional model comparison; HTML+JSON report (no bias-free certificate).

### Frontend
Import → Quality → Groups → Threshold → Report; show n beside every rate.

### Verify
Golden fixtures, Playwright import→groups→export; METRICS.md + README + GITHUB_METADATA; commit & push.
