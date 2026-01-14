from controllers.tools.base_tool import Tool
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMessageBox
from models.shape_model import Shape2D


class ToolDeleteShape(Tool):
    """
    Tool xóa shape sau khi xác nhận.
    """
    toolCompleted = Signal(object)  # shape đã xóa hoặc None

    def __init__(self, model, view, parent=None):
        super().__init__()
        self.model = model
        self.view = view
        self.parent = parent
        self._shape: Shape2D | None = None

    def set_target(self, shape: Shape2D | None):
        self._shape = shape

    def on_activate(self):
        # nếu đã có target → hỏi xóa ngay
        if self._shape:
            self._confirm_and_delete(self._shape)


    # def on_mouse_press(self, pos, button):
    #     if button != "left":
    #         return

    #     shape = self.model.find_nearest(pos)
    #     if not shape:
    #         self.toolCompleted.emit(None)
    #         return

    #     self._confirm_and_delete(shape)

    def _confirm_and_delete(self, shape: Shape2D):
        reply = QMessageBox.question(
            self.parent,
            "Delete annotation",
            "Are you sure you want to delete this annotation?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            self.view.remove_shape(shape.id)
            self.model.remove(shape.id)
            self.toolCompleted.emit(None)
        else:
            self.toolCompleted.emit(None)
