from PySide6.QtWidgets import QVBoxLayout
from pyvistaqt import QtInteractor
import pyvista as pv
import numpy as np

class CloudView:
    def __init__(self, placeholder_widget):
        """
        placeholder_widget: QWidget từ Designer, nơi hiển thị cloud
        """
        self.placeholder_widget = placeholder_widget
        self._camera_locked = False
        # --- Polygon picking attributes ---
        self.polygon_drawing = False
        self.polygon_points = []
        self.polygon_actor = None
        self.picking_enabled = False
        self.picking_callback = None  # Controller gán callback

        self.on_right_click = None

        # tạo QtInteractor
        self.plotter_widget = QtInteractor(placeholder_widget)
        self.plotter_widget.set_background('black')

        self.plotter_widget.add_axes(
        interactive=None,
        line_width=2,
        color=[1.0, 1.0, 1.0],
        viewport=(0, 0, 0.2, 0.2),
        )

        self.plotter_widget.show_axes()  # hiển thị trục XYZ ở góc dưới bên trái

        # Đặt camera nhìn từ +X về gốc
        self.plotter_widget.camera_position = [
            (-1, 0, 0),   # vị trí camera ở +X
            (0, 0, 0),   # nhìn về gốc
            (0, 0, 1)    # vector "up" là +Z
        ]

        # tạo layout cho placeholder widget
        layout = QVBoxLayout()
        layout.addWidget(self.plotter_widget)
        layout.setContentsMargins(0, 0, 0, 0)  # bỏ lề để tràn ra full
        placeholder_widget.setLayout(layout)      

        self.plotter_widget.track_click_position(self._left_click, side='left')
        self.plotter_widget.track_click_position(self._right_click, side='right')


    def get_current_front(self):
        pos_cam, lookat, up = self.plotter_widget.camera_position
        front = np.array(lookat) - np.array(pos_cam)
        norm = np.linalg.norm(front)
        if norm > 0:
            return front / norm
        return np.array([1, 0, 0])  # fallback

    def display_cloud(self, points: np.ndarray, colors: np.ndarray = None, normals: np.ndarray = None):
        self.plotter_widget.clear()
        point_cloud = pv.PolyData(points)

        kwargs = {}

        if colors is not None:
            adjusted_colors = colors.astype(np.float32)

        if normals is not None:
            # factor = normals[:,0]  # hoặc dot với camera direction
            normals = np.abs(normals)
            factor = normals[:,0]  # giả sử dùng component X
            factor_scaled = 0.5 + 0.5 * factor  # scale từ 0->1 thành 0.5->1
            adjusted_colors = colors.astype(np.float32) * factor_scaled[:, np.newaxis]
            adjusted_colors = np.clip(adjusted_colors, 0, 255)
            point_cloud["colors"] = adjusted_colors.astype(np.uint8)
            kwargs = {"scalars": "colors", "rgb": True, "color": None}
        else:
            kwargs = {"scalars": None, "rgb": False, "color": "white"}

        self.plotter_widget.add_points(
            point_cloud,
            point_size=2,
            render_points_as_spheres=False,
            **kwargs
        )

        self.plotter_widget.reset_camera()

    # --- Polygon overlay ---
    def start_polygon(self):
        self.polygon_points = []
        self.polygon_drawing = True
        if self.polygon_actor:
            self.plotter_widget.remove_actor(self.polygon_actor)
            self.polygon_actor = None

    def _left_click(self, pos,*args):
    
        if not self.polygon_drawing:
            return
        # Lấy tọa độ 3D từ viewport click (chiếu vào XY plane)
        # point = self.plotter_widget.pick_mouse_position(pos)

        self.polygon_points.append(pos)
        self._draw_polygon()

    def _right_click(self, pos, *args):
        if self.polygon_drawing:
            if self.on_right_click:
                self.on_right_click()  # thông báo Controller

    def _draw_polygon(self):
        # Xóa polygon/dot cũ nếu có
        if self.polygon_actor:
            self.plotter_widget.remove_actor(self.polygon_actor)

        n = len(self.polygon_points)
        if n == 0:
            return

        # Vẽ line nếu ≥2 điểm
        if n >= 2:
            poly = pv.PolyData(self.polygon_points)
            lines = [[2, i, i+1] for i in range(n-1)]
            poly.lines = lines
            self.polygon_actor = self.plotter_widget.add_mesh(
                poly, color="blue", line_width=2
            )

        # Luôn vẽ điểm (dot) cho tất cả các điểm
        points = pv.PolyData(self.polygon_points)
        self.plotter_widget.add_mesh(
            points, color="blue", point_size=6, render_points_as_spheres=True
        )


    def finish_polygon(self):
        if len(self.polygon_points) >= 3:
            # Close polygon
            self.polygon_points.append(self.polygon_points[0])
            self._draw_polygon()
        else:
            self.polygon_points = []
            
        self.polygon_drawing = False
        return self.polygon_points