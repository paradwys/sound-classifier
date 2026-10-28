# sound-classifier (Chorus)

**Chorus** is a clickable prototype of an acoustic bird-monitoring dashboard for UK conservation teams. Ecologists leave audio recorders at field sites for weeks, producing far more sound than anyone can listen to. Machine learning can pick out which birds were calling, and Chorus is the layer that turns those detections into something people can check and act on: where and when each species was heard, how confident the model is, and a review queue for uncertain detections. This bootcamp version uses clearly labelled **illustrative data**, built against a data contract so real model output can replace it later.

> Status: week 1, project setup. See [`roadmap.md`](roadmap.md).

## Project docs
- [`PRD.md`](PRD.md): who it's for, what it does, what's in and out of scope
- [`roadmap.md`](roadmap.md): features in order, each with a finish line
- [`specs/`](specs/): one spec per feature
- [`decisions/`](decisions/): architecture decision records (ADRs)

## Folder layout
```
src/chorus/   Python package: data contract and illustrative-data generator
tests/        automated tests (pytest)
specs/        feature specs
decisions/    ADRs
```

## Getting started
```bash
python -m venv .venv
source .venv/Scripts/activate   # Git Bash on Windows (macOS/Linux: .venv/bin/activate)
pip install -e ".[dev]"
ruff check .
pytest
```

## AI assistance
This project is built with AI assistance (Claude). Significant contributions are logged in [`ai-usage.md`](ai-usage.md).
