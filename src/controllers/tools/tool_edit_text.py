from controllers.tools.base_tool import Tool
from PySide6.QtCore import Signal
from models.shape_model import Shape2D
from views.ui.annotation_input_dialog_ui import AnnotationInputDialog  # import dialog


class ToolEditText(Tool):
    """
    Tool chỉ chỉnh sửa nội dung Text2D.
    """
    toolCompleted = Signal(object)

    def __init__(self, model, view,parent=None):
        super().__init__()
        self.model = model
        self.view = view
        self._shape: Shape2D | None = None
        self.requires_disable_view = True  # khóa camera khi edit
        self.parent = parent


    def _edit(self,shape):
        # mở dialog nhập text
        if shape.type != "text":
            return

        dialog = AnnotationInputDialog(self.parent)
        dialog.edit.setText(shape.text)
        x1, y1 = shape.world_points()[0]
        dialog.move_to(x1, y1)

        if dialog.exec():  # user nhấn OK
            new_text = dialog.edit.text()
            shape.update_text(new_text)
            self.view.draw_text(
                shape.id,
                shape.world_points()[0],  # vị trí text
                shape.text,
                color=shape.color
            )
            self.toolCompleted.emit(shape)
        else:
            self.toolCompleted.emit(None)

    def on_activate(self):
        if self._shape is not None:
            self._edit(self._shape)

    def on_mouse_press(self, pos, button):
        if button != "left":
            return

        # tìm text gần click
        self._shape = self.model.find_nearest(pos)
        
        if not self._shape:
            self.toolCompleted.emit(None)
            return

        self._edit(self._shape)

    def set_target(self,shape):
        self._shape = shape