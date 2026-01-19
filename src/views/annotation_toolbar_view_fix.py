from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QDialog, QWidget
from views.ui.annotation_toolbar_ui import Ui_AnnotationToolbar
from views.components.tool_bar_base import ToolBar

class AnnotationToolbarView(QWidget):
    """
    Annotation Toolbar Dialog (View)
    - Chỉ hiển thị UI
    - Controller gán callback
    """

    # -------- signals (camelCase) --------
    addText = Signal()
    addLine = Signal()
    move = Signal()
    editSignal = Signal()
    deleteSignal = Signal()
    closeClicked = Signal()
    cancelSignal = Signal()
    selectSignal = Signal()

    fontChanged = Signal(str)
    fontsizeChanged = Signal(int)
    sizeChanged = Signal(int)


    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_AnnotationToolbar()
        self.ui.setupUi(self)
        # self.installEventFilter(self)

        # Ẩn khi khởi tạo

        # -------- connect UI --------
        self.ui.btnAddText.clicked.connect(self._onAddText)
        self.ui.btnAddLine.clicked.connect(self._onAddLine)
        self.ui.btnMove.clicked.connect(self._onMove)
        self.ui.btnDelete.clicked.connect(self._onDelete)
        self.ui.btnClose.clicked.connect(self._onClose)
        self.ui.btnEdit.clicked.connect(self._onEdit)
        self.ui.btnSelect.clicked.connect(self._onSelect)

        self.ui.cbbFont.currentFontChanged.connect(
            lambda font: self.fontChanged.emit(font.family())
        )
        self.ui.cbbSize.currentTextChanged.connect(
            lambda size: self.sizeChanged.emit(int(size))
        )
        self.ui.cbbFontSize.currentTextChanged.connect(
            lambda size: self.fontsizeChanged.emit(int(size))
        )
        # -------- button map --------
        self._btn_map = {
            "addtext": self.ui.btnAddText,
            "addline": self.ui.btnAddLine,
            "move": self.ui.btnMove,
            "delete": self.ui.btnDelete,
            "close": self.ui.btnClose,
            'edit': self.ui.btnEdit
        }


    def setButtonVisible(self, names=None, visible: bool = True):
        """
        Hiện / Ẩn các button
        names: None | str | list[str]
        """
        if names is None:
            names = self._btn_map.keys()

        if isinstance(names, str):
            names = [names]

        for name in names:
            key = name.lower()
            btn = self._btn_map.get(key)
            if not btn:
                raise ValueError(f"Button '{name}' not found")
            btn.setVisible(visible)
            

    # -------- enable / disable --------
    def enable(self, names=None):
        self.disable()
        self._set_buttons_enabled(names, True)

    def disable(self, names=None):
        self._set_buttons_enabled(names, False)

    def _set_buttons_enabled(self, names, enabled: bool):
        if names is None:
            names = self._btn_map.keys()

        if isinstance(names, str):
            names = [names]

        for name in names:
            key = name.lower()
            btn = self._btn_map.get(key)
            if not btn:
                raise ValueError(f"Button '{name}' not found")
            btn.setEnabled(enabled)

    # -------- slots --------
    def _onAddText(self):
        self.addText.emit()


    def _onAddLine(self):
        self.addLine.emit()

    def _onMove(self):
        self.move.emit()

    def _onEdit(self):
        self.editSignal.emit()

    def _onDelete(self):
        self.deleteSignal.emit()

    def _onClose(self):
        self.closeClicked.emit()
        self.cancelSignal.emit()
        self.hide()

    def _onSelect(self):
        self.selectSignal.emit()
