# Data Dictionary — Mock EDC Package

## edc_subjects.csv
- `STUDY_CODE`: study identifier
- `SITE_NUM`: site identifier
- `PATIENT_NUM`: site/study patient number
- `EDC_SUBJECT_ID`: source-style EDC subject identifier
- `SOURCE_SUBJECT_ID`: original CDISC `USUBJID`
- `CONSENT_DATE`: mock consent/screening date based on DM collection date
- `FIRST_TREATMENT_DATE`: first study treatment date/time
- `SEX_REPORTED`: source-style sex value
- `PLANNED_ARM_CODE`: planned treatment arm code
- `ACTUAL_ARM_CODE`: actual treatment arm code

## edc_visits.csv
- `EDC_VISIT_ID`: generated visit identifier
- `VISIT_NUMBER`: visit number from VS
- `VISIT_NAME`: visit label
- `ACTUAL_VISIT_DATE`: visit/measurement date
- `VISIT_STATUS`: mock operational status

## edc_vitals.csv
- `VITAL_RECORD_ID`: generated vital record identifier
- `VITAL_TEST_CODE`: source test code
- `RESULT_VALUE_RAW`: original/source-like result value
- `RESULT_UNIT_RAW`: original/source-like unit
- `STANDARD_VALUE`: standard numeric value from VS
- `STANDARD_UNIT`: standard unit from VS
