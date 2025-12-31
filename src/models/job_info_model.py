import json
from pathlib import Path
from typing import Dict, Any


class JobInfoModel:
    def __init__(self, data: Dict[str, Any]):
        self.data = data

    @staticmethod
    def from_file(path: Path) -> "JobInfoModel":
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return JobInfoModel(data)

    def to_dict(self) -> Dict[str, Any]:
        return self.data


#Sample job_info.json content:
# {
#     "name": "ARM0Deg",
#     "created": "2025-11-19 08:40:22",
#     "status": "pending",
#     "description": "",
#     "parameters": {
#         "target_thickness": 50,
#         "tolerance": 10
#     }
# }