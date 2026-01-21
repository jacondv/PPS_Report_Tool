from models.shape_model import create_shape, Shape2D
from typing import Tuple, Optional
from PySide6.QtCore import Signal, Qt, QPoint
from controllers.tools.base_tool import Tool
from PySide6.QtWidgets import QDialog

from views.ui.annotation_input_dialog_ui import AnnotationInputDialog  # import dialog

class ToolDrawText(Tool):

    toolCompleted = Signal(object)

    def __init__(self, shape_model, view, parent=None):
        super().__init__()
        self.requires_disable_view = True
        self.model = shape_model
        self.view = view
        self.parent = parent
        self._shape: Optional[Shape2D] = None
        self._font_size = 11

    def on_activate(self):
        self._shape = None

    def set_font_size(self,font_size):
        self._font_size = font_size

    def on_deactivate(self):
        if self._shape:
            self.model.remove(self._shape.id)
            self.view.remove_shape(self._shape.id)
        self._shape = None

    def on_left_pressed(self, pos: Tuple[int, int], button: str):
        pass

    def on_mouse_release(self, pos: Tuple[int, int], button: str):
        if button != "left":
            return

        # mở dialog nhập text
        dialog = AnnotationInputDialog(self.parent)
        _x, _y = pos
        dialog.move_to(_x, _y)

        if dialog.exec() != QDialog.Accepted:
            self.toolCompleted.emit(None)
            return

        text = dialog.edit.text()
        if not text:
            self.toolCompleted.emit(None)
            return

        # tạo shape text với nội dung nhập vào
        self._shape = create_shape(
            "text",
            text=text,
            offset = pos,
            font_size=self._font_size,
            color="yellow"
        )

        if not self._shape:
            self.toolCompleted.emit(None)
            return

        self.model.add(self._shape)
        self.view.render_shape(self._shape)
        self.toolCompleted.emit(self._shape)
        self._shape = None  # reset tool state


  