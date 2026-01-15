from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton
)
from PySide6.QtCore import Qt, QPoint, Signal, QSize

from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)

from . import resource_rc

class AnnotationInputDialog(QDialog):
    
    btnDeleteClicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)  # bỏ title bar
        self.setModal(True)

        # Drag support
        self._drag_pos = None

        # Textbox
        self.edit = QLineEdit(self)
        self.edit.setPlaceholderText("Enter annotation...")
        
        # Buttons
        btn_cancel = QPushButton()
        btn_cancel.clicked.connect(self.reject)

        icon = QIcon()
        icon.addFile(u":/icon/icon/multiplication.png", QSize(), QIcon.Normal, QIcon.Off)
        btn_cancel.setIcon(icon)

        # btn_delete = QPushButton("Delete")
        # btn_delete.clicked.connect(self.on_delete)

        self._btn_ok = QPushButton()       # không thêm vào layout → không hiển thị
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/check.png", QSize(), QIcon.Normal, QIcon.Off)
        self._btn_ok.setIcon(icon1)
        self._btn_ok.clicked.connect(self.accept)

        # Layout ngang
        layout = QHBoxLayout(self)
        layout.addWidget(self.edit)
        layout.addWidget(btn_cancel)
        layout.addWidget(self._btn_ok)
        # layout.addWidget(btn_delete)
        layout.setContentsMargins(0, 0, 20, 0)  # lề trái, trên, phải, dưới


    # Drag events
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._drag_pos = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()


    def mouseMoveEvent(self, event):
        if self._drag_pos and event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self._drag_pos)
            event.accept()


    def mouseReleaseEvent(self, event):
        self._drag_pos = None

    # Enter = OK, Esc = Cancel
    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            self._btn_ok.click()       # trigger accept
        elif event.key() == Qt.Key_Escape:
            self.reject()
        else:
            super().keyPressEvent(event)


    def on_delete(self):
        self.btnDeleteClicked.emit()
        self.reject()


    def text(self):
        return self.edit.text().strip()


    def get_text(self):
        return self.edit.text().strip()


    def set_text(self, text: str):
        """
        Set sẵn text vào QLineEdit
        """
        if text is None or text.strip() == "":
            self.edit.clear()  
        else:
            self.edit.setText(text.strip())


    def get_pos(self):
        """
        Return (x, y) of dialog center in parent coordinate system.
        Dialog must have a parent and be visible.
        """
        parent = self.parentWidget()
        if parent is None:
            raise RuntimeError("AnnotationInputDialog has no parent")

        # center_global = self.geometry().center()
        global_pos = self.frameGeometry().bottomLeft()
        pos_in_parent = parent.mapFromGlobal(global_pos)

        pos_in_parent = parent.mapFromGlobal(global_pos)

        x = pos_in_parent.x()
        y = pos_in_parent.y()

        #  Invert Y (Qt -> bottom-left)
        y = parent.height() - y 

        return x, y
    
    # --- hàm di chuyển dialog ---
    def move_to(self, x: int, y: int):
        """
        Move TOP-LEFT of dialog to (x, y) in parent widget coordinate system.
        """
        parent = self.parentWidget()

        #  Invert Y (Qt -> bottom-left)
        y = parent.height() - y

        if parent is None:
            raise RuntimeError("Dialog has no parent")

        global_pos = parent.mapToGlobal(QPoint(int(x), int(y)))
        self.move(global_pos)
