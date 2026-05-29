"""Generate mock EDC source files from CDISC Dataset-JSON SDTM domains.
Currently supports DM and VS. Place dm.json and vs.json in input_dir.
"""
from pathlib import Path
import json
import pandas as pd


def dataset_to_df(path: Path):
    data = json.loads(path.read_text())
    cols = [c["name"] for c in data["columns"]]
    return pd.DataFrame(data["rows"], columns=cols)


def main(input_dir: str = "data/raw/cdisc_sdtm", output_dir: str = "data/mock_sources/edc"):
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    dm = dataset_to_df(input_dir / "dm.json")
    vs = dataset_to_df(input_dir / "vs.json")
    # This script is a simplified reusable version; see generated package for full mapping logic.
    dm.rename(columns={"STUDYID":"STUDY_CODE", "SITEID":"SITE_NUM", "SUBJID":"PATIENT_NUM"}).to_csv(output_dir / "edc_subjects.csv", index=False)
    vs.rename(columns={"STUDYID":"STUDY_CODE", "VSDTC":"MEASUREMENT_DATE"}).to_csv(output_dir / "edc_vitals.csv", index=False)

if __name__ == "__main__":
    main()
