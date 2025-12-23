import sys
from pathlib import Path

# Thêm src folder vào path
sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

import open3d as o3d

# Load point cloud
pcd = o3d.io.read_point_cloud(r"C:\WORK\projects\PPS_Report_Tool\data\Job01\2\ARM0Deg#20251120_150901#post_scan_cloud_06.ply")

# Mở cửa sổ để người dùng chọn points
vis = o3d.visualization.VisualizerWithEditing()
vis.create_window()
vis.add_geometry(pcd)
vis.run()  # Người dùng chọn points trên GUI
vis.destroy_window()

# Lấy các indices của points đã chọn
picked_indices = vis.get_picked_points()
cropped_cloud = pcd.select_by_index(picked_indices)

# Hiển thị cloud đã crop
o3d.visualization.draw_geometries([cropped_cloud])
