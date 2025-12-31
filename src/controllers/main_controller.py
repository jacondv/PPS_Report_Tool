# controllers/main_controller.py

from PySide6.QtWidgets import QFileDialog
from controllers.job_data_controller import JobDataController
from controllers.cloud_controller import CloudController
from views.main_window import MainWindow
from services.cloud_service import CloudService
from services.job_service import JobService
from views.report_creator_dialog_view import ReportCreateDialog
from controllers.report_creator_controller import ReportCreatorController
from event_bus import event_bus
from paths import BASE_DIR, DATA_DIR
DEFAULT_JOB_PATH = str(DATA_DIR)

class MainController:
    def __init__(self, main_window: MainWindow):
        self.main_window = main_window

        # ---------------- Services ----------------
        self.job_service = JobService()  # Nếu cần thêm service cho job
        self.cloud_service = CloudService()

        # ---------------- Views ----------------
        self.tree_view = self.main_window.tree_job_view  # TreeJobDataView
        self.cloud_view = self.main_window.cloud_view   # CloudView
        
        self.report_viewer = ReportCreateDialog()  # ReportCreateDialog

        # ---------------- Controllers ----------------
        self.cloud_controller = CloudController(
            cloud_view=self.cloud_view,
            cloud_service=self.cloud_service,
            job_service=self.job_service
        )

        self.job_controller = JobDataController(
            tree_job_view=self.tree_view,
            job_service=self.job_service
        )

        self.report_controller = ReportCreatorController(
            dialog=self.report_viewer,
            cloud_service=self.cloud_service,
            job_service=self.job_service
        )

        # ---------------- Actions ----------------
        self.main_window.ui.actionOpen_Job.triggered.connect(self.open_job_dialog)
        self.main_window.ui.actionSegment.triggered.connect(self.cloud_controller.start_segment)
        self.main_window.ui.actionCreate_Report.triggered.connect(self.open_report_creator_dialog)
        self.main_window.ui.actionCreate_Report.setEnabled(False)

        # ---------------- Connect main window buttons ----------------

        #---------------- Signals handler ----------------
        self.main_window.closeRequested.connect(self.on_main_window_close)
        
        event_bus.enable_create_report_action_button.connect(self.on_enable_create_report_action)


        # Nếu muốn, giữ reference các controller dialog
        self._report_controllers = []

    def on_enable_create_report_action(self, visible):
        self.main_window.ui.actionCreate_Report.setEnabled(visible)

    # ---------------- Job workflow ----------------
    def open_job_dialog(self):
        folder = QFileDialog.getExistingDirectory(
            self.main_window,
            "Open PPS Job Folder",
            DEFAULT_JOB_PATH,
            QFileDialog.ShowDirsOnly
        )
        if not folder:
            return

        self.job_controller.open_job(folder)

    # ---------------- Report workflow ----------------
    def open_report_creator_dialog(self):
        # Tạo dialog
        current_cloud_ids = list(self.job_controller.cloud_active_ids)
        self.report_controller.show(cloud_ids=current_cloud_ids)


    def on_main_window_close(self):
        """Xử lý khi main window đóng: cleanup các controller nếu cần"""
        print("Main window is closing. Cleaning up controllers...")
        self.cloud_controller.cleanup()
        self.job_controller.close_job()
        self.main_window.close()