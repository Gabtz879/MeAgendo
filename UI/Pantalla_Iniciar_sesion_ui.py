# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Pantalla_Iniciar_sesion.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)
import test_rc
import test_rc
import test_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(750, 521)
        MainWindow.setMinimumSize(QSize(750, 521))
        MainWindow.setMaximumSize(QSize(750, 500))
        MainWindow.setStyleSheet(u"QWidget#centralwidget{background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:0.994318 rgba(219, 208, 242, 255));}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 100, 281, 71))
        self.label.setStyleSheet(u"font: 900 26pt \"Segoe UI\";\n"
"color: rgb(2, 165, 163);")
        self.btnAcceder = QPushButton(self.centralwidget)
        self.btnAcceder.setObjectName(u"btnAcceder")
        self.btnAcceder.setGeometry(QRect(130, 330, 121, 31))
        self.btnAcceder.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAcceder.setStyleSheet(u"background-color: rgb(43, 182, 179);\n"
"selection-color: rgb(71, 71, 71);\n"
"border-color: rgb(111, 221, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 9pt \"Cascadia Code\";")
        self.txtUsuario = QLineEdit(self.centralwidget)
        self.txtUsuario.setObjectName(u"txtUsuario")
        self.txtUsuario.setGeometry(QRect(90, 200, 201, 21))
        self.txtUsuario.setStyleSheet(u"\n"
"border-color: rgb(0, 0, 0);")
        self.txtUsuario.setDragEnabled(True)
        self.txtUsuario.setClearButtonEnabled(True)
        self.txtClave = QLineEdit(self.centralwidget)
        self.txtClave.setObjectName(u"txtClave")
        self.txtClave.setGeometry(QRect(90, 250, 201, 21))
        self.txtClave.setEchoMode(QLineEdit.EchoMode.Password)
        self.txtClave.setDragEnabled(True)
        self.txtClave.setClearButtonEnabled(True)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(390, 0, 360, 501))
        self.label_2.setStyleSheet(u"border-image: url(:/prefijoNuevo/Fondo MeAgendo #1.jpeg);")
        self.label_2.setPixmap(QPixmap(u":/prefijoNuevo/Fondo MeAgendo #1.jpeg"))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 40, 71, 21))
        self.label_3.setStyleSheet(u"font: 9pt \"Cascadia Code\";\n"
"color: rgb(255, 255, 255);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 20, 41, 51))
        self.label_4.setStyleSheet(u"border-image: url(:/prefijoNuevo/Logo #1 Meagendo.jpeg);")
        self.label_4.setPixmap(QPixmap(u":/prefijoNuevo/Logo #1 Meagendo.png"))
        self.label_4.setScaledContents(True)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(430, 120, 291, 71))
        self.label_5.setStyleSheet(u"font: 900 26pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(430, 200, 291, 41))
        self.label_6.setStyleSheet(u"font: 9pt \"Cascadia Code\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(510, 260, 121, 41))
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(43, 182, 179);\n"
"border-bottom-color: rgb(85, 85, 255);\n"
"border-color: rgb(111, 221, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 9pt \"Cascadia Code\";\n"
"border-radius:10px;")
        self.lblMensaje = QLabel(self.centralwidget)
        self.lblMensaje.setObjectName(u"lblMensaje")
        self.lblMensaje.setGeometry(QRect(80, 380, 231, 20))
        font = QFont()
        font.setFamilies([u"Cascadia Code"])
        self.lblMensaje.setFont(font)
        self.lblMensaje.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.btnMenu = QPushButton(self.centralwidget)
        self.btnMenu.setObjectName(u"btnMenu")
        self.btnMenu.setGeometry(QRect(90, 290, 201, 20))
        self.btnMenu.setMinimumSize(QSize(1, 16))
        self.btnMenu.setMaximumSize(QSize(16777215, 16777215))
        self.btnMenu.setSizeIncrement(QSize(0, 80))
        self.btnMenu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnMenu.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"background: transparent;\n"
"font: 600 9pt \"Cascadia Code\";\n"
"}\n"
"")
        self.btnMenu.setIconSize(QSize(30, 30))
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_2.raise_()
        self.label.raise_()
        self.btnAcceder.raise_()
        self.txtUsuario.raise_()
        self.txtClave.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.pushButton_2.raise_()
        self.lblMensaje.raise_()
        self.btnMenu.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Iniciar sesi\u00f3n</p></body></html>", None))
        self.btnAcceder.setText(QCoreApplication.translate("MainWindow", u"Iniciar sesi\u00f3n", None))
        self.txtUsuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"    Usuario", None))
        self.txtClave.setPlaceholderText(QCoreApplication.translate("MainWindow", u"     Clave", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">MeAgendo</span></p></body></html>", None))
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:400;\">\u00a1Hola de nuevo!</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Cascadia Code'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Introduce tus datos para continuar</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">gestionando tus tareas y eventos</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Crear Cuenta", None))
        self.lblMensaje.setText(QCoreApplication.translate("MainWindow", u"Usuario y/o contrase\u00f1a no validos", None))
        self.btnMenu.setText(QCoreApplication.translate("MainWindow", u"\u00bfOlvidaste tu contrase\u00f1a?", None))
    # retranslateUi

