from PySide6.QtWidgets import QMessageBox


class MensagemErro(QMessageBox):
    def __init__(self):
        super().__init__()


    def erro_cadastro(self):
        self.mensagem_erro = QMessageBox()
        self.mensagem_erro.setText("Erro nos dados informados.")
        self.mensagem_erro.setIcon(QMessageBox.Warning)
        self.mensagem_erro.show()


    def erro_deposito_sacar(self):
        self.mensagem_erro = QMessageBox()
        self.mensagem_erro.setText("O valor informado é inválido.")
        self.mensagem_erro.setIcon(QMessageBox.Warning)
        self.mensagem_erro.show()


    def erro_saldo_insuf(self):
        self.mensagem_erro = QMessageBox()
        self.mensagem_erro.setText("Saldo Insuficiente.")
        self.mensagem_erro.setIcon(QMessageBox.Warning)
        self.mensagem_erro.show()