from pathlib import Path
import json
from typing import List
from models.job_model import JobModel
from models.scan_unit_model import ScanUnitModel

def load_job(root_dir: str) -> JobModel:
    root = Path(root_dir)
    if not root.exists() or not root.is_dir():
        raise ValueError(f"Job root folder does not exist: {root_dir}")

    # Load job_info.json từ root
    job_info_path = root / "job_info.json"
    if not job_info_path.exists():
        raise RuntimeError("job_info.json not found in job root")
    with job_info_path.open("r", encoding="utf-8") as f:
        job_info = json.load(f)

    scan_units: List[ScanUnitModel] = []

    # Iterate sub-folders (mỗi sub-folder là 1 ScanUnit)
    for sub in sorted(root.iterdir()):
        if not sub.is_dir():
            continue

        pre_scans = list(sub.glob("*pre*.ply"))
        post_scans = list(sub.glob("*post*.ply"))

        scan_unit = ScanUnitModel(
            name=sub.name,
            path=sub,
            pre_scans=pre_scans,
            post_scans=post_scans
        )
        scan_units.append(scan_unit)

    job_name = root.name
    return JobModel(root=root, name=job_name, job_info=job_info, scan_units=scan_units)
