from PySide6.QtWidgets import QApplication
from Cadastro_Paciente import Consultorio
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    consultorio = Consultorio()
    consultorio.show()
    sys.exit(app.exec())