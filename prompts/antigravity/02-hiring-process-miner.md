# Audit · Implement · Verify — Hiring Process Miner

> **Scope:** Local edit/verify only. Apply `00-SYSTEM.md`. No push, no visibility change, no deploy, no LICENSE creation.

Repo: `../hiring-process-miner`  
Ports: API **8102**, web **5102**, compose postgres **5402**  
Read first: `docs/REVIEW_AMENDMENTS.md` (**HPM-1: PM4Py is AGPL — core analytics must work without pm4py; optional extra only**), then `docs/PRODUCT_SPEC.md` (**historical**), README shipped table.

### Data contract
- CSV import with field mapper; stable tie-breaker; documented dedupe; DST policy (HPM-3).
- Seed 500–2000 synthetic cases with interview-scheduling bottleneck, ongoing cases, rework, skip stages; bad-record fixture.

### Analytics
- **Shipped core:** DFG/variants/funnel/performance/rework in **pandas/NumPy** (`canonical_order` HPM-2). Rule-based conformance without PM4Py.
- **Optional / not required:** lazy PM4Py adapter for advanced token-replay/alignment only (`uv sync --extra pm4py`). Do not list PM4Py as a hard stack dependency in README.

### Frontend
Import wizard, Process Explorer (React Flow), bottlenecks, variants compare, case explorer, methodology, filters, PNG/SVG/CSV/HTML export — all real API.

### Verify
pytest + Playwright upload→explore→export; README + GITHUB_METADATA. Document AGPL decision in DECISIONS/ENGINEERING_DECISIONS. Local commit only if owner asks; **do not push**.
