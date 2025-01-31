from PyQt6.QtWidgets import QApplication

from Pantalla_Iniciar_sesion import Login

class MeAgendo():
    def __init__(self):
        self.app = QApplication([])
        self.login = Login()

        self.app.exec()