from pathlib import Path
from typing import Dict, List, Optional
import uuid


class JobModel:
    """
    Đại diện cho 1 Job PPS (logic job, không dính filesystem I/O)
    """

    def __init__(self, job_path: str):
        self.id: str = f"job_{uuid.uuid4().hex[:8]}"
        self.job_path: Path = Path(job_path)

        # ==================================================
        # Raw files (được inject từ JobLoaderService)
        # ==================================================
        self.files: List["FileModel"] = []
        self.job_info: Optional["JobInfoModel"] = None

        # ==================================================
        # Domain models
        # ==================================================
        self.clouds: Dict[str, "CloudModel"] = {}
        self.segments: Dict[str, "CloudSegment"] = {}
        self.reports: Dict[str, "ReportModel"] = {}

        # ==================================================
        # Working state (UI / workflow)
        # ==================================================
        self.active_cloud_id: Optional[str] = None
        self.active_segment_id: Optional[str] = None
        self.active_report_id: Optional[str] = None

    # ==================================================
    # Files
    # ==================================================

    def add_file(self, job_file: "JobFile"):
        self.files.append(job_file)

    # ==================================================
    # Cloud
    # ==================================================

    def add_cloud(self, cloud: "CloudModel"):
        self.clouds[cloud.id] = cloud
        self.active_cloud_id = cloud.id

    def get_cloud(self, cloud_id: str):
        return self.clouds.get(cloud_id)

    def get_active_cloud(self):
        return self.clouds.get(self.active_cloud_id)

    # ==================================================
    # Segment
    # ==================================================

    def add_segment(self, segment: "CloudSegment"):
        self.segments[segment.id] = segment
        self.active_segment_id = segment.id

    def get_segments_of_cloud(self, cloud_id: str):
        return [
            seg for seg in self.segments.values()
            if seg.cloud_id == cloud_id
        ]

    def get_active_segment(self):
        return self.segments.get(self.active_segment_id)

    # ==================================================
    # Report
    # ==================================================

    def add_report(self, report: "ReportModel"):
        self.reports[report.id] = report
        self.active_report_id = report.id

    def get_active_report(self):
        return self.reports.get(self.active_report_id)
