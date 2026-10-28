# ADR 0001: A static, clickable web prototype built against a data contract

**Status:** Accepted
**Date:** 2026-10-22

## Context
This is a 3-week bootcamp project. The aim is to show the idea, the user experience and an understanding of the ML, not a working model. The bootcamp's view is that AI agents can produce implementation code, so the idea and design are what matter. Longer term, I want to turn it into a real product before interviews. Budget is zero.

## Decision
Build a **static, clickable web prototype** in HTML, CSS and JavaScript, hosted on **GitHub Pages** and deployed by **GitHub Actions**. It's mostly AI-generated and reviewed by me.

All screens read **JSON fixtures that follow a documented data contract** (`specs/01-data-contract.md`). The fixtures come from a seeded Python generator. Later, real model output in the same shape can replace them.

Supporting libraries (all free): a mapping library such as Leaflet for the site map, a charting library for activity charts, and pre-rendered spectrogram images from real recordings.

## Alternatives rejected
- **Figma (or similar) design-only mockup.** It's fast to produce polished screens, but it can't evolve into the real product, and realistic data and audio playback are awkward. It's still fine for rough wireframes in roadmap feature 3.
- **Streamlit or Dash app.** These are Python-friendly, but they need a running server. Free tiers sleep, so a demo might start with a long wait. Custom interactions like the review queue are also clunky.
- **Quarto dashboard.** Good for charts in Python, but weak for app-style interaction (audio playback, confirm/reject buttons).
- **A full front-end framework plus backend now** (e.g. React and FastAPI). That's the right shape for the eventual product, but too much for 3 weeks. The data contract keeps the path open.

## Consequences
- ✅ Free, fast to load and easy to demo from a link.
- ✅ The data contract makes "prototype → product" an incremental change, not a rewrite. This is a strong interview talking point.
- ✅ Python still does the data work (schema, generator, stretch proof-of-concept).
- ❌ Most front-end code will be AI-generated in a language I use less. I need to review it carefully and be able to explain its structure.
- ❌ Review decisions can't be saved across sessions without a backend. That's acceptable for a prototype.
