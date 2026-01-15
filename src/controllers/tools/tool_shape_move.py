from controllers.tools.base_tool import Tool
from typing import Optional

from PySide6.QtCore import Signal
from models.shape_model import Shape2D

class MoveShape(Tool):

    toolCompleted = Signal(object)

    def __init__(self, shape_model, view):
        super().__init__() 
        self.requires_disable_view = True
        self._shape = None
        self.model = shape_model
        self.view = view

    def on_activate(self):
        self.dragging = False


    def on_mouse_press(self, pos, button):

        if button != "left":
            return
        
        self._shape = self.model.find_nearest(pos)
        if not self._shape:
            return
        
        self.highlight_shape(self._shape)
        
        self.dragging = True
        self.press_pos = pos                       # vị trí chuột lúc click
        self.start_offset = self._shape.offset      # snapshot offset ban đầu

    def on_mouse_move(self, pos):
        if not self.dragging:
            return

        dx = pos[0] - self.press_pos[0]
        dy = pos[1] - self.press_pos[1]

        offset = (self.start_offset[0] + dx,self.start_offset[1] + dy)
        self._shape.set_offset(offset)

        # self.view.render_shape(self._shape)
        self.highlight_shape(self._shape)

    def on_mouse_release(self, pos, button):
        if button != "left" or not self._shape:
            return
        self.dragging = False
        # self.view.render_shape(self._shape)
        self._shape = None
        self.highlight_shape(None)


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