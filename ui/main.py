import archivo_rc
from PyQt6 import QtGui
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve
from PyQt6.QtWidgets import QApplication, QMainWindow, QSizePolicy
import sys
from sidebar import Ui_Principal

class Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Principal()
        self.ui.setupUi(self)

        self.ui.btnPrincipal.clicked.connect(
            lambda: self.ui.paginas.setCurrentWidget(self.ui.principal)
        )
        self.ui.btnListaPendientes.clicked.connect(
            lambda: self.ui.paginas.setCurrentWidget(self.ui.listaPendientes)
        )
        self.ui.btnCalendario.clicked.connect(
            lambda: self.ui.paginas.setCurrentWidget(self.ui.calendario)
        )
        self.ui.btnPomodoro.clicked.connect(
            lambda: self.ui.paginas.setCurrentWidget(self.ui.pomodoro)
        )

        self.ui.btnMenu.clicked.connect(self.expandir)

        # Ajuste inicial del ancho del menú derecho
        self.ui.menuDerecho.setMinimumWidth(50)

    def expandir(self):
        ancho = self.ui.menuDerecho.width()
        nuevoAncho = 50

        if ancho == 50:
            nuevoAncho = 180
            self.ui.btnMenu.setIcon(QtGui.QIcon(":/Iconos/Iconos/Expandir.png"))
        elif ancho == 180:
            nuevoAncho = 50
            self.ui.btnMenu.setIcon(QtGui.QIcon(":/Iconos/Iconos/Icono menu.png"))

        print(f"Ancho actual: {ancho}, Nuevo ancho: {nuevoAncho}")  # Mensaje de depuración

        try:
            # Crear animación de la propiedad "minimumWidth"
            self.animacion = QPropertyAnimation(self.ui.menuDerecho, b"minimumWidth")
            self.animacion.setStartValue(ancho)
            self.animacion.setEndValue(nuevoAncho)
            self.animacion.setDuration(350)
            self.animacion.setEasingCurve(QEasingCurve.Type.InOutQuad)
            self.animacion.start()
            print("Animación iniciada correctamente.")  # Mensaje de depuración
        except Exception as e:
            print("Error en la animación:", e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Principal()
    window.show()
    sys.exit(app.exec())
