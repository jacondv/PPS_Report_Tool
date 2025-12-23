from services.job_loader import load_job

class JobDataController:
    def __init__(self, main_window, tree_job_view):
        self.main_window = main_window
        self.tree_job_view = tree_job_view
        self.main_window.openJobRequested.connect(self.open_job)

    def open_job(self, folder_path):
        try:
            # 1️⃣ Load JobModel từ folder
            job_model = load_job(folder_path)

            # 2️⃣ Cập nhật TreeJobDataView
            self.tree_job_view.display(job_model)

            # 3️⃣ (Optional) cập nhật status bar / log
            self.main_window.statusBar().showMessage(f"Job '{job_model.name}' loaded successfully.")

        except Exception as e:
            # Xử lý lỗi, show message box
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.critical(self.main_window, "Error", f"Failed to load job:\n{e}")