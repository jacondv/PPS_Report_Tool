from typing import Tuple, Optional
from PySide6.QtCore import Signal
from controllers.tools.base_tool import Tool
from models.shape_model import Shape2D
import math
HIT_RADIUS = 16  # pixel

class DragHandle:
    NONE = 0
    START = 1
    END = 2

def distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

class ToolEditLine(Tool):

    toolCompleted = Signal(object)

    def __init__(self, shape_model, view, parent=None):
        super().__init__()
        self.requires_disable_view = True
        self.model = shape_model
        self.view = view

        self._shape: Optional[Shape2D] = None
        self._drag_handle = DragHandle.NONE

    def on_activate(self):
        self._shape = None
        self._drag_handle = DragHandle.NONE

    def on_deactivate(self):
        self._shape = None
        self._drag_handle = DragHandle.NONE

    def _hit_test_endpoint(self, shape: Shape2D, pos: Tuple[int, int]) -> int:

        ox, oy = shape.offset
        start_w = (shape.start[0] + ox, shape.start[1] + oy)
        end_w   = (shape.end[0]   + ox, shape.end[1]   + oy)


        dx = end_w[0] - start_w[0]
        dy = end_w[1] - start_w[1]
        length = math.hypot(dx, dy)
        HIT_RADIUS = max(0.4*length, 0.01)

        if distance(start_w, pos) <= HIT_RADIUS:
            return DragHandle.START
        if distance(end_w, pos) <= HIT_RADIUS:
            return DragHandle.END
        return DragHandle.NONE

    def on_mouse_press(self, pos: Tuple[int, int], button: str):
        if button != "left":
            return

        # giả sử view hoặc model có API lấy shape được click
        shape = self.model.find_nearest(pos)

        if not shape or shape.type != "line":
            return

        self._shape = shape
          
        handle = self._hit_test_endpoint(shape, pos)
        if handle == DragHandle.NONE:
            return

        self._shape = shape
        self._drag_handle = handle

        self.highlight_shape(self._shape)  


    def on_mouse_move(self, pos: Tuple[int, int]):
        if not self._shape or self._drag_handle == DragHandle.NONE:
            return

        ox, oy = self._shape.offset
        new_pos = pos[0] - ox, pos[1] - oy

        if self._drag_handle == DragHandle.START:
            self._shape.start = new_pos
        elif self._drag_handle == DragHandle.END:
            self._shape.end = new_pos

        self.highlight_shape(self._shape)      


    def on_mouse_release(self, pos: Tuple[int, int], button: str):
        if button != "left":
            return

        if self._drag_handle == DragHandle.NONE:
            return

        self._shape.update_bbox()
        # self.toolCompleted.emit(self._shape)
    
        self.highlight_shape(None) 
        self._shape = None
        self._drag_handle = DragHandle.NONE


    def highlight_shape(self, shape: Optional[Shape2D]):
        # render lại tất cả shapes, shape được chọn vẽ màu đỏ
        import copy
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