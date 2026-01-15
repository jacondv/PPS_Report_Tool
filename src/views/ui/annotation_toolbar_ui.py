# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'annotation_tollbar.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFontComboBox,
    QFrame, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
from . import resource_rc

class Ui_AnnotationToolbar(object):
    def setupUi(self, AnnotationToolbar):
        if not AnnotationToolbar.objectName():
            AnnotationToolbar.setObjectName(u"AnnotationToolbar")
        AnnotationToolbar.resize(488, 34)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AnnotationToolbar.sizePolicy().hasHeightForWidth())
        AnnotationToolbar.setSizePolicy(sizePolicy)
        AnnotationToolbar.setInputMethodHints(Qt.ImhNone)
        self.verticalLayout = QVBoxLayout(AnnotationToolbar)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(AnnotationToolbar)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 10, 2)
        self.btnSelect = QPushButton(self.widget)
        self.btnSelect.setObjectName(u"btnSelect")
        self.btnSelect.setMaximumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u":/icon/icon/cursor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSelect.setIcon(icon)

        self.horizontalLayout.addWidget(self.btnSelect)

        self.btnAddText = QPushButton(self.widget)
        self.btnAddText.setObjectName(u"btnAddText")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnAddText.sizePolicy().hasHeightForWidth())
        self.btnAddText.setSizePolicy(sizePolicy1)
        self.btnAddText.setMinimumSize(QSize(30, 30))
        self.btnAddText.setMaximumSize(QSize(30, 30))
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/text.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAddText.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btnAddText)

        self.cbbFont = QFontComboBox(self.widget)
        self.cbbFont.setObjectName(u"cbbFont")
        self.cbbFont.setMinimumSize(QSize(0, 30))
        self.cbbFont.setMaximumSize(QSize(100, 30))
        self.cbbFont.setCurrentIndex(9)

        self.horizontalLayout.addWidget(self.cbbFont)

        self.cbbFontSize = QComboBox(self.widget)
        self.cbbFontSize.addItem("")
        self.cbbFontSize.addItem("")
        self.cbbFontSize.addItem("")
        self.cbbFontSize.addItem("")
        self.cbbFontSize.addItem("")
        self.cbbFontSize.addItem("")
        self.cbbFontSize.addItem("")
        self.cbbFontSize.addItem("")
        self.cbbFontSize.addItem("")
        self.cbbFontSize.addItem("")
        self.cbbFontSize.addItem("")
        self.cbbFontSize.addItem("")
        self.cbbFontSize.addItem("")
        self.cbbFontSize.addItem("")
        self.cbbFontSize.addItem("")
        self.cbbFontSize.setObjectName(u"cbbFontSize")
        self.cbbFontSize.setMinimumSize(QSize(40, 30))
        self.cbbFontSize.setMaximumSize(QSize(40, 30))

        self.horizontalLayout.addWidget(self.cbbFontSize)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.btnAddLine = QPushButton(self.widget)
        self.btnAddLine.setObjectName(u"btnAddLine")
        sizePolicy1.setHeightForWidth(self.btnAddLine.sizePolicy().hasHeightForWidth())
        self.btnAddLine.setSizePolicy(sizePolicy1)
        self.btnAddLine.setMinimumSize(QSize(30, 30))
        self.btnAddLine.setMaximumSize(QSize(30, 30))
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/line.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAddLine.setIcon(icon2)

        self.horizontalLayout.addWidget(self.btnAddLine)

        self.cbbSize = QComboBox(self.widget)
        self.cbbSize.addItem("")
        self.cbbSize.addItem("")
        self.cbbSize.addItem("")
        self.cbbSize.addItem("")
        self.cbbSize.addItem("")
        self.cbbSize.setObjectName(u"cbbSize")
        self.cbbSize.setMinimumSize(QSize(30, 30))
        self.cbbSize.setMaximumSize(QSize(40, 30))

        self.horizontalLayout.addWidget(self.cbbSize)

        self.btnEdit = QPushButton(self.widget)
        self.btnEdit.setObjectName(u"btnEdit")
        sizePolicy1.setHeightForWidth(self.btnEdit.sizePolicy().hasHeightForWidth())
        self.btnEdit.setSizePolicy(sizePolicy1)
        self.btnEdit.setMinimumSize(QSize(30, 30))
        self.btnEdit.setMaximumSize(QSize(30, 30))
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/note.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnEdit.setIcon(icon3)

        self.horizontalLayout.addWidget(self.btnEdit)

        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.btnMove = QPushButton(self.widget)
        self.btnMove.setObjectName(u"btnMove")
        sizePolicy1.setHeightForWidth(self.btnMove.sizePolicy().hasHeightForWidth())
        self.btnMove.setSizePolicy(sizePolicy1)
        self.btnMove.setMinimumSize(QSize(30, 30))
        self.btnMove.setMaximumSize(QSize(30, 30))
        icon4 = QIcon()
        icon4.addFile(u":/icon/icon/move.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnMove.setIcon(icon4)

        self.horizontalLayout.addWidget(self.btnMove)

        self.btnDelete = QPushButton(self.widget)
        self.btnDelete.setObjectName(u"btnDelete")
        sizePolicy1.setHeightForWidth(self.btnDelete.sizePolicy().hasHeightForWidth())
        self.btnDelete.setSizePolicy(sizePolicy1)
        self.btnDelete.setMinimumSize(QSize(30, 30))
        self.btnDelete.setMaximumSize(QSize(30, 30))
        icon5 = QIcon()
        icon5.addFile(u":/icon/icon/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnDelete.setIcon(icon5)

        self.horizontalLayout.addWidget(self.btnDelete)

        self.btnClose = QPushButton(self.widget)
        self.btnClose.setObjectName(u"btnClose")
        sizePolicy1.setHeightForWidth(self.btnClose.sizePolicy().hasHeightForWidth())
        self.btnClose.setSizePolicy(sizePolicy1)
        self.btnClose.setMinimumSize(QSize(30, 30))
        self.btnClose.setMaximumSize(QSize(30, 30))
        icon6 = QIcon()
        icon6.addFile(u":/icon/icon/multiplication.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnClose.setIcon(icon6)

        self.horizontalLayout.addWidget(self.btnClose)

        self.line_3 = QFrame(self.widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_3)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(15, 15))
        self.label.setPixmap(QPixmap(u":/icon/icon/drag.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(AnnotationToolbar)

        self.cbbFontSize.setCurrentIndex(7)
        self.cbbSize.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AnnotationToolbar)
    # setupUi

    def retranslateUi(self, AnnotationToolbar):
        AnnotationToolbar.setWindowTitle(QCoreApplication.translate("AnnotationToolbar", u"Dialog", None))
        self.cbbFontSize.setItemText(0, QCoreApplication.translate("AnnotationToolbar", u"6", None))
        self.cbbFontSize.setItemText(1, QCoreApplication.translate("AnnotationToolbar", u"7", None))
        self.cbbFontSize.setItemText(2, QCoreApplication.translate("AnnotationToolbar", u"8", None))
        self.cbbFontSize.setItemText(3, QCoreApplication.translate("AnnotationToolbar", u"9", None))
        self.cbbFontSize.setItemText(4, QCoreApplication.translate("AnnotationToolbar", u"10", None))
        self.cbbFontSize.setItemText(5, QCoreApplication.translate("AnnotationToolbar", u"11", None))
        self.cbbFontSize.setItemText(6, QCoreApplication.translate("AnnotationToolbar", u"12", None))
        self.cbbFontSize.setItemText(7, QCoreApplication.translate("AnnotationToolbar", u"13", None))
        self.cbbFontSize.setItemText(8, QCoreApplication.translate("AnnotationToolbar", u"14", None))
        self.cbbFontSize.setItemText(9, QCoreApplication.translate("AnnotationToolbar", u"15", None))
        self.cbbFontSize.setItemText(10, QCoreApplication.translate("AnnotationToolbar", u"16", None))
        self.cbbFontSize.setItemText(11, QCoreApplication.translate("AnnotationToolbar", u"17", None))
        self.cbbFontSize.setItemText(12, QCoreApplication.translate("AnnotationToolbar", u"18", None))
        self.cbbFontSize.setItemText(13, QCoreApplication.translate("AnnotationToolbar", u"19", None))
        self.cbbFontSize.setItemText(14, QCoreApplication.translate("AnnotationToolbar", u"20", None))

        self.cbbSize.setItemText(0, QCoreApplication.translate("AnnotationToolbar", u"1", None))
        self.cbbSize.setItemText(1, QCoreApplication.translate("AnnotationToolbar", u"2", None))
        self.cbbSize.setItemText(2, QCoreApplication.translate("AnnotationToolbar", u"3", None))
        self.cbbSize.setItemText(3, QCoreApplication.translate("AnnotationToolbar", u"4", None))
        self.cbbSize.setItemText(4, QCoreApplication.translate("AnnotationToolbar", u"5", None))

    # retranslateUi

