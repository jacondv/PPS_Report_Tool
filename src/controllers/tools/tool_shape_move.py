from controllers.tools.base_tool import Tool
from PySide6.QtCore import Signal

class MoveShape(Tool):

    toolCompleted = Signal(object)

    def __init__(self, shape_model, view):
        super().__init__() 
        self.requires_disable_view = True
        self._shape = None
        self.shape_model = shape_model
        self.view = view

    def on_activate(self):
        self.dragging = False


    def on_mouse_press(self, pos, button):

        if button != "left":
            return
        
        self._shape = self.shape_model.find_nearest(pos)
        if not self._shape:
            return
        
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

        self.view.render_shape(self._shape)

    def on_mouse_release(self, pos, button):
        if button != "left" or not self._shape:
            return
        self.dragging = False
        self.view.render_shape(self._shape)
        self.toolCompleted.emit(None)
        self._shape = None