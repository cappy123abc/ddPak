# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Documents and Settings/cpusey/My Documents/Development/Python/ddPak/User Interface Files/PrefsNew.ui'
#
# Created: Wed Oct 31 13:40:37 2012
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(653, 507)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Resources/path2829.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("QDialog {\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.057, y2:0.0681818, stop:0 rgba(81, 81, 81, 151), stop:0.98 rgba(0, 0, 0, 255));\n"
"background-image: url(:/newPrefix/Resources/dinpattern-stripe.gif);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
" QTabWidget::pane { /* The tab widget frame */\n"
"     border-top: 2px solid #C2C7CB;\n"
" }\n"
"\n"
" QTabWidget::tab-bar {\n"
"     left: 5px; /* move to the right by 5px */\n"
" }\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
" QTabBar::tab {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"     border: 2px solid #C4C4C3;\n"
"     border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"     border-top-left-radius: 4px;\n"
"     border-top-right-radius: 4px;\n"
"     min-width: 8ex;\n"
"     padding: 2px;\n"
" }\n"
"\n"
"\n"
"\n"
"QTabBar::tab:selected,QTabBar::tab:hover{\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                 stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"}\n"
" QTabBar::tab:selected {\n"
"     border-color: #9B9B9B;\n"
"     border-bottom-color: #C2C7CB; /* same as pane color */\n"
" }\n"
"\n"
" QTabBar::tab:!selected {\n"
"     margin-top: 2px; /* make non-selected tabs look smaller */\n"
" }\n"
"\n"
"\n"
"\n"
"#tab,#tab_2,#tab_3 {\n"
"    font: 8pt \"Arial\";\n"
"background-color:  qlineargradient(spread:pad, x1:1, y1:1, x2:0.057, y2:0.0681818, stop:0 rgba(81, 81, 81, 151), stop:0.98 rgba(0, 0, 0, 255));\n"
"background-image: url(:/newPrefix/Resources/dinpattern-stripe.gif);\n"
"}\n"
"\n"
"QLabel,QRadioButton,QCheckBox {\n"
"\n"
"color:#f26522;font: 75 10pt \"Arial\";font-size:16px;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator {\n"
"width: 30px;\n"
"height: 30px;\n"
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
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(110, 450, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(40, 30, 581, 421))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(100, 270, 46, 14))
        self.label_6.setObjectName("label_6")
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(100, 140, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(100, 180, 81, 16))
        self.label_4.setObjectName("label_4")
        self.comboBox_2 = QtGui.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(190, 270, 69, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtGui.QComboBox(self.tab)
        self.comboBox_3.setGeometry(QtCore.QRect(330, 270, 69, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(100, 230, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(210, 40, 46, 21))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(350, 40, 46, 14))
        self.label_2.setObjectName("label_2")
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(100, 90, 81, 16))
        self.label_7.setObjectName("label_7")
        self.comboBox = QtGui.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(190, 140, 121, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_4 = QtGui.QComboBox(self.tab)
        self.comboBox_4.setGeometry(QtCore.QRect(330, 140, 121, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_5 = QtGui.QComboBox(self.tab)
        self.comboBox_5.setGeometry(QtCore.QRect(190, 180, 121, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_6 = QtGui.QComboBox(self.tab)
        self.comboBox_6.setGeometry(QtCore.QRect(330, 180, 121, 22))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_7 = QtGui.QComboBox(self.tab)
        self.comboBox_7.setGeometry(QtCore.QRect(190, 220, 121, 22))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_8 = QtGui.QComboBox(self.tab)
        self.comboBox_8.setGeometry(QtCore.QRect(330, 220, 121, 22))
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_9 = QtGui.QComboBox(self.tab)
        self.comboBox_9.setGeometry(QtCore.QRect(190, 90, 121, 22))
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_10 = QtGui.QComboBox(self.tab)
        self.comboBox_10.setGeometry(QtCore.QRect(330, 90, 121, 22))
        self.comboBox_10.setObjectName("comboBox_10")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.checkBox = QtGui.QCheckBox(self.tab_2)
        self.checkBox.setGeometry(QtCore.QRect(20, 40, 261, 17))
        self.checkBox.setObjectName("checkBox")
        self.frame = QtGui.QFrame(self.tab_2)
        self.frame.setGeometry(QtCore.QRect(10, 180, 261, 161))
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.label_9 = QtGui.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(40, 10, 181, 20))
        self.label_9.setObjectName("label_9")
        self.checkBox_2 = QtGui.QCheckBox(self.frame)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 50, 161, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtGui.QCheckBox(self.frame)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 80, 161, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtGui.QCheckBox(self.frame)
        self.checkBox_4.setGeometry(QtCore.QRect(30, 110, 161, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.comboBox_11 = QtGui.QComboBox(self.tab_2)
        self.comboBox_11.setGeometry(QtCore.QRect(150, 350, 131, 22))
        self.comboBox_11.setObjectName("comboBox_11")
        self.label_11 = QtGui.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(40, 350, 101, 20))
        self.label_11.setObjectName("label_11")
        self.pushButton_2 = QtGui.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 140, 94, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtGui.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(240, 110, 181, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtGui.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(430, 110, 94, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 140, 181, 20))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_12 = QtGui.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(30, 140, 201, 20))
        self.label_12.setObjectName("label_12")
        self.label_10 = QtGui.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(30, 110, 201, 20))
        self.label_10.setObjectName("label_10")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Edit Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Parity", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Baud Rate", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Data Bits", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Stop Bit", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Printer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Scale", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "Serial Port", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Dialog", "Serial Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("Dialog", "Operate in Cameraless Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Dialog", "Production Line Visibility", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_2.setText(QtGui.QApplication.translate("Dialog", "High Volume", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_3.setText(QtGui.QApplication.translate("Dialog", "Low Volume", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_4.setText(QtGui.QApplication.translate("Dialog", "Super Cell", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Dialog", "Printer Model", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Dialog", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("Dialog", "MountMES database file ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Dialog", "Folder for Database Backup", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Dialog", "General", None, QtGui.QApplication.UnicodeUTF8))

import myrc_rc
