# controllers/cloud_controller.py

from event_bus import event_bus
from PySide6.QtCore import QObject, Signal
from views.segment_toolbar_view import SegmentToolbarView
from models.polygon_model import PolygonModel
from controllers.base_controller import BaseController

from controllers.tools.tool_draw_polygon import PolygonDrawer

class CloudController(QObject, BaseController):

    # segmentCreated = Signal(object)

    def __init__(self, cloud_view: "CloudView", cloud_service: "CloudService", job_service: "JobService"):
        super().__init__()
        self.cloud_view = cloud_view
        self.cloud_service = cloud_service
        self.job_service = job_service
        self.cloud_model = None  # CloudModel gắn vào Controller

        self.crop_direction = None
        
        # polygon/segment workflow
        self._segment_indices = None

        self.current_tool =  None
        self.segment_tool = PolygonDrawer(view=self.cloud_view)
        self.segment_tool.toolCompleted.connect(self.on_draw_polygon_completed)


        # # Segment toolbar
        self.segment_toolbar = SegmentToolbarView(self.cloud_view.placeholder_widget)
        self.segment_toolbar.hide()
        self.segment_toolbar.segment_in.connect(lambda: self.preview_segment("in"))
        self.segment_toolbar.export_selected.connect(self.export_segment)
        self.segment_toolbar.cancel.connect(self.export_cancel)
        self.segment_toolbar.clear.connect(self.clear_polygon)


        # # subscribe trực tiếp vào EventBus

        ############################################

        self.cloud_view.leftClicked3D.connect(self.on_3d_left_click)
        self.cloud_view.rightClicked3D.connect(self.on_3d_right_click)

        ############################################
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

    # def on_left_click(self, pos):
    #     """
    #     Xử lý sự kiện click trái từ CloudView
    #     :param pos: (x, y, z) trong hệ tọa độ view
    #     :param mode: ViewMode hiện tại
    #     """
    #     self.add_polygon_point(pos)

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

    def render_cloud(self, cloud_model=None,**kwargs):
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
            cloud_id=cloud_model.id,
            **kwargs
        )
    
    def clear_cloud(self, cloud_id=None):
        """Xoá cloud khỏi View"""
        self.cloud_view.clear_cloud(cloud_id)


########################################


    def set_tool(self, tool):

        # 1. Deactivate tool hiện tại nếu có
        if self.current_tool:
            self.current_tool = None

        if tool is None:
            self.cloud_view.enable(True)
            return

        # 2. Set tool mới
        self.current_tool = tool
        if self.current_tool:
            self.current_tool.on_activate()
            
            # Disable view nếu tool yêu cầu
            if getattr(self.current_tool, "requires_disable_view", False):
                self.cloud_view.enable(False)
            else:
                self.cloud_view.enable(True)

        
    def start_segment(self):
        self.segment_toolbar.show()
        self.segment_toolbar.disable()
        self.set_tool(self.segment_tool)
        

    def on_draw_polygon_completed(self, polygon):
        self.set_tool(None)
        self.current_polygon = polygon

        # Tính indices segment
        self._segment_indices = self.cloud_model.select_by_polygon(
            polygon.get_points(),
            crop_direction=self.crop_direction
        )
        self.segment_toolbar.enable(names=["segmentin", "clear"])
        print("on_segment_completed")


    # ---------------- forward events to shape draw interface----------------
    def on_3d_left_click(self, pos):
        print('on_3d_left_click')

        if self.current_tool:
            self.current_tool.on_left_click(pos)
            self.crop_direction = self.cloud_view.get_current_front()


    def on_3d_right_click(self, pos):
        print('on_3d_right_click')

        if self.current_tool:
            self.current_tool.on_right_click()


#########################################


    def preview_segment(self, mode=None):
        """Hiển thị các điểm segment trên View"""
        if self._segment_indices is not None and len(self._segment_indices) > 0:
            points = self.cloud_model.points[self._segment_indices]
            self.cloud_view.display_cloud(points=points, colors="pink", point_size=3, cloud_id="segment_preview", reset_camera=False)
            self.segment_toolbar.enable(names=["clear", "close","exportselection"])


    def export_segment(self):
        if self.cloud_model and self._segment_indices is not None:
            new_segment = self.cloud_model.create_segment(self._segment_indices, name=None)
            new_segment.set_polygon_indicate(self._segment_indices)
 
            event_bus.segment_created.emit(new_segment)
            self.cloud_view.clear_cloud("segment_preview")
            self.cloud_view.draw_polygon([])  # Xoá polygon
            self.segment_toolbar.hide()


    def export_cancel(self):
        # self.clear_polygon()
        self.segment_tool.cancel_drawing()

        self.segment_toolbar.hide()
        

    def clear_polygon(self):
        """Xoá polygon hiện tại"""
        # self.cloud_view.clear_cloud("segment_preview")
        # self.cloud_view.draw_polygon([])  # Xoá polygon
        self.segment_tool.clear_points()
        self.start_segment()


    def cleanup(self):
        self.cloud_model = None
        self.cloud_view.cleanup()

  