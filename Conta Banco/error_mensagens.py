from PySide6.QtWidgets import QMessageBox


class MensagemErro(QMessageBox):
    def __init__(self):
        super().__init__()

        self.msg = QMessageBox
        self.msg.setText("Erro na coleta de dados!")
        self.msg.setIcon(QMessageBox.Warning)