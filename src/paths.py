import sys
from pathlib import Path


def _detect_base_dir() -> Path:
    # Trường hợp build exe
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent.parent

    current = Path(__file__).resolve()

    for parent in current.parents:
        main_py = parent / "main.py"
        if main_py.exists():
            return parent.parent   

    raise RuntimeError("Cannot detect project root")

BASE_DIR = _detect_base_dir()
SRC_DIR = BASE_DIR / "src"
CONFIG_DIR   = BASE_DIR / "config"
LOGS_DIR     = BASE_DIR / "logs"
DATA_DIR     = BASE_DIR / "data"

#FILE PATHS
WKHTMLTOPDF_PATH_EXE = str(BASE_DIR / "packages" / "wkhtmltox" / "bin" / "wkhtmltopdf.exe")
LOGO_REPORT_FILE_PATH = str(SRC_DIR / "pps_shared" / "tunnel_report" / "assets" / "images" / "logo.png")
