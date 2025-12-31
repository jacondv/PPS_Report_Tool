from typing import List
import numpy as np
import uuid

class PolygonModel:
    """
    Model lưu polygon vẽ trên cloud.
    - points: danh sách các điểm 3D hoặc 2D (numpy array)
    - id: unique id để quản lý
    """

    def __init__(self, points: np.ndarray = None):
        """
        points: Nx3 numpy array (3D) hoặc Nx2 (2D)
        """
        self.id = f"polygon_{uuid.uuid4().hex[:8]}"
        self.points: np.ndarray = points if points is not None else np.zeros((0, 3))
        self.closed: bool = False  # polygon đã đóng chưa
        self._crop_direction = None

    @property
    def crop_direction(self):
        return self._crop_direction


    @crop_direction.setter
    def crop_direction(self, direction: np.ndarray):
        vec = np.array(direction)
        if np.linalg.norm(vec) == 0:
            raise ValueError("Crop direction cannot be zero vector")
        self._crop_direction = vec / np.linalg.norm(vec)
    # ==================================================
    # Thêm / xóa điểm
    # ==================================================
    def add_point(self, point: np.ndarray):
        """
        Thêm 1 điểm vào polygon
        """
        point = np.array(point)
        if self.points.shape[0] == 0:
            self.points = point.reshape(1, -1)
        else:
            self.points = np.vstack([self.points, point])

    def remove_last_point(self):
        """Xóa điểm cuối cùng"""
        if self.points.shape[0] > 0:
            self.points = self.points[:-1, :]

    def clear(self):
        """Xóa tất cả điểm"""
        self.points = np.zeros((0, self.points.shape[1] if self.points.shape[0] > 0 else 3))
        self.closed = False


    # ==================================================
    # Polygon state
    # ==================================================

    def finish_polygon(self):
        if self.points is None:
            return

        if len(self.points) >= 3:
            self.close_polygon()
            # tính segment, enable toolbar
        else:
            # Nếu chưa đủ 3 điểm, người dùng có thể finish → treat như cancel
            self.cancel_polygon()


    def cancel_polygon(self):
        """Hủy polygon đang vẽ"""
        if self.points:
            self.points = None


    def close_polygon(self):
        """Đóng polygon: thêm điểm đầu vào cuối nếu chưa có"""
        if not self.closed and len(self.points) >= 3:
            if not np.allclose(self.points[0], self.points[-1]):
                self.points = np.vstack([self.points, self.points[0]])  # thêm điểm đầu vào cuối
            self.closed = True

    def is_closed(self) -> bool:
        return self.closed

    def get_points(self) -> np.ndarray:
        return self.points
