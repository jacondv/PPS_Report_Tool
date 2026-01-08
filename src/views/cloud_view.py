from PySide6.QtWidgets import QVBoxLayout, QWidget
from PySide6.QtCore import Signal
from pyvistaqt import QtInteractor
import pyvista as pv
import numpy as np
import matplotlib.colors as mcolors
from PySide6.QtCore import QTimer

VIEW_MODE = 0
SEGMENT_MODE = 1
ANNOTATION_MODE = 2

class CloudView(QWidget):

    leftClicked = Signal(object, int)
    leftDoubleClick = Signal(object,int)

    def __init__(self, placeholder_widget):
        """
        placeholder_widget: QWidget từ Designer, nơi hiển thị cloud
        """
        super().__init__(placeholder_widget)
        self.placeholder_widget = placeholder_widget
        self._camera_locked = False

        # Working mode
        self.mode = VIEW_MODE
        self.is_editing =False

        # --- Polygon picking attributes ---
        self.polygon_actor = None
        self.on_right_click = None
        self.on_left_click = None
        self.is_drawing_polygon = False

        # --- Left click / drag / double click ---
        self._left_pressed = False
        self._dragged = False
        self._start_pos = (0, 0)
        self._drag_threshold = 5  # pixels

        # tạo QtInteractor
        self._cloud_actors: dict[str, pv.Actor] = {}  # cloud_id -> actor
        self.plotter_widget = QtInteractor(placeholder_widget)
        self.plotter_widget.set_background('black')

        self.plotter_widget.add_axes(
            interactive=None,
            line_width=2,
            color=[1.0, 1.0, 1.0],
            viewport=(0, 0, 0.2, 0.2),
        )
        self.plotter_widget.show_axes()  # hiển thị trục XYZ ở góc

        #--- Annotation metadata ---
        self._annotations: list[dict] = []  
        self._annotation_actors = {}


        # Đặt camera nhìn từ +X về gốc
        self.plotter_widget.camera_position = [
            (-1, 0, 0),
            (0, 0, 0),
            (0, 0, 1)
        ]

        # tạo layout cho placeholder widget
        layout = QVBoxLayout()
        layout.addWidget(self.plotter_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        placeholder_widget.setLayout(layout)

        # --- Đăng ký VTK callbacks cho left click / drag / double click ---
        iren = self.plotter_widget.iren
        iren.add_observer("LeftButtonPressEvent", lambda o,e: self._on_left_press(iren, e))
        
        # iren.add_observer("MouseMoveEvent", lambda o,e: self._on_mouse_move(iren, e))
        iren.add_observer("LeftButtonReleaseEvent", lambda o,e: self._on_left_release(iren, e))
        self.plotter_widget.track_click_position(self._on_left_double_click, side='left', double=True)

        # Right click vẫn dùng track_click_position
        self.plotter_widget.track_click_position(self._right_click, side='right')


    # =========================
    # Camera
    # =========================

    def get_current_front(self):
        pos_cam, lookat, up = self.plotter_widget.camera_position
        front = np.array(lookat) - np.array(pos_cam)
        norm = np.linalg.norm(front)
        if norm > 0:
            return front / norm
        return np.array([1, 0, 0])


    def reset_camera(self):
        self.plotter_widget.reset_camera()
    # =========================
    # Cloud management
    # =========================
    def clear_cloud(self, cloud_id=None):
        if cloud_id:
            actor = self._cloud_actors.pop(cloud_id, None)
            if actor:
                self.plotter_widget.remove_actor(actor)
        else:
            self.plotter_widget.clear()


    def display_cloud(self, points: np.ndarray, colors=None, normals: np.ndarray = None, point_size: int = 2, cloud_id: str = None, reset_camera=True):
        point_cloud = pv.PolyData(points)

        if isinstance(colors, str):
            color = np.array(mcolors.to_rgb(colors), dtype=np.float32)
            colors = np.tile(color, (points.shape[0], 1)) * 255
            point_cloud["colors"] = colors.astype(np.uint8)
        else:
            if colors is not None:
                adjusted_colors = colors.astype(np.float32)

        kwargs = {}
        if normals is not None:
            normals = np.abs(normals)
            factor = normals[:, 0]  # giả sử dùng component X
            factor_scaled = 0.5 + 0.5 * factor
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

        if reset_camera:
            self.plotter_widget.reset_camera()
        else:
            self.plotter_widget.render()


    def cleanup(self):
        for actor in self._cloud_actors.values():
            self.plotter_widget.remove_actor(actor)
        self._cloud_actors.clear()
        self.plotter_widget.reset_camera()

    # =========================
    # Anotation
    # =========================

    # ---------------- Annotation HUD ----------------
    def render_annotation(self, ann: 'Annotation'):
        """Vẽ hoặc cập nhật annotation"""
        if not ann:
            return
        actor = self._annotation_actors.get(ann.id)
        if actor:
            self.plotter_widget.remove_actor(actor)
        actor = self.plotter_widget.add_text(
            ann.msg,
            position=(ann.x, ann.y),
            font_size=ann.font_size,
            color=ann.color,
            shadow=False,
            viewport=False,
        )
        self._annotation_actors[ann.id] = actor


    def remove_annotation(self, ann_id: str):
        actor = self._annotation_actors.pop(ann_id, None)
        if actor:
            self.plotter_widget.remove_actor(actor)


    def set_annotation_visible(self, ann_id:str, visible=True):
        actor = self._annotation_actors.get(ann_id)
        if actor:
            actor.SetVisibility(visible)
            self.plotter_widget.render()

    # =========================
    # Polygon overlay
    # =========================
    def start_polygon(self):
        """Chỉ reset overlay, không lưu points"""
        if self.polygon_actor:
            self.plotter_widget.remove_actor(self.polygon_actor)
            self.polygon_actor = None
        
        self.is_drawing_polygon = True
        self.mode = self.is_drawing_polygon

    # =========================
    # Left click / drag / double click handlers
    # =========================
    def _on_left_press(self, interactor, event):
        self._start_pos = interactor.get_event_position()


    def _on_left_release(self, interactor, event):
        
        current_pos = interactor.get_event_position()
        dx = current_pos[0] - self._start_pos[0]
        dy = current_pos[1] - self._start_pos[1]
        if (dx*dx + dy*dy)**0.5 > self._drag_threshold:
            self._dragged = True
        else:
            self._dragged = False
        
        if not self._dragged:
            picked_3d = self.plotter_widget.pick_mouse_position()
            if picked_3d is not None:
                self._left_click(picked_3d)
     

    def _left_click(self, pos):
        """Thông báo Controller về click trái"""

        #Emit su kien leftclick
        x2d, y2d = self.plotter_widget.iren.get_event_position()
        self.leftClicked.emit((x2d, y2d), self.mode)

        # if self.is_drawing_polygon:
        if self.on_left_click:
            self.on_left_click(pos, self.mode)
        

    def _on_left_double_click(self, pos, *args):
        x2d, y2d = self.plotter_widget.iren.get_event_position()
        QTimer.singleShot(100, lambda: self.leftDoubleClick.emit((x2d, y2d), self.mode))
        
        

    def _right_click(self, pos, *args):
        """Thông báo Controller khi click phải (finish polygon)"""
        if not self.is_drawing_polygon:
            return
        if self.on_right_click:
            self.on_right_click()


    def draw_polygon(self, points):
        """Vẽ polygon (line + dot) bằng 1 mesh duy nhất."""
        if hasattr(self, 'polygon_actor') and self.polygon_actor:
            self.plotter_widget.remove_actor(self.polygon_actor)
            self.polygon_actor = None

        n = len(points)
        if n == 0:
            return

        poly = pv.PolyData(points)
        if n >= 2:
            poly.lines = [[2, i, i + 1] for i in range(n - 1)]
        poly['dots'] = np.arange(n)
        self.polygon_actor = self.plotter_widget.add_mesh(
            poly,
            color='blue',
            line_width=2,
            point_size=6,
            render_points_as_spheres=True
        )


    def finish_polygon(self):
        # Finish chuyển sang view mode, reset self.is_drawing_polygon
        self.is_drawing_polygon = False
        self.mode = self.is_drawing_polygon
    # =========================
    # Capture view
    # =========================
    def capture_current_view(self):
        return self.plotter_widget.screenshot(return_img=True)



