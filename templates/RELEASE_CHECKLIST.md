# Public-release checklist

- [ ] The product's defining workflow actually works from UI to backend to database/engine.
- [ ] README headline and features match implemented code; pending features are marked as roadmap.
- [ ] Clean setup was tested from documented instructions; `.env.example` has no secrets.
- [ ] API endpoints, example commands, ports, versions and links in README are correct.
- [ ] Deterministic, explicitly synthetic demo dataset is included; no private employee/candidate information.
- [ ] Backend unit/integration tests pass; frontend typecheck/test/build pass; core E2E smoke test passes (or failure documented).
- [ ] GitHub Actions CI runs on pushes and pull requests.
- [ ] Upload validation, input schemas, authentication scope and privacy boundaries are documented and tested.
- [ ] No credentials, hidden `.env`, uploaded documents, dumps, local model weights or `.venv` were committed.
- [ ] Genuine screenshots exist at referenced paths and show the current working version.
- [ ] Actual license is chosen and added; third-party asset and code license requirements honored.
- [ ] Nontrivial domain claims have method, assumptions, metrics and limitations documented.
- [ ] `docs/GITHUB_METADATA.md` contains description, recommended topics and honest release summary.
- [ ] Broken-link checks, lint, tests and builds were run, with outputs recorded.
- [ ] Repository is public only when ready, GitHub About and social preview are set, profile README links work.
