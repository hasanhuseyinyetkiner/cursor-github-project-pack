# Release readiness template

> **Status:** Reusable blank. Presence in this pack does **not** mean any product repo has filled or applied this template.

Use with [`RELEASE_CHECKLIST.md`](RELEASE_CHECKLIST.md) and [`GITHUB_PUBLISH.md`](GITHUB_PUBLISH.md). Agents verify locally only; **no** push, visibility change, deploy, or silent `LICENSE` creation.

## Meta

| Field | Value |
| --- | --- |
| Repository | |
| Candidate version / tag | |
| Commit SHA | |
| Date | |
| Owner approvals on file (push / public / license) | none / listed |

## Verification matrix

Record **real** results only. Use `SKIP` when blocked (e.g. Docker unavailable) and state why.

| Check | Command / evidence | Result (`PASS` / `FAIL` / `SKIP`) | Notes |
| --- | --- | --- | --- |
| Backend unit/integration | | | |
| Frontend typecheck | | | |
| Frontend unit | | | |
| Frontend build | | | |
| E2E smoke | | | |
| Compose / Docker smoke | | | |
| Markdown / local link check | | | |
| Secret scan (local) | | | |
| Screenshots authentic | | | |
| README claims vs code | | | |

## Licensing & visibility gates

| Gate | Status | Evidence |
| --- | --- | --- |
| Owner chose SPDX / LICENSE text | | |
| Dependency license constraints documented | | |
| Owner approved push (this chat) | | |
| Owner approved private→public (this chat) | | |

See [`../docs/LICENSING.md`](../docs/LICENSING.md).

## Go / no-go

**Decision:** `NO-GO` / `GO` (owner only for public)

**Blockers:**
