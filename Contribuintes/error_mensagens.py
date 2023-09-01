from PySide6.QtWidgets import QMessageBox


class MensagemErro(QMessageBox):
    def __init__(self):
        super().__init__()


    def erro_cadastro(self):
        self.mensagem_erro = QMessageBox()
        self.mensagem_erro.setText("Erro nos dados informados.")
        self.mensagem_erro.setIcon(QMessageBox.Warning)
        self.mensagem_erro.show()
