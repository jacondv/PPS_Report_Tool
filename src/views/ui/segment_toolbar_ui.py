# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'segment_toolbar.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
from . import resource_rc

class Ui_SegmentToolbar(object):
    def setupUi(self, SegmentToolbar):
        if not SegmentToolbar.objectName():
            SegmentToolbar.setObjectName(u"SegmentToolbar")
        SegmentToolbar.resize(160, 34)
        SegmentToolbar.setInputMethodHints(Qt.ImhNone)
        self.verticalLayout = QVBoxLayout(SegmentToolbar)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(SegmentToolbar)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 10, 2)
        self.btnSegmentIn = QPushButton(self.widget)
        self.btnSegmentIn.setObjectName(u"btnSegmentIn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSegmentIn.sizePolicy().hasHeightForWidth())
        self.btnSegmentIn.setSizePolicy(sizePolicy)
        self.btnSegmentIn.setMinimumSize(QSize(30, 30))
        self.btnSegmentIn.setMaximumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u":/icon/icon/crop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSegmentIn.setIcon(icon)

        self.horizontalLayout.addWidget(self.btnSegmentIn)

        self.btnClear = QPushButton(self.widget)
        self.btnClear.setObjectName(u"btnClear")
        sizePolicy.setHeightForWidth(self.btnClear.sizePolicy().hasHeightForWidth())
        self.btnClear.setSizePolicy(sizePolicy)
        self.btnClear.setMinimumSize(QSize(30, 30))
        self.btnClear.setMaximumSize(QSize(30, 30))
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/brush.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnClear.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btnClear)

        self.btnExportSelection = QPushButton(self.widget)
        self.btnExportSelection.setObjectName(u"btnExportSelection")
        sizePolicy.setHeightForWidth(self.btnExportSelection.sizePolicy().hasHeightForWidth())
        self.btnExportSelection.setSizePolicy(sizePolicy)
        self.btnExportSelection.setMinimumSize(QSize(30, 30))
        self.btnExportSelection.setMaximumSize(QSize(30, 30))
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/check.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnExportSelection.setIcon(icon2)

        self.horizontalLayout.addWidget(self.btnExportSelection)

        self.btnClose = QPushButton(self.widget)
        self.btnClose.setObjectName(u"btnClose")
        sizePolicy.setHeightForWidth(self.btnClose.sizePolicy().hasHeightForWidth())
        self.btnClose.setSizePolicy(sizePolicy)
        self.btnClose.setMinimumSize(QSize(30, 30))
        self.btnClose.setMaximumSize(QSize(30, 30))
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/multiplication.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnClose.setIcon(icon3)

        self.horizontalLayout.addWidget(self.btnClose)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(20, 20))
        self.label.setPixmap(QPixmap(u":/icon/icon/drag.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(SegmentToolbar)

        QMetaObject.connectSlotsByName(SegmentToolbar)
    # setupUi

    def retranslateUi(self, SegmentToolbar):
        SegmentToolbar.setWindowTitle(QCoreApplication.translate("SegmentToolbar", u"Dialog", None))
    # retranslateUi

