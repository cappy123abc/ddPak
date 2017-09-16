#!/usr/bin/python


import sys
import os
import ConfigParser
import socket
import datetime
import subprocess
import serial
import shutil
import QtPoppler
from serial.tools.list_ports import *
from PyQt4 import QtGui, QtCore, QtSql
from ScannerInterface import Ui_MainWindow
from login import Ui_loginDialog
from PrefsNew import Ui_Dialog
from EditKitTable import Ui_EditKitTableDialog
from about import Ui_aboutDialog
from ProductionReporting import Ui_ProductionReportDialog
from EditUsers import Ui_EditUsersDialog
from UserManual import Ui_UMDialog
        
class Login (QtGui.QDialog) :
    
    def __init__ (self) :
        
        QtGui.QDialog.__init__(self)
    
        # Set up the user interface from Designer.
        self.ui = Ui_loginDialog()
        self.ui.setupUi(self)
            
        # Connect up the Signals 
        self.connect(self.ui.pushButton, QtCore.SIGNAL('clicked()'),self.validateUser )
        self.connect(self.ui.pushButton_2, QtCore.SIGNAL('clicked()'),self, QtCore.SLOT('close()'))
        


            
    def validateUser(self):

        if fp.db.open() :
            
                        
            username = self.ui.lineEdit.text()
            password = self.ui.lineEdit_2.text()
            query = QtSql.QSqlQuery(fp.db)
            query.exec_(''' Select passwd,role,initials from users where user_id = '%s'   ''' % username)      
            query.next()
            role = str(query.value(1).toString())
            
            if (str(query.value(0).toString()) == password) and query.isValid() :
                if role <> 'admin' : fp.ui.menuEDit.setEnabled(False)
                fp.ui.label_19.setText(str(query.value(2).toString()))
                query.clear() 
                fp.showMaximized()
                fp.weighStart()
                self.close()
    
            else:
                self.ui.label_3.setText('Bad username or password!')
                
            return
        
        else :
            
            self.ui.label_3.setText('Database does not exist or can\'t connect!')

class FisherPak(QtGui.QMainWindow) :
    
    
    class EditKitTable(QtGui.QDialog):
   
        def __init__(self):
        
            QtGui.QDialog.__init__(self)
            self.ui = Ui_EditKitTableDialog()
            self.ui.setupUi(self)
            self.connect(self.ui.pushButton_2, QtCore.SIGNAL('clicked()'),self.insRow )
            self.connect(self.ui.pushButton, QtCore.SIGNAL('clicked()'),self, QtCore.SLOT('close()'))
  
        def setupDatabaseViews (self) :
            
            self.model = QtSql.QSqlTableModel(self)
            self.model.setTable("item_master")
            self.model.sort(0,0)
            self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
            self.model.select()    
            self.ui.tableView.setModel(self.model)
            self.ui.tableView.setSelectionMode(QtGui.QTableView.SingleSelection)
            self.ui.tableView.setSelectionBehavior(QtGui.QTableView.SelectRows)
            
        def insRow(self) :
            
            row = self.model.rowCount()
            self.model.insertRows(row,1)
            index = self.model.index(row,0)
            self.ui.tableView.setCurrentIndex(index)
            self.ui.tableView.edit(index)
            
            
    class EditUsers(QtGui.QDialog) :
        
        def __init__(self) :
            
            QtGui.QDialog.__init__(self)
            self.ui = Ui_EditUsersDialog()
            self.ui.setupUi(self)
            
            self.connect(self.ui.pushButton, QtCore.SIGNAL('clicked()'),self.insRow )
            self.connect(self.ui.pushButton_2, QtCore.SIGNAL('clicked()'),self, QtCore.SLOT('close()'))
            
        def setupDatabaseViews (self, dbname = '') :
            
            self.model = QtSql.QSqlTableModel(self)
            self.model.setTable("users")
            self.model.select()    
            self.ui.tableView.setModel(self.model)
            self.ui.tableView.setSelectionMode(QtGui.QTableView.SingleSelection)
                   
        def insRow(self) :
            
            row = self.model.rowCount()
            self.model.insertRows(row,1)
            index = self.model.index(row,0)
            self.ui.tableView.setCurrentIndex(index)
            self.ui.tableView.edit(index)
            
        
    class ChangePrefs (QtGui.QDialog):

        def __init__ (self) :
        
            QtGui.QDialog.__init__(self)
            
            self.ui = Ui_Dialog()
            self.ui.setupUi(self)
            self.connect(self.ui.buttonBox, QtCore.SIGNAL('accepted()'),self.updatePreferences )
            self.connect(self.ui.buttonBox, QtCore.SIGNAL('rejected()'),QtCore.SLOT('close()'))
            self.connect(self.ui.pushButton, QtCore.SIGNAL('clicked()'),self.getDirectory )
            self.connect(self.ui.pushButton_2, QtCore.SIGNAL('clicked()'),self.getMountsMESFile )
            
        def loadConfig (self):
            
            """ Read and display config settings """
        
            self.config = ConfigParser.ConfigParser()
            # need following line so that app can find config file with a relative path 
            self.ini_file = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "ddPak.ini") 
            self.config.read(self.ini_file)
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
            self.ui.comboBox_9.setCurrentIndex(self.ui.comboBox_9.findText(self.config.get('printerport','portnumber')))
            self.ui.comboBox_10.setCurrentIndex(self.ui.comboBox_10.findText(self.config.get('scaleport','portnumber')))
            self.ui.comboBox.setCurrentIndex(self.ui.comboBox.findText(self.config.get('printerport','baud')))
            self.ui.comboBox_4.setCurrentIndex(self.ui.comboBox_4.findText(self.config.get('scaleport','baud')))
            self.ui.comboBox_5.setCurrentIndex(self.ui.comboBox_5.findText(self.config.get('printerport','databits')))
            self.ui.comboBox_6.setCurrentIndex(self.ui.comboBox_6.findText(self.config.get('scaleport','databits')))
            self.ui.comboBox_7.setCurrentIndex(self.ui.comboBox_7.findText(self.config.get('printerport','stopbit')))
            self.ui.comboBox_8.setCurrentIndex(self.ui.comboBox_8.findText(self.config.get('scaleport','stopbit')))
            self.ui.comboBox_2.setCurrentIndex(self.ui.comboBox_2.findText(self.config.get('printerport','parity')))
            self.ui.comboBox_3.setCurrentIndex(self.ui.comboBox_3.findText(self.config.get('scaleport','parity')))
            self.ui.checkBox.setCheckState(self.config.getint('general','cameramode'))
            self.ui.lineEdit.setText(self.config.get('general','dbbackuppath'))
            self.ui.lineEdit_2.setText(self.config.get('general','mountsmesdb'))

            if self.config.getboolean('general', 'highvolume') :  self.ui.checkBox_2.setCheckState(2)
            if self.config.getboolean('general', 'lowvolume') :  self.ui.checkBox_3.setCheckState(2)
            if self.config.getboolean('general', 'supercell') :  self.ui.checkBox_4.setCheckState(2)


        def updatePreferences(self) :
            
            """ Write new preferences to config file and restart weighing operation"""
            
            self.config.set('printerport', 'portnumber', self.ui.comboBox_9.currentText())
            self.config.set('scaleport','portnumber', self.ui.comboBox_10.currentText())
            self.config.set('printerport','baud', self.ui.comboBox.currentText())
            self.config.set('scaleport','baud', self.ui.comboBox_4.currentText())
            self.config.set('printerport','databits', self.ui.comboBox_5.currentText())
            self.config.set('scaleport','databits', self.ui.comboBox_6.currentText())
            self.config.set('printerport','stopbit', self.ui.comboBox_7.currentText())
            self.config.set('scaleport','stopbit', self.ui.comboBox_8.currentText())
            self.config.set('printerport','parity', self.ui.comboBox_2.currentText())
            self.config.set('scaleport','parity', self.ui.comboBox_3.currentText())
            self.config.set('general','cameramode', self.ui.checkBox.checkState())
            self.config.set('general','dbbackuppath', self.ui.lineEdit.text())
            self.config.set('general','mountsmesdb', self.ui.lineEdit_2.text())
            if self.ui.checkBox_2.isChecked() :  self.config.set('general','highvolume', 1)
            else : self.config.set('general','highvolume', 0)
            if self.ui.checkBox_3.isChecked() :  self.config.set('general','lowvolume', 1)
            else : self.config.set('general','lowvolume', 0)
            if self.ui.checkBox_4.isChecked() :  self.config.set('general','supercell', 1)
            else : self.config.set('general','supercell', 0)
    
            self.config.write(open(self.ini_file, 'wb'))
            fp.weighStart()
            
            
        def getDirectory(self) :
            
            directory = QtGui.QFileDialog.getExistingDirectory(self, 'Open file','/home')
            self.ui.lineEdit.setText(str(directory))
        
        def getMountsMESFile(self) :
            
            filename = QtGui.QFileDialog.getOpenFileName(self, 'Locate MountsMES','/home', 'Access database files (*.mdb)')
            self.ui.lineEdit_2.setText(str(filename))
        
    class ProductionReporting(QtGui.QDialog):
   
        def __init__(self):
        
            QtGui.QDialog.__init__(self)
            self.ui = Ui_ProductionReportDialog()
            self.ui.setupUi(self)  
            
            self.connect(self.ui.pushButton, QtCore.SIGNAL('clicked()'),self.generateReport)
            self.connect(self.ui.pushButton_2, QtCore.SIGNAL('clicked()'),self, QtCore.SLOT('close()'))
            self.connect(self.ui.pushButton_3, QtCore.SIGNAL('clicked()'),self.printReport)
            #self.connect(self.ui.pushButton_4, QtCore.SIGNAL('clicked()'),self.emailReport)
            
        def generateReport(self):
            
            ''' THis generates an ugly textbox report, would be nice to use reportlab or something '''
            
            production_date = self.ui.calendarWidget.selectedDate().toPyDate().isoformat()
            
            self.ui.textEdit.clear()



            self.loadPictureData(production_date,self.hostname)
            self.ui.textEdit.insertPlainText('Kits packed on Workstation: ' + query1.value(0).toString() + ' on Date: ' + production_date + '\n\n' ) 
            query2 = QtSql.QSqlQuery()
            strsql = """Select distinct(substr(label_id,13,length(label_id)-12)), count(substr(label_id,13,length(label_id)-12)) 
                        from labels_printed where DATE(date_printed) = '%s'
                        and pack_station_host_name = '%s'
                        and label_delete = 'false'
                        group by substr(label_id,13,length(label_id)-12)""" % (production_date, query1.value(0).toString()) 
            query2.exec_(strsql)
            while (query2.next()) :
                self.ui.textEdit.insertPlainText(query2.value(0).toString() + '   (' + query2.value(1).toString() + ')\n')
                
            query2.exec_("select label_id from labels_printed where label_delete = true and DATE(date_printed) = '%s'" % production_date) 
            self.ui.textEdit.insertPlainText('\n\nLabels deleted:   \n\n')
            while (query2.next()) :
                self.ui.textEdit.insertPlainText(query2.value(0).toString() + '\n')
                
            query2.exec_("select label_id from labels_printed where label_reprint = 'true' and DATE(date_printed) = '%s'" % production_date) 
            self.ui.textEdit.insertPlainText('\n\nLabels reprinted:   \n\n')
            while (query2.next()) :
                self.ui.textEdit.insertPlainText(query2.value(0).toString() + '\n')
                
                
            success = query2.exec_("select photo_id from photo_temp left outer join labels_printed on photo_id = label_id where label_id is null ")
            self.ui.textEdit.insertPlainText('\n\nPhotos with no corresponding label:   \n\n')
            if success :
              while (query2.next()) :
                  self.ui.textEdit.insertPlainText(query2.value(0).toString() + '\n')
            else : self.ui.textEdit.insertPlainText('Query failed \n')
            strsql = """select label_id from  labels_printed left outer join photo_temp on  photo_id = label_id
            where photo_id is null and DATE(date_printed) = '%s''""" % production_date
            success = query2.exec_("""select label_id from  labels_printed left outer join photo_temp on  photo_id = label_id
            where photo_id is null and DATE(date_printed) = '%s'""" % production_date)
            self.ui.textEdit.insertPlainText('\n\nLabels with no corresponding photo:   \n\n')
            if success :
              while (query2.next()) :
                  self.ui.textEdit.insertPlainText(query2.value(0).toString() + '\n')
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
            
            printer = QtGui.QPrinter()
            printDialog = QtGui.QPrintDialog(printer)
            if (printDialog.exec_() == QtGui.QDialog.Accepted) :               
                self.ui.textEdit.print_(printer)
        
                
        def emailReport (self) :
            
            return
            
    class UserManual (QtGui.QDialog) :
        
        def __init__ (self) :
            
            QtGui.QDialog.__init__(self)
            self.ui = Ui_UMDialog()
            self.ui.setupUi(self)
            
            self.connect(self.ui.pushButton, QtCore.SIGNAL('clicked()'),self, QtCore.SLOT('close()'))
            
            self.ui.webView.load(QtCore.QUrl("User Manual/ddPak User Manual.html"))
            self.ui.webView.show()
            
                       
                
    class AboutBox (QtGui.QDialog) :
        
        def __init__(self):
    
            QtGui.QDialog.__init__(self)
            self.abui = Ui_aboutDialog()
            self.abui.setupUi(self)
            
            self.connect(self.abui.pushButton_2, QtCore.SIGNAL('clicked()'),self, QtCore.SLOT('close()'))
    
    class MyDelegate (QtGui.QItemDelegate):
    
        """ This adds a combo box as item selector in kits on carriers table view. """ 
            
                 
        def __init__ (self, parent = None):
                        
            QtGui.QItemDelegate.__init__(self,parent)
        
        def createEditor(self, parent, option, index):
            if index.column() == 0 :
                editor = QtGui.QComboBox( parent )
                query = QtSql.QSqlQuery()
                query.exec_("""Select item_id from item_master where prd_line in (%s)  order by item_id""" % fp.prd_line_viz) 
                while (query.next()) :
                    item = query.value(0).toString()           
                    editor.addItem(item)
            else:
                return QtGui.QItemDelegate.createEditor(self, parent, option, index)

            return editor
    
    
        def setModelData(self, editor, model, index):
            
            if index.column() == 0 :
                value = editor.currentIndex()
                model.setData( index, editor.itemData( value, QtCore.Qt.DisplayRole ) )
                
            else :
                QtGui.QItemDelegate.setModelData(self, editor, model, index)
                 
    def __init__ (self) :
        
        """Main window object"""
        
        
        QtGui.QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
        #Create serial port objects, timer, etc. todo --- add exception handling when opening serial ports.
        
        self.config = ConfigParser.ConfigParser()
        self.config.read(os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "ddPak.ini"))
        self.timer = QtCore.QTimer()
        self.serial_no = ''
        self.host_name = socket.gethostname()
        self.scaleport = serial.Serial()
        self.printerport = serial.Serial()
        self.signalMapper = QtCore.QSignalMapper(self)
        
        # Create all window objects that will be needed
        
        self.ab = self.AboutBox()
        self.cp = self.ChangePrefs()
        self.ekt = self.EditKitTable()
        self.pr = self.ProductionReporting()
        self.eu = self.EditUsers()
        self.um = self.UserManual()
       
        # Connect up the Signals and Slots (Events and Event Handlers) for the UI
        self.connect(self.ui.pushButton_4, QtCore.SIGNAL('clicked()'),self.takePic )
        self.connect(self.ui.pushButton_2, QtCore.SIGNAL('clicked()'),self.printLabel )
        self.connect(self.timer, QtCore.SIGNAL('timeout()'), self.checkScale)
        self.connect(self.ui.actionPreferences,QtCore.SIGNAL('triggered()'), self.editPref)
        self.connect(self.ui.actionExit,QtCore.SIGNAL('triggered()'),QtGui.qApp, QtCore.SLOT('closeAllWindows()'))

        self.connect(self.ui.actionKit_Table,QtCore.SIGNAL('triggered()'), self.editKitTable)
        self.connect(self.ui.actionUpdate_Kit_Queue,QtCore.SIGNAL('triggered()'), self.updateKitQueue)

        self.connect(self.ui.actionEdit_Users,QtCore.SIGNAL('triggered()'), self.editUsers)
        self.connect(self.ui.actionManual,QtCore.SIGNAL('triggered()'), self.um.show)
        self.connect(self.ui.actionProduction_Reporting,QtCore.SIGNAL('triggered()'), self.prodReporting)
        self.connect(self.ui.actionAbout_DDPak,QtCore.SIGNAL('triggered()'), self.showAbout)
        self.connect(self.ui.pushButton, QtCore.SIGNAL('clicked()'),self.setTare )
        self.connect(self.ui.pushButton, QtCore.SIGNAL('clicked()'),self.zeroScale)
        self.connect(self.ui.pushButton_5, QtCore.SIGNAL('clicked()'),self.deleteLabels)
        self.connect(self.ui.pushButton_6, QtCore.SIGNAL('clicked()'),self.reprintLabel)
        self.connect(self.ui.pushButton_8, QtCore.SIGNAL('clicked()'),self.selectKit)
        self.connect(self.ui.pushButton_7, QtCore.SIGNAL('clicked()'),self.addKit)
        self.connect(self.ui.radioButton, QtCore.SIGNAL('clicked()'),self.setupCarriersView)
        self.connect(self.ui.radioButton_2, QtCore.SIGNAL('clicked()'),self.setupCarriersView)
        
        self.connect(self.ui.pushButton_9, QtCore.SIGNAL('clicked()'),self.signalMapper, QtCore.SLOT("map()"))
        self.connect(self.ui.pushButton_10, QtCore.SIGNAL('clicked()'),self.signalMapper, QtCore.SLOT("map()"))
        self.connect(self.ui.pushButton_11, QtCore.SIGNAL('clicked()'),self.signalMapper, QtCore.SLOT("map()"))
        self.connect(self.ui.pushButton_12, QtCore.SIGNAL('clicked()'),self.signalMapper, QtCore.SLOT("map()"))

        self.signalMapper.setMapping (self.ui.pushButton_9, "first")
        self.signalMapper.setMapping (self.ui.pushButton_10, "previous")
        self.signalMapper.setMapping (self.ui.pushButton_11, "next")
        self.signalMapper.setMapping (self.ui.pushButton_12, "last")
        
        self.connect (self.signalMapper, QtCore.SIGNAL("mapped(const QString &)"), self.navPdf)
        
        # Set up the default database connection,  (database file must be in same directory as application)
        
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db_file = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "mounts.sqlite")
        self.db.setDatabaseName(self.db_file)
        
        # Set up the MountsMES database connection
        
        self.MESdb = QtSql.QSqlDatabase.addDatabase("QODBC", "mountsMES_db")
        self.MESdb_file = self.config.get("general", "mountsmesdb")
        self.MESdb.setDatabaseName("Driver={Microsoft Access Driver (*.mdb)};FIL={MS Access};DBQ=%s"  % self.MESdb_file )
        
        # Set up labels_printed tableview
        
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable("labels_printed")
        self.model.sort(1,1)
        self.model.setFilter(QtCore.QString("label_delete<>'true'"))
        self.model.select()
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.hideColumn(3)
        self.ui.tableView.hideColumn(4)
        self.ui.tableView.hideColumn(5)
        self.ui.tableView.resizeColumnsToContents()
        self.ui.tableView.setSelectionMode(QtGui.QTableView.SingleSelection)
        self.ui.tableView.setSelectionBehavior(QtGui.QTableView.SelectRows)
        self.ui.radioButton.setChecked(1)
        
        # initialize test switch states
        
        self.label_printed = False
        self.backupDatabase()

        
    def weighStart (self) :
        
        """This function starts or restarts the weighing based on preferences"""
        
        self.config.read(os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "ddPak.ini"))
        self.camera_mode = self.config.getint('general','cameramode')
        self.prd_line_viz = ''
        if self.config.getboolean('general','highvolume')  : self.prd_line_viz += '3,'
        if self.config.getboolean('general','lowvolume')  : self.prd_line_viz += '1,'
        if self.config.getboolean('general','supercell')  : self.prd_line_viz += '2,' 
        self.prd_line_viz = self.prd_line_viz.rstrip( ',')
        self.setupCarriersView()

        
        try:
            
            self.printerport.port = self.config.get('printerport','portnumber')
            self.printerport.baudrate = self.config.getint('printerport','baud')
            self.printerport.bytesize = self.config.getint('printerport','databits')
            self.printerport.stopbits = self.config.getfloat('printerport','stopbit')
            self.printerport.parity = self.config.get('printerport','parity')[:1]
            if not(self.printerport.isOpen()) : self.printerport.open()
            
        except:
            
            self.ui.plainTextEdit.appendPlainText('Cannot connect to printer, check settings.')
            
        try:
            
            self.scaleport.port = self.config.get('scaleport','portnumber')
            self.scaleport.baudrate = self.config.getint('scaleport','baud')
            self.scaleport.bytesize = self.config.getint('scaleport','databits')
            self.scaleport.stopbits = self.config.getfloat('scaleport','stopbit')
            self.scaleport.parity = self.config.get('scaleport','parity')[:1]
            if not(self.scaleport.isOpen()) : self.scaleport.open()
            
        except :
            
            self.ui.plainTextEdit.appendPlainText('Cannot connect to scale, check settings.')
  
        
        if self.scaleport.isOpen() : self.timer.start()
        
        return
        
    def backupDatabase (self) :
        """ Todo - write over old db file"""
        
        self.db_backup_dir = self.config.get('general','dbbackuppath')
        try: shutil.copy(self.db_file , self.db_backup_dir + '/' + self.host_name + '_' + datetime.datetime.today().strftime("%m_%d_%Y") + '.sqlite' )
        except Exception as inst : self.ui.plainTextEdit.appendPlainText('Database file not backed up! %s' % inst)
        
            
        
               
    def setupCarriersView (self) :
  

        #set up kits on carriers table view, depending on carrierviewmode from radio buttons we'll interface with MountsMES or the internal SQLite database.

        if self.ui.radioButton.isChecked()  :
            self.MESdb.open()
            self.modelpq = QtSql.QSqlRelationalTableModel(self, self.MESdb)
            self.modelpq.setTable("production_queue")
            self.modelpq.setFilter(QtCore.QString("Queue=94"))
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
            self.modelpq.setFilter(QtCore.QString("Queue=5"))
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
        self.ui.tableView_2.setSelectionMode(QtGui.QTableView.SingleSelection)
        my_delegate = self.MyDelegate()
        self.ui.tableView_2.setItemDelegate(my_delegate)
        self.ui.tableView_2.show()
            
            
        
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
        elif event.key() == QtCore.Qt.Key_F10:
            self.changeMood()
                       
    def takePic(self) :
        # Take a picture and put it in file
        
        if self.camera_mode == 0 :
            
            if self.label_printed  :
            
                # Tell PSRemote to take a picture, PSRemote process must be running
                cmd = ["C:\Program Files\BreezeSys\PSRemote\PSRemoteTest\PSRemoteTest.exe","-o","C:\PSRemote","-p","%s" % self.serial_no]
                
                # Windows centric startup info, to keep ddPak from losing focus. Suppresses console window for PSRemoteTest
                
                si = subprocess.STARTUPINFO()
                si.dwFlags = subprocess.STARTF_USESTDHANDLES | subprocess.STARTF_USESHOWWINDOW                
                output = subprocess.Popen(cmd, stdout=subprocess.PIPE, startupinfo=si).communicate()[0]
                
                # rename and renumber jpeg
                
                if output == '' :
                    self.ui.plainTextEdit.setPlainText('PSRemote not responding, retake picture.')
                else :
                    directory = os.path.split(os.path.abspath((output[25:len(output)-2])))[0]
        
                    number_of_files = len([item for item in os.listdir(directory) if os.path.isfile(os.path.join(directory,item))])
        
                    original_file_name = output[25:len(output)-2]
                    new_file_name = output[25:len(output)-10] + '_' + str(number_of_files) + '.jpg'
                    os.rename(original_file_name,new_file_name)
                    self.label_printed = False
                    self.ui.plainTextEdit.setPlainText('')
                    self.ui.activateWindow()
            else : 
                
                self.ui.plainTextEdit.setPlainText('Must print label first!')
                
        else:
            
            self.label_printed = False
            self.ui.plainTextEdit.setPlainText('Running without pictures!')
            
        return

    def checkScale(self)  :
        # Update scale display 
        
        # keep reading 1 char until start character detected, added this for stability
        start_char = ''
        while start_char <> chr(2) :   
            start_char = self.scaleport.read(1)
        line = start_char +  self.scaleport.read(16)
        
        #start parsing the Mettler Toledo continuous output
             
        statusworda  = line[1]
        statuswordb  = line[2]
        statuswordc  = line[3]

        
        #decimal point location
        
        decimalposition  = (0b0000111 & ord(statusworda)) - 2
        
        # sign
        
        if (0b10 & ord(statuswordb)) > 0 : sign = '-'
        else : sign = '+'
        
        weightstring = sign +  ((line[3:(10- decimalposition)]).lstrip()).lstrip('0') + '.' + line[(10- decimalposition):10]
        tarestring = ((line[10:(16- decimalposition)]).lstrip()).lstrip('0') + '.' + line[(16- decimalposition):16]
        
        self.ui.label_10.setText(weightstring)
        self.ui.label_20.setText(tarestring)
        
        # Weight verification for high-low indicator

        self.indicated_weight = float(weightstring)
        tare = float(tarestring)

    
        self.gross_weight = self.indicated_weight + tare
        if fp.ui.label_14.text() <> '' :
            
            if self.indicated_weight > (self.net_weight[0] + self.weight_tol[0]) :
                self.ui.highlabel.setStyleSheet("QLabel { 	background-color: rgb(255, 0, 0);}")
                self.ui.goodlabel.setStyleSheet("QLabel { background-color: rgb(161, 161, 161); }")
                self.ui.lowlabel.setStyleSheet("QLabel { background-color: rgb(161, 161, 161); }")
                return False
            elif self.indicated_weight < (self.net_weight[0] - self.weight_tol[0]):
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
        kit = str(fp.ui.label_12.text())
        
        if kit <> '' and not(self.label_printed)  :
            query = QtSql.QSqlQuery()
            query.exec_("""Select description, description_2, scale_weight, weight_tolerance, brand_graphic
            from item_master 
            where item_id = '%s'"""  % kit) 
            query.next()
            timestamp = datetime.datetime.now()
            self.serial_no = (timestamp.strftime("%y%m%d%H%M%S")) + kit
            desc = str(query.value(0).toString())
            desc2 = str(query.value(1).toString())
            brand = str(query.value(4).toString())
            packdate = timestamp.strftime("%Y-%m-%d %H:%M:%S")
            packer = str(fp.ui.label_19.text())
                    
            if  self.checkScale()  or override :
                
                string2d = ('serial no:'+self.serial_no+',packer:'+packer+',packdate:'+packdate+',gross weight:'+ str(self.gross_weight)+',net weight:'+str(self.indicated_weight))
                string_info = ('P:'+packer+' G:'+ str(self.gross_weight)+' N:'+str(self.indicated_weight))
                self.label_second = """~PS^XA
                ^LH0,0
                ^PR4,4
                ^FT349,2946^A0B,277,196^FD%s^FS
                ^BY600,600^FT75,1061^BXN,25,200,0,0,1
                ^FD%s^FS
                ^FT949,3000^A0B,277,196^FD%s^FS
                ^PQ1,0,1,Y^XZ""" % (self.serial_no,string2d, string_info)
                
                self.printerport.write(self.label_second)
                
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
                    
                self.printerport.write(self.label_first)

                
                #Update labels printed table
                sqlstring = ("""Insert into labels_printed values ('%s','%s','%s','%s','false','false',%s,%s,'false') """ %(self.serial_no,packdate,packer,self.host_name,self.gross_weight,self.indicated_weight) )
                query.exec_(sqlstring)
                
                # Update number of kits packed field
                sqlstring = ("""Select count(label_id)  from labels_printed where date(date_printed) = '%s' and pack_station_host_name = '%s' and label_delete = 'false' """ %(timestamp.date(),self.host_name) )
                query.exec_(sqlstring)
                query.next()
                self.ui.label_22.setText(str(query.value(0).toString()))
                
                    
                if self.camera_mode == 0 : self.label_printed  = True
                self.ui.plainTextEdit.setPlainText('')
                self.model.select()
                

            
            
            return
        
        
        else : 
            if self.label_printed : self.ui.plainTextEdit.setPlainText('Must take picture first')
            else : self.ui.plainTextEdit.setPlainText('No kit selected')
        
        return
    
    def editPref(self) :
        
        self.cp.loadConfig()
        self.cp.show()
    
        return
    
    def updateKitQueue(self) :
        
        self.epq.setupDatabaseViews(self.db)
        self.epq.show()
    
    def editKitTable(self):
        
        self.ekt.setupDatabaseViews()
        self.ekt.show()
        
        return
    
    def setTare(self) :
        
        self.scaleport.write('T')
        
    def zeroScale(self) :
        
        self.scaleport.write('Z')  
        
        
    def deleteLabels(self) :
        
        
        index = self.ui.tableView.currentIndex()
        row = index.row()
        label_id = str(self.model.data(self.model.index(row, 0)).toString())
        query = QtSql.QSqlQuery()
        query.exec_("""Update labels_printed set label_delete = 'true'
        where label_id = '%s'"""  % label_id ) 
        self.model.select()        
        
        
        return 
    
    def reprintLabel(self) :
        
        self.printerport.write(self.label_second)
        self.printerport.write(self.label_first)
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
            kit = str(self.modelpq.data(self.modelpq.index(row, 0)).toString())
            carrier = self.modelpq.data(self.modelpq.index(row, 7)).toInt()[0]
            specdoc_path = self.config.get('general','specpath')
            
            query = QtSql.QSqlQuery()
            sqlstring = ("""Select description, scale_weight, weight_tolerance, box, label_text, pdf
            from item_master inner join label_strings on item_master.brand_graphic = label_strings.brand 
            where item_id = '%s'"""  % kit) 
            query.exec_(sqlstring)
            query.next()
            desc = str(query.value(0).toString())
            weight = str(query.value(1).toString())
            self.net_weight = query.value(1).toFloat()
            weight_tolerance = str(query.value(2).toString())
            self.weight_tol = query.value(2).toFloat()
            box = str(query.value(3).toString())
            labelformat = str(query.value(4).toString())
            blah = str(query.value(5).toString())
            self.specdoc_file = specdoc_path + '/' + str(query.value(5).toString()) 
            self.printerport.write(labelformat)
            self.ui.label_12.setText(kit)
            self.ui.label_13.setText(desc)
            self.ui.label_14.setText(weight)
            self.ui.label_15.setText(box)
            self.ui.label_17.setText(weight_tolerance)

            # Load up spec document
            
            try:
                self.specdoc = QtPoppler.Poppler.Document.load(self.specdoc_file)
                self.specdoc.setRenderHint(QtPoppler.Poppler.Document.Antialiasing)
                self.specdoc.setRenderHint(QtPoppler.Poppler.Document.TextAntialiasing) 
                self.navPdf("first")
                self.ui.plainTextEdit.setPlainText('Place empty %s box on scale and push Tare button' % box)
                packdate = datetime.datetime.now().strftime("%m-%d-%y")
                
            except:

                self.ui.plainTextEdit.setPlainText("Couldn't find specification document")
                

            
            #Move selected kit to completed queue in either MountsMES or the internal SQLite database depending on preferences
            
            if self.config.getboolean('general','carrierviewmode')  :
                query = QtSql.QSqlQuery(self.MESdb)
                old_queue = 94
                old_position = self.modelpq.data(self.modelpq.index(row, 1)).toInt()[0]
            else :  
                query = QtSql.QSqlQuery()
                old_queue = 5
                old_position = self.modelpq.data(self.modelpq.index(row, 2)).toInt()[0]
            query.exec_("""Select max(position) from production_queue 
            where Queue = 99""" ) 
            query.next()
            position = query.value(0).toInt()[0] + 1
            
            sqlstring = ("""Update production_queue set  end_date = '%s', Queue = 99, position = %s 
                            where  Queue = %s and position = %s"""  % (packdate, position, old_queue, old_position )) 
            query.exec_(sqlstring)
            self.modelpq.select()
            
        else : self.ui.plainTextEdit.setPlainText('Must take picture of last kit before selecting new kit')

        

    def navPdf (self,nav_direction):

        if str(nav_direction) == 'first' : self.current_page = 0
        elif str(nav_direction) == 'last' : self.current_page = self.specdoc.numPages() - 1 
        elif (str(nav_direction) == 'next') and ((self.current_page + 1) <= self.specdoc.numPages()) : self.current_page += 1
        elif (str(nav_direction) == 'previous') and ((self.current_page - 1) >= 0) : self.current_page -= 1
            
        image = self.specdoc.page(self.current_page).renderToImage()
        self.ui.label_11.setPixmap(QtGui.QPixmap.fromImage(image, QtCore.Qt.MonoOnly))

        return
            
       
    def addKit(self) :
        
        """This method only used with carriers view looking at internal SQLite database"""
        
        query = QtSql.QSqlQuery()
        query.exec_("""Select max(position) from production_queue 
        where Queue = 5"""  ) 
        query.next()
        position = query.value(0).toInt()[0] + 1
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
        
        self.eu.setupDatabaseViews(self.db)
        self.eu.show()
        
    def changeMood(self) :
        
        '''Playing with stylesheets, Should move this stuff to  file  '''
       
        self.setStyleSheet("#MainWindow{\n"
"    font: 87 8pt \"Germany\";\n"
"    background-color: rgb(255, 0, 0);\n"
"background-image: url(:/newPrefix/Resources/patt_4cc99719cf715.jpg);\n"
"}\n"
"\n"
"#label,#label_8,#label_2{color:#f26522;font: 75 10pt \"Germany\";font-size:38px;}\n"
"#lcdNumber{\n"
"    color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 0, 0);}\n"
"#label_3,#label_4,#label_5,#label_6,#label_9,#label_16,#label_18,#label_21,#label_26,#label_23,#label_24{color:#f26522;font: 75 10pt \"Germany\";font-size:16px;}\n"
"#label_12,#label_13,#label_14,#label_15,#label_17,#label_19,#label_20,#label_22{color: rgb(255, 170, 0);font: 75 10pt \"Germany\";font-size:16px;}\n"
"\n"
"#label_7{\n"
"    \n"
"    \n"
"    font: 48pt \"Germany\";\n"
"    \n"
"    \n"
"    color: rgb(170, 0, 255);\n"
"    }\n"
"\n"
"#centralwidget{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.057, y2:0.0681818, stop:0 rgba(81, 81, 81, 151), stop:0.98 rgba(0, 0, 0, 255));\n"
"\n"
"}\n"
"#label_10{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 0, 0);\n"
"    \n"
"    font: 75 48pt \"Germany\";\n"
"\n"
"}\n"
"QPushButton{\n"
"    \n"
"    \n"
"font: 75 8pt \"Germany\";\n"
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
"}\n"
"#label_11{\n"
"\n"
"    background-color: rgb(255, 170, 127);\n"
"\n"
"}\n"
"#highlabel,#goodlabel,#lowlabel{\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"    background-color: rgb(179, 179, 179);\n"
"font: 70 7pt \"Germany\";\n"
"\n"
"\n"
"}\n"
"\n"
"#tableView  {\n"
"gridline-color:  rgb(170, 85, 255);\n"
"\n"
"}\n"
"\n"
"")
       
        return
            
    def showAbout(self) :
        
        self.ab.show()
        
        return  
    
    
    def prodReporting(self) :
        
        self.pr.show()
        
        return
    

# Main event loop

app = QtGui.QApplication(sys.argv)
li = Login()      
fp = FisherPak()
li.show() 
app.exec_()





