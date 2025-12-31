from PySide6.QtCore import QObject, Signal

class EventBus(QObject):
    # các signal sự kiện chung
    cloud_visibility_changed = Signal(str, bool)
    segment_created = Signal(object)
    enable_create_report_action_button = Signal(bool)
# tạo singleton để các module dùng chung
event_bus = EventBus()
