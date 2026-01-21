# file: views/segment_toolbar_view.py
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QDialog
from views.ui.segment_toolbar_ui import Ui_SegmentToolbar
from views.components.tool_bar_base import ToolBar

class SegmentToolbarView(ToolBar):

    segment_in = Signal()
    segment_out = Signal()
    export_selected = Signal()
    clear = Signal()
    cancel = Signal()

    """
    Segment Toolbar Dialog (View)
    - Chỉ hiển thị UI: Confirm, Cancel, Close, type combo
    - Controller sẽ gán callback
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SegmentToolbar()
        self.ui.setupUi(self)
        # self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
        # self.setFocusPolicy(Qt.StrongFocus)

        self.installEventFilter(self)
        
        # Ẩn dialog khi khởi tạo
        self.hide()
        self.ui.btnSegmentIn.clicked.connect(self._on_btn_segment_in_clicked)
        # self.ui.btnSegmentOut.clicked.connect(self._on_btn_segment_out_clicked)
        self.ui.btnExportSelection.clicked.connect(self._on_btn_export_selected_clicked)
        self.ui.btnClose.clicked.connect(self._on_btn_close_clicked)
        self.ui.btnClear.clicked.connect(self._on_btn_clear_clicked)

        self.__buttons_to_disable = [self.ui.btnSegmentIn, self.ui.btnClose]

        self._btn_map = {
            "segmentin": self.ui.btnSegmentIn,
            # "segmentout": self.ui.btnSegmentOut,
            "exportselection": self.ui.btnExportSelection,
            "close": self.ui.btnClose,
            "clear": self.ui.btnClear
        }

    # Tuỳ chọn: expose method show/hide shortcut
    def open(self):
        self.show()

    def closeEvent(self, event):
        """
        Hàm này được gọi khi user đóng dialog (bấm X hoặc Alt+F4)
        """
        self.cancel.emit()      # emit signal cancel
        # self.hide()             # chỉ ẩn dialog
        # super().closeEvent(event)  # gọi base class để dialog thực sự đóng

    def reject(self):
        pass

    # Wrapper tiện dụng
    def enable(self, names=None):
        self.disable()  # disable tất cả trước
        self._set_buttons_enabled(names, True)

    def disable(self, names=None):
        self._set_buttons_enabled(names, False)

    def _set_buttons_enabled(self, names, enabled: bool):
        """Bật/tắt nhiều nút theo danh sách hoặc tên đơn"""

        if names is None:
            names = self._btn_map.keys()  # tất cả nút

        if isinstance(names, str):
            names = [names]  # convert thành list

        for name in names:
            key = name.lower()
            btn = self._btn_map.get(key)
            if btn:
                btn.setEnabled(enabled)
            else:
                raise ValueError(f"Button '{name}' not found")

    def _on_btn_close_clicked(self):
        self.cancel.emit()

    def _on_btn_segment_in_clicked(self):
        self.segment_in.emit() 

    def _on_btn_segment_out_clicked(self):
        self.segment_out.emit() 

    def _on_btn_export_selected_clicked(self):
        self.export_selected.emit()

    def _on_btn_clear_clicked(self):
        self.clear.emit()

