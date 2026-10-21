# CI failure triage guide

> **Status:** Reusable blank / process guide. Presence in this pack does **not** mean any product’s CI was triaged with this file.

Use when GitHub Actions (or local equivalents) fail. Prefer root-cause fixes over deleting tests or weakening gates.

## 1. Capture identity

| Field | Value |
| --- | --- |
| Repository | |
| Workflow / job / step | |
| Run URL or local log path | |
| Commit SHA | |
| Branch | |
| First failing command | |
| Exit code / error signature | |

## 2. Classify

Pick one primary class:

- `build` — packaging, COPY context, missing README in image, lockfile
- `typecheck` — TypeScript / mypy contract drift
- `unit` — assertion or fixture
- `integration` — DB / API / queue
- `e2e` — UI / timing / env
- `compose` — Docker / service health (may be `SKIP` locally if Docker absent)
- `lint` / `format`
- `flaky` — only after two green re-runs with same SHA prove non-determinism
- `infra` — runner, Actions outage, secret missing

## 3. Reproduce

1. Same command locally (record exit code).
2. If Docker-only: document `BLOCKED` locally; use CI logs + smallest Dockerfile repro.
3. Note env differences (OS, Python, Node, optional extras).

## 4. Root cause

One paragraph: what is true in code vs what the job expected.

## 5. Fix options (choose minimal)

| Option | Risk | Chosen? |
| --- | --- | --- |
| Fix product code / Dockerfile / types | low–med | |
| Fix test to match intentional contract | med (justify) | |
| Skip/xfail with ticket + reason | high scrutiny | |
| Delete assertion / disable job | **avoid** unless obsolete | |

## 6. Verify

| Check | Result |
| --- | --- |
| Local command exit code | |
| New/updated regression test | |
| CI re-run on same branch (if owner allows push) | not run / URL |

## 7. Prevent

- Checklist item or doc line to stop recurrence:
- Related templates: [`TEST_EVIDENCE_TEMPLATE.md`](TEST_EVIDENCE_TEMPLATE.md), [`RELEASE_READINESS_TEMPLATE.md`](RELEASE_READINESS_TEMPLATE.md)
