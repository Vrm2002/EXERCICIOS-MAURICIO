from PySide6.QtWidgets import QVBoxLayout, QListWidget, QWidget

class Estoque(QWidget):
    def __init__(self, mercado):
        super().__init__()
        self.mercado = mercado
        self.setWindowTitle('Estoque de Produtos')
        self.layout = QVBoxLayout()
        self.list_produtos = QListWidget()
        self.atualizar_lista_produtos()
        self.layout.addWidget(self.list_produtos)
        self.setLayout(self.layout)

    def atualizar_lista_produtos(self):
        self.list_produtos.clear()
        for produto in self.mercado.produtos:
            self.list_produtos.addItem(f'{produto.nome} - Preço: R${produto.preco_unitario:.2f} - Estoque: {produto.quantidade}')