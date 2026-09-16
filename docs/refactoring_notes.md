# Portfolio Refactoring Notes

This repository is a cleaned and reorganized portfolio version of a group academic project. The analytical goals of the original project were preserved, while several implementation details were improved.

## Main improvements

1. **Normalized artist relationships** - the original schema stored an artist string directly against each track. The portfolio schema uses `Artist` plus a many-to-many `Track_Artist` table, so collaborations are represented correctly.
2. **No hard-coded credentials** - MySQL credentials are read from environment variables via `.env` (which is ignored by Git).
3. **Defensive data cleaning** - malformed numeric values are safely coerced to `NULL`; the 953-row source dataset is preserved.
4. **Idempotent loader** - the loader uses upserts and can be rerun without creating duplicate tracks.
5. **Nine consistent queries** - SQL and the interactive Python query tool now expose the same nine analyses.
6. **Query 9 semantics refined** - the original project described an average stream count for individual collaborative tracks, although each track has one stream count. The portfolio version reports the stream count directly and ranks collaborative tracks by that value.
7. **Reproducible project structure** - schema, queries, loader, query tool, tests, dataset notes, environment template and sample results are separated into clear folders.

## Original presentation

A sanitized copy of the original academic presentation is included in `docs/academic_presentation.pdf` for context. It reflects the original submission. The refactored schema, code and documentation in this repository are the authoritative portfolio version.
