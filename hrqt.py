from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_HealtRecord(object):
    def setupUi(self, HealtRecord):
        HealtRecord.setObjectName("HealtRecord")
        HealtRecord.resize(741, 453)
        self.centralwidget = QtWidgets.QWidget(parent=HealtRecord)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser_7 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser_7.setGeometry(QtCore.QRect(400, 420, 631, 31))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.textBrowser_3 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(40, 510, 291, 231))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_10 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser_10.setGeometry(QtCore.QRect(510, 580, 421, 31))
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.textBrowser_9 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser_9.setGeometry(QtCore.QRect(400, 500, 631, 31))
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.textBrowser_6 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser_6.setGeometry(QtCore.QRect(400, 380, 631, 31))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(660, 580, 113, 32))
        self.pushButton_7.setObjectName("pushButton_7")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(370, 40, 631, 79))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(920, 420, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(400, 210, 631, 71))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(910, 240, 113, 32))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(920, 380, 113, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(920, 540, 113, 32))
        self.pushButton_6.setObjectName("pushButton_6")
        self.textBrowser_5 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser_5.setGeometry(QtCore.QRect(400, 340, 631, 31))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_2 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(40, 160, 291, 331))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(920, 500, 113, 32))
        self.pushButton_5.setObjectName("pushButton_5")
        self.textBrowser_8 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser_8.setGeometry(QtCore.QRect(400, 460, 631, 31))
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.textBrowser_4 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(400, 300, 631, 31))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(920, 340, 113, 32))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(920, 460, 113, 32))
        self.pushButton_10.setObjectName("pushButton_10")
        self.textBrowser_11 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser_11.setGeometry(QtCore.QRect(400, 540, 631, 31))
        self.textBrowser_11.setObjectName("textBrowser_11")
        HealtRecord.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=HealtRecord)
        self.statusbar.setObjectName("statusbar")
        HealtRecord.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(parent=HealtRecord)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 741, 24))
        self.menubar.setObjectName("menubar")
        self.menuFront_page = QtWidgets.QMenu(parent=self.menubar)
        self.menuFront_page.setObjectName("menuFront_page")
        self.menum_knkml = QtWidgets.QMenu(parent=self.menubar)
        self.menum_knkml.setObjectName("menum_knkml")
        self.menuAppointments = QtWidgets.QMenu(parent=self.menubar)
        self.menuAppointments.setObjectName("menuAppointments")
        self.menuMessage = QtWidgets.QMenu(parent=self.menubar)
        self.menuMessage.setObjectName("menuMessage")
        self.menu = QtWidgets.QMenu(parent=self.menubar)
        self.menu.setTitle("")
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_2.setObjectName("menu_2")
        HealtRecord.setMenuBar(self.menubar)
        self.menu.addSeparator()
        self.menubar.addAction(self.menuFront_page.menuAction())
        self.menubar.addAction(self.menum_knkml.menuAction())
        self.menubar.addAction(self.menuAppointments.menuAction())
        self.menubar.addAction(self.menuMessage.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(HealtRecord)
        QtCore.QMetaObject.connectSlotsByName(HealtRecord)

    def retranslateUi(self, HealtRecord):
        _translate = QtCore.QCoreApplication.translate
        HealtRecord.setWindowTitle(_translate("HealtRecord", "MainWindow"))
        self.textBrowser_7.setHtml(_translate("HealtRecord", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Date: xx/xx/xxxx - TITLE</p></body></html>"))
        self.textBrowser_3.setHtml(_translate("HealtRecord", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Medicin:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; text-decoration: underline;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Regular basis:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">History:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; text-decoration: underline;\"><br /></p></body></html>"))
        self.textBrowser_10.setHtml(_translate("HealtRecord", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_9.setHtml(_translate("HealtRecord", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Date: xx/xx/xxxx - TITLE</p></body></html>"))
        self.textBrowser_6.setHtml(_translate("HealtRecord", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Date: xx/xx/xxxx - TITLE</p></body></html>"))
        self.pushButton_7.setText(_translate("HealtRecord", "Load more"))
        self.textEdit.setHtml(_translate("HealtRecord", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt;\">Patients Health Record</span></p></body></html>"))
        self.pushButton_2.setText(_translate("HealtRecord", "View"))
        self.textBrowser.setHtml(_translate("HealtRecord", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">+ Add new Record</span></p></body></html>"))
        self.pushButton_8.setText(_translate("HealtRecord", "Edit"))
        self.pushButton_3.setText(_translate("HealtRecord", "View"))
        self.pushButton_6.setText(_translate("HealtRecord", "View"))
        self.textBrowser_5.setHtml(_translate("HealtRecord", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Date: 4/7/2022 - Consultation: Diabetes control</p></body></html>"))
        self.textBrowser_2.setHtml(_translate("HealtRecord", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Patient information:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Name: </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">CPR-number: xxxxxx-xxxx</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Phone number:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adress: </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; text-decoration: underline;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Emergency contact:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Name: </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Phone number:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adress: </p></body></html>"))
        self.pushButton_5.setText(_translate("HealtRecord", "View"))
        self.textBrowser_8.setHtml(_translate("HealtRecord", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Date: xx/xx/xxxx - TITLE</p></body></html>"))
        self.textBrowser_4.setHtml(_translate("HealtRecord", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; text-decoration: underline;\">Previous Records:</span></p></body></html>"))
        self.pushButton_9.setText(_translate("HealtRecord", "View"))
        self.pushButton_10.setText(_translate("HealtRecord", "View"))
        self.textBrowser_11.setHtml(_translate("HealtRecord", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Date: xx/xx/xxxx - TITLE</p></body></html>"))
        self.menuFront_page.setTitle(_translate("HealtRecord", "Front_page"))
        self.menum_knkml.setTitle(_translate("HealtRecord", "Patients_Health_Record"))
        self.menuAppointments.setTitle(_translate("HealtRecord", "Appointments"))
        self.menuMessage.setTitle(_translate("HealtRecord", "Message"))
        self.menu_2.setTitle(_translate("HealtRecord", " "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HealtRecord = QtWidgets.QMainWindow()
    ui = Ui_HealtRecord()
    ui.setupUi(HealtRecord)
    HealtRecord.show()
    sys.exit(app.exec())
