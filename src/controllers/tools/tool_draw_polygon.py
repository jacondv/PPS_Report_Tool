import numpy as np
from typing import Tuple, Optional
from models.polygon_model import PolygonModel

from PySide6.QtCore import Signal, QObject

class PolygonDrawer(QObject):
    """
    Class phục vụ quá trình bắt sự kiện chuột và vẽ polygon.
    - Quản lý PolygonModel hiện tại
    - Lắng nghe sự kiện chuột: click, move, double-click
    - Cập nhật polygon theo thao tác người dùng
    """

    toolCompleted = Signal(object)


    def __init__(self, view):
        super().__init__() 

        self.view = view
        self.is_drawing: bool = False
        self.current_polygon = None
        self.is_drawing = False


    def on_activate(self):
        self.current_polygon = None
        

    # ==================================================
    # Sự kiện chuột
    # ==================================================

    def on_left_click(self, pos: Tuple[float, float, float]):
        """
        Khi người dùng click chuột để thêm điểm
        """
        x,y,z, = pos
        if not self.is_drawing:
            # Bắt đầu polygon mới
            self.current_polygon = PolygonModel()
            self.is_drawing = True

        point = np.array([x, y, z])
        self.current_polygon.add_point(point)
        print(f"Added point: {point}")
        self.view.draw_polygon(self.current_polygon.get_points())


    # def on_mouse_move(self, pos: Tuple[float, float, float]):
    #     """
    #     Khi người dùng di chuyển chuột (có thể dùng để preview polygon)
    #     """

    #     x,y,z, = pos

    #     if self.is_drawing and self.current_polygon.num_points() > 0:
    #         # Cập nhật điểm cuối cùng tạm thời để preview
    #         temp_points = self.current_polygon.get_points().copy()
    #         temp_points[-1] = np.array([x, y, z])
    #         print(f"Preview polygon with {len(temp_points)} points")


    def on_double_click(self):
        self.on_right_click()


    def on_right_click(self):
        """
        Khi người dùng double-click để kết thúc polygon
        """
        if self.is_drawing and self.current_polygon is not None:
            self.current_polygon.finish_polygon()
            self.is_drawing = False
            self.toolCompleted.emit(self.current_polygon)
            print("Polygon finished")


    def cancel_drawing(self):
        """
        Hủy polygon đang vẽ
        """
        self.clear_points()

        if self.current_polygon:
            self.current_polygon.cancel_polygon()
        self.is_drawing = False
        print("Polygon cancelled")


    def clear_points(self):
        self.view.clear_cloud("segment_preview")
        self.view.draw_polygon([])  # Xoá polygon
        self.current_polygon.clear_points()

    # ==================================================
    # Truy cập polygon
    # ==================================================

    
    def get_polygon(self) -> Optional[PolygonModel]:
        return self.current_polygon