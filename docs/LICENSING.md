# Licensing layers (pack + product repos)

This pack does **not** choose a license for the owner. Keep these layers distinct:

## 1. Historical / development constraint

Product `docs/REVIEW_AMENDMENTS.md` (C-4) told builders: **do not add a `LICENSE` file** during implementation; README states `License: pending owner decision`; do not push.

That constraint prevented agents from inventing a license mid-build. It is **not** a claim that the software is unlicenseable forever.

## 2. Current release requirement

[`templates/RELEASE_CHECKLIST.md`](../templates/RELEASE_CHECKLIST.md) requires an **owner-chosen** license before (or as part of) making a repository public, plus dependency compatibility review (notably HPM optional PM4Py / AGPL).

## 3. Owner-pending

Until the owner decides:

- Do not create `LICENSE`.
- Do not silently select MIT, Apache-2.0, AGPL, or any other SPDX id.
- Document blockers (e.g. “core is pandas-only; optional `pm4py` extra is AGPL-3.0-or-later”).

## Pack repository

This meta pack carries its own root [`LICENSE`](../LICENSE) (owner-added MIT). That does **not** license the five product repositories. Treat each product repo independently and keep them owner-pending until the owner adds a `LICENSE` there.
