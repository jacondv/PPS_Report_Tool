from controllers.tools.base_tool import Tool
from PySide6.QtCore import Signal
from typing import Optional
from models.shape_model import Shape2D
import copy

class ToolSelectShape(Tool):
    """
    Tool chỉ chọn shape khi click.
    Highlight shape được chọn và emit signal.
    """
    shapeSelected = Signal(object)  # Shape2D được chọn

    def __init__(self, model, view):
        super().__init__()
        self.model = model
        self.view = view
        self.selected_shape: Optional[Shape2D] = None
        self.requires_disable_view = False  # không cần khóa camera

    def on_activate(self):
        self.selected_shape = None

    def on_mouse_press(self, pos, button):
        if button != "left":
            return

        shape = self.model.find_nearest(pos)

        if shape is not self.selected_shape:
            self.selected_shape = shape
            self.highlight_shape(shape)
            self.shapeSelected.emit(shape)
        

    def highlight_shape(self, shape: Optional[Shape2D]):
        # render lại tất cả shapes, shape được chọn vẽ màu đỏ
        if shape is not None:
            _temp = copy.deepcopy(shape)
            _temp.color = "blue"
            for s in self.model.all():
                if s.id != shape.id:
                    self.view.render_shape(s)
                else:
                    self.view.render_shape(_temp)
        else:
            for s in self.model.all():
                self.view.render_shape(s)
