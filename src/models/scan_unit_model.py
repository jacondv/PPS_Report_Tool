# models/scan_unit.py
from dataclasses import dataclass
from pathlib import Path
from typing import List

@dataclass
class ScanUnitModel:
    name: str                 # tên folder / section
    path: Path                # path folder
    pre_scans: List[Path]            # 1 file pre-scan
    post_scans: List[Path]    # nhiều file post-scan
