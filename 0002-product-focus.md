# ADR 0002: A conservation monitoring dashboard for UK birds

**Status:** Accepted
**Date:** 2026-10-22

## Context
Bioacoustics projects can target very different users. The project should show environmental relevance, suit a 3-week timebox, and feel personally meaningful.

## Decision
- **Product:** a monitoring dashboard for ecologists who deploy audio recorders at field sites and need to know which species were calling, where, when, and how confident the system is.
- **Scope:** UK birds, about 15 common species with distinctive calls, at about 6 illustrative sites in England.
- **Signature feature:** a human-in-the-loop **review queue** for uncertain detections. It's what makes this a monitoring tool rather than a classifier demo, and it links naturally to active learning.

## Alternatives rejected
- **Public "what's singing?" phone app.** Easy to understand, but it's a crowded space dominated by well-known existing apps, and it shows less about pipelines, scale and data quality.
- **Hybrid citizen-science map.** A broader story, but it splits focus across two user groups in 3 weeks.
- **Multi-taxa (birds, bats, insects).** Novel, but harder to explain simply. Bats also need ultrasonic recording, which complicates things. Kept as future work.
- **Tropical or benchmark datasets** (e.g. BirdCLEF). Well known, but less relevant to UK environmental employers and less familiar to me.

## Consequences
- ✅ Directly relevant to UK conservation NGOs, wildlife trusts and ecological consultancies.
- ✅ Familiar species make the demo relatable and the illustrative data easier to make believable.
- ❌ UK bird ID from sound is already well served by existing tools. The differentiator is the monitoring workflow, review and honest explanation, not the classifier itself.
