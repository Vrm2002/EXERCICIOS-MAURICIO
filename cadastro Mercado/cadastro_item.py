import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox, QListWidget, QMessageBox, QTextBrowser
from produtos import Produto

class Cadastro(QWidget):
    def __init__(self, mercado):
        super().__init__()
        self.mercado = mercado
        self.setWindowTitle('Cadastro de Produtos')
        self.layout = QVBoxLayout()
        self.lbl_nome = QLabel('Nome do Produto:')
        self.txt_nome = QLineEdit()
        self.lbl_preco = QLabel('Preço Unitário:')
        self.txt_preco = QLineEdit()
        self.lbl_quantidade = QLabel('Quantidade em Estoque:')
        self.txt_quantidade = QLineEdit()
        self.btn_cadastrar_button = QPushButton('Cadastrar')
        self.btn_cadastrar_button.clicked.connect(self.cadastrar_produto)
        self.layout.addWidget(self.lbl_nome)
        self.layout.addWidget(self.txt_nome)
        self.layout.addWidget(self.lbl_preco)
        self.layout.addWidget(self.txt_preco)
        self.layout.addWidget(self.lbl_quantidade)
        self.layout.addWidget(self.txt_quantidade)
        self.layout.addWidget(self.btn_cadastrar_button)
        self.setLayout(self.layout)

    def cadastrar_produto(self):
        nome = self.txt_nome.text()
        preco = self.txt_preco.text()
        quantidade = self.txt_quantidade.text()

        if not nome.isalpha():
            QMessageBox.warning(self, 'Cadastro', 'O nome do produto deve conter apenas letras e caracteres válidos.')
            return

        try:
            quantidade = int(quantidade)
        except ValueError:
            QMessageBox.warning(self, 'Cadastro', 'A quantidade deve ser um número inteiro válido.')
            return

        try:
            preco = float(preco)
        except ValueError:
            QMessageBox.warning(self, 'Cadastro', 'O preço deve ser um número válido.')
            return

        for produto in self.mercado.produtos:
            if produto.nome == nome:
                QMessageBox.warning(self, 'Cadastro', 'Produto com o mesmo nome já existe.')
                return

        produtos = Produto(nome, preco, quantidade)
        self.mercado.produtos.append(produtos)
        self.txt_nome.clear()
        self.txt_preco.clear()
        self.txt_quantidade.clear()
        QMessageBox.information(self, 'Cadastro', 'Produto cadastrado com sucesso!')