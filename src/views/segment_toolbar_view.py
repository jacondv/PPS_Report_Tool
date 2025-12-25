# file: views/segment_toolbar_view.py
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QDialog
from views.ui.segment_toolbar_ui import Ui_SegmentToolbar

class SegmentToolbarView(QDialog):

    segment_in = Signal()
    segment_out = Signal()
    export_selected = Signal()

    """
    Segment Toolbar Dialog (View)
    - Chỉ hiển thị UI: Confirm, Cancel, Close, type combo
    - Controller sẽ gán callback
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SegmentToolbar()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
        self.setFocusPolicy(Qt.StrongFocus)

        self.installEventFilter(self)
        
        # Ẩn dialog khi khởi tạo
        self.hide()
        self.ui.btnSegmentIn.clicked.connect(self._on_btn_segment_in_clicked)
        self.ui.btnSegmentOut.clicked.connect(self._on_btn_segment_out_clicked)
        self.ui.btnClose.clicked.connect(self.close_toolbar)
        self.__buttons_to_disable = [self.ui.btnSegmentOut, self.ui.btnSegmentIn, self.ui.btnClose]



    # Tuỳ chọn: expose method show/hide shortcut
    def open(self):
        self.show()


    def close_toolbar(self):
        self.hide()


    def disable(self):
        """Disable buttons khi toolbar mất focus"""
        for btn in self.__buttons_to_disable:
            btn.setEnabled(False)


    def enable(self):
        """Enable lại khi toolbar lấy focus"""
        for btn in self.__buttons_to_disable:
            btn.setEnabled(True)


    def _on_btn_segment_in_clicked(self):
        print("Segment In")
        self.segment_in.emit() 


    def _on_btn_segment_out_clicked(self):
        print("Segment Out")
        self.segment_out.emit() 