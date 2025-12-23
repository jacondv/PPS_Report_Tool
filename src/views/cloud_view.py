from PySide6.QtWidgets import QVBoxLayout
from pyvistaqt import QtInteractor
import pyvista as pv
import numpy as np

class CloudView:
    def __init__(self, placeholder_widget):
        """
        placeholder_widget: QWidget từ Designer, nơi hiển thị cloud
        """
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