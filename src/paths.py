import sys
from pathlib import Path

def resource_path(*parts) -> Path:
    if getattr(sys, "frozen", False):
        base = Path(sys._MEIPASS)
    else:
        base = Path(__file__).resolve().parents[1]  # project root
        current = Path(__file__).resolve()
        for parent in current.parents:
            main_py = parent / "main.py"
            if main_py.exists():
                return parent.parent.joinpath(*parts)
    return base.joinpath(*parts)


def exe_base_dir() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent

    # DEV: project root
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / "main.py").exists():
            return parent.parent
    raise RuntimeError("Cannot detect project root")

# def _detect_base_dir() -> Path:
#     # Trường hợp build exe
#     if getattr(sys, "frozen", False):
#         return Path(sys.executable).parent

#     current = Path(__file__).resolve()

#     for parent in current.parents:
#         main_py = parent / "main.py"
#         if main_py.exists():
#             return parent.parent   

#     raise RuntimeError("Cannot detect project root")

# def _detect_base_dir() -> Path:
#     # Khi chạy file exe (PyInstaller)
#     if getattr(sys, "frozen", False):
#         return Path(sys.executable).parent

#     # Khi chạy dev (python)
#     return Path(__file__).resolve().parents[1]


# BASE_DIR = _detect_base_dir()
# SRC_DIR = BASE_DIR / "src"
# CONFIG_DIR   = BASE_DIR / "config"
# LOGS_DIR     = BASE_DIR / "logs"
# DATA_DIR     = BASE_DIR / "data"

# THIRD_PARTY_DIR = BASE_DIR / "third_party"
# ASSETS_DIR      = BASE_DIR / "assets"
# CONFIG_DIR      = BASE_DIR / "config"

# #FILE PATHS
# # WKHTMLTOPDF_PATH_EXE = str(BASE_DIR / "third_party" / "wkhtmltox" / "bin" / "wkhtmltopdf.exe")
# # LOGO_REPORT_FILE_PATH = str(SRC_DIR / "pps_shared" / "tunnel_report" / "assets" / "images" / "logo.png")

# WKHTMLTOPDF_PATH_EXE = THIRD_PARTY_DIR / "wkhtmltox" / "bin" / "wkhtmltopdf.exe"
# LOGO_REPORT_FILE_PATH = str(ASSETS_DIR / "images" / "logo.png")


# nơi ghi file / chạy exe ngoài
BASE_DIR = exe_base_dir()

LOGS_DIR  = BASE_DIR / "logs"
DATA_DIR  = BASE_DIR / "data"
THIRD_PARTY_DIR = BASE_DIR / "third_party"

# asset readonly
ASSETS_DIR = resource_path("assets")

WKHTMLTOPDF_PATH_EXE = str(
    THIRD_PARTY_DIR
    / "wkhtmltox"
    / "bin"
    / "wkhtmltopdf.exe"
)

LOGO_REPORT_FILE_PATH = str(resource_path("assets", "images", "logo.png"))

print("BASE_DIR:", BASE_DIR)
print("ASSETS_DIR:", ASSETS_DIR)
print("WKHTMLTOPDF_PATH_EXE:", WKHTMLTOPDF_PATH_EXE)
print("LOGO_REPORT_FILE_PATH:", LOGO_REPORT_FILE_PATH)