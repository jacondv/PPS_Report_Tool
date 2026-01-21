from PySide6.QtWidgets import QVBoxLayout, QWidget
from PySide6.QtCore import Signal, Qt, QEvent


from pyvistaqt import QtInteractor
import pyvista as pv
import numpy as np
import matplotlib.colors as mcolors
from PySide6.QtCore import QTimer
import vtk

from views.components.save_plotter import SafePlotter


from views.components.overlay_factory import OverlayFactory

# VIEW_MODE = 0
SCALE = 1
SCREEN_SCALE = 1.0
class CloudView(QWidget):

    leftClicked = Signal(object)
    leftPressed = Signal(object)
    leftReleased = Signal(object)
    leftDoubleClick = Signal(object)

    leftClicked3D = Signal(object)
    rightClicked3D = Signal(object)

    mouseMoved = Signal(object)
    mouseDragged =  Signal(object)

    def __init__(self, placeholder_widget):
        """
        placeholder_widget: QWidget từ Designer, nơi hiển thị cloud
        """
        super().__init__(placeholder_widget)
        self.placeholder_widget = placeholder_widget
        
        
        self._camera_locked = False

        # Working mode
        # self.mode = VIEW_MODE
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
  
        self.container = QWidget(self.placeholder_widget)
        self.container.setObjectName("vtk_container")
        layout = QVBoxLayout(self.container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.plotter_widget = QtInteractor(self.container)
        layout.addWidget(self.plotter_widget)

        self._cloud_actors: dict[str, pv.Actor] = {}  # cloud_id -> actor

 

        self.plotter_widget.set_background('black')

        # self.plotter_widget.setFixedSize(800, 600)


        self.plotter = SafePlotter(self.plotter_widget)

        # 2. THIẾT LẬP LAYER OVERLAY
        # Cho phép render window hỗ trợ nhiều layer
        self.plotter_widget.render_window.SetNumberOfLayers(2)

        # Tạo Renderer cho lớp 2D
        self.overlay_renderer = vtk.vtkRenderer()
        self.overlay_renderer.SetLayer(1)           # Nằm trên Layer 0
        self.overlay_renderer.InteractiveOff()      # Không chặn chuột của lớp 3D bên dưới
        self.overlay_renderer.SetViewport(0, 0, 1, 1)

        self.plotter_widget.render_window.AddRenderer(self.overlay_renderer)

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
        self._text_actors = {}
        self._shape_actors = {}


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
        
        # iren.add_observer("MouseMoveEvent", self._on_mouse_move)
        iren.add_observer("LeftButtonReleaseEvent", lambda o,e: self._on_left_release(iren, e))
        self.plotter_widget.track_click_position(self._on_left_double_click, side='left', double=True)
        self.plotter_widget.track_mouse_position()

        # Right click vẫn dùng track_click_position
        self.plotter_widget.track_click_position(self._right_click, side='right')
        self.plotter_widget.installEventFilter(self)



    def normalize_pos(self,pos):
        rw = self.plotter_widget.GetRenderWindow()
        x, y = pos
        w,h = rw.GetSize()
        scale =  1/self.get_screen_scale()
        norm_pos = (scale*x/w, scale*y/h)
        return norm_pos
    
    def denormalize_pos(self, norm_pos):
        rw = self.plotter_widget.GetRenderWindow()
        w,h = rw.GetSize()
        nx, ny = norm_pos
        world_pos = (int(nx*w), int(ny*h))
        return world_pos

    def get_mouse_pos(self, normal=True):
        x2d, y2d = self.plotter_widget.iren.get_event_position()
        if normal:
            norm_pos = self.normalize_pos((x2d, y2d))
        else:
            norm_pos = (x2d, y2d)
        return norm_pos
    
    def get_screen_scale(self):
        scale = self.plotter_widget.devicePixelRatioF()
        return scale

    def set_view(self, view: str):
        """
        view: 'top', 'bottom', 'front', 'back', 'left', 'right', 'iso'
        """

        p = self.plotter_widget

        views = {
            'top':      [(0, 0, 1),     (0, 0, 0), (1, 0, 0)],
            'bottom':   [(0, 0, -1),    (0, 0, 0), (-1, 0, 0)],
            'back':     [(1, 0, 0),     (0, 0, 0), (0, 0, 1)],
            'front':    [(-1, 0, 0),    (0, 0, 0), (0, 0, 1)],
            'right':    [(0, -1, 0),    (0, 0, 0), (0, 0, 1)],
            'left':     [(0, 1, 0),     (0, 0, 0), (0, 0, 1)],
            'iso':      [(-1, 1, 1),    (0, 0, 0), (0, 0, 1)],
        }


        if view in views:
            direction, focal, up = views[view]
            p.camera_position = [direction, focal, up]
        else:
            raise ValueError(f"Unknown view: {view}")

        p.reset_camera()
        p.render()


    def eventFilter(self, obj, event):

        if obj == self.plotter_widget:
            if event.type() == QEvent.MouseButtonPress:
                if event.button() == Qt.LeftButton:
                    # x = event.pos().x()
                    # _height = self.placeholder_widget.height()
                    # y = _height - event.pos().y()

                    # self.leftPressed.emit((x, y))
                    # x2d, y2d = self.plotter_widget.iren.get_event_position()
                    norm_pos = self.get_mouse_pos()
                    self.leftPressed.emit(norm_pos)


            elif event.type() == QEvent.MouseButtonRelease:
                if event.button() == Qt.LeftButton:
                    # x = event.pos().x()
                    # _height = self.placeholder_widget.height()
                    # y = _height - event.pos().y()
                    # self.leftReleased.emit((x, y))
                    # x2d, y2d = self.plotter_widget.iren.get_event_position()
                    norm_pos = self.get_mouse_pos()
                    self.leftReleased.emit(norm_pos)

            elif event.type() == QEvent.MouseMove:
                # x = event.pos().x()
                # _height = self.placeholder_widget.height()
                # y = _height - event.pos().y()
                # self.mouseMoved.emit((x, y))
                # x2d, y2d = self.plotter_widget.iren.get_event_position()
                norm_pos = self.get_mouse_pos()

                self.mouseMoved.emit(norm_pos)
                
                # --- CHECK LEFT BUTTON IS PRESSED → DRAG ---
                if event.buttons() & Qt.LeftButton:
                    self.mouseDragged.emit(norm_pos)


        return super().eventFilter(obj, event)


    # =========================
    # Left click / drag / double click handlers
    # =========================
    def _on_left_press(self, interactor, event):
        self._start_pos = self.plotter_widget.iren.get_event_position()
        # self.leftPressed.emit(self._start_pos)
        pass


    def _on_left_release(self, interactor, event):
        
        current_pos = self.plotter_widget.iren.get_event_position()
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
     
    # Sư kiện left click được xử lý để loại bỏ double click
    def _left_click(self, pos):
        """Thông báo Controller về click trái"""

        #Emit su kien leftclick
        # x2d, y2d = self.plotter_widget.iren.get_event_position()
        # norm_pos = self.normalize_pos((x2d, y2d))
        norm_pos = self.get_mouse_pos()
        self.leftClicked.emit(norm_pos)
        self.leftClicked3D.emit(pos)
        # if self.is_drawing_polygon:
        # if self.on_left_click:
        #     self.on_left_click(pos)
        

    def _on_left_double_click(self, pos, *args):
        x2d, y2d = self.plotter_widget.iren.get_event_position()
        norm_pos = self.get_mouse_pos()
        QTimer.singleShot(100, lambda: self.leftDoubleClick.emit(norm_pos))
        
        
    def _right_click(self, pos, *args):
        """Thông báo Controller khi click phải (finish polygon)"""

        self.rightClicked3D.emit(pos)

        if not self.is_drawing_polygon:
            return
        if self.on_right_click:
            self.on_right_click()


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
  
  
    def capture_current_view(self):
        return self.plotter_widget.screenshot(
            return_img=True,
            scale=SCALE)


    def enable(self, value=True):
        """
        Bật/Tắt camera interaction trên self.plotter_widget
        value=True -> bật camera (xoay/pan/zoom)
        value=False -> khóa camera, vẫn cho phép vẽ overlay 2D
        """
        # Lưu style gốc lần đầu
        if not hasattr(self.plotter_widget, "_camera_enabled_style"):
            self.plotter_widget._camera_enabled_style = self.plotter_widget.interactor.GetInteractorStyle()
            self.plotter_widget._camera_disabled_style = vtk.vtkInteractorStyleUser()

        if value:
            # Bật camera
            self.plotter_widget.interactor.SetInteractorStyle(self.plotter_widget._camera_enabled_style)
        else:
            # Khóa camera
            self.plotter_widget.interactor.SetInteractorStyle(self.plotter_widget._camera_disabled_style)


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


    def _auto_set_camera(self, points: np.ndarray):
        plotter = self.plotter_widget

        # ----------------------------
        # 1. Kiểm tra có gần phẳng không
        # ----------------------------
        extent = points.max(axis=0) - points.min(axis=0)
        e = np.sort(extent)
        flatness = e[0] / (e[1] + 1e-6)

        if flatness >= 0.45:
            # plotter.reset_camera()
            return  # KHÔNG xoay camera


        # --------------------------------
        # 2. Estimate normal TỪ POINT
        #    (PCA trên sample nhỏ)
        # --------------------------------
        N = points.shape[0]
        k = min(50000, N)   # rất nhanh
        idx = np.random.choice(N, k, replace=False)

        P = points[idx]
        center = P.mean(axis=0)
        X = P - center

        cov = np.cov(X.T)
        eigvals, eigvecs = np.linalg.eigh(cov)

        normal = eigvecs[:, np.argmin(eigvals)]
        normal /= np.linalg.norm(normal)
        
        # ----------------------------
        # 3. Xác định hướng pháp tuyến
        # ----------------------------
        # trục mỏng nhất = pháp tuyến

        view_dir = -normal

        # ----------------------------
        # 4. Set camera
        # ----------------------------
        center = points.mean(axis=0)

        bounds = plotter.bounds
        diag = np.linalg.norm([
            bounds[1] - bounds[0],
            bounds[3] - bounds[2],
            bounds[5] - bounds[4],
        ])
        dist = diag * 1.5

        cam_pos = center + view_dir * dist

        up = np.array([0, 0, 1])
        if abs(np.dot(up, view_dir)) > 0.9:
            up = np.array([0, 1, 0])

        plotter.camera_position = [
            cam_pos.tolist(),
            center.tolist(),
            up.tolist()
        ]
        

    def display_cloud(self, points: np.ndarray, colors=None, normals: np.ndarray = None, point_size: int = 2, cloud_id: str = None, reset_camera=True, **kwargs):
        """
        Docstring for display_cloud
        
        :param wkargs: auto_rotate_camera=False -  Automatically rotate the cloud to provide users with a better viewing experience.
        """
        
        point_cloud = pv.PolyData(points)
        auto_rotate_camera = kwargs.get("auto_rotate_camera", False)

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

        if auto_rotate_camera:
                self._auto_set_camera(points)
                
        self.plotter.render()


    def cleanup(self):
        for actor in self._cloud_actors.values():
            self.plotter_widget.remove_actor(actor)
        self._cloud_actors.clear()
        self.plotter_widget.reset_camera()

    def release(self):
        rw = self.plotter_widget.render_window
        rw.RemoveAllObservers()
        rw.Finalize()
        self.plotter_widget = None
        
    # =========================
    # Anotation
    # =========================

    # ---------------- Annotation Text  ----------------

    def remove_annotation(self, ann_id: str):
        actor = self._annotation_actors.pop(ann_id, None)
        if actor:
            self.plotter_widget.remove_actor(actor)

    # ---------------- Annotation Shape----------------
    
    def _color_to_rgb(self, color_name: str):
        """Chuyển tên màu sang RGB tuple"""
        colors = {
            "red": (1.0, 0.0, 0.0),
            "yellow": (1.0, 1.0, 0.0),
            "green": (0.0, 1.0, 0.0),
            "blue": (0.0, 0.0, 1.0),
            "white": (1.0, 1.0, 1.0),
        }
        return colors.get(color_name.lower(), (1.0, 1.0, 1.0))

    
    def draw_text(
        self,
        name: str,
        pos: tuple[int, int],
        text: str,
        color: str = "red",
        **kwargs
    ):
        """
        Vẽ hoặc cập nhật text 2D trên QtInteractor.
        pos: (x, y) pixel viewport
        """

        # kiểm tra xem text actor đã tồn tại chưa
        actor = self._text_actors.get(name)
        font_size = kwargs.get('font_size', 11)
        x,y = self.denormalize_pos(pos)
        if actor:
            # update text và vị trí
            actor.SetInput(text)
            x,y = self.denormalize_pos(pos)
            actor.SetDisplayPosition(int(x), int(y))
            actor.GetTextProperty().SetFontSize(font_size)
            actor.GetTextProperty().SetColor(self._color_to_rgb(color))
        else:
            # tạo actor mới
            actor = vtk.vtkTextActor()
            actor.SetInput(text)
            actor.SetDisplayPosition(int(x), int(y))
            actor.GetTextProperty().SetFontSize(font_size)
            actor.GetTextProperty().SetColor(self._color_to_rgb(color))
            actor.GetTextProperty().SetShadow(False)

            # thêm vào viewport
            self.overlay_renderer.AddActor(actor)
            self._text_actors[name] = actor

        # self.plotter_widget.render()
        self.plotter.render()


    def draw_line(self, name, points_2d, **kwargs):
        """Controller sẽ gọi hàm này để yêu cầu View vẽ lại"""
        if name in self._shape_actors:
            self.overlay_renderer.RemoveActor(self._shape_actors[name])
        
        # Gọi Factory để lấy Actor mới
        points_2d = [ self.denormalize_pos((nx, ny)) for nx, ny in points_2d]

        actor = OverlayFactory.create_polyline(points_2d,plotter_widget=self.plotter_widget,**kwargs)
        
        self.overlay_renderer.AddActor(actor)
        # self.plotter_widget.render()
        self.plotter.render()
        self._shape_actors[name] = actor


    def render_shape(self, shape: 'Shape2D', draw_box: bool = False):
        """
        Render một shape Arrow2D / Line2D trên QtInteractor (plotter_widget)
        mà không cần import trực tiếp class Arrow2D / Line2D.
        """
     
        if not shape:
            return
            
        # Nếu shape có thuộc tính text → render text
        if getattr(shape, "type", "") == "text":
            pos = shape.offset  # top-left của text
            color = shape.color if hasattr(shape, "color") else "yellow"
            self.draw_text(shape.id, pos, shape.text, color=color, 
                           font_size=getattr(shape, "font_size", 11))

        elif getattr(shape, "type", "") == "line":
            # mặc định vẽ line
            self.draw_line(shape.id, shape.world_points(),
                        color=getattr(shape, "color", "yellow"),
                        line_width=getattr(shape, "line_width", 1))
            
            
    def remove_shape(self, shape_id: str):

        if shape_id in self._shape_actors:
            self.overlay_renderer.RemoveActor(self._shape_actors[shape_id])
        
        if shape_id in self._text_actors:
            self.overlay_renderer.RemoveActor(self._text_actors[shape_id])


    # =========================
    # Polygon overlay
    # =========================
    def draw_polygon(self, points):
        """Vẽ polygon (line + dot) bằng 1 mesh duy nhất."""
        if hasattr(self, 'polygon_actor') and self.polygon_actor:
            self.plotter_widget.remove_actor(self.polygon_actor)
            self.polygon_actor = None

        if points is None:
            return

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


    def get_pos(self):
        from PySide6.QtCore import QRect, QPoint
        widget = self.placeholder_widget
        widget.mapToGlobal(QPoint(0, 0))
        top_left = widget.mapToGlobal(QPoint(0, 0))
        size = widget.size()
        return QRect(top_left, size)