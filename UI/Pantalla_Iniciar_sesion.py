from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox, QMainWindow

class Login():
    def __init__(self):
        self.login = uic.loadUi("Pantalla_Iniciar_sesion.ui")
        self.login.lblMensaje.setText("")
        self.login.show()

    def ingresar(self):
        if len(self.Pantalla_Iniciar_sesion.txtUsuario.text()) < 2:
            self.login.lblMensaje.setText("Ingrese un nombre de Usuario Valido")
        elif len(self.Pantalla_Iniciar_sesion.txtClave.text()) < 2:
            self.login.lblMensaje.setText("Clave invalida")
        else:
            pass