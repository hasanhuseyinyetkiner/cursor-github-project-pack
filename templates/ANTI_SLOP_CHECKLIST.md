# Anti-slop checklist

> **Status:** Reusable blank. Presence in this pack does **not** mean any product repo has filled or applied this template.

Use before publishing README, profile blurbs, or case studies. Goal: evidence-first prose, not AI filler.

## Claims

- [ ] Every metric has a command, dataset, and date
- [ ] No “production-ready”, “enterprise-grade”, “bias-free”, “99% accurate” without proof
- [ ] Planned work is labeled planned (planned ≠ shipped)
- [ ] Stack strings match dependency files and UI (no FullCalendar Premium if custom grid; no required PM4Py if pandas core; embeddings off by default if so)

## Language

- [ ] Remove empty superlatives (“seamless”, “cutting-edge”, “robust solution”) unless tied to a concrete behavior
- [ ] Remove duplicated marketing paragraphs that add no new fact
- [ ] Prefer invariants, limits, and reproduction over adjectives
- [ ] No emoji decoration required for professionalism

## Artifacts

- [ ] Screenshots from the running app at referenced paths (or omit)
- [ ] Badges only for workflows / licenses that exist
- [ ] No placeholder demo URLs
- [ ] Links resolve locally or to real remotes

## Process

- [ ] Diffed README against code and tests
- [ ] Second pass: delete any sentence that could apply to any unrelated product

**Sentences removed (optional log):**
