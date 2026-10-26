# CLAUDE.md

## About me
- Computer science graduate, currently job-hunting. Early-career (junior) level. Currently on a bootcamp.
- Long-term goal: work in the **environmental sector**. Immediate goal: an impressive data science portfolio project.
- Past projects:
  - A **convolutional autoencoder (PyTorch)** to extract behavioural motifs from bee behaviour data.
  - A **database and XML mapping** project.
- Languages: **Python** (main; PyTorch for ML) and **Java** (proficient). Less experienced with front-end JavaScript.
- I have **ADHD**: constant productivity is hard for me, and small, clearly bounded tasks help a lot.
- Availability: every day except **Wednesdays 2pm–5pm** and **Thursdays 9am–5pm** (UK time). Treat Thursdays as light days: suggest low-effort tasks for Thursday evenings.
- Budget: as close to **zero** as possible. Free tiers only unless I say otherwise.

## How I like to work
- **Prototype first, then test.** Get something working, then harden it with tests.
- **Small PRs.** Keep each change focused on one thing.
- **Detailed explanations.** Explain the why behind choices, the trade-offs, and what you rejected. Use plain English before jargon.
- **Code style:** scalable and strongly encapsulated.
  - Use clear interfaces or abstract base classes at boundaries such as data sources and models.
  - Keep internals private (`_name`) and expose small public APIs.
  - Use type hints throughout, and dataclasses or pydantic for configs and data models.
  - Prefer small modules with a single responsibility. Avoid god-scripts.
  - Keep side effects (network, disk, randomness) behind classes or passed-in objects so tests can swap in fakes.
  - In front-end code: keep data loading separate from rendering, and keep each screen in its own module.
- Before writing code for a feature, check that it has a spec in `specs/`. If it doesn't, propose one first.
- **AI assistance is encouraged.** Write code, tests, scaffolding, front-end pages and doc drafts freely once a spec exists, but:
  - explain what you wrote and why, so I can defend it in an interview, especially front-end code
  - keep changes PR-sized so I can review them
  - flag anything I should understand more deeply rather than just accept
  - keep a short log of significant AI contributions in `ai-usage.md` for the write-up.

## Helping me stay on track
- Break work into tasks of about half a day, each with a clear finish line.
- At the end of a session, update `progress.md` with what was done and the single **next step**.
- If I go off on a tangent, put the idea in `ideas.md` and steer me back to the current roadmap feature.
- Remind me of the roadmap's decision gate and finish lines when scope starts to creep.

## Current project: Chorus (working name)
- A **3-week bootcamp** project (about 14 days of planned work plus buffer): a **clickable prototype of an acoustic bird-monitoring dashboard** for UK conservation teams, using illustrative data. I plan to turn it into a real product afterwards.
- Key docs: `PRD.md`, `roadmap.md`, `specs/`, `decisions/` (ADRs), and later `docs/technical-design.md` and `docs/model-card.md`.
- Core principles:
  - Static clickable prototype on GitHub Pages; screens read JSON fixtures that follow the data contract (ADR 0001, spec 01).
  - The data contract is what lets the prototype become a product. Don't let screens depend on anything outside it.
  - Illustrative data is always labelled as illustrative. Never present it as real results (ADR 0004).
  - The ML approach is a proposal, explained but not implemented in v1 (ADR 0003). Real model output only via the stretch proof-of-concept, after the decision gate.
  - Credit every recording with its recordist and licence.
- Never commit credentials or large audio files.
