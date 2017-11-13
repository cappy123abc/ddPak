#!/usr/bin/python
import sys
import os
import configparser
import socket
import datetime
import subprocess
import serial
import shutil
import hashlib
import fnmatch
from serial.tools.list_ports import *
from PyQt5 import QtCore, QtGui, QtPrintSupport, QtSql, QtWidgets 
from PyQt5.QAxContainer import QAxWidget
from ScannerInterface import Ui_MainWindow
from login import Ui_loginDialog
from PrefsNew import Ui_Dialog
from EditKitTable import Ui_EditKitTableDialog
from about import Ui_aboutDialog
from ProductionReporting import Ui_ProductionReportDialog
from EditUsers import Ui_EditUsersDialog
from UserManual import Ui_UMDialog


        
try:
    QString = unicode
except NameError:
    # Python 3
    QString = str

class Login (QtWidgets.QDialog) :
    
    def __init__ (self) :
        
        QtWidgets.QDialog.__init__(self)

        # Set up the user interface from Designer.
        self.ui = Ui_loginDialog()
        self.ui.setupUi(self)
            
        # Connect up the Signals 
        self.ui.pushButton.clicked.connect(self.validateUser)
        self.ui.pushButton_2.clicked.connect(self.close)
        
    def validateUser(self):
        

        if db.open() :

            if self.ui.label.text() == 'Password' :
                self.ui.lineEdit.setEchoMode(2)
                password = self.ui.lineEdit.text()
                stored_password = config.get('general','admin_password')
                if password == stored_password :
                    self.ui.label_3.clear()
                    self.accept()
                else :
                    self.ui.lineEdit.clear()  
                    self.ui.label_3.setText('Incorrect password.')
            else :
                username = self.ui.lineEdit.text()
                query = QtSql.QSqlQuery(db)
                query.exec_(''' Select initials from users where user_id = '%s'   ''' % username)      
                query.next()
                
                if  query.isValid() :
                    ddpak.ui.label_19.setText(query.value(0))
                    ddpak.weighStart()
                    self.accept()
      
                else:
                    self.ui.label_3.setText("User doesn't exist.")

        
        else :
            self.ui.label_3.setText('Database does not exist or can\'t connect!')
            return false
        
class EditKitTable(QtWidgets.QDialog):

    def __init__(self):
    
        QtWidgets.QDialog.__init__(self)
        self.ui = Ui_EditKitTableDialog()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.insRow)
        self.ui.pushButton.clicked.connect(self.close)

    def setupDatabaseViews (self) :
        
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable("item_master")
        self.model.sort(0,0)
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()    
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setSelectionMode(QtWidgets.QTableView.SingleSelection)
        self.ui.tableView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        
    def insRow(self) :
        
        row = self.model.rowCount()
        self.model.insertRows(row,1)
        index = self.model.index(row,0)
        self.ui.tableView.setCurrentIndex(index)
        self.ui.tableView.edit(index)
        
class EditUsers(QtWidgets.QDialog) :
    
    def __init__(self) :
        
        QtWidgets.QDialog.__init__(self)
        self.ui = Ui_EditUsersDialog()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.insRow)
        self.ui.pushButton_2.clicked.connect(self.close)
        
    def setupDatabaseViews (self, dbname = '') :
        
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable("users")
        self.model.select()    
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setSelectionMode(QtWidgets.QTableView.SingleSelection)
               
    def insRow(self) :
        
        row = self.model.rowCount()
        self.model.insertRows(row,1)
        index = self.model.index(row,0)
        self.ui.tableView.setCurrentIndex(index)
        self.ui.tableView.edit(index)
        
        
        
class ChangePrefs (QtWidgets.QDialog):

    def __init__ (self) :
    
        QtWidgets.QDialog.__init__(self)
        
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.updatePreferences)
        self.ui.buttonBox.rejected.connect(self.close)
        self.ui.pushButton.clicked.connect(self.getDirectory)
        self.ui.pushButton_2.clicked.connect(self.getMountsMESFile)
        self.ui.pushButton_3.clicked.connect(self.getPSRemoteExe)
        
    def loadConfig (self):
        
        """ Read and display config settings """
    

        # need following line so that app can find config file with a relative path 
        #self.ini_file = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "ddPak.ini") blah
        

        available_ports = serial.tools.list_ports.comports()
        for port in available_ports :
            self.ui.comboBox_9.addItem(port[0])
            self.ui.comboBox_10.addItem(port[0])
            
        self.ui.comboBox.addItems (('50', '75', '110', '134', '150','200', '300', '600', '1200', '1800', '2400', '4800', '9600', '19200', '38400', '57600', '115200'))
        self.ui.comboBox_4.addItems (('50', '75', '110', '134', '150','200', '300', '600', '1200', '1800', '2400', '4800', '9600', '19200', '38400', '57600', '115200'))
        self.ui.comboBox_5.addItems(('5', '6', '7',  '8'))
        self.ui.comboBox_6.addItems(('5', '6', '7',  '8'))
        self.ui.comboBox_7.addItems(('1', '1.5', '2'))
        self.ui.comboBox_8.addItems(('1', '1.5', '2'))
        self.ui.comboBox_2.addItems(('Odd', 'Even', 'None'))
        self.ui.comboBox_3.addItems(('Odd', 'Even', 'None'))
        self.ui.comboBox_11.addItems(('Zebra 105SL', 'Zebra LP2844'))
        self.ui.comboBox_9.setCurrentIndex(self.ui.comboBox_9.findText(config.get('printerport','portnumber')))
        self.ui.comboBox_10.setCurrentIndex(self.ui.comboBox_10.findText(config.get('scaleport','portnumber')))
        self.ui.comboBox.setCurrentIndex(self.ui.comboBox.findText(config.get('printerport','baud')))
        self.ui.comboBox_4.setCurrentIndex(self.ui.comboBox_4.findText(config.get('scaleport','baud')))
        self.ui.comboBox_5.setCurrentIndex(self.ui.comboBox_5.findText(config.get('printerport','databits')))
        self.ui.comboBox_6.setCurrentIndex(self.ui.comboBox_6.findText(config.get('scaleport','databits')))
        self.ui.comboBox_7.setCurrentIndex(self.ui.comboBox_7.findText(config.get('printerport','stopbit')))
        self.ui.comboBox_8.setCurrentIndex(self.ui.comboBox_8.findText(config.get('scaleport','stopbit')))
        self.ui.comboBox_2.setCurrentIndex(self.ui.comboBox_2.findText(config.get('printerport','parity')))
        self.ui.comboBox_3.setCurrentIndex(self.ui.comboBox_3.findText(config.get('scaleport','parity')))
        self.ui.checkBox.setCheckState(config.getboolean('general','cameramode',fallback=True))
        self.ui.lineEdit.setText(config.get('general','dbbackuppath',fallback=''))
        self.ui.lineEdit_2.setText(config.get('general','mountsmesdb',fallback=''))
        self.ui.lineEdit_3.setText(config.get('general','psremote_path',fallback=''))
        self.ui.speedSlider.setSliderPosition(config.getint('general','printer_speed',fallback=2))

        if config.getboolean('general', 'highvolume') :  self.ui.checkBox_2.setCheckState(2)
        if config.getboolean('general', 'lowvolume') :  self.ui.checkBox_3.setCheckState(2)
        if config.getboolean('general', 'supercell') :  self.ui.checkBox_4.setCheckState(2)


    def updatePreferences(self) :
        
        """ Write new preferences to config file and restart weighing operation"""
        
        config.set('printerport', 'portnumber', self.ui.comboBox_9.currentText())
        config.set('scaleport','portnumber', self.ui.comboBox_10.currentText())
        config.set('printerport','baud', self.ui.comboBox.currentText())
        config.set('scaleport','baud', self.ui.comboBox_4.currentText())
        config.set('printerport','databits', self.ui.comboBox_5.currentText())
        config.set('scaleport','databits', self.ui.comboBox_6.currentText())
        config.set('printerport','stopbit', self.ui.comboBox_7.currentText())
        config.set('scaleport','stopbit', self.ui.comboBox_8.currentText())
        config.set('printerport','parity', self.ui.comboBox_2.currentText())
        config.set('scaleport','parity', self.ui.comboBox_3.currentText())
        config.set('general','cameramode', str(self.ui.checkBox.isChecked()))
        config.set('general','dbbackuppath', self.ui.lineEdit.text())
        config.set('general','mountsmesdb', self.ui.lineEdit_2.text())
        config.set('general','psremote_path', self.ui.lineEdit_3.text())
        config.set('general','printer_speed', str(self.ui.speedSlider.value()))
        if self.ui.checkBox_2.isChecked() :  config.set('general','highvolume', '1')
        else : config.set('general','highvolume', '0')
        if self.ui.checkBox_3.isChecked() :  config.set('general','lowvolume', '1')
        else : config.set('general','lowvolume', '0')
        if self.ui.checkBox_4.isChecked() :  config.set('general','supercell', '1')
        else : config.set('general','supercell', '0')

        config.write(open(config_path, 'w'))
        ddpak.weighStart()
        
        
    def getDirectory(self) :
        
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, 'Open file','/home')
        self.ui.lineEdit.setText(str(directory))
    
    def getMountsMESFile(self) :
        
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Locate MountsMES','/home', 'Access database files (*.mdb)')[0]
        self.ui.lineEdit_2.setText(str(filename))

    def getPSRemoteExe(self) :
        
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Locate PSRemote','/home', 'Executable Files (*.exe)')[0]
        self.ui.lineEdit_3.setText(str(filename))
        
class ProductionReporting(QtWidgets.QDialog):

    def __init__(self):
    
        QtWidgets.QDialog.__init__(self)
        self.ui = Ui_ProductionReportDialog()
        self.ui.setupUi(self)  
        
        self.ui.pushButton.clicked.connect(self.generateReport)
        self.ui.pushButton_2.clicked.connect(self.close)
        self.ui.pushButton_3.clicked.connect(self.printReport)
        #self.connect(self.ui.pushButton_4, QtCore.SIGNAL('clicked()'),self.emailReport)
        
    def generateReport(self):
        
        ''' THis generates an ugly textbox report, would be nice to use reportlab or something '''
        
        production_date = self.ui.calendarWidget.selectedDate().toPyDate().isoformat()
        
        self.ui.textEdit.clear()


        import pdb; pdb.set_trace()
        self.loadPictureData(production_date,ddpak.host_name)
        self.ui.textEdit.insertPlainText('Kits packed on Workstation: ' + ddpak.host_name + ' on Date: ' + production_date + '\n\n' ) 
        query2 = QtSql.QSqlQuery()
        strsql = """Select distinct(substr(label_id,13,length(label_id)-12)), count(substr(label_id,13,length(label_id)-12)) 
                    from labels_printed where DATE(date_printed) = '%s'
                    and pack_station_host_name = '%s'
                    and label_delete = 'false'
                    group by substr(label_id,13,length(label_id)-12)""" % (production_date, ddpak.host_name) 
        query2.exec_(strsql)
        while (query2.next()) :
            self.ui.textEdit.insertPlainText(str(query2.value(0)) + '   (' + str(query2.value(1)) + ')\n')
            
        query2.exec_("select label_id from labels_printed where label_delete = 'true' and DATE(date_printed) = '%s'" % production_date) 
        self.ui.textEdit.insertPlainText('\n\nLabels deleted:   \n\n')
        while (query2.next()) :
            self.ui.textEdit.insertPlainText(str(query2.value(0)) + '\n')
            
        query2.exec_("select label_id from labels_printed where label_reprint = 'true' and DATE(date_printed) = '%s'" % production_date) 
        self.ui.textEdit.insertPlainText('\n\nLabels reprinted:   \n\n')
        while (query2.next()) :
            self.ui.textEdit.insertPlainText(str(query2.value(0)) + '\n')
            
            
        success = query2.exec_("select photo_id from photo_temp left outer join labels_printed on photo_id = label_id where label_id is null ")
        self.ui.textEdit.insertPlainText('\n\nPhotos with no corresponding label:   \n\n')
        if success :
          while (query2.next()) :
              self.ui.textEdit.insertPlainText(str(query2.value(0)) + '\n')
        else : self.ui.textEdit.insertPlainText('Query failed \n')
        strsql = """select label_id from  labels_printed left outer join photo_temp on  photo_id = label_id
        where photo_id is null and DATE(date_printed) = '%s''""" % production_date
        success = query2.exec_("""select label_id from  labels_printed left outer join photo_temp on  photo_id = label_id
        where photo_id is null and DATE(date_printed) = '%s'""" % production_date)
        self.ui.textEdit.insertPlainText('\n\nLabels with no corresponding photo:   \n\n')
        if success :
          while (query2.next()) :
              self.ui.textEdit.insertPlainText(str(query2.value(0)) + '\n')
        else : self.ui.textEdit.insertPlainText('Query failed \n')
        self.ui.textEdit.insertPlainText('**************************************************************************************') 
        
            
    def loadPictureData(self,date ='',hostname = '') :
        """ Retrieve photo names from PSRemote directory"""
        try :
            picpath = "//%s/PSRemote/%s" % (hostname,date)
            pic_ids = os.listdir(picpath)
            query = QtSql.QSqlQuery()
            query.exec_("delete  from photo_temp")
            for pic in pic_ids :
                if pic.endswith('jpg') :  # Don't store thumbs.db etc.
                    strsql = "insert into photo_temp values ('%s')" % pic.split('_')[0]
                    query.exec_(strsql)

        except:
            
            return "No photo info available"
                
                
    def printReport(self) :
        
        printer = QtPrintSupport.QPrinter()
        printDialog = QtPrintSupport.QPrintDialog(printer)
        if (printDialog.exec_() == QtWidgets.QDialog.Accepted) :               
            self.ui.textEdit.print_(printer)
    
            
    def emailReport (self) :
        
        return
        
class AboutBox (QtWidgets.QDialog) :
    
    def __init__(self):

        QtWidgets.QDialog.__init__(self)
        self.about_boxui = Ui_aboutDialog()
        self.about_boxui.setupUi(self)
        
        self.about_boxui.pushButton_2.clicked.connect(self.close)
        
class UserManual (QtWidgets.QDialog) :
    
    def __init__ (self) :
        
        QtWidgets.QDialog.__init__(self)
        self.ui = Ui_UMDialog()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.close)
        #help_file = os.path.join(application_path, 'C:/Users/caleb//User\ Manual/ddPak\ User\ Manual.html')
        help_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "User Manual/ddPak User Manual.html"))
        print (help_file)
        self.ui.webView.load(QtCore.QUrl.fromLocalFile(help_file))
        self.ui.webView.show()
        
        
class MyDelegate (QtWidgets.QItemDelegate):

    """ This adds a combo box as item selector in kits on carriers table view. """ 
        
             
    def __init__ (self, parent = None):
                    
        QtWidgets.QItemDelegate.__init__(self,parent)
    
    def createEditor(self, parent, option, index):
        if index.column() == 0 :
            editor = QtWidgets.QComboBox( parent )
            query = QtSql.QSqlQuery()
            query.exec_("""Select item_id from item_master where prd_line in (%s)  order by item_id""" % ddpak.production_reportingd_line_viz) 
            while (query.next()) :
                item = query.value(0)           
                editor.addItem(item)
        else:
            return QtWidgets.QItemDelegate.createEditor(self, parent, option, index)

        return editor


    def setModelData(self, editor, model, index):
        
        if index.column() == 0 :
            value = editor.currentIndex()
            model.setData( index, editor.itemData( value, QtCore.Qt.DisplayRole ) )
            
        else :
            QtWidgets.QItemDelegate.setModelData(self, editor, model, index)
             
        
        
        

class DDPak(QtWidgets.QMainWindow) :
    

    def __init__ (self) :
        
        """Primary user interface window"""
        
        
        QtWidgets.QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        if not self.ui.pdf_view.setControl("Adobe PDF Reader") :
            QtWidgets.QMessageBox.critical(self, "Error", "Make sure you have Adobe Reader (and its ActiveX) installed!")
    
        #Create serial port objects, timer, etc. todo --- add exception handling when opening serial ports.
        


        config.read(config_path)
        self.timer = QtCore.QTimer()
        self.serial_no = ''
        self.host_name = socket.gethostname()
        self.scaleport = serial.Serial()
        self.printerport = serial.Serial()
        self.signalMapper = QtCore.QSignalMapper(self)
        
        # Create all window objects that will be needed
        
        self.about_box = AboutBox()
        self.change_preferences = ChangePrefs()
        self.edit_kit_table = EditKitTable()
        self.production_reporting = ProductionReporting()
        self.edit_user = EditUsers()
        self.user_manual = UserManual()
       
        # Connect up the Signals and Slots (Events and Event Handlers) for the UI
        self.ui.pushButton_4.clicked.connect(self.takePic)
        self.ui.pushButton_2.clicked.connect(self.printLabel)
        self.timer.timeout.connect(self.checkScale)
        self.ui.actionPreferences.triggered.connect(self.editPref)
        self.ui.actionExit.triggered.connect(QtWidgets.QApplication.closeAllWindows)
        self.ui.actionKit_Table.triggered.connect(self.editKitTable)
        self.ui.actionEdit_Users.triggered.connect(self.editUsers)
        self.ui.actionManual.triggered.connect(self.user_manual.show)
        self.ui.actionProduction_Reporting.triggered.connect(self.prodReporting)
        self.ui.actionAbout_DDPak.triggered.connect(self.showAbout)
        self.ui.pushButton.clicked.connect(self.setTare)
        self.ui.pushButton.clicked.connect(self.zeroScale)
        self.ui.pushButton_5.clicked.connect(self.deleteLabels)
        self.ui.pushButton_6.clicked.connect(self.reprintLabel)
        self.ui.pushButton_8.clicked.connect(self.selectKit)
        self.ui.pushButton_7.clicked.connect(self.addKit)
        self.ui.radioButton.clicked.connect(self.setupCarriersView)
        self.ui.radioButton_2.clicked.connect(self.setupCarriersView)
        
        
        # Set up the MountsMES database connection
        
        self.MESdb = QtSql.QSqlDatabase.addDatabase("QODBC", "mountsMES_db")
        self.MESdb_file = config.get("general", "mountsmesdb")
        self.MESdb.setDatabaseName("Driver={Microsoft Access Driver (*.mdb)};FIL={MS Access};DBQ=%s"  % self.MESdb_file )
        

        self.ui.radioButton.setChecked(1)
        
        # initialize test switch states
        
        self.label_printed = False
        self.backupDatabase()
        self.timestamp = datetime.datetime.now()

        
    def weighStart (self) :
        
        """This function starts or restarts the weighing based on preferences"""
        
        config.read(config_path)
        self.camera_mode = config.getboolean('general','cameramode')
        self.production_reportingd_line_viz = ''
        if config.getboolean('general','highvolume')  : self.production_reportingd_line_viz += '3,'
        if config.getboolean('general','lowvolume')  : self.production_reportingd_line_viz += '1,'
        if config.getboolean('general','supercell')  : self.production_reportingd_line_viz += '2,' 
        self.production_reportingd_line_viz = self.production_reportingd_line_viz.rstrip( ',')
        self.setupCarriersView()
        self.setupLabelsPrintedView()

        
        try:
            
            self.printerport.port = config.get('printerport','portnumber')
            self.printerport.baudrate = config.getint('printerport','baud')
            self.printerport.bytesize = config.getint('printerport','databits')
            self.printerport.stopbits = config.getfloat('printerport','stopbit')
            self.printerport.parity = config.get('printerport','parity')[:1]
            if not(self.printerport.isOpen()) : self.printerport.open()
            
        except:
            
            self.ui.plainTextEdit.appendPlainText('Cannot connect to printer, check settings.')
            
        try:
            
            self.scaleport.port = config.get('scaleport','portnumber')
            self.scaleport.baudrate = config.getint('scaleport','baud')
            self.scaleport.bytesize = config.getint('scaleport','databits')
            self.scaleport.stopbits = config.getfloat('scaleport','stopbit')
            self.scaleport.parity = config.get('scaleport','parity')[:1]
            #self.scaleport.parity = serial.PARITY_EVEN
            if not(self.scaleport.isOpen()) : self.scaleport.open()
            
        except :
            
            self.ui.plainTextEdit.appendPlainText('Cannot connect to scale, check settings.')
  
        
        if self.scaleport.isOpen() : self.timer.start()
        #self.timer.start()
        return
        
    def backupDatabase (self) :
        """ Backs up database when ddpak is started."""
        
        self.db_backup_dir = config.get('general','dbbackuppath')
        try: shutil.copy(db_file , self.db_backup_dir + '/' + self.host_name  + '.sqlite' )
        except Exception as inst : self.ui.plainTextEdit.appendPlainText('Database file not backed up! %s' % inst)
        
            
        
               
    def setupCarriersView (self) :
  

        # set up kits on carriers table view, depending on carrierviewmode
        # from radio buttons we'll interface with MountsMES(access) or the
        # internal SQLite database.
        # TODO view mode can be selected from ini file or radio button --- FIX!

        if self.ui.radioButton.isChecked()  :
            self.MESdb.open()
            self.modelpq = QtSql.QSqlRelationalTableModel(self, self.MESdb)
            self.modelpq.setTable("production_queue")
            self.modelpq.setFilter(QString("Queue=94"))
            self.modelpq.sort(1,0)
            self.modelpq.select()
            self.ui.tableView_2.setModel(self.modelpq)
            self.ui.tableView_2.hideColumn(2)
            self.ui.tableView_2.hideColumn(3)
            self.ui.tableView_2.hideColumn(4)
            self.ui.tableView_2.hideColumn(6)
            self.ui.tableView_2.hideColumn(8)
            self.ui.tableView_2.hideColumn(9)
            # Hide the Add kit Button
            self.ui.pushButton_7.hide()

            
        else :
            
            self.modelpq = QtSql.QSqlRelationalTableModel(self)
            self.modelpq.setTable("production_queue")
            self.modelpq.setFilter(QString("Queue=5"))
            self.modelpq.sort(3,0)
            blah = self.modelpq.selectStatement()
            self.modelpq.select()
            self.ui.tableView_2.setModel(self.modelpq)
            self.ui.tableView_2.hideColumn(1)
            self.ui.tableView_2.hideColumn(3)
            self.ui.tableView_2.hideColumn(4)
            self.ui.tableView_2.hideColumn(6)
            self.ui.pushButton_7.show()
            
        
        self.ui.tableView_2.resizeColumnsToContents()
        self.ui.tableView_2.setColumnWidth(0,75)
        self.ui.tableView_2.setSelectionMode(QtWidgets.QTableView.SingleSelection)
        my_delegate = MyDelegate()
        self.ui.tableView_2.setItemDelegate(my_delegate)
        self.ui.tableView_2.show()
            
    def setupLabelsPrintedView(self) :
        
        # Set up labels_printed tableview
        
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable("labels_printed")
        self.model.sort(1,1)
        self.model.setFilter(QString("label_delete<>'true' and date(date_printed) = '%s' "   % self.timestamp.strftime("%Y-%m-%d")))
        self.model.select()
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.hideColumn(3)
        self.ui.tableView.hideColumn(4)
        self.ui.tableView.hideColumn(5)
        self.ui.tableView.resizeColumnsToContents()
        self.ui.tableView.setSelectionMode(QtWidgets.QTableView.SingleSelection)
        self.ui.tableView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)        
        
    def keyPressEvent(self, event):
        """ Define keyboard shortcut keys"""
    
        if event.key() == QtCore.Qt.Key_F1:
            self.printLabel()
        elif event.key() == QtCore.Qt.Key_F2:
            self.takePic()
        elif event.key() == QtCore.Qt.Key_F3:
            self.setTare()
        elif event.key() == QtCore.Qt.Key_F4:
            self.zeroScale()
        elif event.key() == QtCore.Qt.Key_F5:
            self.reprintLabel() 

    def takePic(self) :
        # Take a picture and put it in file
        
        if self.camera_mode == 0 :
            
            if self.label_printed  :
                
                # Tell PSRemote to take a picture, PSRemote process must be running
                #TODO Put this in the configuration file.
                psremote_path = config.get('general','psremote_path')
                cmd = [psremote_path,"-o","C:\PSRemote","-p","%s" % self.serial_no]
                
                # Windows centric startup info, to keep ddPak from losing focus. Suppresses console window for PSRemoteTest
                
                si = subprocess.STARTUPINFO()
                si.dwFlags = subprocess.STARTF_USESTDHANDLES | subprocess.STARTF_USESHOWWINDOW                
                output = subprocess.Popen(cmd, stdout=subprocess.PIPE, startupinfo=si).communicate()[0].decode('ascii')
                
                # rename and renumber jpeg
                
                if output == '' :
                    self.ui.plainTextEdit.setPlainText('PSRemote not responding, retake picture.')
                else :
                    directory = os.path.split(os.path.abspath((output[25:len(output)-2])))[0]
        
                    number_of_files = len([item for item in os.listdir(directory) if os.path.isfile(os.path.join(directory,item))])
                    #import pdb; pdb.set_trace()
                    original_file_name = output[25:len(output)-2]
                    new_file_name = output[25:len(output)-10] + '_' + str(number_of_files) + '.jpg'
                    os.rename(original_file_name,new_file_name)
                    self.label_printed = False
                    self.ui.plainTextEdit.setPlainText('')
            else : 
                
                self.ui.plainTextEdit.setPlainText('Must print label first!')
                
        else:
            
            self.label_printed = False
            self.ui.plainTextEdit.setPlainText('Running without pictures!')
            
        return

    def checkScale(self)  :
        # Update scale display 
        
        # keep reading 1 char until start character detected, added this for stability
        # TODO If scaleport is available but unreadable
        # program will freeze. CHANGE!
        
        start_char = b'\x00'
        while start_char != b'\x02' :
            start_char = self.scaleport.read(1)
        #import pdb; pdb.set_trace()
        line = start_char +  self.scaleport.read(16)
        
        #start parsing the Mettler Toledo continuous output
             
        statusworda  = line[1]
        statuswordb  = line[2]
        statuswordc  = line[3]

        
        #decimal point location
        
        decimalposition  = (0b0000111 & statusworda) - 2
        
        # sign
        
        if (0b10 & statuswordb) > 0 : sign = '-'
        else : sign = '+'
        #import pdb; pdb.set_trace()
        weightstring = sign +  line[3:(10- decimalposition)].decode('ascii').lstrip().lstrip('0') + '.' + line[(10- decimalposition):10].decode('ascii')
        tarestring = line[10:(16- decimalposition)].decode('ascii').lstrip().lstrip('0') + '.' + line[(16- decimalposition):16].decode('ascii')
        print (tarestring, weightstring)
        self.ui.label_10.setText(weightstring)
        self.ui.label_20.setText(tarestring)
        #weightstring = '+81.6'
        #tarestring = '+7.6'
        # Weight verification for high-low indicator
        
        try:

            self.indicated_weight = float(weightstring)
            tare = float(tarestring)
            
        except :
            print ('Scale brain fart')
            return False
            
        
        self.gross_weight = round(self.indicated_weight + tare,1)
        if ddpak.ui.label_14.text() != '' :
            
            if self.indicated_weight > (self.net_weight + self.weight_tol) :
                self.ui.highlabel.setStyleSheet("QLabel { 	background-color: rgb(255, 0, 0);}")
                self.ui.goodlabel.setStyleSheet("QLabel { background-color: rgb(161, 161, 161); }")
                self.ui.lowlabel.setStyleSheet("QLabel { background-color: rgb(161, 161, 161); }")
                return False
            elif self.indicated_weight < (self.net_weight - self.weight_tol):
                self.ui.highlabel.setStyleSheet("QLabel { background-color: rgb(161, 161, 161);  }")
                self.ui.goodlabel.setStyleSheet("QLabel { background-color: rgb(161, 161, 161);  }")
                self.ui.lowlabel.setStyleSheet("QLabel { 	background-color: rgb(255, 0, 0); }")                
                return False
            else :
                self.ui.highlabel.setStyleSheet("QLabel { background-color: rgb(161, 161, 161); }")
                self.ui.goodlabel.setStyleSheet("QLabel { background-color: rgb(0, 255, 0);}")
                self.ui.lowlabel.setStyleSheet("QLabel { background-color: rgb(161, 161, 161); }")
                return True 

        return False
    
    def printLabel(self,override=False) :
        kit = str(ddpak.ui.label_12.text())
        
        if kit != '' and not(self.label_printed)  :
            query = QtSql.QSqlQuery()
            query.exec_("""Select description, description_2, scale_weight, weight_tolerance, brand_graphic
            from item_master 
            where item_id = '%s'"""  % kit) 
            query.next()
            timestamp = datetime.datetime.now()
            self.serial_no = (timestamp.strftime("%y%m%d%H%M%S")) + kit
            desc = str(query.value(0))
            desc2 = str(query.value(1))
            brand = str(query.value(4))
            packdate = timestamp.strftime("%Y-%m-%d %H:%M:%S")
            packer = str(ddpak.ui.label_19.text())
            print_speed = config.getint('general','printer_speed',fallback=2)
                    
            if  self.checkScale()  or override :
                string2d = ('serial no:'+self.serial_no+',packer:'+packer+',packdate:'+packdate+',gross weight:'+ str(self.gross_weight)+',net weight:'+str(self.indicated_weight))
                string_info = ('P:'+packer+' G:'+ str(self.gross_weight)+' N:'+str(self.indicated_weight))
                self.label_second = """~PS^XA
                ^LH0,0
                ^PR%s,%s,%s
                ^FT349,2946^A0B,277,196^FD%s^FS
                ^BY600,600^FT75,1061^BXN,25,200,0,0,1
                ^FD%s^FS
                ^FT949,3000^A0B,277,196^FD%s^FS
                ^PQ1,0,1,Y^XZ""" % (print_speed, print_speed, print_speed, self.serial_no,string2d, string_info)
                
                self.printerport.write(bytes(self.label_second,'ascii'))
                self.label_first = """^XA^XF%s^FS
                ^FN1^FD%s^FS
                ^FN2^FD%s^FS
                ^FN3^FD%s^FS
                ^FN4^FD%s^FS
                ^FN5^FD%s^FS
                ^FN6^FD%s^FS
                ^FN7^FD%s^FS
                ^FN8^FD%s^FS
                ^FN9^FD%s^FS
                ^FN10^FD%s^FS
                ^FN11^FD%s^FS
                ^FN12^FD%s^FS
                ^FN13^FD%s^FS
                ^FN14^FD%s^FS
                ^FN15^FD%s^FS
                ^FN16^FD%s^FS
                ^FN17^FD%s^FS
                ^FN18^FD%s^FS
                ^FN19^FD%s^FS
                ^FN20^FD%s^FS
                ^XZ"""  % (brand,self.serial_no,self.serial_no,kit,desc,desc2,self.indicated_weight,packdate,'',packer,self.gross_weight,self.indicated_weight,packdate,'',packer,self.gross_weight,desc,desc2,kit, string2d,self.serial_no )
                    
                self.printerport.write(bytes(self.label_first,'ascii'))

                
                #Update labels printed table
                sqlstring = ("""Insert into labels_printed values ('%s','%s','%s','%s','false','false',%s,%s,'false') """ %(self.serial_no,packdate,packer,self.host_name,self.gross_weight,self.indicated_weight) )
                query.exec_(sqlstring)
                blah = str(query.lastError().text())
                
                
                # Update number of kits packed field
                sqlstring = ("""Select count(label_id)  from labels_printed where date(date_printed) = '%s' and pack_station_host_name = '%s' and label_delete = 'false' """ %(timestamp.date(),self.host_name) )
                query.exec_(sqlstring)
                query.next()
                self.ui.label_22.setText(str(query.value(0)))
                
                    
                if self.camera_mode == 0 : self.label_printed  = True
                
                self.ui.plainTextEdit.setPlainText('')
                self.model.select()
                

            
            
            return
        
        
        else : 
            if self.label_printed : self.ui.plainTextEdit.setPlainText('Must take picture first')
            else : self.ui.plainTextEdit.setPlainText('No kit selected')
        
        return
    
    def editPref(self) :
        
        log_in.ui.label.setText('Password')
        log_in.ui.lineEdit.clear()
        if log_in.exec_() == QtWidgets.QDialog.Accepted :
            self.change_preferences.loadConfig()
            self.change_preferences.show()

    
    
    def editKitTable(self):
        
        log_in.ui.label.setText('Password')
        log_in.ui.lineEdit.clear()
        if log_in.exec_() == QtWidgets.QDialog.Accepted :
            self.edit_kit_table.setupDatabaseViews()
            self.edit_kit_table.show()

        
        
    
    def setTare(self) :
        
        self.scaleport.write(b'T')
        
    def zeroScale(self) :
        
        self.scaleport.write(b'Z')  
        
        
    def deleteLabels(self) :
        
        
        index = self.ui.tableView.currentIndex()
        row = index.row()
        label_id = str(self.model.data(self.model.index(row, 0)))
        query = QtSql.QSqlQuery()
        query.exec_("""Update labels_printed set label_delete = 'true'
        where label_id = '%s'"""  % label_id ) 
        self.model.select()        
        
        
        return 
    
    def reprintLabel(self) :
        
        self.printerport.write(bytes(self.label_second,'ascii'))
        self.printerport.write(bytes(self.label_first,'ascii'))
        query = QtSql.QSqlQuery()
        query.exec_("""Update labels_printed set label_reprint = True
        where label_id = '%s'"""  % self.serial_no)
        self.model.select()
        
    def selectKit(self) :
        
        if not(self.label_printed) :
            
            #Load up main screen with data and mark kit as completed in queue
            # and write label format to printer. Also load kit image
            
            index = self.ui.tableView_2.currentIndex()
            row = index.row()
            kit = str(self.modelpq.data(self.modelpq.index(row, 0)))
            carrier = self.modelpq.data(self.modelpq.index(row, 7))
            specdoc_path = config.get('general','specpath')
            
            query = QtSql.QSqlQuery()
            sqlstring = ("""Select description, scale_weight, weight_tolerance, box, label_text, pdf
            from item_master inner join label_strings on item_master.brand_graphic = label_strings.brand 
            where item_id = '%s'"""  % kit) 
            query.exec_(sqlstring)
            query.next()
            desc = str(query.value(0))
            weight = str(query.value(1))
            self.net_weight = query.value(1)
            weight_tolerance = str(query.value(2))
            self.weight_tol = query.value(2)
            box = str(query.value(3))
            labelformat = bytes(query.value(4).encode('ascii'))
            
             
            self.printerport.write(labelformat)
            self.ui.label_12.setText(kit)
            self.ui.label_13.setText(desc)
            self.ui.label_14.setText(weight)
            self.ui.label_15.setText(box)
            self.ui.label_17.setText(weight_tolerance)

            # Load up spec document
            try: 
                specfiles = os.listdir(specdoc_path)
                self.specdoc_file = specdoc_path + fnmatch.filter(specfiles,str(query.value(5)) + '*')[0]
                self.ui.pdf_view.dynamicCall("LoadFile(const QString &)", self.specdoc_file)
                #self.ui.pdf_view.dynamicCall("LoadFile(const QString &)", "C:/Users/caleb/Development/AcRdrTest/42157.02_091512.pdf")		       

            except:
                self.ui.plainTextEdit.setPlainText("Couldn't find specification document, check if folder exists")
                return

            self.ui.plainTextEdit.setPlainText('Place empty %s box on scale and push Tare button' % box)
            packdate = datetime.datetime.now().strftime("%m-%d-%y")
                
            #Move selected kit to completed queue in either MountsMES or the internal SQLite database depending on preferences
            
            if self.ui.radioButton.isChecked():
                query = QtSql.QSqlQuery(self.MESdb)
                old_queue = 94
                old_position = self.modelpq.data(self.modelpq.index(row, 1))
            else :  
                query = QtSql.QSqlQuery()
                old_queue = 5
                old_position = self.modelpq.data(self.modelpq.index(row, 2))
            query.exec_("""Select max(position) from production_queue 
            where Queue = 99""" ) 
            query.next()
            position = query.value(0) + 1
            sqlstring = ("""Update production_queue set  end_date = '%s', Queue = 99, position = %s 
                            where  Queue = %s and position = %s"""  % (packdate, position, old_queue, old_position )) 
            query.exec_(sqlstring)
            self.modelpq.select()
            
        else : self.ui.plainTextEdit.setPlainText('Must take picture of last kit before selecting new kit')

       
    def addKit(self) :
        
        """This method only used with carriers view looking at internal SQLite database"""
        
        query = QtSql.QSqlQuery()
        query.exec_("""Select max(position) from production_queue 
        where Queue = 5"""  ) 
        query.next()
        position = int(query.value(0)) + 1
        row = self.modelpq.rowCount()
        self.modelpq.insertRows(row,1)
        self.modelpq.setData(self.modelpq.index(row,1),False)
        self.modelpq.setData(self.modelpq.index(row,2),position)
        self.modelpq.setData(self.modelpq.index(row,3),datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.modelpq.setData(self.modelpq.index(row,6),5)
        index = self.modelpq.index(row,0)
        self.ui.tableView_2.setCurrentIndex(index)
        self.ui.tableView_2.edit(index)
        
    def editUsers(self):
               
        log_in.ui.label.setText('Password')
        log_in.ui.lineEdit.clear()
        if log_in.exec_() == QtWidgets.QDialog.Accepted :
            self.edit_user.setupDatabaseViews(db)
            self.edit_user.show()
        

        

       
        return
            
    def showAbout(self) :
        
        self.about_box.show()
        
        return  
    
    
    def prodReporting(self) :
        
        self.production_reporting.show()
        
        return
    

# Main event loop

app = QtWidgets.QApplication(sys.argv)
config_name = 'ddPak.ini'

# Determine whether application is running as a script or as a frozen exe.

if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__ :
    application_path = os.path.dirname(__file__)
    
config_path = os.path.join(application_path, config_name)
config = configparser.ConfigParser()
config.read(config_path)  
# Set up the default database connection,  (database file must be in same directory as application)
db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
db_file = os.path.join(application_path, 'mounts.sqlite')
db.setDatabaseName(db_file)
log_in = Login()      
ddpak = DDPak()
ddpak.showMaximized()
log_in.exec_() 
app.exec_()





