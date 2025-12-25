
# class JobModel:
#     """
#     Đại diện cho 1 Job PPS (1 folder trên disk)
#     """

#     def __init__(self, job_path: str):
#         self.id: str = self._new_id()
#         self.job_path: Path = Path(job_path)

#         # -------- raw files --------
#         self.files: Dict[str, Path] = {}      # all files in job folder

#         # -------- models --------
#         self.clouds: Dict[str, "CloudModel"] = {}
#         self.segments: Dict[str, "CloudSegment"] = {}
#         self.reports: Dict[str, "ReportModel"] = {}

#         # -------- state --------
#         self.active_cloud_id: Optional[str] = None
#         self.active_segment_id: Optional[str] = None
#         self.active_report_id: Optional[str] = None

#         self._scan_files()

#     def _new_id(self) -> str:
#         return f"job_{uuid.uuid4().hex[:8]}"

#     # ==================================================
#     # File system
#     # ==================================================

#     def _scan_files(self):
#         if not self.job_path.exists():
#             raise FileNotFoundError(self.job_path)

#         for p in self.job_path.iterdir():
#             if p.is_file():
#                 self.files[p.name] = p

#     # ==================================================
#     # Cloud
#     # ==================================================

#     def add_cloud(self, cloud: "CloudModel"):
#         self.clouds[cloud.id] = cloud
#         self.active_cloud_id = cloud.id

#     def get_active_cloud(self):
#         return self.clouds.get(self.active_cloud_id)

#     # ==================================================
#     # Segment
#     # ==================================================

#     def add_segment(self, segment: "CloudSegment"):
#         self.segments[segment.id] = segment
#         self.active_segment_id = segment.id

#     def get_segments_of_cloud(self, cloud_id: str):
#         return [
#             s for s in self.segments.values()
#             if s.cloud_id == cloud_id
#         ]

#     # ==================================================
#     # Report
#     # ==================================================

#     def add_report(self, report: "ReportModel"):
#         self.reports[report.id] = report
#         self.active_report_id = report.id

#     def get_active_report(self):
#         return self.reports.get(self.active_report_id)


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
