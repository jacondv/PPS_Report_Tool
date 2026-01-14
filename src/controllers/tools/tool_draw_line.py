
from models.shape_model import create_shape, Shape2D
from typing import Tuple, Optional
from PySide6.QtCore import Signal
from controllers.tools.base_tool import Tool

class ToolDrawLine(Tool):

    toolCompleted = Signal(object)

    def __init__(self, shape_model, view):
        super().__init__() 
        self.requires_disable_view = True
        self.model = shape_model
        self.view = view
        self._shape: Optional[Shape2D] = None
        self._line_width = 1.0

    def on_activate(self):
        self._shape = None

    def set_line_width(self, line_width):
        self._line_width = line_width

    def on_deactivate(self):
        if self._shape:
            self.model.remove(self._shape.id)
            self.view.remove_shape(self._shape.id)
        self._shape = None

    def on_mouse_press(self, pos: Tuple[int, int], button: str):
        if button != "left":
            return
        self._shape = create_shape(
            "line",
            start=pos,
            end=pos,
            line_width=self._line_width,
            color="yellow"
        )
        
        if not self._shape:
            return
        self.model.add(self._shape)
        self.view.render_shape(self._shape)

    def on_mouse_move(self, pos: Tuple[int, int]):
        if not self._shape:
            return
        self._shape.end = pos
        self.view.render_shape(self._shape)

    def on_mouse_release(self, pos: Tuple[int, int], button: str):
        if button != "left" or not self._shape:
            return
        self._shape.end = pos
        self.view.render_shape(self._shape)
        self.toolCompleted.emit(self._shape)
        self._shape = None
