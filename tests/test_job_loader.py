# test_job_loader.py
import sys
from pathlib import Path

# Thêm src folder vào path
sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

from services.job_loader import load_job
def test_load_job():
    job_folder = r"C:\WORK\projects\PPS_Report_Tool\data\Job01"  # đường dẫn tới folder test
    job = load_job(job_folder)

    print(f"Job name: {job.name}")
    print("Job Info:")
    for k, v in job.job_info.items():
        if isinstance(v, dict):
            print(f"  {k}:")
            for sk, sv in v.items():
                print(f"    {sk}: {sv}")
        else:
            print(f"  {k}: {v}")
    
    print(f"\nNumber of scan units: {len(job.scan_units)}")
    for unit in job.scan_units:
        print(f"ScanUnit: {unit.name}")
        print(f"  Path: {unit.path}")
        print(f"  Pre-scans: {[f.name for f in unit.pre_scans]}")
        print(f"  Post-scans: {[f.name for f in unit.post_scans]}")
        print("")

if __name__ == "__main__":
    test_load_job()


# Result test

# (venv) C:\WORK\projects\PPS_Report_Tool\tests>python test_job_loader.py
# Job name: Job01
# Job Info:
#   name: ARM0Deg
#   created: 2025-11-19 08:40:22
#   status: pending
#   description: 
#   parameters:
#     target_thickness: 50
#     tolerance: 10

# Number of scan units: 2
# ScanUnit: 1
#   Path: C:\WORK\projects\PPS_Report_Tool\data\Job01\1
#   Pre-scans: ['ARM0Deg#20251120_143449#pre_scan_cloud_01.ply']
#   Post-scans: ['ARM0Deg#20251120_150017#post_scan_cloud_01.ply', 'ARM0Deg#20251120_150209#post_scan_cloud_02.ply', 'ARM0Deg#20251120_150323#post_scan_cloud_03.ply']

# ScanUnit: 2
#   Path: C:\WORK\projects\PPS_Report_Tool\data\Job01\2
#   Pre-scans: ['ARM0Deg#20251120_143901#pre_scan_cloud_02.ply', 'ARM0Deg#20251120_144641#pre_scan_cloud_07.ply', 'ARM0Deg#20251120_145209#pre_scan_cloud_08.ply', 'ARM0Deg#20251120_145405#pre_scan_cloud_09.ply']
#   Post-scans: ['ARM0Deg#20251120_150447#post_scan_cloud_04.ply', 'ARM0Deg#20251120_150634#post_scan_cloud_05.ply', 'ARM0Deg#20251120_150901#post_scan_cloud_06.ply']
