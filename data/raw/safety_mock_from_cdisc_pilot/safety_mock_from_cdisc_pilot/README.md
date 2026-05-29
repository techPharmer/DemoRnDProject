# Safety Mock Data Package

This package simulates a Safety / Pharmacovigilance source system feed, inspired by Oracle Argus-like case management data.

## Source basis
- Subjects are derived from CDISC Pilot DM.
- Safety adverse event cases are synthetically generated.
- Intentional issues are seeded for reconciliation and DQ testing.

## Files
- safety_subjects.csv: Safety-system patient identifiers.
- safety_cases.csv: Case-level safety records.
- safety_case_events.csv: Event-level safety records.
- safety_followups.csv: Case follow-up records.
- subject_crosswalk_safety.csv: Mapping between safety patient IDs and canonical/EDC subject IDs.
- safety_recon_rules.csv: Seed reconciliation rules.
- safety_issue_seed.csv: Seed issues for issue registry/dashboard.
- safety_data_dictionary.csv: Field descriptions.

## Intended MVP use
Use this package to test:
- Safety case ingestion
- Subject crosswalk / identity mapping
- Seriousness mismatch checks
- Event chronology checks
- Potential duplicate safety event detection
- Issue registry and query recommendation workflows
