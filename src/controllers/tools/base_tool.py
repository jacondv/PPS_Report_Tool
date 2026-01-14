from PySide6.QtCore import QObject

class Tool(QObject):
    requires_disable_view = False 

    def on_mouse_press(self, pos, button): pass
    def on_mouse_move(self, pos): pass
    def on_mouse_release(self, pos, button): pass
    def on_activate(self): pass
    def on_deactivate(self): pass
