# Spec 01: Data contract and illustrative data

**Roadmap feature:** 2
**Status:** Draft
**Depends on:** 0 (project setup), 1 (users and workflow)

## Purpose

Define the shape of the data the dashboard displays, and generate a realistic illustrative dataset in that shape.

This is the most important foundation for the "real product later" goal. The prototype screens only ever read data that follows this contract. Later, real model output that follows the same contract can replace the illustrative data without changing the screens.

## Behaviour

### The data model
Defined once in Python (pydantic models) and exported as JSON Schema, so Python and the front end share one source of truth.

| Entity | Key fields |
|---|---|
| **Species** | code, common name, scientific name, conservation status (e.g. UK Birds of Conservation Concern list), call description |
| **Site** | id, name, latitude, longitude, habitat, recorder id, deployment start and end dates |
| **Recording** | id, site id, start time, duration, file reference (if a real clip exists) |
| **Detection** | id, recording id, start and end offset (seconds), species code, confidence (0–1), top alternative species with scores, model version, review status (unreviewed / confirmed / rejected / corrected) |
| **Dataset metadata** | `illustrative: true/false`, generator version, random seed, date generated, attribution list |

### The illustrative dataset
1. About **6 sites** across England in different habitats (woodland, wetland, farmland, heath, parkland, coastal), covering about **6 weeks** in spring.
2. About **15 species** with distinctive calls, for example: Robin, Blackbird, Song Thrush, Wren, Chiffchaff, Willow Warbler, Blackcap, Great Tit, Blue Tit, Chaffinch, Wood Pigeon, Skylark, Cuckoo, Tawny Owl, Nightingale. The final list is recorded in `decisions/0005-species-and-sites.md`.
3. **Realistic patterns**, so the charts tell a believable story:
   - a dawn chorus peak in the early morning
   - Tawny Owl mostly at night
   - migrants (Chiffchaff, Cuckoo, Willow Warbler) appearing from their typical spring arrival dates
   - habitat fit (Skylark on farmland and heath, not woodland).
4. **Deliberate imperfections**, so the review queue and limitations pages have something to show: about 10% low-confidence detections, a few false positives between similar-sounding species, and some detections during noisy periods (rain or wind).
5. A **seeded Python generator** produces the dataset, so the same seed always gives the same output.
6. A small number of **real, openly licensed recordings** (about one per species) supply the audio clips and spectrogram images in the review queue and species pages. Each clip's recordist, source and licence go in `attribution.json`. Check the source's current access terms and use only licences that allow this kind of reuse.

## Design notes (encapsulation)

- A `DetectionSource` interface defines what the dashboard data layer needs. `IllustrativeDetectionSource` (the generator) is the first implementation. A future `ModelDetectionSource` (real model output) plugs in without changing anything downstream. This is the main design talking point.
- Pattern rules (daily activity curves, arrival dates, habitat preferences) live in a config file, not hard-coded in the generator, so they're easy to read and adjust.
- Randomness comes from one seeded generator object passed in explicitly, never from global state, so the output is reproducible and testable.
- The exporter writes JSON fixtures for the front end. It's separate from the generator, so either can change independently.

## Acceptance criteria

- [ ] The pydantic models exist, and an exported JSON Schema file is committed.
- [ ] Running the generator with the default seed produces the fixture files in the prototype's data folder.
- [ ] Running it twice with the same seed produces identical files.
- [ ] Every fixture file validates against the schema.
- [ ] Dataset metadata has `illustrative: true`.
- [ ] The species list and sites are recorded in `decisions/0005-species-and-sites.md`.
- [ ] Every real audio clip has an entry in `attribution.json` with recordist, source URL and licence.
- [ ] A short notebook or script prints summary charts (detections per hour, per species, per site) that look believable at a glance.

## Checks / tests

- **Unit:** the models reject invalid data (confidence outside 0–1, end offset before start offset, unknown species code, a recording outside its site's deployment dates).
- **Unit:** same seed → identical output; different seed → different output.
- **Pattern tests:** most Tawny Owl detections fall between dusk and dawn; no Cuckoo detections before its configured arrival date; no Skylark detections at woodland sites; early-morning activity is higher than midday.
- **Contract test:** the exported JSON Schema matches the pydantic models (catches the two drifting apart).
- **Sanity (manual):** look at the summary charts and check they tell a plausible story.

## Out of scope for this feature

- Building any screens (features 4–8).
- Running any real model (feature 11, stretch).
- Saving review decisions.
