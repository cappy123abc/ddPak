# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Documents and Settings/cpusey/My Documents/Development/Python/ddPak/User Interface Files/ProductionReporting.ui'
#
# Created: Fri Sep 21 15:27:14 2012
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ProductionReportDialog(object):
    def setupUi(self, ProductionReportDialog):
        ProductionReportDialog.setObjectName("ProductionReportDialog")
        ProductionReportDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        ProductionReportDialog.resize(1037, 806)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ProductionReportDialog.sizePolicy().hasHeightForWidth())
        ProductionReportDialog.setSizePolicy(sizePolicy)
        ProductionReportDialog.setMinimumSize(QtCore.QSize(400, 400))
        ProductionReportDialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        ProductionReportDialog.setBaseSize(QtCore.QSize(400, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Resources/path2829.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ProductionReportDialog.setWindowIcon(icon)
        ProductionReportDialog.setStyleSheet("#loginDialog{\n"
"background-image: url(:/newPrefix/Resources/dinpattern-stripe.gif);\n"
"}\n"
"\n"
"#label,#label_2,#label_4{color:#f26522;}\n"
"\n"
"\n"
"\n"
"#widget{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.057, y2:0.0681818, stop:0 rgba(81, 81, 81, 151), stop:0.98 rgba(0, 0, 0, 255));\n"
"\n"
"}\n"
"#label_3 {\n"
"\n"
"\n"
"    color: rgb(255, 0, 0);\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"    \n"
"    \n"
"font: 75 8pt \"Arial Black\";\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 11px;\n"
"padding: 5px;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
"min-width: 80px;\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"background: qradialgradient(cx: 0.4, cy: -0.1,\n"
"fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
"}")
        ProductionReportDialog.setModal(True)
        self.gridLayout_2 = QtGui.QGridLayout(ProductionReportDialog)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtGui.QWidget(ProductionReportDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(425, 425))
        self.widget.setBaseSize(QtCore.QSize(425, 425))
        self.widget.setStyleSheet("None")
        self.widget.setObjectName("widget")
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(179, 216, 16, 16))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtGui.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(370, 760, 102, 29))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtGui.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(510, 760, 102, 29))
        self.pushButton_4.setObjectName("pushButton_4")
        self.layoutWidget = QtGui.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(21, 21, 214, 241))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.calendarWidget = QtGui.QCalendarWidget(self.layoutWidget)
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setVerticalHeaderFormat(QtGui.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setDateEditAcceptDelay(750)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtGui.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.textEdit = QtGui.QTextEdit(self.widget)
        self.textEdit.setGeometry(QtCore.QRect(283, 53, 531, 691))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtGui.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(640, 760, 102, 29))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(ProductionReportDialog)
        QtCore.QMetaObject.connectSlotsByName(ProductionReportDialog)

    def retranslateUi(self, ProductionReportDialog):
        ProductionReportDialog.setWindowTitle(QtGui.QApplication.translate("ProductionReportDialog", "Production Reporting", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("ProductionReportDialog", "Print", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("ProductionReportDialog", "E-mail", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ProductionReportDialog", "Production Date", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("ProductionReportDialog", "Create Report", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("ProductionReportDialog", "Exit", None, QtGui.QApplication.UnicodeUTF8))

import myrc_rc
