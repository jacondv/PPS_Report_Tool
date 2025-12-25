import numpy as np
from matplotlib.path import Path
import open3d as o3d
from scipy.spatial import Delaunay

# View (vẽ polygon)
#    ↓
# Controller (quyết định create segment)
#    ↓
# CloudModel.select_indices_by_polygon()
#    ↓
# Controller.create_segment(indices, polygon, dir)
#    ↓
# CloudModel.add_segment(segment)

class CloudModel:
    def __init__(self):
        self._cloud = None
        self.cloud_points = None      # Nx3 numpy array
        self.polygon_points = []      # polygon overlay points
        self.segmented_indices = []   # lưu index các điểm bên trong polygon

        self.segments = []  # list[CloudSegment]


    def _update(self,cloud):
        self._cloud = cloud
        # chuyển sang Nx3 numpy
        self.cloud_points = self._cloud.point.positions.cpu().numpy()
        self.clear_polygon()

    def set_cloud(self, cloud: o3d.t.geometry.PointCloud):
        """Load point cloud Open3D Tensor -> numpy array."""
        self._update(cloud)
    
    def get_cloud(self):
        return self._cloud
       
    def clear_polygon(self):
        self.polygon_points = []
        self.segmented_indices = []

    def select_by_polygon(self, polygon_points, crop_direction=np.array([1, 0, 0])):
        """
        Chọn các điểm nằm bên trong polygon (chiếu lên plane vuông góc với crop_direction)
        
        polygon_points: Nx3 numpy array hoặc list
        crop_direction: vector 3D xác định hướng cắt (mặc định [0,1,0])
        """
        self.polygon_points = np.array(polygon_points, dtype=float)

        if len(self.polygon_points) < 3:
            print(f"Cannot segment: polygon too few points ({len(self.polygon_points)} < 3)")
            return []

        if self.cloud_points is None or len(self.cloud_points) == 0:
            print("Cannot segment: cloud_points is None or empty")
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
        cloud_proj = np.dot(self.cloud_points, np.vstack([u, v]).T)

        # Tạo Path polygon 2D và mask
        path = Path(poly_proj)
        mask = path.contains_points(cloud_proj)
        self.segmented_indices = np.where(mask)[0].tolist()

        return self.segmented_indices
