# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'report_creator_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSplitter,
    QTimeEdit, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_ReportCreate(object):
    def setupUi(self, ReportCreate):
        if not ReportCreate.objectName():
            ReportCreate.setObjectName(u"ReportCreate")
        ReportCreate.resize(836, 878)
        ReportCreate.setStyleSheet(u"/* =========================\n"
"   GLOBAL\n"
"========================= */\n"
"QMainWindow {\n"
"    background-color: #f5f6f8;\n"
"    color: #2b2b2b;\n"
"    font-family: \"Segoe UI\", \"Roboto\", \"Arial\";\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"/* =========================\n"
"   CENTRAL WIDGET\n"
"========================= */\n"
"QWidget#centralwidget {\n"
"    background-color: #f5f6f8;\n"
"}\n"
"\n"
"/* =========================\n"
"   TOOLBAR\n"
"========================= */\n"
"QToolBar {\n"
"    background: #ffffff;\n"
"    border-bottom: 1px solid #dcdcdc;\n"
"    spacing: 6px;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QToolButton {\n"
"    background-color: transparent;\n"
"    border: 1px solid transparent;\n"
"    padding: 6px 10px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #e8f1fb;\n"
"    border: 1px solid #c9def4;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #0078d7;\n"
"    border: 1px solid #0078d7;\n"
"    color: #ffffff;\n"
"}\n"
""
                        "\n"
"/* =========================\n"
"   MENU BAR\n"
"========================= */\n"
"QMenuBar {\n"
"    background-color: #ffffff;\n"
"    color: #2b2b2b;\n"
"    border-bottom: 1px solid #dcdcdc;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    background-color: #e8f1fb;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #dcdcdc;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    background-color: #0078d7;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"/* =========================\n"
"   DOCK WIDGET\n"
"========================= */\n"
"QDockWidget {\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QDockWidget::title {\n"
"    background: #f0f2f5;\n"
"    padding: 6px;\n"
"    border-bottom: 1px solid #dcdcdc;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QDockWidget::close-button,\n"
"QDockWidget::float-button {\n"
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QDockWidget::close-button:hover,\n"
"QDockWidget::float-button:hover {\n"
"    background: #e8f1fb;\n"
"}\n"
"\n"
""
                        "/* =========================\n"
"   TREE WIDGET\n"
"========================= */\n"
"QTreeWidget {\n"
"    background-color: #ffffff;\n"
"    alternate-background-color: #f6f8fa;\n"
"    border: 1px solid #dcdcdc;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QTreeWidget::item {\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QTreeWidget::item:selected {\n"
"    background-color: #cfe5ff;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #f0f2f5;\n"
"    color: #333333;\n"
"    padding: 4px;\n"
"    border: 1px solid #dcdcdc;\n"
"}\n"
"\n"
"/* =========================\n"
"   LIST WIDGET\n"
"========================= */\n"
"QListWidget {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #dcdcdc;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #cfe5ff;\n"
"    color: #000000;\n"
"}\n"
"\n"
"/* =========================\n"
"   SPLITTER\n"
"========================= */\n"
"QSplitter::handle {\n"
"    backgr"
                        "ound-color: #dcdcdc;\n"
"}\n"
"\n"
"QSplitter::handle:hover {\n"
"    background-color: #0078d7;\n"
"}\n"
"\n"
"/* =========================\n"
"   STATUS BAR\n"
"========================= */\n"
"QStatusBar {\n"
"    background-color: #f0f2f5;\n"
"    border-top: 1px solid #dcdcdc;\n"
"    color: #333333;\n"
"}\n"
"\n"
"/* =========================\n"
"   SCROLL BAR\n"
"========================= */\n"
"QScrollBar:vertical {\n"
"    background: #f0f2f5;\n"
"    width: 12px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #c4c4c4;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #0078d7;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"/* =========================\n"
"   CLOUD VIEW PLACEHOLDER\n"
"========================= */\n"
"QWidget#cloud_viewer {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #cfcfcf;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(ReportCreate)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(ReportCreate)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_12 = QWidget(self.widget)
        self.widget_12.setObjectName(u"widget_12")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy1)
        self.widget_12.setMinimumSize(QSize(0, 35))
        self.widget_12.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_10 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 2, -1, 2)
        self.btnOpen = QPushButton(self.widget_12)
        self.btnOpen.setObjectName(u"btnOpen")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnOpen.sizePolicy().hasHeightForWidth())
        self.btnOpen.setSizePolicy(sizePolicy2)
        self.btnOpen.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_10.addWidget(self.btnOpen)

        self.btnAddText = QPushButton(self.widget_12)
        self.btnAddText.setObjectName(u"btnAddText")
        sizePolicy2.setHeightForWidth(self.btnAddText.sizePolicy().hasHeightForWidth())
        self.btnAddText.setSizePolicy(sizePolicy2)

        self.horizontalLayout_10.addWidget(self.btnAddText)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addWidget(self.widget_12)

        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setMaximumSize(QSize(16777215, 150))
        self.horizontalLayout_9 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 20, -1, -1)
        self.widget_2 = QWidget(self.groupBox)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.txtSiteName = QLineEdit(self.widget_3)
        self.txtSiteName.setObjectName(u"txtSiteName")

        self.horizontalLayout.addWidget(self.txtSiteName)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.txtJobName = QLineEdit(self.widget_4)
        self.txtJobName.setObjectName(u"txtJobName")

        self.horizontalLayout_2.addWidget(self.txtJobName)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_5)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.dateEdit = QDateEdit(self.widget_5)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMaximumDate(QDate(2100, 12, 31))
        self.dateEdit.setMinimumDate(QDate(2000, 9, 14))
        self.dateEdit.setDate(QDate(2025, 12, 29))

        self.horizontalLayout_3.addWidget(self.dateEdit)


        self.verticalLayout_2.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget_6)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.timeEdit = QTimeEdit(self.widget_6)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setMaximumDate(QDate(2000, 1, 1))

        self.horizontalLayout_4.addWidget(self.timeEdit)


        self.verticalLayout_2.addWidget(self.widget_6)


        self.horizontalLayout_9.addWidget(self.widget_2)

        self.widget_7 = QWidget(self.groupBox)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_3 = QVBoxLayout(self.widget_7)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.widget_7)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget_8)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.txtShotcreteApplied = QLineEdit(self.widget_8)
        self.txtShotcreteApplied.setObjectName(u"txtShotcreteApplied")

        self.horizontalLayout_5.addWidget(self.txtShotcreteApplied)

        self.label_9 = QLabel(self.widget_8)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_5.addWidget(self.label_9)


        self.verticalLayout_3.addWidget(self.widget_8)

        self.widget_11 = QWidget(self.widget_7)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget_11)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.txtTolerance = QLineEdit(self.widget_11)
        self.txtTolerance.setObjectName(u"txtTolerance")

        self.horizontalLayout_8.addWidget(self.txtTolerance)

        self.label_10 = QLabel(self.widget_11)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_8.addWidget(self.label_10)


        self.verticalLayout_3.addWidget(self.widget_11)

        self.widget_9 = QWidget(self.widget_7)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.widget_9)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.txtAverageThickness = QLineEdit(self.widget_9)
        self.txtAverageThickness.setObjectName(u"txtAverageThickness")

        self.horizontalLayout_6.addWidget(self.txtAverageThickness)

        self.label_11 = QLabel(self.widget_9)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_6.addWidget(self.label_11)


        self.verticalLayout_3.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.widget_7)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.widget_10)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.txtShotcreteVolume = QLineEdit(self.widget_10)
        self.txtShotcreteVolume.setObjectName(u"txtShotcreteVolume")

        self.horizontalLayout_7.addWidget(self.txtShotcreteVolume)

        self.label_12 = QLabel(self.widget_10)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_7.addWidget(self.label_12)


        self.verticalLayout_3.addWidget(self.widget_10)


        self.horizontalLayout_9.addWidget(self.widget_7)

        self.widget_14 = QWidget(self.groupBox)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.btnUpdate = QPushButton(self.widget_14)
        self.btnUpdate.setObjectName(u"btnUpdate")
        self.btnUpdate.setMinimumSize(QSize(60, 30))

        self.horizontalLayout_13.addWidget(self.btnUpdate)

        self.btnExport = QPushButton(self.widget_14)
        self.btnExport.setObjectName(u"btnExport")
        self.btnExport.setMinimumSize(QSize(80, 30))

        self.horizontalLayout_13.addWidget(self.btnExport)


        self.horizontalLayout_9.addWidget(self.widget_14)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.splitter = QSplitter(self.widget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.groupBox_2 = QGroupBox(self.splitter)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QSize(0, 300))
        self.horizontalLayout_12 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 20, -1, -1)
        self.splitter_2 = QSplitter(self.groupBox_2)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.widget_13 = QWidget(self.splitter_2)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.widget_13)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.treeJobData = QTreeWidget(self.widget_13)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeJobData.setHeaderItem(__qtreewidgetitem)
        self.treeJobData.setObjectName(u"treeJobData")

        self.verticalLayout_5.addWidget(self.treeJobData)

        self.splitter_2.addWidget(self.widget_13)
        self.cloud_viewer = QWidget(self.splitter_2)
        self.cloud_viewer.setObjectName(u"cloud_viewer")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.cloud_viewer.sizePolicy().hasHeightForWidth())
        self.cloud_viewer.setSizePolicy(sizePolicy3)
        self.splitter_2.addWidget(self.cloud_viewer)

        self.horizontalLayout_12.addWidget(self.splitter_2)

        self.widget_15 = QWidget(self.groupBox_2)
        self.widget_15.setObjectName(u"widget_15")
        self.verticalLayout_7 = QVBoxLayout(self.widget_15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.btnAnnotationTool = QPushButton(self.widget_15)
        self.btnAnnotationTool.setObjectName(u"btnAnnotationTool")
        sizePolicy2.setHeightForWidth(self.btnAnnotationTool.sizePolicy().hasHeightForWidth())
        self.btnAnnotationTool.setSizePolicy(sizePolicy2)

        self.verticalLayout_7.addWidget(self.btnAnnotationTool)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)


        self.horizontalLayout_12.addWidget(self.widget_15)

        self.splitter.addWidget(self.groupBox_2)
        self.groupBox_3 = QGroupBox(self.splitter)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QSize(0, 300))
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 20, -1, -1)
        self.chart_viewer_widget = QWidget(self.groupBox_3)
        self.chart_viewer_widget.setObjectName(u"chart_viewer_widget")
        sizePolicy3.setHeightForWidth(self.chart_viewer_widget.sizePolicy().hasHeightForWidth())
        self.chart_viewer_widget.setSizePolicy(sizePolicy3)
        self.horizontalLayout_11 = QHBoxLayout(self.chart_viewer_widget)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.chart_viewer = QLabel(self.chart_viewer_widget)
        self.chart_viewer.setObjectName(u"chart_viewer")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.chart_viewer.sizePolicy().hasHeightForWidth())
        self.chart_viewer.setSizePolicy(sizePolicy4)
        self.chart_viewer.setMinimumSize(QSize(400, 0))
        self.chart_viewer.setMaximumSize(QSize(400, 16777215))
        self.chart_viewer.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.chart_viewer)


        self.verticalLayout_6.addWidget(self.chart_viewer_widget)

        self.splitter.addWidget(self.groupBox_3)

        self.verticalLayout_4.addWidget(self.splitter)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(ReportCreate)

        QMetaObject.connectSlotsByName(ReportCreate)
    # setupUi

    def retranslateUi(self, ReportCreate):
        ReportCreate.setWindowTitle(QCoreApplication.translate("ReportCreate", u"Dialog", None))
        self.btnOpen.setText(QCoreApplication.translate("ReportCreate", u"Open", None))
        self.btnAddText.setText(QCoreApplication.translate("ReportCreate", u"Add Text", None))
        self.groupBox.setTitle(QCoreApplication.translate("ReportCreate", u"REPORT INFORMATION", None))
        self.label.setText(QCoreApplication.translate("ReportCreate", u"Site", None))
        self.label_2.setText(QCoreApplication.translate("ReportCreate", u"Job Name", None))
        self.label_3.setText(QCoreApplication.translate("ReportCreate", u"Date", None))
        self.label_4.setText(QCoreApplication.translate("ReportCreate", u"Time", None))
        self.timeEdit.setDisplayFormat(QCoreApplication.translate("ReportCreate", u"hh:mm:ss", None))
        self.label_5.setText(QCoreApplication.translate("ReportCreate", u"Shotcrete Applied", None))
        self.label_9.setText(QCoreApplication.translate("ReportCreate", u"(mm)", None))
        self.label_8.setText(QCoreApplication.translate("ReportCreate", u"Tolerance", None))
        self.label_10.setText(QCoreApplication.translate("ReportCreate", u"(mm)", None))
        self.label_6.setText(QCoreApplication.translate("ReportCreate", u"Average Thickness", None))
        self.label_11.setText(QCoreApplication.translate("ReportCreate", u"(mm)", None))
        self.label_7.setText(QCoreApplication.translate("ReportCreate", u"Shotcrete Volume", None))
        self.label_12.setText(QCoreApplication.translate("ReportCreate", u"(m\u00b3)", None))
        self.btnUpdate.setText(QCoreApplication.translate("ReportCreate", u"Apply", None))
        self.btnExport.setText(QCoreApplication.translate("ReportCreate", u"Export to PDF", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ReportCreate", u"TUNNEL VIEW", None))
        self.btnAnnotationTool.setText(QCoreApplication.translate("ReportCreate", u"Annotation", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("ReportCreate", u"SHOTCRETE THICKNESS DISTRIBUTION", None))
        self.chart_viewer.setText("")
    # retranslateUi

