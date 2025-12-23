import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Signal
from views.ui.main_window_ui import Ui_MainWindow

class MainWindow(QMainWindow):

    openJobRequested = Signal(str)
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        # ------------------- Tạo View + Controller + Service ở đây -------------------
        from views.tree_job_data_view import TreeJobDataView
        from views.cloud_view import CloudView
        from controllers.job_data_controller import JobDataController
        from controllers.cloud_controller import CloudController

        from services.cloud_service import CloudService


        self.tree_job_view = TreeJobDataView(self.ui.treeJobData)
        self.job_controller = JobDataController(self, self.tree_job_view)

        # Cloud view
        self.cloud_view = CloudView(self.ui.cloud_viewer)
        
        self.cloud_service = CloudService()
        self.cloud_controller = CloudController(
            tree_view=self.tree_job_view,
            cloud_view=self.cloud_view,
            cloud_service=self.cloud_service
        )
        # -------------------------------------------------------------------


        # Connect actions
        self.ui.actionOpen_Job.triggered.connect(self.open_file)

    def open_file(self):
        folder = QFileDialog.getExistingDirectory(
            self,                
            "Open PPS Job Folder",
            "",
            QFileDialog.ShowDirsOnly
        )
        if folder:
            self.openJobRequested.emit(folder)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)

#     mainapp = MainApp()
#     mainapp.showMaximized()

#     sys.exit(app.exec())
