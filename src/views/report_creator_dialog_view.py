# report_create_view.py
import os
from datetime import datetime
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QDate

from views.ui.report_creator_dialog_ui import Ui_ReportCreate  # đường dẫn tới file UI của bạn
from views.annotation_toolbar_view_fix import AnnotationToolbarView

from views.cloud_view import CloudView

from utils.image_utils import image_to_pixmap



class ReportCreateDialog(QDialog):
    """
    View cho chức năng tạo report.
    Dựa trên Ui_ReportCreate.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        # Tạo instance UI
        self.ui = Ui_ReportCreate()
        self.ui.setupUi(self)

        self.ann_toolbar = AnnotationToolbarView(parent=self.ui.widget_toolbar)
        layout = self.ui.widget_toolbar.layout()
        layout.addWidget(self.ann_toolbar)
        # self.ann_toolbar.show()
        # ---------------- Views ----------------

        self.cloud_view = CloudView(self.ui.cloud_viewer)


        # Tùy chỉnh thêm nếu cần
        self.setWindowTitle("Create Report")
        self.setModal(True)  # dialog modal

        # Kết nối signal/slot (nếu có)
        self._connect_signals()

    def _connect_signals(self):

        # Kết nối cleanup khi dialog đóng
        pass
        # """
        # Kết nối các nút / widget với các phương thức xử lý
        # """
        # # Ví dụ: nút export
        # if hasattr(self.ui, "btnExport"):
        #     self.ui.btnExport.clicked.connect(self.on_export_clicked)

        # # Ví dụ: nút chọn cloud
        # if hasattr(self.ui, "btnSelectCloud"):
        #     self.ui.btnSelectCloud.clicked.connect(self.on_select_cloud)


    def closeEvent(self, event):
        """
        Khi user đóng dialog:
        - Chỉ hide dialog, không destroy
        - CloudView vẫn còn
        """
        # self.cloud_view.cleanup()
        event.ignore()   # Bỏ qua close event mặc định
        self.hide()      # Chỉ hide dialog, không destroy widget


    def reject(self):
        # self.cloud_view.cleanup()
        self.hide()      # Chỉ hide dialog, không destroy widget
         
    # ----- pull dữ liệu từ GUI -----
    def get_report_info(self) -> str:
        """
        Lấy tất cả thông tin hiện tại từ GUI/dialog, trả về JSON
        """
        def _safe_float(txt):
            try:
                return float(txt)
            except ValueError:
                return 0.0

        def _safe_int(txt):
            try:
                return int(txt)
            except ValueError:
                return 0

        # Chuẩn hóa date và time sang string ISO
        date_val = self.ui.dateEdit.date().toPyDate()
        time_val = self.ui.timeEdit.time().toPyTime()

        report_dict = {
            "site_name": self.ui.txtSiteName.text(),
            "job_name": self.ui.txtJobName.text(),
            "date": date_val.strftime("%d-%b-%Y") if date_val else "",
            "time": time_val.isoformat() if time_val else "",
            "shotcrete_volume": _safe_float(self.ui.txtShotcreteVolume.text()),
            "applied_thickness": _safe_int(self.ui.txtShotcreteApplied.text()),
            "tolerance": _safe_int(self.ui.txtTolerance.text()),
            "average_thickness": _safe_float(self.ui.txtAverageThickness.text())
        }
        return report_dict

    # Set parameters for use in report
    def set_report_info(self, site_name: str=None, job_name: str=None, date: datetime.date=None, time: datetime.time=None, 
                        shotcrete_volume: float=None, applied_thickness: int=None, tolerance: int=None, average_thickness: float=None):
        """
        Thiết lập thông tin báo cáo hiển thị trên dialog
        """

        self.set_site_name(site_name)
        self.set_job_name(job_name)
        self.set_date(date)
        self.set_time(time) 
        self.set_shotcrete_volume(shotcrete_volume)
        self.set_shotcrete_applied(applied_thickness)
        self.set_tolerance(tolerance)
        self.set_average_thickness(average_thickness)

    
    def set_site_name(self, site_name: str):
        if site_name is None:
            site_name = ""
        self.ui.txtSiteName.setText(site_name)


    def set_job_name(self, job_name: str):
        if job_name is None:
            job_name = ""
        self.ui.txtJobName.setText(job_name)


    def set_date(self, date: datetime.date):
        if date is None:
            return
        self.ui.dateEdit.setDate(QDate(date.year, date.month, date.day))


    def set_time(self, time: datetime.time):
        if time is None:
            return
        self.ui.timeEdit.setTime(time)


    def set_shotcrete_volume(self, volume: float):
        if volume is None:
            self.ui.txtShotcreteVolume.setText("")
            return
        self.ui.txtShotcreteVolume.setText(f"{volume:.2f}")


    def set_shotcrete_applied(self, applied_thickness: int):
        if applied_thickness is None:
            return
        self.ui.txtShotcreteApplied.setText(f"{applied_thickness}")


    def set_tolerance(self, tolerance: int):
        if tolerance is None:
            return
        self.ui.txtTolerance.setText(f"{tolerance}")


    def set_average_thickness(self, thickness: float):
        if thickness is None:
            self.ui.txtAverageThickness.setText("")
            return
        self.ui.txtAverageThickness.setText(f"{thickness:.0f}")

    
    def show_image(self, image):
        """
        image: numpy image (BGR or RGB) or file path
        """
        pixmap = image_to_pixmap(image)
        if pixmap:
            self.ui.chart_viewer.setPixmap(pixmap)
            self.ui.chart_viewer.setScaledContents(True)
