# Cursor continuation prompt — paste into the same repository's Agent chat

Inspect the current repository, project plan, and the real state of code/tests. Read `.cursor/rules/*.mdc`, README and docs. Do not reset working code, hallucinate completed features, or restart from scratch.

1. Identify what is actually implemented and what is not, using file inspection and test runs.
2. Choose the next smallest unfinished vertical slice in the original project specification.
3. Implement it fully, including backend, frontend, data, validation, tests, and docs where relevant.
4. Run available lint/typecheck/unit/integration/build commands; repair failures caused by this change.
5. Update README to describe only genuinely shipped behavior.
6. At the end, give me a concise status table: complete, tested, incomplete, blocker; include exact command outputs and the next slice.

Do not call an external paid service, deploy or push to GitHub without my permission. Continue implementation rather than just describing how it could be done.
