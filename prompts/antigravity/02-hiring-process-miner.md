# Audit · Implement · Verify — Hiring Process Miner

Repo: `C:\Users\Hasan Hsey\Desktop\hr-portfolio\hiring-process-miner`  
Ports: API **8102**, web **5102**, compose postgres **5402**  
Read first: `docs/PRODUCT_SPEC.md`, `docs/REVIEW_AMENDMENTS.md` (**HPM-1: PM4Py is AGPL — core analytics must work without pm4py; optional extra only**)

### Data contract
- CSV import with field mapper; stable tie-breaker; documented dedupe; DST policy (HPM-3).
- Seed 500–2000 synthetic cases with interview-scheduling bottleneck, ongoing cases, rework, skip stages; bad-record fixture.

### Analytics
- Core DFG/variants/funnel/performance/rework in **pandas** (canonical_order HPM-2). Optional lazy PM4Py adapter for advanced conformance only.
- Never put ongoing cases in completed cycle-time; transparent insight cards with n, numerator, method.

### Frontend
Import wizard, Process Explorer (React Flow), bottlenecks, variants compare, case explorer, methodology, filters, PNG/SVG/CSV/HTML export — all real API.

### Verify
pytest + Playwright upload→explore→export; README + GITHUB_METADATA; commit & push. Document AGPL decision in DECISIONS.md.
