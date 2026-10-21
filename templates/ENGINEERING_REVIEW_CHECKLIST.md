# Engineering review checklist

> **Status:** Reusable blank. Presence in this pack does **not** mean any product repo has filled or applied this template.

Copy into a product `docs/` only when you actually run a review. Fill with evidence (paths, commands, exit codes). Do not invent PASS.

## Meta

| Field | Value |
| --- | --- |
| Repository | |
| Reviewer | |
| Date (local) | |
| Scope (commit SHA / branch) | |
| Related findings IDs | |

## Architecture

- [ ] Critical request paths traced in code (not folder names only)
- [ ] Domain / application / API boundaries clear; no circular imports
- [ ] Persistence models match migrations; SQLite local vs Postgres CI documented
- [ ] Long-running jobs: status, cancellation, and process-death behavior understood
- [ ] Configuration and secrets loading reviewed (`.env.example` only in git)

## Correctness

- [ ] Defining domain workflow works end-to-end on synthetic data
- [ ] Happy path + at least one failure / empty / invalid input path tested
- [ ] Invariants documented (or ADR) where algorithms make hard claims
- [ ] Planned features not described as shipped

## Reliability & ops

- [ ] `/health` (or equivalent) reflects real readiness
- [ ] Logging useful for triage; no secrets in logs
- [ ] Timeouts / size limits on uploads and expensive endpoints

## Security & privacy

- [ ] Bind/demo assumptions match SECURITY docs (e.g. loopback-only)
- [ ] AuthN/AuthZ scope honest (or explicitly “none — demo only”)
- [ ] No PII / real HR data in fixtures

## Tests & evidence

- [ ] Commands run locally recorded in [`TEST_EVIDENCE_TEMPLATE.md`](TEST_EVIDENCE_TEMPLATE.md)
- [ ] CI status checked; failures triaged via [`CI_FAILURE_TRIAGE.md`](CI_FAILURE_TRIAGE.md)

## Outcome

| Severity | Count | Top IDs |
| --- | --- | --- |
| P0 | | |
| P1 | | |
| P2 | | |
| P3 | | |

**Verdict:** `BLOCK` / `CONDITIONAL` / `PASS` (choose one; justify below)

**Justification / follow-ups:**
