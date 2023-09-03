from PySide6.QtWidgets import QVBoxLayout, QWidget, QComboBox, QLabel, QLineEdit, QPushButton, QMessageBox

class Vendas(QWidget):
    def __init__(self, mercado, text_browser):
        super().__init__()
        self.mercado = mercado
        self.text_browser = text_browser
        self.setWindowTitle('Realizar Venda')
        self.layout = QVBoxLayout()
        self.lista_produtos = QComboBox()
        self.atualizar_lista_produtos()
        self.layout.addWidget(self.lista_produtos)
        self.lbl_quantidade = QLabel('Quantidade Vendida:')
        self.txt_quantidade = QLineEdit()
        self.btn_calcular_button = QPushButton('Calcular Valor')
        self.btn_calcular_button.clicked.connect(self.calcular_valor)
        self.lbl_valor = QLabel('Valor Total:')
        self.layout.addWidget(self.lbl_quantidade)
        self.layout.addWidget(self.txt_quantidade)
        self.layout.addWidget(self.btn_calcular_button)
        self.layout.addWidget(self.lbl_valor)
        self.setLayout(self.layout)

    def atualizar_lista_produtos(self):
        self.lista_produtos.clear()
        for produto in self.mercado.produtos:
            self.lista_produtos.addItem(f'{produto.nome}')

    def calcular_valor(self):
        produto_index = self.lista_produtos.currentIndex()
        quantidade_vendida_text = self.txt_quantidade.text()
        
        if produto_index >= 0:
            produto = self.mercado.produtos[produto_index]
            
            try:
                quantidade_vendida = int(quantidade_vendida_text)
                if quantidade_vendida <= 0 or quantidade_vendida > produto.quantidade:
                    raise ValueError
            except ValueError:
                QMessageBox.warning(self, 'Venda', 'Quantidade em estoque insuficiente, quantidade inválida ou digitou letras.')
                return
            
            valor_total = produto.preco_unitario * quantidade_vendida
            self.lbl_valor.setText(f'Valor Total: R${valor_total:.2f}')
            produto.quantidade -= quantidade_vendida
            self.atualizar_lista_produtos()
            compra_info = f'Produto: {produto.nome} - Quantidade Vendida: {quantidade_vendida} - Valor Total: R${valor_total:.2f}'
            self.mercado.compras.append(compra_info)
            self.text_browser.append(compra_info)  
            QMessageBox.information(self, 'Venda', f'Venda realizada com sucesso! Total: R${valor_total:.2f}')
            self.txt_quantidade.clear()
        else:
            QMessageBox.warning(self, 'Venda', 'Selecione um produto da lista.')