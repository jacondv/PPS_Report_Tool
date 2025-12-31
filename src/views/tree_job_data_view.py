
import os
from PySide6.QtCore import Qt, Signal, QObject
from PySide6.QtWidgets import QTreeWidgetItem, QMenu, QAbstractItemView
from services.pps_filename_parser import PpsFilenameParser

class TreeJobDataView(QObject):

    openItemRequested = Signal(str)
    selectCloudRequested = Signal(str)
    cloudVisibilityChanged = Signal(str, bool)
    selectedItemsChanged = Signal(list)
    deleteCloudRequested = Signal()

    ROLE_DATA = Qt.UserRole

    def __init__(self, tree_widget):
        super().__init__()
        self.tree = tree_widget
        # Multi selection
        self.tree.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tree.customContextMenuRequested.connect(self.on_context_menu)

        self.tree.itemChanged.connect(self.on_item_changed)
        self.tree.itemSelectionChanged.connect(self.on_selection_changed)
    

    def _find_item(self, item_type: str, item_id: str) -> QTreeWidgetItem | None:
        root = self.tree.invisibleRootItem()

        def dfs(item: QTreeWidgetItem):
            data = item.data(0, self.ROLE_DATA)
            if data and data[0] == item_type and data[1] == item_id:
                return item

            for i in range(item.childCount()):
                found = dfs(item.child(i))
                if found:
                    return found
            return None

        for i in range(root.childCount()):
            found = dfs(root.child(i))
            if found:
                return found

        return None

    def _add_dict_to_tree(self, parent_item, data: dict):
        """
        Hiển thị dict lên Tree recursively
        """
        for key, value in data.items():
            if isinstance(value, dict):
                item = QTreeWidgetItem(parent_item, [key])
                self._add_dict_to_tree(item, value)
            else:
                QTreeWidgetItem(parent_item, [f"{key}: {value}"])
                

    def _get_selected_cloud_ids(self) -> list[str]:
        cloud_ids = []
        for item in self.tree.selectedItems():
            data = item.data(0, self.ROLE_DATA)
            if data is None:
                continue
            data_type, obj_id = data
            if data_type == "cloud":
                cloud_ids.append(obj_id)
        return cloud_ids


    # ==================================================
    # Display
    # ==================================================

    def display(self, job_model):
        self.tree.clear()

        # Root = Job
        root_item = QTreeWidgetItem([job_model.job_path.name])
        root_item.setData(0, self.ROLE_DATA, ("job", None))
        self.tree.addTopLevelItem(root_item)

        # ---------------- Job Info ----------------
        if job_model.job_info:
            info_item = QTreeWidgetItem(root_item, ["Job Info"])
            self._add_dict_to_tree(info_item, job_model.job_info.to_dict())

        # # ---------------- Files ----------------
        # files_item = QTreeWidgetItem(root_item, ["Files"])
        # for f in job_model.files:
        #     item = QTreeWidgetItem(files_item, [f.path.name])
        #     item.setData(0, self.ROLE_DATA, ("file", str(f.path)))

        # ---------------- Clouds ----------------
        # clouds_item = QTreeWidgetItem(root_item, ["Clouds"])
        # for cloud in job_model.clouds.values():
        #     cloud_item = QTreeWidgetItem(clouds_item, [cloud.source_path.name])
        #     cloud_item.setData(0, self.ROLE_DATA, ("cloud", cloud.id))

        clouds_item = QTreeWidgetItem(root_item, ["Clouds"])

        # group các cloud theo file gốc (source_path)
        # map file_name -> file_group item
        file_group_map = {}
        # map cloud.id -> QTreeWidgetItem, dùng cho segment thêm vào
        cloud_item_map = {}

        for cloud in job_model.clouds.values():
            if cloud.parent_id is None:
                # Cloud gốc -> tạo file-group
                file_name = cloud.source_path.name if cloud.source_path else cloud.name
                file_group_item = QTreeWidgetItem(clouds_item, [file_name])
                file_group_item.setData(0, self.ROLE_DATA, ("file_group", file_name))
                file_group_map[file_name] = file_group_item

                # Cloud original

                name_parse = PpsFilenameParser.parse(file_name) if file_name else None
                display_name = f"{name_parse['scan_type']}_scan_({name_parse['index']})" if name_parse else cloud.name
                display_name = f"{display_name}-original"
                cloud_item = QTreeWidgetItem(file_group_item, [display_name])
                cloud_item.setData(0, self.ROLE_DATA, ("cloud", cloud.id))
                cloud_item.setFlags(cloud_item.flags() | Qt.ItemIsUserCheckable)
                cloud_item.setCheckState(0, Qt.Unchecked)

                cloud_item_map[cloud.id] = cloud_item
            else:
                # Segment -> thêm vào group của cloud cha
                parent_cloud_item = cloud_item_map.get(cloud.parent_id)
                if parent_cloud_item is not None:
                    # Lấy file-group của parent
                    file_group_item = parent_cloud_item.parent()
                    if file_group_item is None:
                        file_group_item = clouds_item  # fallback

                    display_name = f"{cloud.name}"
                    cloud_item = QTreeWidgetItem(file_group_item, [display_name])
                    cloud_item.setData(0, self.ROLE_DATA, ("cloud", cloud.id))
                    cloud_item.setFlags(cloud_item.flags() | Qt.ItemIsUserCheckable)
                    cloud_item.setCheckState(0, Qt.Unchecked)

                    cloud_item_map[cloud.id] = cloud_item

                
        # ---------------- Reports ----------------
        reports_item = QTreeWidgetItem(root_item, ["Reports"])
        for report in job_model.reports.values():
            item = QTreeWidgetItem(reports_item, [report.source_path.name])
            item.setData(0, self.ROLE_DATA, ("report", report.id))

        self.tree.expandAll()

    def add_segment_item(self, parent_id, cloud_model):
        cloud_item = self._find_item("cloud", parent_id)
        if cloud_item is None:
            return

        # Lấy parent của cloud_item
        parent_item = cloud_item.parent()  
        if parent_item is None:
            parent_item = self.tree  # nếu cloud_item là top-level, thêm trực tiếp vào tree

        # Thêm segment vào cùng cấp với cloud_item
        seg_item = QTreeWidgetItem(parent_item, [cloud_model.name])
        seg_item.setData(0, self.ROLE_DATA, ("cloud", cloud_model.id))
        seg_item.setFlags(seg_item.flags() | Qt.ItemIsUserCheckable)
        seg_item.setCheckState(0, Qt.Unchecked)
        # Mở rộng group nếu cần
        if parent_item != self.tree:
            parent_item.setExpanded(True)


    def remove_cloud_item(self, cloud_id):
        cloud_item = self._find_item("cloud", cloud_id)
        if cloud_item is not None:
            parent_item = cloud_item.parent()
            if parent_item is not None:
                parent_item.removeChild(cloud_item)

            # else:
            #     index = self.tree.indexOfTopLevelItem(cloud_item)
            #     self.tree.takeTopLevelItem(index)

    # ==================================================
    # Context menu
    # ==================================================

    def on_context_menu(self, pos):
        item = self.tree.itemAt(pos)
        if not item:
            return

        data = item.data(0, self.ROLE_DATA)
        if not data:
            return

        kind, value = data
        menu = QMenu(self.tree)

        if kind == "file":
            open_action = menu.addAction("Open File")
            action = menu.exec_(self.tree.mapToGlobal(pos))
            if action == open_action:
                self.openItemRequested.emit(value)

        elif kind == "cloud":
            open_action = menu.addAction("View")
            delete_action = menu.addAction("Delete")

            action = menu.exec_(self.tree.mapToGlobal(pos))

            if action == open_action:
                self.selectCloudRequested.emit(value)

            if action == delete_action:
                self.deleteCloudRequested.emit()

    def on_item_changed(self, item, column):
        
        if column != 0:
            return
        data = item.data(0, self.ROLE_DATA)
        if data is None:
            return

        kind, value = data
        if kind != "cloud":
            return
        checked = item.checkState(0) == Qt.Checked
        # Emit ra cho controller
        
        self.cloudVisibilityChanged.emit(value, checked)

    def on_selection_changed(self):
        selected_cloud_ids = self._get_selected_cloud_ids()
        self.selectedItemsChanged.emit(selected_cloud_ids)
