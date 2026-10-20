# GitHub publish guide (existing repositories)

> **Audience:** Owner preparing a **local** sibling product repo (or this pack) for a careful public release.  
> **Default agent policy:** inspect and prepare checklists only. **No push. No visibility change. No deploy. No profile overwrite.**

Sibling product remotes already exist under `https://github.com/hasanhuseyinyetkiner/<repo>`. Treat them as **pre-existing**. Do **not** run greenfield create/push flows against them.

## Never do this on an existing checkout

```bash
# FORBIDDEN when origin already points at the product (or pack) repo
gh repo create … --public --source=. --remote=origin --push
git push  # unless the owner just re-authorized push for this repo in-chat
gh repo edit … --visibility public  # unless the owner just re-authorized visibility
```

Creating a **new** empty remote is a separate, owner-driven action. Agents must not invent remotes or overwrite `origin`.

## Pre-flight for an existing repo

Run locally (report outputs; do not push):

1. **Remotes & branch**
   - `git remote -v` — confirm expected `origin` URL.
   - `git status -sb` — clean working tree or explicitly staged release commit (local only).
   - `git branch -vv` — tracking branch; note unpushed commits (do not push them without fresh approval).
2. **Private → public review (owner decision)**
   - Confirm current visibility (GitHub UI or `gh repo view --json isPrivate,visibility`).
   - Changing private→public requires **explicit owner approval in the current chat** after the checklist below is green.
3. **Secret scan**
   - Ensure `.env`, keys, uploads, dumps, `.venv`, `node_modules`, model caches, local SQLite/Qdrant data are gitignored and never committed.
   - Search history/working tree for tokens (`gh`, `sk-`, `AKIA`, private keys). Rotate anything that ever leaked.
4. **License (owner-pending)**
   - Development amendments often say: do **not** create `LICENSE` while building.
   - Public release requires an owner-chosen license that is compatible with dependencies (e.g. HPM optional AGPL PM4Py path).
   - Agents: document options and blockers; **never silently choose** MIT/Apache/AGPL for the owner.
5. **Actions / CI exposure**
   - Review `.github/workflows/*` for secrets usage, `pull_request_target`, unchecked `workflow_dispatch` inputs, and compose that bind `0.0.0.0` unexpectedly.
   - Confirm CI badges in README match workflows that actually exist.
6. **Claims vs code**
   - README shipped vs roadmap; SQLite local vs Postgres Compose/CI; optional extras (PM4Py, embeddings) not listed as hard requirements.
7. **Explicit owner approvals (gate)**
   - [ ] Push allowed for this repo in this chat?  
   - [ ] Visibility change to public allowed?  
   - [ ] License file content chosen by owner?  
   - [ ] Pin on profile allowed?  
   - Until checked by the owner, stop after local preparation.

## Profile README (prepare content only)

Target path when the owner is ready: public repo `hasanhuseyinyetkiner/hasanhuseyinyetkiner` root `README.md`.

- Draft from [`PROFILE_README_TEMPLATE.md`](PROFILE_README_TEMPLATE.md).
- **Do not** `git push` to the profile repo or overwrite the live profile from an agent session unless the owner explicitly re-authorizes that push.
- Featured product links: label **private / not published yet** until each product repo is intentionally public.

## Pinning

Pin only repositories that are public, documented, and actually runnable. Pinning is an owner UI action after publication.

## If you truly need a brand-new empty remote

Only when `git remote -v` shows **no** origin and the owner asks to create one:

1. Prefer creating an empty repo in the GitHub UI as **private** first.
2. Add `origin`, push after secret scan + owner approval.
3. Flip visibility to public only after [`RELEASE_CHECKLIST.md`](RELEASE_CHECKLIST.md) and license decision.

## References

- Release checklist: [`RELEASE_CHECKLIST.md`](RELEASE_CHECKLIST.md)
- Profile template: [`PROFILE_README_TEMPLATE.md`](PROFILE_README_TEMPLATE.md)
- GitHub profile README docs: https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme
- `gh repo create` manual (greenfield only): https://cli.github.com/manual/gh_repo_create
