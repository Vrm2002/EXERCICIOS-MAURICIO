from cadastro_banco_ui import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    app.exec()