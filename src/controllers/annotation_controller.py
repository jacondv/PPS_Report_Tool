from typing import Optional
from views.ui.annotation_input_dialog_ui import AnnotationInputDialog
from PySide6.QtWidgets import QDialog

class AnnotationController:
    def __init__(self, cloud_view, annotation_model):
        """
        cloud_view: CloudView (render annotation)
        annotation_model: AnnotationModel (data)
        """
        self.view = cloud_view
        self.model = annotation_model
        self.view.leftClicked.connect(self.on_left_click)
        self.view.leftDoubleClick.connect(self.on_left_double_click)
        self.selected_id = None

        self.ann_dialog = AnnotationInputDialog(self.view.placeholder_widget)
        self.ann_dialog.btnDeleteClicked.connect(self.on_delete)


    def request_add_annotation(self):

        ann_dialog = self.ann_dialog
        if ann_dialog.exec_() != QDialog.Accepted:
            return

        text = ann_dialog.text()
        pos = ann_dialog.get_pos()
        if not text:
            return
        ann =self.add_annotation(text,pos)

        if ann:
            self.view.render_annotation(ann)
            self.view.plotter_widget.render()


    def request_edit_annotation(self, ann_id, pos):
        
        ann = self.model.get_by_id(ann_id)
        if not ann:
            return
        
        self.view.set_annotation_visible(ann.id,False)
        
        ann_dialog = self.ann_dialog
        ann_dialog.set_text(ann.msg)  # set text trước
        _x,_y = ann.x, int(ann.y + ann.height/2)
        ann_dialog.move_to(_x,_y)
        if ann_dialog.exec_() != QDialog.Accepted:
            self.view.set_annotation_visible(ann.id, True)
            return
        
        new_text = ann_dialog.get_text()   # None nếu rỗng
        new_pos = ann_dialog.get_pos()     # lấy vị trí nếu dialog có tính năng get_pos()

        if new_text:  # chỉ update nếu có text
            self.model.update(ann_id=ann_id, msg=new_text, position=new_pos)
            self.render_all()  # update view
        

    def on_delete(self):
        self.remove_annotation(self.selected_id)


    def add_annotation(self, msg, position, font_size=10, color='yellow'):
        # ---- validate input ----
        if not isinstance(position, (tuple, list)) or len(position) != 2:
            raise ValueError("position must be (x, y)")

        x, y = int(position[0]), int(position[1])

        # ---- model ----
        ann = self.model.add(msg, x, y, font_size, color)

        return ann


    def remove_annotation(self, ann_id):
        # ---- model ----
        if ann_id is None:
            return
        else:
            self.model.remove(ann_id)
            # ---- update view ----
            self.view.remove_annotation(ann_id)


    def render_all(self):
        """Render lại toàn bộ annotation (khi reload view)"""
        for ann in self.model.annotations:
            self.view.set_annotation_visible(ann.id, True)
            self.view.render_annotation(ann)

        self.view.plotter_widget.render()


    def on_left_click(self, pos, mode): 
        if mode != 0:
            return
        
        ann = self.model.find_nearest(pos)
        if ann is None:
            self.selected_id = None
        else:
            self.selected_id = ann.id
        
        self.set_selected_color(self.selected_id,color='red')
        self.render_all()


    def on_left_double_click(self, pos, mode): 
        if mode != 0:
            return
        
        if self.selected_id is not None:
            self.request_edit_annotation(self.selected_id,pos)
        

    def set_selected_color(self, selected_id: Optional[str], color: str = "red"):
        """
        Đặt màu cho annotation được chọn, giữ nguyên màu của các annotation khác
        Nếu selected_id=None thì bỏ highlight
        """

        for ann in self.model.annotations:
            # reset tất cả annotation về màu gốc
            if hasattr(ann, "_original_color"):
                ann.color = ann._original_color
            else:
                ann._original_color = ann.color  # lưu màu gốc lần đầu

        # highlight annotation được chọn
        if selected_id is not None:
            for ann in self.model.annotations:
                if ann.id == selected_id:
                    ann.color = color
                    break
            

