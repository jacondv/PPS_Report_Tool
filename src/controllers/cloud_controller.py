# controllers/cloud_controller.py
import numpy as np
from PySide6.QtCore import QObject
from views.segment_toolbar_view import SegmentToolbarView

class CloudController(QObject):
    def __init__(self, cloud_view, cloud_service, cloud_model):
        super().__init__()
        self.cloud_view = cloud_view
        self.cloud_service = cloud_service
        self.cloud_model = cloud_model
        self._crop_direction = np.array([1, 0, 0])
        self._current_polygon = None
        self._indices = None

        self.segment_toolbar = SegmentToolbarView(self.cloud_view.placeholder_widget)
        self.segment_toolbar.hide()
        # Kết nối signal từ 
        self.segment_toolbar.segment_in.connect(lambda: self.preview_segment("in"))

        # polygon picking callback

    def on_open_item(self, file_path: str):
        # 1. Load cloud TensorPointCloud
        # print(f"Received form {file_path}")
        # return
        raw_cloud = self.cloud_service.load_cloud(file_path)
        self.cloud_model.set_cloud(raw_cloud)

        # 3. Chuẩn bị dữ liệu numpy để hiển thị,  4. Hiển thị lên CloudView
        _cloud = self.cloud_model.get_cloud()
        data = self.cloud_service.prepare_cloud_for_display(_cloud)
        self.cloud_view.display_cloud(
            points=data['points'],
            colors=data['colors'],
            normals=data['normals']
        )
        

    # ===== Polygon / Segment =====
    def start_segment(self):
        """Bắt đầu vẽ polygon overlay"""
        self.segment_toolbar.show()
        self.segment_toolbar.disable()

        self.cloud_model.clear_polygon()
        self.cloud_view.start_polygon()
        self.cloud_view.on_right_click = self.finish_segment
        self._crop_direction = self.cloud_view.get_current_front()

    def finish_segment(self):
        """Kết thúc polygon, segment cloud, highlight points"""
        polygon = self.cloud_view.finish_polygon()
        if polygon:
            self.segment_toolbar.enable()
        # Segment points nằm trong polygon
        self._current_polygon = polygon
        self._indices = self.cloud_model.select_by_polygon(polygon,crop_direction=self._crop_direction)

    def preview_segment(self, mode):
        print("preview_segment",self._indices)
   
        if self._indices:
            points = self.cloud_model.cloud_points[self._indices]
            self.cloud_view.plotter_widget.add_points(
                points, color="red", point_size=3
            )
