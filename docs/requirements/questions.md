guide to follow :
1. Business objective
2. Users/personas
3. Current process
4. Pain points
5. Data sources
6. Required datasets/entities
7. Data quality expectations
8. Transformation/business rules
9. Output/consumption needs
10. Security/governance needs
11. Non-functional requirements
12. Success criteria
13. Out of scope

# Discovery Questionnaire

## Business Context & Objectives

- What business problem is this initiative trying to solve?

- What are the primary objectives for this platform?
  Examples:
  - Faster analytics
  - Centralized data access
  - Improved data quality
  - Reduced manual effort
  - AI readiness

- Are there specific scientific or business use cases this platform must support initially?

- How will success be measured?
  Examples:
  - Reduced turnaround time
  - Fewer manual interventions
  - Improved trust in reporting datasets
  - Faster study data availability

---

## Current State Understanding

- Can the business provide a high-level overview of the current process for acquiring, transforming, and consuming clinical data?

- What are the biggest pain points in the current ecosystem?

- Which teams currently own different parts of the process?

---

## Users & Consumers

- Who are the expected business and technical users of this platform?
  Examples:
  - Clinical data managers
  - Clinical operations
  - Safety reviewers
  - Biostatistics teams
  - Reporting teams
  - Data scientists
  - Data engineers

- Are there downstream systems, tools, or applications that will consume curated data?

---

## Source Systems & Data Landscape

- What types of data are in scope?
  Examples:
  - Subject data
  - Adverse events
  - Lab results
  - Vitals
  - Exposure
  - Medical history
  - Site metadata
  - Protocol metadata

- What source systems currently provide this data?

- What file / data formats are received?
  Examples:
  - CSV
  - Excel
  - API payloads
  - SAS XPT
  - JSON
  - Database extracts

- What is the approximate size and volume of incoming data?
  Please include:
  - Typical file sizes
  - Record counts
  - Number of studies
  - Frequency of ingestion

- Is historical backfill required, or only future incremental loads?

- Is there any reference / master data involved?
  Examples:
  - Study master
  - Site master
  - Controlled terminology
  - Lookup/code tables

---

## Processing & Transformation

- Are there existing business rules, derivations, transformations, or summarization logic currently being applied?

- Are there standard calculations required before reporting / analytics?

- Is harmonization / standardization across multiple sources expected?

---

## Performance & Operational Expectations

- Are there latency expectations?
  Examples:
  - Near real-time
  - Hourly
  - Daily batch
  - Weekly batch

- What are expected growth volumes over time?

- Are there availability / SLA expectations?

---

## Data Quality & Validation

- What are the current data quality concerns?

- What validation checks are expected?
  Examples:
  - Schema validation
  - Null checks
  - Duplicate detection
  - Referential integrity
  - Domain validation
  - Threshold / anomaly checks

- Should data quality metrics be surfaced through dashboards or reports?

- What should happen when validation failures occur?
  Examples:
  - Reject file
  - Quarantine invalid records
  - Alert users
  - Partial processing

---

## Security, Governance & Compliance

- Are there access control expectations?
  Examples:
  - Dataset-level access
  - Study-level access
  - Role-based access
  - Row-level restrictions

- Are auditability and lineage requirements expected?

- Are there regulatory or compliance constraints?
  Examples:
  - GxP
  - 21 CFR Part 11
  - HIPAA
  - De-identification / anonymization

---

## AI / Advanced Analytics

- Are AI-assisted workflows expected as part of the future roadmap?

- Are there priority AI use cases already being discussed?
  Examples:
  - Dataset Q&A assistant
  - Clinical summarization
  - Protocol deviation review
  - Anomaly detection
  - Data quality copilot

---

## Scope & Constraints

- What is explicitly out of scope?

- Are there preferred technology constraints?
  Examples:
  - AWS
  - Azure
  - Databricks
  - Snowflake

- Are there timeline expectations or milestone deadlines?


