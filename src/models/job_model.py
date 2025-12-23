from dataclasses import dataclass
from pathlib import Path
from typing import List
from models.scan_unit_model import ScanUnitModel

@dataclass
class JobModel:
    root: Path
    name: str
    job_info: dict            # nội dung job_info.json
    scan_units: List[ScanUnitModel]
