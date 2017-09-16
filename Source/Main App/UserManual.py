# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserManual.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets 
import myrc_rc

class Ui_UMDialog(object):
    def setupUi(self, UMDialog):
        UMDialog.setObjectName("UMDialog")
        UMDialog.resize(835, 661)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Resources/path2829.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UMDialog.setWindowIcon(icon)
        self.webView = QtWebKitWidgets.QWebView(UMDialog)
        self.webView.setGeometry(QtCore.QRect(29, 20, 791, 581))
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.pushButton = QtWidgets.QPushButton(UMDialog)
        self.pushButton.setGeometry(QtCore.QRect(390, 620, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(UMDialog)
        QtCore.QMetaObject.connectSlotsByName(UMDialog)

    def retranslateUi(self, UMDialog):
        _translate = QtCore.QCoreApplication.translate
        UMDialog.setWindowTitle(_translate("UMDialog", "User Manual"))
        self.pushButton.setText(_translate("UMDialog", "Close"))

