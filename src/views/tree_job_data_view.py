from PySide6.QtCore import Qt, Signal, QObject
from PySide6.QtWidgets import QTreeWidgetItem, QMenu

class TreeJobDataView(QObject):

    openItemRequested = Signal(str)
    def __init__(self, tree_widget):
        super().__init__()
        self.tree = tree_widget

    def display(self, job_model):
        self.tree.clear()


        # Thiết lập context menu
        self.tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tree.customContextMenuRequested.connect(self.on_context_menu)

        # Root node = Job name
        root_item = QTreeWidgetItem(self.tree, [job_model.name])

        # Job Info
        info_item = QTreeWidgetItem(root_item, ["Job Info"])
        for k, v in job_model.job_info.items():
            if isinstance(v, dict):
                sub_item = QTreeWidgetItem(info_item, [k])
                for sk, sv in v.items():
                    QTreeWidgetItem(sub_item, [f"{sk}: {sv}"])
            else:
                QTreeWidgetItem(info_item, [f"{k}: {v}"])

        # Scan Units
        for unit in job_model.scan_units:
            unit_item = QTreeWidgetItem(root_item, [unit.name])

            # Pre-Scan
            pre_item = QTreeWidgetItem(unit_item, ["Pre-Scan"])
            for f in unit.pre_scans:
                f_item = QTreeWidgetItem(pre_item, [f.name])
                f_item.path = f

            # Post-Scan
            post_item = QTreeWidgetItem(unit_item, ["Post-Scan"])
            for f in unit.post_scans:
                f_item = QTreeWidgetItem(post_item, [f.name])
                f_item.path = f

        self.tree.expandAll()


    def on_context_menu(self, pos):
        item = self.tree.itemAt(pos)

        if item and hasattr(item, "path"):
            menu = QMenu()
            open_action = menu.addAction("Open")
            action = menu.exec_(self.tree.mapToGlobal(pos))
            if action == open_action:
                self.openItemRequested.emit(str(item.path))
                