from pathlib import Path
from models.job_model import JobModel
from models.file_model import FileModel
from models.cloud_model import CloudModel
from models.job_info_model import JobInfoModel

class JobService:

    CLOUD_EXTS = {".ply"}
    REPORT_EXTS = {".pdf"}

    def __init__(self):
        self.job_model: JobModel | None = None


    # @staticmethod
    def load(self, job_folder: str) -> JobModel:
        job_path = Path(job_folder)

        if not job_path.is_dir():
            raise FileNotFoundError(job_folder)

        job = JobModel(job_path)

        # --------------------------------------------------
        # 1. Scan all files (recursive)
        # --------------------------------------------------
        for p in job_path.rglob("*"):
            if not p.is_file():
                continue

            file_model = FileModel(p)
            job.add_file(file_model)

            ext = file_model.ext

            # --------------------------------------------------
            # 2. Create domain models (RAW)
            # --------------------------------------------------
            if ext in JobService.CLOUD_EXTS:
    
                cloud_model = CloudModel(source_path=p)
                # cloud_model.set_cloud(cloud_data)
                job.add_cloud(cloud_model)

            elif p.name == "job_info.json":
                job.job_info = JobInfoModel.from_file(p)
        self.job_model = job
        return self.job_model


    def get_cloud_model(self, cloud_id: str) -> CloudModel:
        return self.job_model.clouds[cloud_id]


    def get_all_cloud_models(self) -> list[CloudModel]:
        return list(self.job_model.clouds.values())


    def get_file(self, file_id: str) -> FileModel:
        return self.job_model.files[file_id]


    def add_cloud_model(self, cloud_model: CloudModel):
        self.job_model.add_cloud(cloud_model)


    def remove_cloud_model(self, cloud_id: str):
        if cloud_id in self.job_model.clouds:
            del self.job_model.clouds[cloud_id]


    def add_file(self, file_model: FileModel):
        self.job_model.add_file(file_model)


    def update_job_info(self, job_info: JobInfoModel):
        self.job_model.job_info = job_info


    def find_file_by_name(self, name: str) -> list[FileModel]:
        return [f for f in self.job_model.files if name in f.path.name]


    def find_cloud_models_by_name(self, name: str) -> list[CloudModel]:
        return [c for c in self.job_model.clouds.values() if name in c.name]
