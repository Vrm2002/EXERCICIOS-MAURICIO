from PySide6.QtWidgets import QVBoxLayout, QWidget, QMainWindow, QPushButton
from cadastro_item import Cadastro
from estoque import Estoque
from vendas import Vendas

class MercadoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Sistema de Cadastro e Gestão de Mercado')
        self.setGeometry(100, 100, 600, 400)
        self.produtos = []
        self.compras = []  

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.btn_cadastro_button = QPushButton('Cadastro')
        self.btn_estoque_button = QPushButton('Estoque')
        self.btn_vendas_button = QPushButton('Vendas')

        self.btn_cadastro_button.clicked.connect(self.mostrar_cadastro)
        self.btn_estoque_button.clicked.connect(self.mostrar_estoque)
        self.btn_vendas_button.clicked.connect(self.mostrar_vendas)

        self.layout.addWidget(self.btn_cadastro_button)
        self.layout.addWidget(self.btn_estoque_button)
        self.layout.addWidget(self.btn_vendas_button)

        self.central_widget.setLayout(self.layout)

    def mostrar_cadastro(self):
        self.cadastro_window = Cadastro(self)
        self.cadastro_window.show()

    def mostrar_estoque(self):
        self.estoque_window = Estoque(self)
        self.estoque_window.show()

    def mostrar_vendas(self):
        self.vendas_window = Vendas(self, self.compras)  
        self.vendas_window.show()
