# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDockWidget, QHBoxLayout, QHeaderView,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QSplitter, QStatusBar, QToolBar, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(944, 761)
        MainWindow.setStyleSheet(u"border: 1px solid rgb(170, 170, 170);\n"
"")
        self.actionOpen_Job = QAction(MainWindow)
        self.actionOpen_Job.setObjectName(u"actionOpen_Job")
        icon = QIcon(QIcon.fromTheme(u"accessories-calculator"))
        self.actionOpen_Job.setIcon(icon)
        self.actionOpen_Job.setMenuRole(QAction.TextHeuristicRole)
        self.actionAlign_Cloud = QAction(MainWindow)
        self.actionAlign_Cloud.setObjectName(u"actionAlign_Cloud")
        self.actionAlign_Cloud.setMenuRole(QAction.NoRole)
        self.actionSegment = QAction(MainWindow)
        self.actionSegment.setObjectName(u"actionSegment")
        self.actionSegment.setMenuRole(QAction.NoRole)
        self.actionCreate_Report = QAction(MainWindow)
        self.actionCreate_Report.setObjectName(u"actionCreate_Report")
        self.actionCreate_Report.setMenuRole(QAction.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.cloud_viewer = QWidget(self.centralwidget)
        self.cloud_viewer.setObjectName(u"cloud_viewer")

        self.verticalLayout_4.addWidget(self.cloud_viewer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QDockWidget(MainWindow)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidget.setFeatures(QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(self.dockWidgetContents)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.treeJobData = QTreeWidget(self.splitter)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeJobData.setHeaderItem(__qtreewidgetitem)
        self.treeJobData.setObjectName(u"treeJobData")
        self.splitter.addWidget(self.treeJobData)
        self.listJobProperty = QListWidget(self.splitter)
        self.listJobProperty.setObjectName(u"listJobProperty")
        self.splitter.addWidget(self.listJobProperty)

        self.verticalLayout.addWidget(self.splitter)

        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.dockWidget)
        self.dockWidget_2 = QDockWidget(MainWindow)
        self.dockWidget_2.setObjectName(u"dockWidget_2")
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.verticalLayout_3 = QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.listStatus = QListWidget(self.dockWidgetContents_2)
        self.listStatus.setObjectName(u"listStatus")

        self.verticalLayout_3.addWidget(self.listStatus)

        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(Qt.BottomDockWidgetArea, self.dockWidget_2)
        self.dockWidget_3 = QDockWidget(MainWindow)
        self.dockWidget_3.setObjectName(u"dockWidget_3")
        self.dockWidget_3.setFeatures(QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.dockWidgetContents_3 = QWidget()
        self.dockWidgetContents_3.setObjectName(u"dockWidgetContents_3")
        self.verticalLayout_2 = QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.listReportInfo = QListWidget(self.dockWidgetContents_3)
        self.listReportInfo.setObjectName(u"listReportInfo")

        self.verticalLayout_2.addWidget(self.listReportInfo)

        self.dockWidget_3.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.dockWidget_3)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 944, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        MainWindow.setMenuBar(self.menubar)
        self.dockWidget_4 = QDockWidget(MainWindow)
        self.dockWidget_4.setObjectName(u"dockWidget_4")
        self.dockWidget_4.setFeatures(QDockWidget.DockWidgetFeatureMask)
        self.dockWidget_4.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.dockWidgetContents_8 = QWidget()
        self.dockWidgetContents_8.setObjectName(u"dockWidgetContents_8")
        self.horizontalLayout = QHBoxLayout(self.dockWidgetContents_8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.dockWidgetContents_8)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnSegmentIn = QPushButton(self.widget)
        self.btnSegmentIn.setObjectName(u"btnSegmentIn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnSegmentIn.sizePolicy().hasHeightForWidth())
        self.btnSegmentIn.setSizePolicy(sizePolicy1)
        self.btnSegmentIn.setMinimumSize(QSize(0, 32))

        self.horizontalLayout_2.addWidget(self.btnSegmentIn)

        self.btnSegmentOut = QPushButton(self.widget)
        self.btnSegmentOut.setObjectName(u"btnSegmentOut")
        sizePolicy1.setHeightForWidth(self.btnSegmentOut.sizePolicy().hasHeightForWidth())
        self.btnSegmentOut.setSizePolicy(sizePolicy1)
        self.btnSegmentOut.setMinimumSize(QSize(0, 32))
        self.btnSegmentOut.setFlat(False)

        self.horizontalLayout_2.addWidget(self.btnSegmentOut)

        self.btnExportSelected = QPushButton(self.widget)
        self.btnExportSelected.setObjectName(u"btnExportSelected")
        sizePolicy1.setHeightForWidth(self.btnExportSelected.sizePolicy().hasHeightForWidth())
        self.btnExportSelected.setSizePolicy(sizePolicy1)
        self.btnExportSelected.setMinimumSize(QSize(0, 32))

        self.horizontalLayout_2.addWidget(self.btnExportSelected)

        self.btnClear = QPushButton(self.widget)
        self.btnClear.setObjectName(u"btnClear")
        sizePolicy1.setHeightForWidth(self.btnClear.sizePolicy().hasHeightForWidth())
        self.btnClear.setSizePolicy(sizePolicy1)
        self.btnClear.setMinimumSize(QSize(0, 32))

        self.horizontalLayout_2.addWidget(self.btnClear)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.horizontalLayout.addWidget(self.widget)

        self.dockWidget_4.setWidget(self.dockWidgetContents_8)
        MainWindow.addDockWidget(Qt.TopDockWidgetArea, self.dockWidget_4)

        self.toolBar.addAction(self.actionOpen_Job)
        self.toolBar.addAction(self.actionAlign_Cloud)
        self.toolBar.addAction(self.actionSegment)
        self.toolBar.addAction(self.actionCreate_Report)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen_Job.setText(QCoreApplication.translate("MainWindow", u"Open Job", None))
        self.actionAlign_Cloud.setText(QCoreApplication.translate("MainWindow", u"Align Cloud", None))
        self.actionSegment.setText(QCoreApplication.translate("MainWindow", u"Segment", None))
        self.actionCreate_Report.setText(QCoreApplication.translate("MainWindow", u"Create Report", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.dockWidget_4.setWindowTitle("")
        self.btnSegmentIn.setText(QCoreApplication.translate("MainWindow", u"Segment In", None))
        self.btnSegmentOut.setText(QCoreApplication.translate("MainWindow", u"Segment Out", None))
        self.btnExportSelected.setText(QCoreApplication.translate("MainWindow", u"Export Selected", None))
        self.btnClear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
    # retranslateUi

