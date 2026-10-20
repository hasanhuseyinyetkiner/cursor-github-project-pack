# Cursor GitHub README audit — paste into Agent after MVP is working

You are a senior open-source maintainer, technical writer, product designer and skeptical interviewer reviewing this repository before a public GitHub launch.

Inspect the actual filesystem, working app, API routes, tests, dependency files and screenshots. Refactor the root README.md to be the best **truthful, impressive, skimmable English open-source README** this repository can support. The goal is to show real engineering depth, not hype.

REQUIRED:
- Clear hero headline and meaningful two-sentence pitch; visually attractive but restrained.
- Honest feature matrix with shipped functionality only. Roadmap separate.
- A prominent authentic screenshot or short GIF ONLY if captured from the real running app; otherwise omit and explain how to capture it.
- Working badges only if workflow/license genuinely exists.
- Mermaid architecture diagram corresponding to real modules and infrastructure.
- Exact copy/paste Quick Start commands tested in this checkout; prerequisites, .env.example, expected URLs, seed/demo command, optional API keys.
- Reproducible 60-second example workflow demonstrating the unique value.
- API examples based on routes actually implemented.
- Model/algorithm/method explanation: inputs, constraints, assumptions, metrics, reproducibility and limitations.
- A clear section with test commands and verified results; never invent numbers.
- Privacy, security, sensitive HR data, human oversight, licensing and limitations.
- Links to real docs and example data; contributions instructions and license.
- Set up `docs/GITHUB_METADATA.md` with suggested public description, GitHub topics, release title, social preview concept, and recommended pinned-repo one-line summary.

VALIDATION:
1. Check links and local paths; ensure no dead links.
2. Verify code, commands, imports, ports, API routes, docker services and screenshots.
3. If screenshot generation is feasible, run the app and use Playwright to take REAL screenshots under `docs/screenshots/` (no mockups misrepresented as product).
4. Run relevant tests/build and clearly document what succeeded and failed.
5. Identify unsupported README claims and rewrite or remove them.
6. Finish with a short checklist of what the human owner still needs to supply (e.g., GitHub username, actual deployment URL, logo, chosen license).

Do not create/push remote repositories, claim security/compliance certification or invent a live demo URL.
