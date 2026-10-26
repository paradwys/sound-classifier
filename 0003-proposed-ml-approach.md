# ADR 0003: Proposed ML approach: pretrained bird-sound embeddings plus a small classifier

**Status:** Proposed. This is the design for the real product; it is not implemented in the bootcamp prototype.
**Date:** 2026-10-22

## Context
The real system must find UK bird calls in long, noisy field recordings. Labelled field audio for UK species is limited, compute budget is near zero, and results need to be explainable to ecologists. I have PyTorch and CNN experience (convolutional autoencoder for bee behaviour).

## Decision (proposed)
1. **Pre-process:** resample audio, cut it into short overlapping windows of a few seconds, and convert each window into a mel spectrogram.
2. **Embed:** pass each window through an existing **pretrained bird-sound model** (candidates: BirdNET or Google's Perch) to get an embedding, a compact numeric summary of the sound. Check each model's current licence before use.
3. **Classify:** train a **small classifier** (logistic regression or a shallow PyTorch network) on those embeddings for the chosen UK species, using labelled clips plus reviewer-confirmed detections.
4. **Post-process:** apply **per-species thresholds** chosen from precision–recall curves, and **calibrate** scores so a confidence value means something.
5. **Baseline:** compare everything against the pretrained model's own predictions used off the shelf. The custom classifier has to beat it to justify itself.
6. **Evaluate** on held-out field recordings, splitting by **site** (not by random clip) so the model is tested on places it has never heard. Report per-species precision, recall and the effect of noise.
7. **Improve** using review-queue decisions (active learning): prioritise reviewing the detections the model is least sure about.

## Alternatives rejected
- **Train a CNN from scratch on spectrograms.** It's the classic approach and close to my previous project, but it needs far more labelled audio and compute than is available, and would likely underperform pretrained models.
- **Use a pretrained model off the shelf only.** It's the simplest option and a strong baseline, so it's kept as the baseline, but it doesn't adapt to local recording conditions or learn from reviewers.
- **Fine-tune a large audio transformer.** Potentially the most accurate, but too much compute for a zero budget and harder to explain.
- **Random train/test split by clip.** Clips from the same site and day are very similar, so this leaks information and gives overly optimistic results.

## Consequences
- ✅ Realistic on a small budget, and reflects how bioacoustics is commonly done in practice.
- ✅ Gives the prototype a concrete story for its "How it works" pages and model card.
- ✅ The optional proof-of-concept (roadmap feature 11) can test step 2 or the baseline cheaply.
- ❌ Depends on third-party pretrained models and their licences.
- ❌ Unproven until built. The prototype and docs must present it as a design, not a result.
