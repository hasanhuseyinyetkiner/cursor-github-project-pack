# Public-release checklist

Use before making a repository **public**. Agents may verify items locally; they must **not** push, change visibility, or create a `LICENSE` unless the owner has just authorized that specific step.

## Product truth

- [ ] The product's defining workflow actually works from UI to backend to database/engine.
- [ ] README headline and features match implemented code; pending features are marked as roadmap (**planned ≠ shipped**).
- [ ] Stack claims match reality (examples: HPM pandas core + optional PM4Py; WFO custom roster, not FullCalendar Premium; SkillGraph embeddings optional/off by default; SQLite local vs Postgres Compose/CI).
- [ ] Clean setup was tested from documented instructions; `.env.example` has no secrets.
- [ ] API endpoints, example commands, ports, versions and links in README are correct.
- [ ] Deterministic, explicitly synthetic demo dataset is included; no private employee/candidate information.
- [ ] Backend unit/integration tests pass; frontend typecheck/test/build pass; core E2E smoke test passes (or failure documented).
- [ ] GitHub Actions CI workflows exist and are reviewed for secret/Actions exposure before going public.
- [ ] Upload validation, input schemas, authentication scope and privacy boundaries are documented and tested.
- [ ] No credentials, hidden `.env`, uploaded documents, dumps, local model weights or `.venv` were committed.
- [ ] Genuine screenshots exist at referenced paths and show the current working version.
- [ ] Nontrivial domain claims have method, assumptions, metrics and limitations documented.
- [ ] `docs/GITHUB_METADATA.md` contains description, recommended topics and honest release summary.
- [ ] Broken-link checks, lint, tests and builds were run, with outputs recorded.

## Licensing (three layers — do not collapse them)

| Layer | Meaning | Who acts |
| --- | --- | --- |
| **Historical / development** | `REVIEW_AMENDMENTS` C-4: do **not** create `LICENSE` while building; README may say pending | Agent / builder |
| **Release requirement** | A public repo should carry an owner-chosen license compatible with dependencies | **Owner** |
| **Owner-pending** | Until the owner decides, leave `pending owner decision`; document AGPL/optional-extra constraints (e.g. HPM-1) | Owner |

- [ ] Owner has **explicitly chosen** the license text (agents must not silently pick MIT/Apache/AGPL).
- [ ] Third-party asset and dependency license requirements are honored (optional AGPL paths documented).
- [ ] `LICENSE` file added **only after** owner choice (or deliberately deferred with README note if staying private).

## GitHub visibility & distribution (owner gates)

- [ ] Secret scan clean; remotes inspected (`git remote -v`).
- [ ] Owner approved **push** of the release commit (if anything remains unpushed).
- [ ] Owner approved **private → public** (or confirmed already public).
- [ ] About topics / description set from `docs/GITHUB_METADATA.md`.
- [ ] Profile Featured links updated only after publication; private repos labeled as such until then.
- [ ] Pinning done by owner after public release.

See [`GITHUB_PUBLISH.md`](GITHUB_PUBLISH.md). Never run `gh repo create … --public --push` on an existing product remote.
