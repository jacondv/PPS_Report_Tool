import numpy as np
import open3d as o3d
import uuid
from typing import Optional
from matplotlib.path import Path  # để kiểm tra point in polygon


class CloudModel:
    """
    Quản lý dữ liệu point cloud và các công cụ hình học gắn với cloud
    KHÔNG quản lý segment
    """

    def __init__(self, source_path=None, parent_id: Optional[str] = None):
        self.id = f"cloud_{uuid.uuid4().hex[:8]}"
        self.parent_id = parent_id         # cloud gốc
        self.source_path = source_path
        self._cloud: Optional[o3d.t.geometry.PointCloud] = None
        self.points: Optional[np.ndarray] = None   # Nx3 numpy
        self.name=None
        self.loaded: bool = False
        self._polygon_indicate = None
        self._polygon_points = None

    # ==================================================
    # Load / access
    # ==================================================

    def set_cloud(self, cloud: o3d.t.geometry.PointCloud):
        if cloud is None:
            raise ValueError("Input cloud is None")
        
        # Kiểm tra xem cloud có điểm không
        if len(cloud.point.positions) == 0:
            raise ValueError("Input cloud contains no points")
        
        try:
            self.points = cloud.point.positions.cpu().numpy()
        except Exception as e:
            raise RuntimeError(f"Failed to convert cloud points to numpy: {e}")
        
        self._cloud = cloud
        self.loaded = True

    def get_cloud(self):
        return self._cloud

    def get_parent_id(self):
        return self.parent_id

    def is_loaded(self) -> bool:
        return self.loaded

    def set_polygon_points(self, points):
        self._polygon_points = points
    
    def get_polygon_points(self):
        return self._polygon_points

    def set_polygon_indicate(self,indicate):
        self._polygon_indicate = indicate

    def get_polygon_indicate(self):
        return self._polygon_indicate

    def create_segment(self, indices: list[int], name: Optional[str] = None) -> "CloudModel":
        """
        Tạo CloudModel mới từ subset points của self._cloud.
        Giữ nguyên tất cả fields (_cloud, colors, normals, etc.).
        """
        if self._cloud is None:
            raise ValueError("Cloud not loaded")

        if not indices:
            raise ValueError("Indices empty")

        idx = np.asarray(indices, dtype=np.int64)
        if idx.min() < 0 or idx.max() >= len(self._cloud.point.positions):
            raise IndexError("Indices out of range")

        # Tạo cloud con mới
        seg_cloud = CloudModel(parent_id=self.id)
        seg_cloud.id = f"{self.id}_seg_{uuid.uuid4().hex[:6]}"
        seg_cloud.parent_id = self.id
        seg_cloud.name = name or f"{self.id}_seg"

        # Tạo Open3D PointCloud con
        _sub_cloud = o3d.t.geometry.PointCloud(self._cloud.device)
        for field in self._cloud.point:
            _sub_cloud.point[field] = self._cloud.point[field][idx]

        # Gán dữ liệu bằng set_cloud
        seg_cloud.set_cloud(_sub_cloud)

        return seg_cloud

    def select_by_polygon(self, polygon_points, crop_direction=np.array([1, 0, 0]),base_indices=None):
        """
        Chọn các điểm nằm bên trong polygon (chiếu lên plane vuông góc với crop_direction)
        
        polygon_points: Nx3 numpy array hoặc list
        crop_direction: vector 3D xác định hướng cắt (mặc định [0,1,0])
        """

        if polygon_points is None:
            return []
        
        self.polygon_points = np.array(polygon_points, dtype=float)
        if len(self.polygon_points) < 3:
            print(f"Cannot segment: polygon too few points ({len(self.polygon_points)} < 3)")
            return []

        if self.points is None or len(self.points) == 0:
            print("Cannot segment: points is None or empty")
            return []

        # Chuẩn hóa vector hướng
        cut_dir = np.array(crop_direction, dtype=float)
        norm = np.linalg.norm(cut_dir)
        if norm == 0:
            raise ValueError("cut_direction cannot be zero vector")
        cut_dir /= norm

        # Tìm vector tham chiếu không song song
        # Chọn trục chuẩn bất kỳ không gần song song với cut_dir
        ref_candidates = [np.array([1,0,0]), np.array([0,1,0]), np.array([0,0,1])]
        for ref in ref_candidates:
            u = np.cross(cut_dir, ref)
            u_norm = np.linalg.norm(u)
            if u_norm > 1e-6:
                u /= u_norm
                break
        else:
            raise ValueError("Cannot find suitable reference vector for cross-product")

        v = np.cross(cut_dir, u)

        # Chiếu polygon và cloud lên plane (u,v)
        poly_proj = np.dot(self.polygon_points, np.vstack([u, v]).T)

        if base_indices is not None:
            affect_points = self.points[base_indices]
        else:
            affect_points = self.points
            
        cloud_proj = np.dot(affect_points, np.vstack([u, v]).T)

        # Tạo Path polygon 2D và mask
        path = Path(poly_proj)
        mask = path.contains_points(cloud_proj)
        self.segmented_indices = np.where(mask)[0].tolist()

        return self.segmented_indices