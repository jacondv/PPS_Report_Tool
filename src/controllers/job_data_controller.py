from services.job_loader import load_job

class JobDataController:
    def __init__(self, tree_job_view):
        self.tree_job_view = tree_job_view

    def open_job(self, folder_path):

        try:
            # 1. Load Job từ folder
            job_model = load_job(folder_path)

            # 2. Cập nhật TreeJobDataView
            self.tree_job_view.display(job_model)

        except Exception as e:
            # Xử lý lỗi
            print("[JobDataController] error: ", e )
