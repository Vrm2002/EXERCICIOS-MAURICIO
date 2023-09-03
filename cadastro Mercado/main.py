from PySide6.QtWidgets import QApplication
from mercado_app import MercadoApp
import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mercado_app = MercadoApp()
    mercado_app.show()
    sys.exit(app.exec())