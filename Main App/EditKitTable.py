# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Documents and Settings/cpusey/My Documents/Development/Python/ddPakSQLite/User Interface Files/EditKitTable.ui'
#
# Created: Tue Apr 10 08:36:05 2012
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_EditKitTableDialog(object):
    def setupUi(self, EditKitTableDialog):
        EditKitTableDialog.setObjectName("EditKitTableDialog")
        EditKitTableDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        EditKitTableDialog.resize(736, 466)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Resources/path2829.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EditKitTableDialog.setWindowIcon(icon)
        EditKitTableDialog.setStyleSheet("#EditKitTableDialog{\n"
"    \n"
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
"\n"
"#tableView {\n"
"    font: 10pt \"Arial\";\n"
"    background-color: rgb(170, 255, 255);\n"
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
"QPushButton:hover {\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb);\n"
"}\n"
"\n"
"QPushButton:pressed  {\n"
"\n"
"background: qradialgradient(cx: 0.4, cy: -0.1,\n"
"fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
"}")
        EditKitTableDialog.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(EditKitTableDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(EditKitTableDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableView = QtGui.QTableView(EditKitTableDialog)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.pushButton = QtGui.QPushButton(EditKitTableDialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(EditKitTableDialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(EditKitTableDialog)
        QtCore.QMetaObject.connectSlotsByName(EditKitTableDialog)

    def retranslateUi(self, EditKitTableDialog):
        EditKitTableDialog.setWindowTitle(QtGui.QApplication.translate("EditKitTableDialog", "EditKitTable", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("EditKitTableDialog", "Press enter after changing field to commit changes", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("EditKitTableDialog", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("EditKitTableDialog", "Add", None, QtGui.QApplication.UnicodeUTF8))

import myrc_rc
