from Cadastro_exercircio3_ui import *
from Cadastro_pessoa_juridica_ui import *



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    app.exec()