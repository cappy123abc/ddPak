# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Documents and Settings/cpusey/My Documents/Development/Python/ddPakSQLite/User Interface Files/login.ui'
#
# Created: Thu Oct 06 15:31:41 2011
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_loginDialog(object):
    def setupUi(self, loginDialog):
        loginDialog.setObjectName("loginDialog")
        loginDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        loginDialog.resize(400, 400)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginDialog.sizePolicy().hasHeightForWidth())
        loginDialog.setSizePolicy(sizePolicy)
        loginDialog.setMinimumSize(QtCore.QSize(400, 400))
        loginDialog.setMaximumSize(QtCore.QSize(425, 425))
        loginDialog.setBaseSize(QtCore.QSize(400, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resources/path2829.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        loginDialog.setWindowIcon(icon)
        loginDialog.setStyleSheet("#loginDialog{\n"
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
"#pushButton,#pushButton_2{\n"
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
"#pushButton:hover,#pushButton_2:hover{\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb);\n"
"}\n"
"\n"
"#pushButton:pressed,#pushButton_2:pressed {\n"
"\n"
"background: qradialgradient(cx: 0.4, cy: -0.1,\n"
"fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
"}")
        loginDialog.setModal(True)
        self.gridLayout_4 = QtGui.QGridLayout(loginDialog)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.widget = QtGui.QWidget(loginDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(425, 425))
        self.widget.setBaseSize(QtCore.QSize(425, 425))
        self.widget.setStyleSheet("None")
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtGui.QGridLayout(self.widget)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtGui.QSpacerItem(20, 139, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 0, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 1, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(101, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 2, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.widget)
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 1, 1, 2)
        spacerItem2 = QtGui.QSpacerItem(101, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 2, 3, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 138, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 3, 2, 1, 1)
        self.gridLayout_4.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(loginDialog)
        QtCore.QMetaObject.connectSlotsByName(loginDialog)
        loginDialog.setTabOrder(self.lineEdit, self.lineEdit_2)

    def retranslateUi(self, loginDialog):
        loginDialog.setWindowTitle(QtGui.QApplication.translate("loginDialog", "Pak Login", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("loginDialog", "User Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("loginDialog", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("loginDialog", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("loginDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

import myrc_rc
