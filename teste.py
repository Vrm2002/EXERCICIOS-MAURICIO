import sys
from PySide6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora de Impostos")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label_tipo = QLabel("Tipo de Contribuinte:")
        self.layout.addWidget(self.label_tipo)

        self.btn_pessoa_fisica = QPushButton("Pessoa Física")
        self.btn_pessoa_fisica.clicked.connect(self.calcular_imposto_pessoa_fisica)
        self.layout.addWidget(self.btn_pessoa_fisica)

        self.btn_pessoa_juridica = QPushButton("Pessoa Jurídica")
        self.btn_pessoa_juridica.clicked.connect(self.calcular_imposto_pessoa_juridica)
        self.layout.addWidget(self.btn_pessoa_juridica)

        self.result_label = QLabel("")
        self.layout.addWidget(self.result_label)

        self.central_widget.setLayout(self.layout)

    def calcular_imposto_pessoa_fisica(self):
        renda_anual = float(self.get_input("Renda Anual: "))
        gastos_saude = float(self.get_input("Gastos com Saúde: "))

        if renda_anual < 20000:
            imposto = renda_anual * 0.15
        else:
            imposto = renda_anual * 0.25

        if gastos_saude > 0:
            imposto -= gastos_saude * 0.5

        self.result_label.setText(f"Imposto a pagar: R${imposto:.2f}")

    def calcular_imposto_pessoa_juridica(self):
        renda_anual = float(self.get_input("Renda Anual: "))
        num_funcionarios = int(self.get_input("Número de Funcionários: "))

        if num_funcionarios > 10:
            imposto = renda_anual * 0.14
        else:
            imposto = renda_anual * 0.16

        self.result_label.setText(f"Imposto a pagar: R${imposto:.2f}")

    def get_input(self, label_text):
        text, ok = QInputDialog.getText(self, "Input", label_text)
        if ok:
            return text
        return ""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())