# Chorus (working name): Product Requirements

**Status:** Draft v1.0 (22 Oct 2026). Replaces the earlier Butterfly Trends draft.
**Owner:** (you)
**Context:** bootcamp project, 3 weeks. Unavailable Wednesdays 2pm–5pm and Thursdays 9am–5pm. About 15 days of planned work, with the rest kept as buffer. AI assistance is actively used.

## 1. Why this exists

Chorus is a **clickable prototype of an acoustic bird-monitoring dashboard** for UK conservation teams.

Field ecologists increasingly leave small audio recorders out in woods, wetlands and farmland for weeks at a time. That produces hundreds of hours of audio per site, far more than anyone can listen to. Machine learning can find which species are calling, but the results need to be **organised, checked by a human and explained honestly** before anyone can make conservation decisions with them. Chorus is the product layer that does that.

For this bootcamp, the goal is to show:
1. **Product and data science thinking**: a clear problem, a clear user and a well-reasoned ML design.
2. **Understanding of the ML concepts**, explained in the prototype and in a technical design doc, without implementing the full model yet.
3. **Effective, transparent use of AI-assisted tools.**
4. **Interest in environmental science**, specifically passive acoustic monitoring of birds.

**Longer term:** turn the prototype into a working product before job interviews. The prototype is therefore built against a **data contract** (see `specs/01-data-contract.md`), so illustrative data can later be swapped for real model output without redesigning the screens.

## 2. Who it serves

| User | What they need | Priority |
|---|---|---|
| **Field ecologist / survey lead** at an NGO, wildlife trust or ecological consultancy | "Which species were calling at my sites, when, and how sure is the model?" Plus a fast way to check uncertain detections | Primary product user |
| **Project or reserve manager** | A headline view across sites: species richness, notable species (e.g. Cuckoo, Nightingale), changes over the season | Secondary product user |
| **Bootcamp assessors and future employers** | A polished, clickable demo, clear explanations of the ML, and evidence of critical thinking | The real audience for v1 |

## 3. What the prototype does (v1)

All data is **illustrative** and clearly labelled as such on every screen.

1. **Project overview:** a map of recording sites with headline numbers (sites, hours recorded, species detected, detections awaiting review).
2. **Site detail:** species detected at one site, with activity charts by time of day (showing the dawn chorus) and across the season.
3. **Species view:** where and when one species was detected across all sites.
4. **Review queue:** uncertain detections shown as a spectrogram with an audio clip, and confirm / reject / "different species" buttons. This is the human-in-the-loop step.
5. **"How it works" pages:** plain-English explanations of the ML pipeline, from sound to spectrogram to model to detection to review.
6. **Limitations page:** what acoustic detections can and can't tell you.

Alongside the prototype:
- a **technical design doc** describing the proposed real system, its ML approach and evaluation plan
- a **model card** for the proposed model
- **ADRs** recording the big decisions.

## 4. In scope

- About 6 illustrative sites in England and about 15 common UK bird species with distinctive calls.
- A static, clickable web prototype hosted for free (GitHub Pages).
- A seeded Python generator for illustrative detection data, following a documented schema.
- A small number of real, openly licensed bird recordings for spectrograms and audio playback, with attribution.
- Technical design doc, model card, ADRs, case study and README.
- **Stretch (after the decision gate):** a small real proof-of-concept that runs an existing pretrained bird-sound model on about 10 clips and feeds genuine results into the prototype.

## 5. Out of scope (v1)

- Training or fine-tuning any model.
- Real uploads, audio processing or a backend.
- User accounts and permissions. Review decisions are not saved beyond the browser session.
- Species beyond the chosen ~15, and taxa other than birds (bats, insects).
- Abundance or population estimates.
- Paid tools or infrastructure.

## 6. Success criteria

- [ ] A public URL loads the clickable prototype.
- [ ] All 5 core screens (overview, site, species, review queue, how it works) are linked and clickable.
- [ ] Every data screen shows an "illustrative data" notice.
- [ ] The "How it works" pages explain at least 6 ML concepts in plain English (see §8).
- [ ] The limitations page covers at least 6 limitations from §9.
- [ ] The technical design doc and model card are published and linked from the README.
- [ ] At least 4 ADRs exist.
- [ ] The illustrative data validates against the documented schema, and the generator has automated tests.
- [ ] The README and case study explain the project in under 2 minutes and include a section on how AI assistance was used.
- [ ] All audio recordings are credited with their licence.

## 7. Constraints

- **Cost:** free tiers only.
- **Time:** 3 weeks, about 15 days of planned work plus buffer, in tasks of about half a day.
- **AI use:** encouraged. I must be able to explain everything, and the write-up says how AI was used.
- **Data terms:** respect the licence of every recording used; credit recordists.
- **Honesty:** illustrative data must never be presented as real results.

## 8. ML concepts to explain

These are what the "How it works" pages and technical design doc must cover:

1. **Spectrograms:** turning sound into an image of frequency over time, so image-style models can "see" calls.
2. **Windowing:** cutting long recordings into short clips (a few seconds) for the model to classify.
3. **Transfer learning and embeddings:** reusing a model already trained on huge amounts of bird audio, rather than starting from scratch.
4. **Confidence scores and thresholds:** why every detection has a score, and why each species may need its own cut-off.
5. **Precision and recall:** the trade-off between missing birds and false alarms.
6. **Domain shift:** why a model trained on clean, close-up recordings struggles with noisy field audio.
7. **Human-in-the-loop review and active learning:** using reviewers' corrections to improve the model over time.
8. **Calibration:** why a score of 0.9 doesn't automatically mean "90% likely to be right".

## 9. Known limitations (for the limitations page)

1. **Detection is not abundance.** Ten detections might be one very vocal bird.
2. **Detectability varies.** Loud, frequent callers are found far more easily than quiet or rare ones.
3. **Domain shift.** Models trained on clean recordings perform worse on wind, rain and distant birds.
4. **Similar calls and mimics** cause false positives.
5. **Class imbalance.** Rare species, which often matter most, have the least training data.
6. **Recorder placement bias.** Results reflect where recorders were placed, not the whole site.
7. **Confidence is not probability** unless the model is calibrated.
8. **Privacy.** Field recorders can capture human speech, so a real system needs speech filtering and must comply with UK GDPR.

## 10. Path to a real product (after the bootcamp)

1. Run a pretrained model on real field recordings and replace fixtures with genuine detections (the stretch proof-of-concept is the first step).
2. Evaluate it on labelled UK soundscapes and set per-species thresholds.
3. Add a real backend for uploads, processing and saved review decisions.
4. Use review decisions to fine-tune the model (active learning).
5. Future idea: unsupervised discovery of call types with an autoencoder, building on my bee-behaviour project.

## 11. Open questions

- Final species list and site locations: settled in roadmap feature 2.
- Which openly licensed recording source to use for real audio clips, and its current access terms: settled in feature 2.
- Whether the stretch proof-of-concept happens: decision gate at the start of week 3.
