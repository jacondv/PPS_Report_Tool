from PySide6.QtCore import QTimer
from pyvistaqt import QtInteractor

class SafePlotter:
    def __init__(self, plotter: QtInteractor):
        self._plotter = plotter
        self._render_pending = False

    @property
    def widget(self):
        return self._plotter

    def render(self):
        if self._render_pending:
            return
        self._render_pending = True
        QTimer.singleShot(0, self._do_render)

    def _do_render(self):
        self._render_pending = False
        w = self._plotter

        if not w or not w.isVisible():
            return

        try:
            w.render()
        except RuntimeError:
            pass