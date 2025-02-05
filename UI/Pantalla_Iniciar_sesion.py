from PyQt6 import uic,QtCore, QtGui
from PyQt6.QtWidgets import QMessageBox, QMainWindow
import test_rc

class Login:
    def __init__(self):
        self.login = uic.loadUi("UI\Pantalla_Iniciar_sesion.ui")
        self.initGUI()
        self.login.lblMensaje.setText("")
        self.login.show()

    def ingresar(self):
        if len(self.login.txtUsuario.text()) < 2 and len(self.login.txtClave.text()) < 2:
            self.login.lblMensaje.setText("Usuario y/o contraseña no validos")
        elif len(self.login.txtUsuario.text()) < 2:
            self.login.lblMensaje.setText("Ingrese un nombre de Usuario Valido")
            self.login.txtUsuario.setFocus()
        elif len(self.login.txtClave.text()) < 2:
            self.login.lblMensaje.setText("Clave invalida")
            self.login.txtClave.setFocus()
        else:
            self.login.lblMensaje.setText("")
            pass
    def initGUI(self):
            self.login.btnAcceder.clicked.connect(self.ingresar)