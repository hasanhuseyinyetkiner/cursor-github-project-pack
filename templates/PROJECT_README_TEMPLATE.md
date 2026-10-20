<!--
TEMPLATE — replace every placeholder with VERIFIED, project-specific facts and delete unused sections.

First-impression rules (researched 2026-10, GitHub Docs + current README practice):
- The README renders BELOW the file list: the hero must land in the first screenful after that.
- ONE focal asset above the fold: a light/dark <picture> banner OR a real screenshot. Never two.
- Badges are status, not decoration: 3–5 max and only real ones (CI, license, release).
- Dot-separated nav row under the pitch so skimmers can jump.
- Mermaid for structure (re-themes with GitHub, diffable). Theme it with %%{init}%%.
- GitHub alerts (> [!NOTE] etc.) at most once per major section. <details> for reference material.
- Relative paths for repo assets (they update on push; external images are camo-cached).
- Alt text on every image describes what it shows. No running text rendered as image.
- Never: fake screenshots, invented numbers, dead links, "production-ready"/"bias-free" claims.
-->

<a id="readme-top"></a>

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/banner-dark.svg">
  <img alt="PROJECT_NAME — ONE_LINE_PITCH" src="docs/assets/banner-light.svg" width="100%">
</picture>

<!-- Real badges only, e.g. CI once .github/workflows/ci.yml exists and has run:
[![CI](https://github.com/USERNAME/REPO/actions/workflows/ci.yml/badge.svg)](https://github.com/USERNAME/REPO/actions/workflows/ci.yml) -->

**TWO_SENTENCE_PITCH — what it does and why it is different.**

[Quick start](#quick-start) · [How it works](#how-it-works) · [Demo](#60-second-demo) · [Engineering](#engineering-decisions) · [Limitations](#security-privacy-and-limitations)

</div>

<br>

<!-- Real screenshot captured from the running app (light/dark pair if both exist). -->
<p align="center">
  <img alt="DESCRIBE WHAT THE SCREEN SHOWS" src="docs/screenshots/HERO.png" width="100%">
</p>

## Why it exists

**Bold one-line problem.** Two sentences on who has this problem and what they do today. Then what this project does differently — concretely.

## What you get

| | Capability | Status |
| --- | --- | --- |
| 🔎 | **Verified feature** — one-line takeaway | Shipped |
| 🧭 | **Verified feature** — one-line takeaway | Shipped |
| 🧪 | **Planned feature** — one-line takeaway | Roadmap |

## How it works

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#ACCENT_TINT", "primaryBorderColor": "#ACCENT", "lineColor": "#ACCENT", "fontFamily": "Inter, Segoe UI, sans-serif"}}}%%
flowchart LR
  U[Browser · React] -->|REST| A[FastAPI]
  A --> E[Domain engine]
  A --> D[(SQLite local / PostgreSQL CI)]
```

One paragraph walking through the diagram. Link to `docs/ARCHITECTURE.md`. Distinguish **shipped** vs **roadmap**. Do not list optional extras (PM4Py, embeddings) as hard requirements unless required to run the demo.

## Quick start

> [!NOTE]
> State exactly which path was verified where (e.g. native + SQLite verified locally; Docker Compose + PostgreSQL verified in CI).

```bash
# exact, tested commands only
```

| Service | URL |
| --- | --- |
| Web app | http://localhost:PORT |
| API docs (OpenAPI) | http://localhost:PORT/docs |

## 60-second demo

1. Step with the real button/command.
2. Step.
3. What you should see — and what it does **not** prove.

<details>
<summary><b>API example</b></summary>

```bash
curl -s http://localhost:PORT/api/... | jq
```

</details>

## Engineering decisions

Non-trivial choices and trade-offs, each in 2–3 sentences with a link to `docs/DECISIONS.md`.

## Testing

Exact commands and the latest verified result summary (copy real output; no invented coverage).

## Security, privacy and limitations

> [!IMPORTANT]
> Synthetic data only. Not legal/compliance advice. No automated employment decisions.

Link `SECURITY.md`, `docs/LIMITATIONS.md`.

<details>
<summary><b>Project structure</b></summary>

```text
accurate tree
```

</details>

## Roadmap

- [ ] Planned capability

## Contributing · License

See `CONTRIBUTING.md`. License: state the actual license, or "pending owner decision".

<p align="right"><a href="#readme-top">↑ back to top</a></p>
