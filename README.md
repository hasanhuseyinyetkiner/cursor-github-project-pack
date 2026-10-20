# Cursor GitHub Project Pack

**Engineering workflow pack:** agent prompts, Cursor rules, templates, and a design-review archive for building and publishing evidence-first portfolio apps — not the application source code itself.

This repository is a **meta pack**. Each product lives in its own GitHub repository. Clone this pack, follow the workflow below, and drive implementation in those sibling repos. Prefer [`docs/IMPLEMENTATION_STATUS.md`](docs/IMPLEMENTATION_STATUS.md) and each product README for **current** shipped facts; treat greenfield `prompts/01–05` and product `PRODUCT_SPEC.md` as **historical** development briefs.

[Start here](START_HERE.md) · [Antigravity prompts](prompts/antigravity/) · [Design review](docs/DESIGN_REVIEW.md) · [Implementation status](docs/IMPLEMENTATION_STATUS.md) · [Licensing layers](docs/LICENSING.md) · [Templates](templates/)

---

## The five products

Stacks below match **local product README inspection (2026-10-20)**. Optional extras are not hard requirements.

| Product | Stack (accurate) | Engineering problem | Differentiator |
| --- | --- | --- | --- |
| [**HR Policy Copilot**](https://github.com/hasanhuseyinyetkiner/hr-policy-copilot) | FastAPI · SQLite local / PostgreSQL Compose+CI · Qdrant · sentence-transformers · React/Vite/TS | Grounded Q&A over versioned HR policies without inventing rules or losing citation provenance | Hybrid RAG (dense + sparse + RRF), document versioning, abstention, offline extractive demo |
| [**Hiring Process Miner**](https://github.com/hasanhuseyinyetkiner/hiring-process-miner) | FastAPI · **pandas/NumPy core** · optional PM4Py extra · SQLite local / PostgreSQL CI · React Flow | Turn anonymized hiring event logs into discovery graphs and bottlenecks without confusing observation with causation | Traceable KPIs (pandas-verified) + interactive process map; AGPL PM4Py only if extra installed |
| [**Workforce Optimizer**](https://github.com/hasanhuseyinyetkiner/workforce-optimizer) | FastAPI · Google OR-Tools CP-SAT · SQLite local / PostgreSQL CI · React · **custom roster grid** | Feasible, explainable shift schedules under hard coverage/skill/rest constraints — not "AI scheduling" marketing | Constraint programming + independent pure-Python validator + honest INFEASIBLE reporting (no FullCalendar Premium) |
| [**FairHire Audit**](https://github.com/hasanhuseyinyetkiner/fairhire-audit) | FastAPI · scikit-learn · Fairlearn · SciPy · SQLite local / PostgreSQL CI · React · Recharts | Audit model quality and group disparity on authorized/synthetic eval data without issuing a bias-free certificate | Confidence intervals, sample-size flags, threshold sensitivity, reproducible audit reports |
| [**SkillGraph**](https://github.com/hasanhuseyinyetkiner/skillgraph) | FastAPI · NetworkX · embeddings **optional/off by default** · SQLite local / PostgreSQL CI · Cytoscape | Explainable skill-role-learning paths without automated promotion or worth scoring | Knowledge graph + weighted relations + synonym search + deterministic recommendation baseline |

Shared defaults: Python 3.12+, Pydantic v2, SQLAlchemy 2, Alembic, pytest, Ruff, TanStack Query, Vitest, Playwright, Docker Compose (**CI**), GitHub Actions. See [START_HERE.md](START_HERE.md).

> [!NOTE]
> **Planned ≠ shipped.** This pack does not ship product metrics, CI badges for sibling repos, or demo screenshots. Those belong only in each product repo after real measurement and capture.

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
2. Paste **[`prompts/antigravity/00-SYSTEM.md`](prompts/antigravity/00-SYSTEM.md)** first — global execution rules (real DB, no fake APIs, test before claiming done, Docker-absent local path, **no remote push / no visibility change / no deploy**).
3. Then paste the matching product file:
   - [`01-hr-policy-copilot.md`](prompts/antigravity/01-hr-policy-copilot.md)
   - [`02-hiring-process-miner.md`](prompts/antigravity/02-hiring-process-miner.md)
   - [`03-workforce-optimizer.md`](prompts/antigravity/03-workforce-optimizer.md)
   - [`04-fairhire-audit.md`](prompts/antigravity/04-fairhire-audit.md)
   - [`05-skillgraph.md`](prompts/antigravity/05-skillgraph.md)
4. Grant file and terminal permissions only after reviewing the agent's plan.
5. Prefer Phase 1/MVP first; continue later with [`templates/CURSOR_CONTINUE_PROMPT.md`](templates/CURSOR_CONTINUE_PROMPT.md).

### This meta pack

To audit or improve **this** repository, paste `00-SYSTEM.md`, then [`06-project-pack.md`](prompts/antigravity/06-project-pack.md).

### Original greenfield prompts (historical)

Full Phase 1–4 specifications (for empty repos) remain in [`prompts/01-*.md` … `prompts/05-*.md`](prompts/). They are **historical development briefs**; amendments + code win on conflict. Shared Cursor Project Rules: [`common/.cursor/rules/`](common/.cursor/rules/).

### Design review (binding context)

Read [`docs/DESIGN_REVIEW.md`](docs/DESIGN_REVIEW.md) (historical findings + **CURRENT VERIFICATION STATUS**). Product repos should carry `docs/REVIEW_AMENDMENTS.md`; where that file conflicts with `PRODUCT_SPEC`, **amendments win**.

---

## What's in this repository

| Path | Purpose |
| --- | --- |
| [`START_HERE.md`](START_HERE.md) | Onboarding: order, copy rules, continue/publish flow |
| [`prompts/`](prompts/) | Full English product prompts (greenfield / historical) |
| [`prompts/antigravity/`](prompts/antigravity/) | System directive + audit/implement prompts for scaffolded repos |
| [`common/.cursor/rules/`](common/.cursor/rules/) | Engineering + GitHub documentation Project Rules |
| [`templates/`](templates/) | README, profile, continue, review, release, and publish guides |
| [`docs/DESIGN_REVIEW.md`](docs/DESIGN_REVIEW.md) | Historical design review + current verification status |
| [`docs/IMPLEMENTATION_STATUS.md`](docs/IMPLEMENTATION_STATUS.md) | Shipped vs planned snapshot vs outdated claims |
| [`docs/LICENSING.md`](docs/LICENSING.md) | Dev constraint vs release requirement vs owner-pending |

---

## Honest scope

This pack is **instructions and quality gates**, not the five applications. Agents can still fail tests, skip steps, or invent claims — review code, run verification yourself, and never publish fabricated metrics or screenshots.

**Git defaults for agents:** local edits OK; **no** `git push`; **no** repo visibility change; **no** deploy; **no** live profile overwrite. Push or public visibility requires **fresh, explicit owner approval for that repo in the current chat**. Stale "owner authorized push" text is void.

**Licensing:** do not silently create or choose `LICENSE`. See [`docs/LICENSING.md`](docs/LICENSING.md).

---

## License / contributing

Treat each product repository's license as **owner-pending** until the owner adds a `LICENSE`. Dependency licenses can constrain choice (see HPM-1 in the design review). Contributions to this pack: keep prompts accurate, links working, and claims free of invented numbers.
