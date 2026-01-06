# report_creator_controller.py
from datetime import datetime
from paths import DATA_DIR
from pathlib import Path

from PySide6.QtCore import QObject
from PySide6.QtWidgets import QMessageBox, QFileDialog

from controllers.cloud_controller import CloudController
from pps_shared.tunnel_report.report_controler import ReportGenerator
from pps_shared.helper import assign_colors
from utils.image_utils import image_array_to_base64_png


class ReportCreatorController(QObject):
    """
    Controller cho ReportCreateDialog
    Quản lý logic: chọn cloud, preview, export PDF
    """

    def __init__(self, dialog, cloud_service: "CloudService", job_service: "JobService"):
        """
        dialog: instance của ReportCreateDialog
        cloud_service: service quản lý cloud
        job_service: service quản lý job
        """
        super().__init__()
        self.report_dialog = dialog
        self.cloud_service = cloud_service
        self.job_service = job_service
        self.cloud_view = self.report_dialog.cloud_view
        self.cloud_controller = CloudController(self.cloud_view, self.cloud_service, self.job_service)

        self.report_generator = ReportGenerator()

        # Active cloud IDs
        self.cloud_ids = []
        # Kết nối signal/slot từ dialog
        self._connect_signals()

    def _connect_signals(self):

        """Connect các nút / widget từ dialog với handler"""
        ui = self.report_dialog.ui

        if hasattr(ui, "btnExport"):
            ui.btnExport.clicked.connect(self.on_export_clicked)

        if hasattr(ui, "btnUpdate"):
            ui.btnUpdate.clicked.connect(self.on_update_clicked)

        if hasattr(ui, "txtShotcreteApplied"):
            ui.txtShotcreteApplied.textChanged.connect(self.on_shotcrete_applied_changed)


    def show(self,**kwargs):
        """Hiển thị dialog tạo report"""
        
        if 'cloud_ids' in kwargs:
            self.cloud_ids = kwargs['cloud_ids']
            print("We have", self.cloud_ids)

            # Check if the cloud format is correct.
            try:
                cloud = self.job_service.get_cloud_model(self.cloud_ids[0])
                cloud = cloud.get_cloud()
                has_distances = "distances" in cloud.point
            except:
                has_distances = False


            if not has_distances:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Report Error")
                msg.setText("This cloud has not been compared yet, so a report cannot be generated.")
                msg.exec()
                return
                
            self.report_dialog.show()
            self.set_report_info()
            self.upadte()
        else:
            self.cloud_ids = []

        
        
    def display_cloud(self, cloud_id: str | list[str]):
            print("Active cloud IDs for report:", cloud_id)
            """Hiển thị cloud đã chọn trong CloudView của dialog"""

            if not isinstance(cloud_id, list):
                cloud_id = [cloud_id]

            for cid in cloud_id:
                cloud_model = self.job_service.get_cloud_model(cid)
                if cloud_model:
                    self.cloud_controller.cleanup()
                    self.cloud_controller.render_cloud(cloud_model)


    def crete_report(self):
        """Tạo report PDF từ các cloud đã chọn"""
        if self.report_generator is None:
            self.report_generator = ReportGenerator()

        report_info = self.report_dialog.get_report_info()

        self.report_generator.set_info(
            site_name=report_info['site_name'],
            job_name=report_info['job_name'],
            date=report_info['date'],
            time=report_info['time'],
            applied_thickness=report_info['applied_thickness'],
            tolerance=report_info['tolerance']
        )

        image = self.cloud_view.capture_current_view()
        image_base64 = image_array_to_base64_png(image)
        self.report_generator.set_tunnel_view_image(image_base64)

        cloud_id = self.cloud_ids[0]
        cloud_model = self.job_service.get_cloud_model(cloud_id)
        cloud = cloud_model.get_cloud()

        # --- File Save Dialog ---
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog  # tuỳ chọn nếu cần

        file_name = DATA_DIR / f"report_{cloud_id}.pdf"

        report_file_name, _ = QFileDialog.getSaveFileName(
            parent=None,                       
            caption="Save Report to PDF",          
            directory=str(file_name),    
            filter="PDF Files (*.pdf);;All Files (*)",
            options=options
        )
        #---if cancel is return None
        if not report_file_name:
            return

        #---if missing file extension part
        if not report_file_name.lower().endswith(".pdf"):
            report_file_name += ".pdf"

        
        _low = int(report_info['applied_thickness']) - int(report_info['tolerance'])
        _high = int(report_info['applied_thickness']) + int(report_info['tolerance'])
        cloud = assign_colors(cloud,clip_max=150,highlight_range=(_low, _high))

        self.report_generator.export(cloud, report_file_name)


    def set_report_info(self):
        """Tải thông tin job hiện tại từ JobService"""
        job_info = self.job_service.job_model.job_info.to_dict()
        if not job_info:
            return
        job_name = job_info.get("name", "Unknown Job")
        create_date = job_info.get("created", "Unknown Date")
        dt = datetime.strptime(create_date, "%Y-%m-%d %H:%M:%S")
        date_part = dt.date()   # 19/11/2025
        time_part = dt.time()   # 08:40:22

        applied_thickness = job_info.get("parameters", {}).get("target_thickness", None)
        tolerance = job_info.get("parameters", {}).get("tolerance", None)

        site_name = "JACON"
        self.report_dialog.set_report_info(
            site_name=site_name,    
            job_name=job_name,
            date=date_part,
            time=time_part,
            shotcrete_volume=None,
            average_thickness=None,
            applied_thickness=applied_thickness,
            tolerance=tolerance
        )


    def upadte(self):

        report_info = self.report_dialog.get_report_info()

        cloud_id = self.cloud_ids[0]
        cloud_model = self.job_service.get_cloud_model(cloud_id)
        cloud = cloud_model.get_cloud()

        new_thickness = report_info['applied_thickness']
        new_tolerance = report_info['tolerance']
        _low = new_thickness - new_tolerance
        _high = new_thickness + new_tolerance

        cloud = assign_colors(cloud,highlight_range=(_low, _high))
        

        cloud_model.set_cloud(cloud)

        # self.report_generator = ReportGenerator()
        self.report_generator.set_info(
            site_name=report_info['site_name'],
            job_name=report_info['job_name'],
            date=report_info['date'],
            time=report_info['time'],
            applied_thickness=report_info['applied_thickness'],
            tolerance=report_info['tolerance'],
        )
        data = self.report_generator.prepare_data(cloud)
        shotcrete_volume = data.shotcrete_volume
        avg_thickness = data.avg_thickness
        thickness_chart = data.thickness_chart

        # Update to texbox
        self.report_dialog.set_average_thickness(avg_thickness)
        self.report_dialog.set_shotcrete_volume(shotcrete_volume)     

        self.display_cloud(cloud_id)
        self.report_dialog.show_image(thickness_chart)



# Handler button event
    def on_export_clicked(self):
        self.crete_report()

    def on_update_clicked(self):
        self.upadte()
        self.report_dialog.ui.btnExport.setEnabled(True)

    def on_shotcrete_applied_changed(self):
        self.report_dialog.ui.btnExport.setEnabled(False)

#Sample job_info.json content:

# {
#     "name": "ARM0Deg",
#     "created": "2025-11-19 08:40:22",
#     "status": "pending",
#     "description": "",
#     "parameters": {
#         "target_thickness": 50,
#         "tolerance": 10
#     }
# }