
from PyQt6 import QtCore, QtWidgets
from hrqt import Ui_HealthRecord


class Ui_Search(object):

    def setupUi(self, Search):
        Search.setObjectName("Search")
        Search.resize(810, 458)

        self.centralwidget = QtWidgets.QWidget(parent=Search)
        self.centralwidget.setObjectName("centralwidget")

        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(80, 40, 631, 79))
        self.textEdit.setObjectName("textEdit")

        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(330, 150, 121, 21))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.clicked.connect(self.searchLocal)
        self.pushButton.setGeometry(QtCore.QRect(330, 170, 113, 32))
        self.pushButton.setObjectName("pushButton")

        self.textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(200, 150, 111, 31))
        self.textBrowser.setObjectName("textBrowser")

        Search.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Search)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 810, 24))
        self.menubar.setObjectName("menubar")
        self.menuFront_page = QtWidgets.QMenu(parent=self.menubar)
        self.menuFront_page.setObjectName("menuFront_page")
        self.menuPatients_Heath_Record = QtWidgets.QMenu(parent=self.menubar)
        self.menuPatients_Heath_Record.setObjectName("menuPatients_Heath_Record")
        self.menuAppointments = QtWidgets.QMenu(parent=self.menubar)
        self.menuAppointments.setObjectName("menuAppointments")
        self.menuMessafe = QtWidgets.QMenu(parent=self.menubar)
        self.menuMessafe.setObjectName("menuMessafe")
        self.menu = QtWidgets.QMenu(parent=self.menubar)
        self.menu.setTitle("")
        self.menu.setObjectName("menu")
        Search.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Search)
        self.statusbar.setObjectName("statusbar")
        Search.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFront_page.menuAction())
        self.menubar.addAction(self.menuPatients_Heath_Record.menuAction())
        self.menubar.addAction(self.menuAppointments.menuAction())
        self.menubar.addAction(self.menuMessafe.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(Search)
        QtCore.QMetaObject.connectSlotsByName(Search)

    def retranslateUi(self, Search):
        _translate = QtCore.QCoreApplication.translate
        Search.setWindowTitle(_translate("Search", "MainWindow"))
        self.textEdit.setHtml(_translate("Search", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt;\">Patients Health Record</span></p></body></html>"))
        self.pushButton.setText(_translate("Search", "OK"))
        self.textBrowser.setHtml(_translate("Search", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">CPR-number</p></body></html>"))
        self.menuFront_page.setTitle(_translate("Search", "Front_page"))
        self.menuPatients_Heath_Record.setTitle(_translate("Search", "Patients_Heath_Record"))
        self.menuAppointments.setTitle(_translate("Search", "Appointments"))
        self.menuMessafe.setTitle(_translate("Search", "Message"))

    def searchLocal(self):
        inputvalue = self.lineEdit.text()
        if len(inputvalue) == 10:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_HealthRecord()
            self.ui.setupUi(self.window)
            self.ui.UpdateWindow(inputvalue)
            self.window.show()
        else:
            print("The CPR is not true")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Search = QtWidgets.QMainWindow()
    ui = Ui_Search()
    ui.setupUi(Search)
    Search.show()
    sys.exit(app.exec())
