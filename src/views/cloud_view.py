from PySide6.QtWidgets import QVBoxLayout
from pyvistaqt import QtInteractor
import pyvista as pv
import numpy as np
import matplotlib.colors as mcolors


class CloudView:
    def __init__(self, placeholder_widget):
        """
        placeholder_widget: QWidget từ Designer, nơi hiển thị cloud
        """
        self.placeholder_widget = placeholder_widget
        self._camera_locked = False
        # --- Polygon picking attributes ---
        self.polygon_actor = None
        self.on_right_click = None

        self.is_drawing_polygon = False

        # tạo QtInteractor
        self._cloud_actors: dict[str, pv.Actor] = {} # cloud_id -> actor
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


    def clear_cloud(self, cloud_id=None):
        if cloud_id:
            actor = self._cloud_actors.pop(cloud_id, None)
            if actor:
                self.plotter_widget.remove_actor(actor)
        else:
            self.plotter_widget.clear()


    def display_cloud(self, points: np.ndarray, colors=None, normals: np.ndarray = None, point_size: int = 2, cloud_id: str = None):

        point_cloud = pv.PolyData(points)

        if isinstance(colors, str):
            color = np.array(mcolors.to_rgb(colors), dtype=np.float32)
            colors = np.tile(color, (points.shape[0], 1))*255
            point_cloud["colors"] = colors.astype(np.uint8)
        else:
            if colors is not None:
                adjusted_colors = colors.astype(np.float32)   

        kwargs = {}
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
            kwargs = {"scalars": None, "rgb": True, "color": None}

        actor = self.plotter_widget.add_points(
            point_cloud,
            point_size=point_size,
            render_points_as_spheres=False,
            **kwargs
        )
        if cloud_id:
            self._cloud_actors[cloud_id] = actor

        self.plotter_widget.reset_camera()


    def cleanup(self):
        for actor in self._cloud_actors.values():
            self.plotter_widget.remove_actor(actor)
        self._cloud_actors.clear()
        self.plotter_widget.reset_camera()

    # --- Polygon overlay ---
    def start_polygon(self):
        """Chỉ reset overlay, không lưu points"""
        if self.polygon_actor:
            self.plotter_widget.remove_actor(self.polygon_actor)
            self.polygon_actor = None
        
        self.is_drawing_polygon = True


    def _left_click(self, pos, *args):
        """Thông báo Controller về click trái"""
        if not self.is_drawing_polygon:
            return

        if self.on_left_click:
            self.on_left_click(pos)  # Controller sẽ thêm point vào PolygonModel và gọi draw_polygon


    def _right_click(self, pos, *args):
        """Thông báo Controller khi click phải (finish polygon)"""
        if not self.is_drawing_polygon:
            return
        if self.on_right_click:
            self.on_right_click()  # Controller quyết định finish polygon


    def draw_polygon(self, points):
        """Vẽ polygon (line + dot) bằng 1 mesh duy nhất."""
        # Xóa actor cũ nếu có
        if hasattr(self, 'polygon_actor') and self.polygon_actor:
            self.plotter_widget.remove_actor(self.polygon_actor)
            self.polygon_actor = None

        n = len(points)
        if n == 0:
            return

        poly = pv.PolyData(points)

        # Lines
        if n >= 2:
            poly.lines = [[2, i, i+1] for i in range(n-1)]

        # Vertices (để vẽ dot)
        poly['dots'] = np.arange(n)  # dummy scalar để chắc chắn poly có points

        # Add mesh một lần, line + points
        self.polygon_actor = self.plotter_widget.add_mesh(
            poly,
            color='blue',
            line_width=2,
            point_size=6,
            render_points_as_spheres=True
        )


    def finish_polygon(self):
        """Chỉ dùng để render polygon đã đóng; không lưu dữ liệu"""
        self.is_drawing_polygon = False


    def capture_current_view(self):
        # from PIL import Image
        img = self.plotter_widget.screenshot(return_img=True)
        # img_pil = Image.fromarray(img)
        # img_pil.show()
        return img
        
