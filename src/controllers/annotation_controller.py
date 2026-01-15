from typing import Optional
from itertools import chain

from views.annotation_toolbar_view import AnnotationToolbarView

from controllers.tools.tool_draw_line import ToolDrawLine
from controllers.tools.tool_draw_text import ToolDrawText
from controllers.tools.tool_shape_move import MoveShape
from controllers.tools.tool_select_shape import ToolSelectShape
from controllers.tools.tool_edit_text import ToolEditText
from controllers.tools.tool_delete_shape import ToolDeleteShape
from controllers.tools.tool_edit_line import ToolEditLine

from controllers.base_controller import BaseController

class AnnotationController(BaseController):
    def __init__(self, cloud_view, shape_model):
        """
        cloud_view: CloudView (render annotation)
        """
        super().__init__()
        self.view = cloud_view
        self.shape_mode = shape_model

        self.current_tool = None
        self.current_ann = None
        self.ann_line_width = 1
        self.ann_font_size = 11


        self.ann_toolbar = AnnotationToolbarView(self.view.placeholder_widget)
        self.ann_toolbar.addLine.connect(self.on_request_add_line)
        self.ann_toolbar.addText.connect(self.on_request_add_text)
        self.ann_toolbar.move.connect(self.on_request_move)
        self.ann_toolbar.editSignal.connect(self.on_edit)
        self.ann_toolbar.deleteSignal.connect(self.on_delete)
        self.ann_toolbar.sizeChanged.connect(self.on_size_changed)
        self.ann_toolbar.fontsizeChanged.connect(self.on_font_size_changed)
        self.ann_toolbar.selectSignal.connect(self.on_request_select)
        

        self.view.mouseMoved.connect(self.on_mouse_move)
        self.view.leftPressed.connect(self.on_left_pressed)
        self.view.leftReleased.connect(self.on_left_released)

        # edit text request
        self.view.leftDoubleClick.connect(self.on_request_edit_text)

        # tạo tool draw line
        self.draw_line_tool = ToolDrawLine(self.shape_mode, self.view)
        self.draw_line_tool.toolCompleted.connect(self.on_shape_completed)

        # tạo move shape tool
        self.move_tool = MoveShape(self.shape_mode, self.view)
        self.move_tool.toolCompleted.connect(self.on_shape_completed)

        # tạo text tool
        self.draw_text_tool = ToolDrawText(self.shape_mode, self.view,parent=self.view.placeholder_widget)
        self.draw_text_tool.toolCompleted.connect(self.on_shape_completed)

        # tao tool edit shape
        self.edit_text_tool = ToolEditText(self.shape_mode, self.view, parent=self.view.placeholder_widget)
        self.edit_text_tool.toolCompleted.connect(self.on_shape_completed)

        self.edit_line_tool = ToolEditLine(self.shape_mode, self.view, parent=self.view.placeholder_widget)
        self.edit_line_tool.toolCompleted.connect(self.on_shape_completed)

        # tạo tool select shape
        self.select_shape_tool =  ToolSelectShape(self.shape_mode, self.view)
        self.select_shape_tool.shapeSelected.connect(self.on_shape_completed)

        # tạo tool delete shape
        self.delete_shape_tool = ToolDeleteShape(self.shape_mode, self.view, parent=self.view.placeholder_widget)
        self.delete_shape_tool.toolCompleted.connect(self.on_shape_completed)
        # Initial Set tool 
        self.set_tool(self.select_shape_tool)



    def update_buttons(self):
        """
        Update enable / visible state của toolbar buttons
        dựa trên tool hiện tại và selection hiện tại
        """

        tool = self.current_tool
        has_selection = self.current_ann is not None

        ui = self.ann_toolbar.ui

        # ---- mặc định: tắt hết ----
        buttons = [
            ui.btnAddText,
            ui.btnAddLine,
            ui.btnMove,
            ui.btnEdit,
            ui.btnDelete,
        ]

        for btn in buttons:
            btn.setEnabled(True)

        # ---- Close luôn bật ----
        ui.btnClose.setEnabled(True)
        ui.btnClose.setVisible(True)

        # ---- theo tool ----
        if tool == self.draw_text_tool:
            ui.btnAddText.setEnabled(False)

        elif tool == self.draw_line_tool:
            ui.btnAddLine.setEnabled(False)

        elif tool == self.move_tool:
            ui.btnMove.setEnabled(False)

        elif tool == self.edit_text_tool:
            ui.btnEdit.setEnabled(False)
        
        elif tool == self.edit_line_tool:
            ui.btnEdit.setEnabled(False)
        
        # ---- thao tác theo selection ----
        ui.btnDelete.setEnabled(has_selection)


    def show_annotation_toolbar(self):
        if not self.ann_toolbar.isVisible():
            self.ann_toolbar.show()


    def set_tool(self, tool):
        # 1. Deactivate tool hiện tại nếu có
        if self.current_tool:
            self.current_tool = None

        # 2. Set tool mới
        self.current_tool = tool
        if self.current_tool:
            self.current_tool.on_activate()
            
            # Disable view nếu tool yêu cầu
            if getattr(self.current_tool, "requires_disable_view", False):
                self.view.enable(False)
            else:
                self.view.enable(True)

        self.update_buttons()


    def deactivate_current_tool(self):
        """Tắt tool hiện tại và dọn dẹp trạng thái."""
        if self.current_tool:
            self.current_tool = None
            self.view.enable(True)
        
        #Tool mac dinh la select shape tool
        self.set_tool(self.select_shape_tool)


    def on_shape_completed(self, shape):
        self.current_ann = shape
        if shape:
            self.shape_mode.add(shape)
        self.deactivate_current_tool()  # dừng tool sau khi vẽ xong


    def on_request_add_line(self):
         self.draw_line_tool.set_line_width(self.ann_line_width)
         self.set_tool(self.draw_line_tool)


    def on_request_add_text(self):
         self.draw_text_tool.set_font_size(self.ann_font_size)
         self.set_tool(self.draw_text_tool)


    def on_request_select(self):
        self.set_tool(self.select_shape_tool)


    def on_request_edit_text(self):

        if self.current_ann and self.current_tool == self.select_shape_tool:
            self.edit_text_tool.set_target(self.current_ann)
            self.set_tool(self.edit_text_tool)
        
        else:
            self.current_ann = None
            self.set_tool(self.select_shape_tool)

    #Move Annotation
    def on_request_move(self):
        self.set_tool(self.move_tool)
    
    # Edit Shape
    def on_edit(self):
        self.set_tool(self.edit_line_tool)


    def on_delete(self):
        self.delete_shape_tool.set_target(self.current_ann)
        self.set_tool(self.delete_shape_tool)
        

    def on_size_changed(self, size):
        self.ann_line_width = size


    def on_font_size_changed(self, size):
        self.ann_font_size = size
    

    # ---------------- forward events to shape draw interface----------------
    def on_left_pressed(self, pos):
        if self.current_tool:
            self.current_tool.on_mouse_press(pos, "left")


    def on_left_released(self, pos):
        if self.current_tool:
            self.current_tool.on_mouse_release(pos, "left")


    def on_mouse_move(self, pos):
        if self.current_tool:
            self.current_tool.on_mouse_move(pos)

