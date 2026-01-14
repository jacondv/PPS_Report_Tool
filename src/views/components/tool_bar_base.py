from PySide6.QtCore import Qt, QPoint,QRect
from PySide6.QtWidgets import QDialog

class ToolBar(QDialog):
    def __init__(self,parent):
        super().__init__(parent)
 
        self._drag_pos = None
        self.setWindowFlags(Qt.Window  | Qt.FramelessWindowHint| Qt.WindowStaysOnTopHint)
        self.setFocusPolicy(Qt.StrongFocus)
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._drag_pos = event.globalPosition().toPoint()


    def mouseMoveEvent(self, event):
        if self._drag_pos and event.buttons() & Qt.LeftButton:
            delta = event.globalPosition().toPoint() - self._drag_pos
            new_pos = self.pos() + delta

            parent = self.parentWidget()
            if parent:
                parent_top_left = parent.mapToGlobal(QPoint(0, 0))
                parent_rect = QRect(parent_top_left, parent.size())

                w = self.width()
                h = self.height()

                x = max(parent_rect.left(),
                        min(new_pos.x(), parent_rect.right() - w))
                y = max(parent_rect.top(),
                        min(new_pos.y(), parent_rect.bottom() - h))

                new_pos = QPoint(x, y)

            self.move(new_pos)
            self._drag_pos = event.globalPosition().toPoint()
            
