# from PySide6.QtWidgets import QMainWindow, QFileDialog
# from views.ui.main_window_ui import Ui_MainWindow
# from services.cloud_service import CloudService
# from views.tree_job_data_view import TreeJobDataView
# from views.cloud_view import CloudView
# from controllers.job_data_controller import JobDataController
# from controllers.cloud_controller import CloudController

# class MainWindow(QMainWindow):

#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)

#         # ---------------- Views ----------------

#         self.tree_job_view = TreeJobDataView(self.ui.treeJobData)
#         self.cloud_view = CloudView(self.ui.cloud_viewer)

#         # ---------------- Models ----------------


#         # ---------------- Services ----------------

#         self.cloud_service = CloudService()
#         # ---------------- Controllers ----------------

#         self.cloud_controller = CloudController(
#             cloud_view=self.cloud_view,
#             cloud_service=self.cloud_service,
#         )

#         self.job_controller = JobDataController(self.tree_job_view, self.cloud_controller)


#         # ---------------- Signals ----------------


#         # ---------------- Actions ----------------
#         self.ui.actionOpen_Job.triggered.connect(self.open_job_dialog)
#         self.ui.actionSegment.triggered.connect(self.cloud_controller.start_segment)
#         self.ui.actionCreate_Report.triggered.connect(self.open_report_creator_dialog)

#     # ==================================================
#     # UI only: chọn folder job
#     # ==================================================

#     def open_job_dialog(self):
#         default_folder = "C:\\WORK\\projects\\PPS_Report_Tool\\data\\Job01"
#         job_folder = QFileDialog.getExistingDirectory(
#             self,
#             "Open PPS Job Folder",
#             default_folder, 
#             QFileDialog.ShowDirsOnly
#         )
#         if not job_folder:
#             return

#         # Request open job (project)
#         self.job_controller.open_job(job_folder)


#     def open_report_creator_dialog(self):
#         from views.report_creator_dialog_view import ReportCreateDialog

#         dialog = ReportCreateDialog(self)
#         dialog.exec()


from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMainWindow
from views.ui.main_window_ui import Ui_MainWindow
from views.tree_job_data_view import TreeJobDataView
from views.cloud_view import CloudView

class MainWindow(QMainWindow):
    closeRequested = Signal()
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # ---------------- Views ----------------
        self.tree_job_view = TreeJobDataView(self.ui.treeJobData)
        self.cloud_view = CloudView(self.ui.cloud_viewer)

        # # ---------------- Services ----------------
        # self.cloud_service = CloudService()

        # ---------------- Signals / nút ----------------
        # Chỉ emit signal hoặc expose nút, workflow do MainController xử lý
        # Ví dụ expose nút actionOpen_Job, actionSegment, actionCreate_Report
        # MainController sẽ connect các nút này với các controller

    def closeEvent(self, event):
        """
        Khi user đóng main window:
        - Emit signal closeRequested để MainController xử lý cleanup nếu cần
        - Sau đó mới gọi base class để đóng ứng dụng
        """
        self.closeRequested.emit()
        event.ignore() 