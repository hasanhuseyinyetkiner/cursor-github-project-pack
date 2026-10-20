# Audit · Implement · Verify — Workforce Optimizer

Repo: `C:\Users\Hasan Hsey\Desktop\hr-portfolio\workforce-optimizer`  
Ports: API **8103**, web **5103**, compose postgres **5403**  
Read first: `docs/PRODUCT_SPEC.md`, `docs/REVIEW_AMENDMENTS.md` (WFO-1 reproducible CP-SAT, WFO-2 MIT calendar only, WFO-3 UTC TypeDecorator)

### Domain
Employee, Skill, ShiftTemplate, ShiftInstance, Availability, TimeOff, Ruleset, Assignment, OptimizationRun, ScheduleVersion — timezone-aware, overnight shifts correct.

### CP-SAT
Hard constraints (coverage, skills, no overlap, availability/PTO, rest, weekly caps). Soft weighted objectives. Status OPTIMAL/FEASIBLE/INFEASIBLE/UNKNOWN with diagnostics — never fake schedule on INFEASIBLE. Reproducible mode parameters persisted.

### Independent validator
Pure Python validates schedules without calling the solver; API validate + export CSV/ICS.

### Frontend
Editors, demand calendar, Solve screen, roster (no FullCalendar Premium), scenario compare, objective breakdown.

### Verify
Known-optimum tiny instances, overnight/PTO/infeasible tests, 10× reproducibility hash, Playwright demo→solve→validate→export; ALGORITHM.md + README + GITHUB_METADATA; commit & push.
