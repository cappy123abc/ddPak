# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Documents and Settings/cpusey/My Documents/Development/Python/ddPakSQLite/User Interface Files/EditUsers.ui'
#
# Created: Tue Apr 10 08:36:27 2012
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_EditUsersDialog(object):
    def setupUi(self, EditUsersDialog):
        EditUsersDialog.setObjectName("EditUsersDialog")
        EditUsersDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        EditUsersDialog.resize(770, 358)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Resources/path2829.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EditUsersDialog.setWindowIcon(icon)
        EditUsersDialog.setStyleSheet("QDialog{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.057, y2:0.0681818, stop:0 rgba(81, 81, 81, 151), stop:0.98 rgba(0, 0, 0, 255));\n"
"\n"
"}\n"
"\n"
"QLabel {\n"
"\n"
"color:#f26522;font: 75 12pt \"Arial\";font-size:16px;\n"
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
"#pushButton:pressed,#pushButton_2:pressed{\n"
"\n"
"background: qradialgradient(cx: 0.4, cy: -0.1,\n"
"fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
"}\n"
"\n"
"#tableView {\n"
"    font: 10pt \"Arial\";\n"
"    background-color: rgb(255, 170, 255);\n"
"}")
        EditUsersDialog.setModal(True)
        self.gridLayout = QtGui.QGridLayout(EditUsersDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtGui.QLabel(EditUsersDialog)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.tableView = QtGui.QTableView(EditUsersDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton_2 = QtGui.QPushButton(EditUsersDialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(EditUsersDialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.retranslateUi(EditUsersDialog)
        QtCore.QMetaObject.connectSlotsByName(EditUsersDialog)

    def retranslateUi(self, EditUsersDialog):
        EditUsersDialog.setWindowTitle(QtGui.QApplication.translate("EditUsersDialog", "Edit Users", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("EditUsersDialog", "Press enter after changing field to commit changes", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("EditUsersDialog", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("EditUsersDialog", "Add", None, QtGui.QApplication.UnicodeUTF8))

import myrc_rc
