# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Documents and Settings/cpusey/My Documents/Development/Python/ddPak/User Interface Files/UserManual.ui'
#
# Created: Fri Sep 21 15:21:01 2012
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_UMDialog(object):
    def setupUi(self, UMDialog):
        UMDialog.setObjectName("UMDialog")
        UMDialog.resize(835, 661)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Resources/path2829.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UMDialog.setWindowIcon(icon)
        self.webView = QtWebKit.QWebView(UMDialog)
        self.webView.setGeometry(QtCore.QRect(29, 20, 791, 581))
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.pushButton = QtGui.QPushButton(UMDialog)
        self.pushButton.setGeometry(QtCore.QRect(390, 620, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(UMDialog)
        QtCore.QMetaObject.connectSlotsByName(UMDialog)

    def retranslateUi(self, UMDialog):
        UMDialog.setWindowTitle(QtGui.QApplication.translate("UMDialog", "User Manual", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("UMDialog", "Close", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
import myrc_rc
