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
from PySide6.QtWidgets import (QApplication, QDockWidget, QHeaderView, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QSplitter, QStatusBar, QToolBar,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1058, 753)
        MainWindow.setStyleSheet(u"/* =========================\n"
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
        self.menubar.setGeometry(QRect(0, 0, 1058, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        MainWindow.setMenuBar(self.menubar)

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
    # retranslateUi

