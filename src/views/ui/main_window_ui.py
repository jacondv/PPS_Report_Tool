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
from PySide6.QtWidgets import (QApplication, QDockWidget, QHeaderView, QMainWindow,
    QSizePolicy, QSplitter, QStatusBar, QToolBar,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)
from . import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1055, 661)
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
        icon = QIcon()
        icon.addFile(u":/icon/icon/open-folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen_Job.setIcon(icon)
        self.actionOpen_Job.setMenuRole(QAction.TextHeuristicRole)
        self.actionCreate_Report = QAction(MainWindow)
        self.actionCreate_Report.setObjectName(u"actionCreate_Report")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/report.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCreate_Report.setIcon(icon1)
        self.actionCreate_Report.setMenuRole(QAction.NoRole)
        self.actionSegment = QAction(MainWindow)
        self.actionSegment.setObjectName(u"actionSegment")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/crop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSegment.setIcon(icon2)
        self.actionSegment.setMenuRole(QAction.NoRole)
        self.actionSet_Top_View = QAction(MainWindow)
        self.actionSet_Top_View.setObjectName(u"actionSet_Top_View")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/top.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSet_Top_View.setIcon(icon3)
        self.actionSet_Top_View.setMenuRole(QAction.NoRole)
        self.actionSet_Front_View = QAction(MainWindow)
        self.actionSet_Front_View.setObjectName(u"actionSet_Front_View")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icon/front.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSet_Front_View.setIcon(icon4)
        self.actionSet_Front_View.setMenuRole(QAction.NoRole)
        self.actionSet_Left_View = QAction(MainWindow)
        self.actionSet_Left_View.setObjectName(u"actionSet_Left_View")
        icon5 = QIcon()
        icon5.addFile(u":/icon/icon/left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSet_Left_View.setIcon(icon5)
        self.actionSet_Left_View.setMenuRole(QAction.NoRole)
        self.actionSet_Right_View = QAction(MainWindow)
        self.actionSet_Right_View.setObjectName(u"actionSet_Right_View")
        icon6 = QIcon()
        icon6.addFile(u":/icon/icon/right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSet_Right_View.setIcon(icon6)
        self.actionSet_Right_View.setMenuRole(QAction.NoRole)
        self.actionSet_Back_View = QAction(MainWindow)
        self.actionSet_Back_View.setObjectName(u"actionSet_Back_View")
        icon7 = QIcon()
        icon7.addFile(u":/icon/icon/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSet_Back_View.setIcon(icon7)
        self.actionSet_Back_View.setMenuRole(QAction.NoRole)
        self.actionSet_Bottom_View = QAction(MainWindow)
        self.actionSet_Bottom_View.setObjectName(u"actionSet_Bottom_View")
        icon8 = QIcon()
        icon8.addFile(u":/icon/icon/bottom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSet_Bottom_View.setIcon(icon8)
        self.actionSet_Bottom_View.setMenuRole(QAction.NoRole)
        self.actionSet_Isometric = QAction(MainWindow)
        self.actionSet_Isometric.setObjectName(u"actionSet_Isometric")
        icon9 = QIcon()
        icon9.addFile(u":/icon/icon/iso.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSet_Isometric.setIcon(icon9)
        self.actionSet_Isometric.setMenuRole(QAction.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.cloud_viewer = QWidget(self.centralwidget)
        self.cloud_viewer.setObjectName(u"cloud_viewer")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cloud_viewer.sizePolicy().hasHeightForWidth())
        self.cloud_viewer.setSizePolicy(sizePolicy)

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
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.splitter = QSplitter(self.dockWidgetContents)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.treeJobData = QTreeWidget(self.splitter)
        self.treeJobData.setObjectName(u"treeJobData")
        self.splitter.addWidget(self.treeJobData)

        self.verticalLayout.addWidget(self.splitter)

        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.dockWidget)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QToolBar(MainWindow)
        self.toolBar_2.setObjectName(u"toolBar_2")
        MainWindow.addToolBar(Qt.RightToolBarArea, self.toolBar_2)

        self.toolBar.addAction(self.actionOpen_Job)
        self.toolBar.addAction(self.actionSegment)
        self.toolBar.addAction(self.actionCreate_Report)
        self.toolBar_2.addAction(self.actionSet_Top_View)
        self.toolBar_2.addAction(self.actionSet_Front_View)
        self.toolBar_2.addAction(self.actionSet_Left_View)
        self.toolBar_2.addAction(self.actionSet_Back_View)
        self.toolBar_2.addAction(self.actionSet_Right_View)
        self.toolBar_2.addAction(self.actionSet_Bottom_View)
        self.toolBar_2.addAction(self.actionSet_Isometric)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen_Job.setText(QCoreApplication.translate("MainWindow", u"Open Job", None))
#if QT_CONFIG(shortcut)
        self.actionOpen_Job.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionCreate_Report.setText(QCoreApplication.translate("MainWindow", u"Create Report", None))
        self.actionSegment.setText(QCoreApplication.translate("MainWindow", u"Segment", None))
        self.actionSet_Top_View.setText(QCoreApplication.translate("MainWindow", u"Top", None))
#if QT_CONFIG(tooltip)
        self.actionSet_Top_View.setToolTip(QCoreApplication.translate("MainWindow", u"Top view", None))
#endif // QT_CONFIG(tooltip)
        self.actionSet_Front_View.setText(QCoreApplication.translate("MainWindow", u"Front", None))
        self.actionSet_Left_View.setText(QCoreApplication.translate("MainWindow", u"Left", None))
        self.actionSet_Right_View.setText(QCoreApplication.translate("MainWindow", u"Right", None))
        self.actionSet_Back_View.setText(QCoreApplication.translate("MainWindow", u"Back", None))
#if QT_CONFIG(tooltip)
        self.actionSet_Back_View.setToolTip(QCoreApplication.translate("MainWindow", u"Back", None))
#endif // QT_CONFIG(tooltip)
        self.actionSet_Bottom_View.setText(QCoreApplication.translate("MainWindow", u"Bottom", None))
#if QT_CONFIG(tooltip)
        self.actionSet_Bottom_View.setToolTip(QCoreApplication.translate("MainWindow", u"Bottom", None))
#endif // QT_CONFIG(tooltip)
        self.actionSet_Isometric.setText(QCoreApplication.translate("MainWindow", u"ISO", None))
#if QT_CONFIG(tooltip)
        self.actionSet_Isometric.setToolTip(QCoreApplication.translate("MainWindow", u"Isometric", None))
#endif // QT_CONFIG(tooltip)
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.toolBar_2.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_2", None))
    # retranslateUi

