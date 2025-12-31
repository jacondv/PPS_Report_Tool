# controllers/cloud_controller.py

from event_bus import event_bus
from PySide6.QtCore import QObject, Signal
from views.segment_toolbar_view import SegmentToolbarView
from models.polygon_model import PolygonModel

class CloudController(QObject):

    # segmentCreated = Signal(object)

    def __init__(self, cloud_view: "CloudView", cloud_service: "CloudService", job_service: "JobService"):
        super().__init__()
        self.cloud_view = cloud_view
        self.cloud_service = cloud_service
        self.job_service = job_service
        self.cloud_model = None  # CloudModel gắn vào Controller


        # polygon/segment workflow
        self.polygon_model: PolygonModel | None = None
        self._segment_indices = None


        # Segment toolbar
        self.segment_toolbar = SegmentToolbarView(self.cloud_view.placeholder_widget)
        self.segment_toolbar.hide()
        self.segment_toolbar.segment_in.connect(lambda: self.preview_segment("in"))
        self.segment_toolbar.export_selected.connect(self.export_segment)
        self.segment_toolbar.cancel.connect(self.export_cancel)
        self.segment_toolbar.clear.connect(self.clear_polygon)


        # Connect View callbacks
        self.cloud_view.on_left_click = self.add_polygon_point
        self.cloud_view.on_right_click = self.finish_draw_polygon

        # subscribe trực tiếp vào EventBus
        event_bus.cloud_visibility_changed.connect(self.on_cloud_visibility_changed)


    # ==================================================
    # Event handlers
    def on_cloud_visibility_changed(self, cloud_id: str, visible: bool):
        # This function is called when a cloud's visibility is changed in the tree view
        # Update the cloud display based on visibility

        if not visible:
            self.clear_cloud(cloud_id)     
        else:
            cloud_model = self.job_service.get_cloud_model(cloud_id)
            self.set_cloud_model(cloud_model)
            self.render_cloud(cloud_model)


    # ==================================================
    # Cloud loading / rendering
    # ==================================================
    def set_cloud_model(self, cloud_model):
        """Set CloudModel cho controller"""
        self.cloud_model = cloud_model

    def _load_cloud(self, cloud_model):
        """Lazy load cloud khi chưa load"""
        if not cloud_model.is_loaded():
            raw_cloud = self.cloud_service.load_cloud(cloud_model.source_path)
            cloud_model.set_cloud(raw_cloud)
        return cloud_model

    def render_cloud(self, cloud_model=None):
        """Hiển thị cloud lên View"""
        
        # Kiểm tra tham số
        if cloud_model is None:
            raise ValueError("render_cloud: cloud_model không được None")
        
        # Load cloud nếu chưa load
        cloud_model = self._load_cloud(cloud_model)
        
        cloud_data = cloud_model.get_cloud()
        if cloud_data is None:
            raise ValueError(f"render_cloud: cloud_model {cloud_model.id} chưa có dữ liệu _cloud")
        
        # Chuẩn bị dữ liệu cho display
        data = self.cloud_service.prepare_cloud_for_display(cloud_data)
        
        self.cloud_view.display_cloud(
            points=data.get('points'),
            colors=data.get('colors'),
            normals=data.get('normals'),
            cloud_id=cloud_model.id
        )
    
    def clear_cloud(self, cloud_id=None):
        """Xoá cloud khỏi View"""
        self.cloud_view.clear_cloud(cloud_id)


    # ==================================================
    # Polygon / Segment workflow
    # ==================================================
    def start_segment(self):
        """Bắt đầu vẽ polygon"""
        # if not self.cloud_model:
        #     return

        self.segment_toolbar.show()
        self.segment_toolbar.disable()

        # Reset polygon trong Model
        self.polygon_model = PolygonModel()

        # Bắt đầu vẽ trong View
        self.cloud_view.start_polygon()
        self.polygon_model.crop_direction = self.cloud_view.get_current_front()
        self._segment_indices = []


    def add_polygon_point(self, pos):
        """Thêm điểm polygon từ click"""
        if not self.polygon_model:
            return

        self.polygon_model.add_point(pos)
        self.cloud_view.draw_polygon(self.polygon_model.get_points())


    def finish_draw_polygon(self):
        """Kết thúc polygon, tính segment"""
        self.cloud_view.finish_polygon()
        if not self.polygon_model:
            return
        self.polygon_model.finish_polygon()
        self.cloud_view.draw_polygon(self.polygon_model.get_points())

        # # Lưu polygon vào CloudModel (nếu cần)
        # self.cloud_model.set_polygon(self.polygon_model)

        # Tính indices segment
        self._segment_indices = self.cloud_model.select_by_polygon(
            self.polygon_model.get_points(),
            crop_direction=self.polygon_model.crop_direction
            # crop_direction=np.array([0, 1, 0])
        )

        # Enable toolbar
        if self._segment_indices is not None and len(self._segment_indices) > 0:
            self.segment_toolbar.enable(names=["segmentin", "clear"])


    def preview_segment(self, mode=None):
        """Hiển thị các điểm segment trên View"""
        if self._segment_indices is not None and len(self._segment_indices) > 0:
            points = self.cloud_model.points[self._segment_indices]
            self.cloud_view.display_cloud(points=points, colors="pink", point_size=3, cloud_id="segment_preview")
            self.segment_toolbar.enable(names=["clear", "close","exportselection"])

    def export_segment(self):
        if self.cloud_model and self._segment_indices is not None:
            new_segment = self.cloud_model.create_segment(self._segment_indices, name=None)
            # self.segmentCreated.emit(new_segment)

            event_bus.segment_created.emit(new_segment)

            self.cloud_view.clear_cloud("segment_preview")
            self.cloud_view.draw_polygon([])  # Xoá polygon
            self.polygon_model = None
            self.segment_toolbar.hide()

    def export_cancel(self):
        self.clear_polygon()
        self.segment_toolbar.hide()

    def clear_polygon(self):
        """Xoá polygon hiện tại"""
        self.cloud_view.clear_cloud("segment_preview")
        self.cloud_view.draw_polygon([])  # Xoá polygon
        # self.polygon_model = None
        self.segment_toolbar.disable()

    def cleanup(self):
        self.cloud_model = None
        self.cloud_view.cleanup()

  