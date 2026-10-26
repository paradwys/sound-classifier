# ADR 0004: Illustrative data, clearly labelled, with real audio clips

**Status:** Accepted
**Date:** 2026-10-22

## Context
The prototype needs data that looks realistic so the screens can be evaluated properly. No model is being trained, so there are no real detections. Showing fake results as if they were real would undermine trust, and conservation decisions depend on trustworthy data.

## Decision
- Detections, sites and activity patterns are **generated** by a seeded Python script following realistic, documented rules (see `specs/01-data-contract.md`).
- Audio clips and spectrograms come from a small number of **real, openly licensed recordings**, with recordist, source and licence credited.
- Every data screen shows an **"Illustrative data"** notice, and the dataset metadata carries `illustrative: true`. If the stretch proof-of-concept adds real model output, that is labelled separately as real.
- The generator deliberately includes errors (false positives, low-confidence detections, noisy periods) so the review queue and limitations pages are realistic.

## Alternatives rejected
- **Hand-written fixture files.** Quick for one screen, but inconsistent across screens and hard to change.
- **Purely random data.** Charts would show no believable patterns, so the demo wouldn't tell a story.
- **Real detections from a public dataset.** More authentic, but finding UK field data with matching labels would eat the timebox. It's the proof-of-concept's job, not v1's.
- **Synthetic audio.** Unrealistic and unnecessary when real recordings are available.

## Consequences
- ✅ Believable demo, honestly labelled.
- ✅ The generator rules double as documentation of real bird behaviour (dawn chorus, migration timing, habitat), showing domain interest.
- ❌ The patterns reflect my assumptions, not real field results. The case study says so.
