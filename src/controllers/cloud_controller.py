# controllers/cloud_controller.py
from PySide6.QtCore import QObject

class CloudController(QObject):
    def __init__(self, tree_view, cloud_view, cloud_service):
        super().__init__()
        self.tree_view = tree_view
        self.cloud_view = cloud_view
        self.cloud_service = cloud_service

        # Kết nối signal từ TreeJobDataView
        self.tree_view.openItemRequested.connect(self.on_open_item)

    def on_open_item(self, file_path: str):
        # 1. Load cloud TensorPointCloud
        # print(f"Received form {file_path}")
        # return
        cloud = self.cloud_service.load_cloud(file_path)

        # 3. Chuẩn bị dữ liệu numpy để hiển thị
        data = self.cloud_service.prepare_cloud_for_display(cloud)

        # 4. Hiển thị lên CloudView
        self.cloud_view.display_cloud(
            points=data['points'],
            colors=data['colors'],
            normals=data['normals']
        )
