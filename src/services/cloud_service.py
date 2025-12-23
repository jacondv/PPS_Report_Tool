# cloud_service.py
import os
import open3d as o3d
import numpy as np

class CloudService:
    @staticmethod
    def load_cloud(file_name: str) -> o3d.t.geometry.PointCloud:
        # Kiểm tra file tồn tại
        if not file_name or not os.path.exists(file_name):
            raise FileNotFoundError(f"File '{file_name}' not exist!")

        try:
            cloud = o3d.t.io.read_point_cloud(file_name, format="auto")
        except Exception as e:
            raise RuntimeError(f"Can't load '{file_name}': {e}")

        # Estimate normals nếu chưa có
        if "normals" not in cloud.point:
            cloud.estimate_normals(max_nn=30)

        return cloud

    @staticmethod
    def prepare_cloud_for_display(cloud) -> dict:
        data = {}
        data['points'] = cloud.point["positions"].cpu().numpy()
        data['colors'] = cloud.point["colors"].cpu().numpy()*255 if "colors" in cloud.point else None
        data['normals'] = cloud.point["normals"].cpu().numpy() if "normals" in cloud.point else None
        return data