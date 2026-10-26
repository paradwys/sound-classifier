# Roadmap

The project runs for **3 weeks**. I'm available every day except **Wednesdays 2pm–5pm** and **Thursdays 9am–5pm**. Feature estimates add up to about 14 days, so the rest of the available time is deliberately kept as **buffer and rest**, not extra scope.

**Thursdays are light days:** use Thursday evenings for low-effort tasks, such as reviewing `progress.md`, tidying docs, reading what Claude produced and planning the next session.

How this roadmap works:
- **Always shippable.** The prototype shell goes live in week 1 and gets better each week, so there's always something to show.
- **Small tasks.** Each feature is split into tasks of about half a day. Each task ends by writing "next step: …" in `progress.md`, which makes it easy to pick up again after a break.
- **Ideas parking lot.** New ideas go into `ideas.md`, not into the current task.
- **AI-assisted, human-owned.** Claude drafts code, front-end pages, tests and doc drafts. I review, understand and own every change, and I can explain any of it.
- **Day estimates** are shown as (≈ days). If a feature runs more than 50% over, cut scope, not quality.

---

## Week 1: Understand, design, lay foundations

### 0. Project setup (≈ 0.5)
Set up the repo, Python environment, folder structure, linting, test runner, CI (GitHub Actions) and `CLAUDE.md`. Copy in these planning docs.
**Finish line:** the empty test suite passes locally and in CI, and the README has a one-paragraph pitch.

### 1. Users and workflow (≈ 1)
Learn how passive acoustic monitoring works in practice: recorders, deployment, data volumes, how ecologists check results. Write 2 short personas and the main user journey ("recorders come back from the field → which species, where, when, and how sure?").
**Finish line:** `docs/users.md` with 2 personas, 1 journey and a list of the 5 screens it implies.

### 2. Data contract and illustrative data (≈ 1.5) → see `specs/01-data-contract.md`
Define the data schema, choose species and sites, find openly licensed recordings, and write the seeded generator.
**Finish line:** all acceptance criteria in the spec pass.

### 3. Wireframes (≈ 1)
Rough low-fidelity layouts of the 5 screens (overview, site, species, review queue, how it works), on paper, in Figma's free tier or drafted with Claude.
**Finish line:** one wireframe per screen in `docs/wireframes/`, each with a one-line note of the question it answers for the user.

### 4. Prototype shell deployed (≈ 0.5)
Navigation, layout, the "illustrative data" banner and empty pages for all 5 screens, published to GitHub Pages.
**Finish line:** a public URL loads, every page is reachable, and every push to `main` redeploys automatically.

*(Buffer: about 1–2 days at the end of week 1.)*

## Week 2: Build the clickable prototype

### 5. Project overview (≈ 1)
Map of sites plus headline cards: sites, hours recorded, species detected, detections awaiting review.
**Finish line:** clicking a site on the map opens its site page.

### 6. Site detail (≈ 1.5)
Species list for one site with detection counts, plus two charts: activity by time of day (showing the dawn chorus) and across the season.
**Finish line:** works for every site in the fixtures, and each chart has a one-line plain-English caption.

### 7. Review queue (≈ 1.5)
A list of uncertain detections. Each shows a spectrogram, an audio player, the model's top guesses with confidence, and confirm / reject / "different species" buttons.
**Finish line:** a user can review 5 detections in a row, and the queue counter updates. Decisions live only in the browser session.

### 8. Species view (≈ 1)
For one species: which sites it was detected at, when, and a short species card (call description, conservation status, link to a recording).
**Finish line:** every species in the fixtures has a working page, reachable from site pages.

## Week 3: Explain, decide, polish

### ⛳ Decision gate (first session of week 3)
- If features 0–8 are done → do **feature 11** (proof-of-concept).
- Otherwise → skip it and use the buffer to finish 0–8. Write it up as future work.

### 9. "How it works" and limitations pages (≈ 1)
Plain-English explanations of the 8 ML concepts and 8 limitations in the PRD, with a simple diagram of the pipeline.
**Finish line:** pages are live, and a non-technical friend can explain back what a spectrogram and a confidence threshold are.

### 10. Technical design doc and model card (≈ 1.5)
`docs/technical-design.md`: architecture, data flow, proposed model, evaluation plan, risks. `docs/model-card.md`: intended use, training data, metrics to report, known failure modes.
**Finish line:** both docs are complete, link to the relevant ADRs, and are linked from the README and the prototype.

### 11. (Stretch) Real proof-of-concept (≈ 1.5)
Run an existing pretrained bird-sound model on about 10 real recordings and load its genuine outputs into the prototype through the same data contract.
**Finish line:** at least one site in the prototype shows real model output, clearly labelled as such, and the case study compares it with what's in the recordings.

### 12. Case study and README (≈ 1)
Problem, users, design, ML approach, limitations, how AI was used, and the path to a real product.
**Finish line:** the case study is published, and the README links to it, the live prototype and the design docs.

### 13. Final QA and demo script (≈ 0.5)
Check links, mobile layout, attribution and the illustrative-data labels. Write a 3-minute demo walkthrough script.
**Finish line:** the PRD success-criteria checklist is all ticked.

---

## Progress

| # | Feature | Week | Status |
|---|---|---|---|
| 0 | Project setup | 1 | ⬜ |
| 1 | Users and workflow | 1 | ⬜ |
| 2 | Data contract | 1 | ⬜ |
| 3 | Wireframes | 1 | ⬜ |
| 4 | Prototype shell | 1 | ⬜ |
| 5 | Project overview | 2 | ⬜ |
| 6 | Site detail | 2 | ⬜ |
| 7 | Review queue | 2 | ⬜ |
| 8 | Species view | 2 | ⬜ |
| 9 | How it works + limitations | 3 | ⬜ |
| 10 | Technical design + model card | 3 | ⬜ |
| 11 | Proof-of-concept (stretch) | 3 | ⬜ |
| 12 | Case study + README | 3 | ⬜ |
| 13 | Final QA + demo script | 3 | ⬜ |
