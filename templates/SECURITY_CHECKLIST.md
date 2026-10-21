# Security checklist

> **Status:** Reusable blank. Presence in this pack does **not** mean any product repo has filled or applied this template.

Portfolio demos are usually loopback + synthetic data. Do not claim compliance, penetration-test completion, or “production hardened” without evidence.

## Meta

| Field | Value |
| --- | --- |
| Repository | |
| Commit SHA | |
| Reviewer / date | |
| Threat model scope | demo / local / networked |

## Surface inventory

- [ ] HTTP API routes listed (auth required? public?)
- [ ] File upload / import endpoints listed
- [ ] Admin or destructive endpoints listed
- [ ] Background jobs / workers listed

## Configuration

- [ ] Default bind address reviewed (prefer loopback for demos)
- [ ] CORS / CSRF posture documented honestly
- [ ] Secrets only via env; `.env` gitignored; `.env.example` sanitized
- [ ] Dependency pins / known advisories spot-checked for critical libs

## Input & data

- [ ] Request size / upload limits enforced
- [ ] Path traversal / zip bombs considered where archives used
- [ ] SQL / ORM usage parameterized; no string-built queries
- [ ] Synthetic fixtures contain no real PII

## Auth & tenancy (if any)

- [ ] Unauthenticated demo mode labeled as such
- [ ] Session / token handling reviewed **or** N/A documented
- [ ] No cross-tenant IDOR on demo multi-user paths (or single-tenant only)

## Supply chain & CI

- [ ] Workflows do not print secrets
- [ ] Third-party Actions pinned or reviewed before public
- [ ] No credentials in git history of this branch (local scan)

## Documentation

- [ ] `SECURITY.md` (or equivalent) states boundaries and how to report issues
- [ ] Limitations: what this software does **not** protect against

## Outcome

**Residual risks:**

**Blockers before public host:**
