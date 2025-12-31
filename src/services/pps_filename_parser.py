from pathlib import Path
from datetime import datetime
import re
from typing import Optional, Dict, Union

class PpsFilenameParser:
    """
    Parse PPS filename format:

    ARM0Deg#20251120_143449#pre_scan_cloud_01.ply
    """

    # pre_scan_cloud_01.ply
    _TAIL_PATTERN = re.compile(
        r"(?P<scan_type>pre|post)_scan_"
        r"(?P<data_type>[a-zA-Z]+)_"
        r"(?P<index>\d+)\."
        r"(?P<ext>[a-zA-Z0-9]+)$",
        re.IGNORECASE
    )

    @staticmethod
    def parse(path: Union[str, Path]) -> Optional[Dict]:
        """
        Parse filename and return metadata dict.
        Return None if filename does not match PPS format.
        """

        # Convert sang Path nếu là str
        if isinstance(path, str):
            path = Path(path)
        name = path.name

        parts = name.split("#")
        if len(parts) < 3:
            return None

        job_name = parts[0]

        # ---- timestamp ----
        timestamp = None
        try:
            timestamp = datetime.strptime(parts[1], "%Y%m%d_%H%M%S")
        except ValueError:
            pass

        # ---- tail ----
        tail = parts[2]

        m = PpsFilenameParser._TAIL_PATTERN.match(tail)
        if not m:
            return None

        return {
            "job_name": job_name,
            "timestamp": timestamp,
            "scan_type": m.group("scan_type").lower(),   # pre / post
            "data_type": m.group("data_type").lower(),   # cloud
            "index": int(m.group("index")),
            "ext": m.group("ext").lower()
        }
