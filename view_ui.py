# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Root(object):
    def setupUi(self, Root):
        if not Root.objectName():
            Root.setObjectName(u"Root")
        Root.resize(483, 323)
        Root.setAcceptDrops(False)
        self.centralwidget = QWidget(Root)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.TemperatureConverter = QGroupBox(self.centralwidget)
        self.TemperatureConverter.setObjectName(u"TemperatureConverter")
        self.TemperatureConverter.setAutoFillBackground(False)
        self.TemperatureConverter.setStyleSheet(u"\n"
"background-color: rgb(0, 0, 200);")
        self.verticalLayout_4 = QVBoxLayout(self.TemperatureConverter)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lblInput = QLabel(self.TemperatureConverter)
        self.lblInput.setObjectName(u"lblInput")
        self.lblInput.setAutoFillBackground(False)
        self.lblInput.setFrameShape(QFrame.Shape.NoFrame)
        self.lblInput.setFrameShadow(QFrame.Shadow.Plain)
        self.lblInput.setTextFormat(Qt.TextFormat.PlainText)

        self.verticalLayout_4.addWidget(self.lblInput)

        self.entDegree = QLineEdit(self.TemperatureConverter)
        self.entDegree.setObjectName(u"entDegree")
        self.entDegree.setStyleSheet(u"color: rgb(White);")

        self.verticalLayout_4.addWidget(self.entDegree)


        self.verticalLayout.addWidget(self.TemperatureConverter)

        self.btnFrame = QFrame(self.centralwidget)
        self.btnFrame.setObjectName(u"btnFrame")
        self.btnFrame.setAutoFillBackground(False)
        self.btnFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.btnFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.btnFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.radC2F = QRadioButton(self.btnFrame)
        self.radC2F.setObjectName(u"radC2F")

        self.verticalLayout_3.addWidget(self.radC2F)

        self.radF2C = QRadioButton(self.btnFrame)
        self.radF2C.setObjectName(u"radF2C")

        self.verticalLayout_3.addWidget(self.radF2C)


        self.verticalLayout.addWidget(self.btnFrame)

        self.outFrame = QFrame(self.centralwidget)
        self.outFrame.setObjectName(u"outFrame")
        self.outFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.outFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.outFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lblResult = QLabel(self.outFrame)
        self.lblResult.setObjectName(u"lblResult")
        self.lblResult.setFrameShape(QFrame.Shape.Box)
        self.lblResult.setTextFormat(Qt.TextFormat.PlainText)
        self.lblResult.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lblResult)


        self.verticalLayout.addWidget(self.outFrame)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"CandFThermometer.jpg"))
        self.label.setScaledContents(True)
        self.label.setMargin(0)

        self.horizontalLayout.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.frame)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnConvert = QPushButton(self.frame_2)
        self.btnConvert.setObjectName(u"btnConvert")
        self.btnConvert.setBaseSize(QSize(18, 0))

        self.gridLayout.addWidget(self.btnConvert, 0, 0, 1, 1)

        self.btnClear = QPushButton(self.frame_2)
        self.btnClear.setObjectName(u"btnClear")
        self.btnClear.setBaseSize(QSize(18, 0))

        self.gridLayout.addWidget(self.btnClear, 0, 1, 1, 1)

        self.btnExit = QPushButton(self.frame_2)
        self.btnExit.setObjectName(u"btnExit")
        self.btnExit.setBaseSize(QSize(18, 0))

        self.gridLayout.addWidget(self.btnExit, 0, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        Root.setCentralWidget(self.centralwidget)

        self.retranslateUi(Root)

        self.btnConvert.setDefault(False)


        QMetaObject.connectSlotsByName(Root)
    # setupUi

    def retranslateUi(self, Root):
        Root.setWindowTitle(QCoreApplication.translate("Root", u"Temperature Converter", None))
        self.TemperatureConverter.setTitle(QCoreApplication.translate("Root", u"Temperature Converter", None))
        self.lblInput.setText(QCoreApplication.translate("Root", u"*Enter a Value:", None))
        self.entDegree.setInputMask("")
        self.entDegree.setText("")
        self.entDegree.setPlaceholderText(QCoreApplication.translate("Root", u"eg: 10, 20.2, 100", None))
        self.radC2F.setText(QCoreApplication.translate("Root", u"Celcius (C) to Farenheight (F)", None))
        self.radF2C.setText(QCoreApplication.translate("Root", u"Farenheight (F) to Celcius (C)", None))
        self.lblResult.setText(QCoreApplication.translate("Root", u"Result shows here", None))
        self.label.setText("")
        self.btnConvert.setText(QCoreApplication.translate("Root", u"Convert", None))
        self.btnClear.setText(QCoreApplication.translate("Root", u"Clear", None))
        self.btnExit.setText(QCoreApplication.translate("Root", u"Exit", None))
    # retranslateUi

