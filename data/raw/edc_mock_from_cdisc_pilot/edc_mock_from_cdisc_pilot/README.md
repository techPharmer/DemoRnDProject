# Mock EDC Source Data — CDISC Pilot Based

This package reverse-engineers a first-pass mock **Electronic Data Capture (EDC)** source layer from the CDISC SDTM/ADaM Pilot Project.

## Source basis

- `dm.json` / SDTM DM = used to create `edc_subjects.csv`.
- `vs.json` / SDTM VS = used to create `edc_visits.csv` and `edc_vitals.csv`.

## Generated files

```text
data/mock_sources/edc/edc_subjects.csv
data/mock_sources/edc/edc_visits.csv
data/mock_sources/edc/edc_vitals.csv

data/mock_sources/metadata/study_master.csv
data/mock_sources/metadata/site_master.csv
data/mock_sources/metadata/treatment_arm_master.csv
data/mock_sources/metadata/visit_master.csv

data/mock_sources/mappings/subject_crosswalk.csv

configs/sdtm_to_edc_mapping.yml
configs/dq_seed_rules.yml
```

## Design choice

The SDTM files are already standardized. To simulate an upstream EDC feed, this package intentionally:

- renames SDTM-style fields into source-like EDC columns,
- keeps original subject IDs as source references,
- creates EDC-specific IDs,
- separates subjects, visits, and vitals,
- injects a small number of controlled DQ issues for testing.

## Generated on

2026-05-28T06:03:48.250485Z
