# Cursor GitHub Project Pack

**Build five evidence-first HR-tech products with Cursor or Antigravity — prompts, rules, and review findings, not product source code.**

This repository is a **meta pack**: detailed agent prompts, shared engineering rules, README templates, and a pre-implementation design review. Each product lives in its own GitHub repository. Clone this pack, follow the workflow below, and drive implementation in those sibling repos.

[Start here](START_HERE.md) · [Antigravity prompts](prompts/antigravity/) · [Design review](docs/DESIGN_REVIEW.md) · [Templates](templates/)

---

## The five products

| Product | Stack | Engineering problem | Differentiator |
| --- | --- | --- | --- |
| [**HR Policy Copilot**](https://github.com/hasanhuseyinyetkiner/hr-policy-copilot) | FastAPI · PostgreSQL · Qdrant · sentence-transformers · React/Vite/TS | Grounded Q&A over versioned HR policies without inventing rules or losing citation provenance | Hybrid RAG (dense + sparse + RRF), document versioning, abstention, offline extractive demo |
| [**Hiring Process Miner**](https://github.com/hasanhuseyinyetkiner/hiring-process-miner) | FastAPI · pandas · PM4Py · PostgreSQL · React Flow/Cytoscape · Recharts | Turn anonymized hiring event logs into discovery graphs, bottlenecks, and conformance without confusing observation with causation | Mathematically traceable KPIs (pandas-verified) + interactive process map |
| [**Workforce Optimizer**](https://github.com/hasanhuseyinyetkiner/workforce-optimizer) | FastAPI · Google OR-Tools CP-SAT · PostgreSQL · React · FullCalendar (MIT views) | Feasible, explainable shift schedules under hard coverage/skill/rest constraints — not “AI scheduling” marketing | Constraint programming + independent pure-Python validator + honest INFEASIBLE reporting |
| [**FairHire Audit**](https://github.com/hasanhuseyinyetkiner/fairhire-audit) | FastAPI · scikit-learn · Fairlearn · SciPy · PostgreSQL · React · Recharts | Audit model quality and group disparity on authorized/synthetic eval data without issuing a bias-free certificate | Confidence intervals, sample-size flags, threshold sensitivity, reproducible audit reports |
| [**SkillGraph**](https://github.com/hasanhuseyinyetkiner/skillgraph) | FastAPI · NetworkX · sentence-transformers · PostgreSQL · React Flow/Cytoscape | Explainable skill–role–learning paths without automated promotion or worth scoring | Knowledge graph + weighted relations + synonym search + deterministic recommendation baseline |

Shared defaults across products: Python 3.12+, Pydantic v2, SQLAlchemy 2, Alembic, pytest, Ruff, TanStack Query, Vitest, Playwright, Docker Compose (CI), GitHub Actions. See [START_HERE.md](START_HERE.md) for the full preferred stack.

> [!NOTE]
> This pack does **not** ship product metrics, CI badges for sibling repos, or demo screenshots. Those belong only in each product repo after real measurement and capture.

---

## Recommended build order

1. **hr-policy-copilot** — RAG, document processing, cited answers  
2. **hiring-process-miner** — event-log analytics, process mining  
3. **workforce-optimizer** — constraint programming, mathematical validation  
4. **fairhire-audit** — ML metrics, model auditing  
5. **skillgraph** — knowledge graph, explainable recommendations  

---

## How to use with Cursor / Antigravity

Antigravity (and Cursor Agent) prompts for completing scaffolded product repos live under [`prompts/antigravity/`](prompts/antigravity/).

### Per product (sibling repo)

1. Open the **product repository** folder (not this pack) in Cursor or Antigravity.
2. Paste **[`prompts/antigravity/00-SYSTEM.md`](prompts/antigravity/00-SYSTEM.md)** first — global execution rules (real DB, no fake APIs, test before claiming done, Docker-absent local path, commit/push policy).
3. Then paste the matching product file:
   - [`01-hr-policy-copilot.md`](prompts/antigravity/01-hr-policy-copilot.md)
   - [`02-hiring-process-miner.md`](prompts/antigravity/02-hiring-process-miner.md)
   - [`03-workforce-optimizer.md`](prompts/antigravity/03-workforce-optimizer.md)
   - [`04-fairhire-audit.md`](prompts/antigravity/04-fairhire-audit.md)
   - [`05-skillgraph.md`](prompts/antigravity/05-skillgraph.md)
4. Grant file and terminal permissions only after reviewing the agent’s plan.
5. Prefer Phase 1/MVP first; continue later with [`templates/CURSOR_CONTINUE_PROMPT.md`](templates/CURSOR_CONTINUE_PROMPT.md).

### This meta pack

To audit or improve **this** repository, paste `00-SYSTEM.md`, then [`06-project-pack.md`](prompts/antigravity/06-project-pack.md).

### Original greenfield prompts

Full Phase 1–4 specifications (for empty repos) remain in [`prompts/01-*.md` … `prompts/05-*.md`](prompts/). Shared Cursor Project Rules: [`common/.cursor/rules/`](common/.cursor/rules/).

### Design review (binding context)

Read [`docs/DESIGN_REVIEW.md`](docs/DESIGN_REVIEW.md) before treating any product as “done.” It documents blockers and high-severity risks (Docker DoD vs local environment, auth/bind defaults, dual-write consistency, AGPL/PM4Py licensing, CP-SAT reproducibility, and more). Product repos should carry `docs/REVIEW_AMENDMENTS.md`; where that file conflicts with `PRODUCT_SPEC`, **amendments win**.

---

## What’s in this repository

| Path | Purpose |
| --- | --- |
| [`START_HERE.md`](START_HERE.md) | Turkish onboarding: order, copy rules, continue/publish flow |
| [`prompts/`](prompts/) | Full English product prompts (greenfield) |
| [`prompts/antigravity/`](prompts/antigravity/) | System directive + audit/implement prompts for scaffolded repos |
| [`common/.cursor/rules/`](common/.cursor/rules/) | Engineering + GitHub documentation Project Rules |
| [`templates/`](templates/) | README, profile, continue, review, release, and publish guides |
| [`docs/DESIGN_REVIEW.md`](docs/DESIGN_REVIEW.md) | Pre-implementation design review with evidence-backed findings |

---

## Honest scope

This pack is **instructions and quality gates**, not the five applications. Agents can still fail tests, skip steps, or invent claims — review code, run verification yourself, and never publish fabricated metrics or screenshots. Owner-authorized commit/push applies only where explicitly stated for that repo.

---

## License / contributing

Treat each product repository’s `LICENSE` as authoritative (dependency licenses can constrain choice — see HPM-1 in the design review). Contributions to this pack: keep prompts accurate, links working, and claims free of invented numbers.
