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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_SegmentToolbar(object):
    def setupUi(self, SegmentToolbar):
        if not SegmentToolbar.objectName():
            SegmentToolbar.setObjectName(u"SegmentToolbar")
        SegmentToolbar.resize(502, 32)
        SegmentToolbar.setInputMethodHints(Qt.ImhNone)
        self.verticalLayout = QVBoxLayout(SegmentToolbar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(SegmentToolbar)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.btnSegmentIn = QPushButton(self.widget)
        self.btnSegmentIn.setObjectName(u"btnSegmentIn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSegmentIn.sizePolicy().hasHeightForWidth())
        self.btnSegmentIn.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.btnSegmentIn)

        self.btnSegmentOut = QPushButton(self.widget)
        self.btnSegmentOut.setObjectName(u"btnSegmentOut")
        sizePolicy.setHeightForWidth(self.btnSegmentOut.sizePolicy().hasHeightForWidth())
        self.btnSegmentOut.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.btnSegmentOut)

        self.btnClear = QPushButton(self.widget)
        self.btnClear.setObjectName(u"btnClear")
        sizePolicy.setHeightForWidth(self.btnClear.sizePolicy().hasHeightForWidth())
        self.btnClear.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.btnClear)

        self.btnExportSelection = QPushButton(self.widget)
        self.btnExportSelection.setObjectName(u"btnExportSelection")
        sizePolicy.setHeightForWidth(self.btnExportSelection.sizePolicy().hasHeightForWidth())
        self.btnExportSelection.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.btnExportSelection)

        self.btnClose = QPushButton(self.widget)
        self.btnClose.setObjectName(u"btnClose")
        sizePolicy.setHeightForWidth(self.btnClose.sizePolicy().hasHeightForWidth())
        self.btnClose.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.btnClose)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(SegmentToolbar)

        QMetaObject.connectSlotsByName(SegmentToolbar)
    # setupUi

    def retranslateUi(self, SegmentToolbar):
        SegmentToolbar.setWindowTitle(QCoreApplication.translate("SegmentToolbar", u"Dialog", None))
        self.btnSegmentIn.setText(QCoreApplication.translate("SegmentToolbar", u"Segment In", None))
        self.btnSegmentOut.setText(QCoreApplication.translate("SegmentToolbar", u"Segment Out", None))
        self.btnClear.setText(QCoreApplication.translate("SegmentToolbar", u"Clear Segment", None))
        self.btnExportSelection.setText(QCoreApplication.translate("SegmentToolbar", u"Export Selection", None))
        self.btnClose.setText(QCoreApplication.translate("SegmentToolbar", u"X", None))
    # retranslateUi

