import sys, re
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QTextBrowser, QCheckBox, QComboBox, QDateEdit, QMessageBox
from datetime import datetime
from paciente import Paciente


class Consultorio(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Consultório Médico")
        self.setGeometry(100, 100, 1000, 500)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.lbl_dados_paciente = QLabel("Digite os dados do paciente:")
        self.layout.addWidget(self.lbl_dados_paciente)

        self.txt_nome = QLineEdit()
        self.txt_nome.setPlaceholderText("Nome")
        self.layout.addWidget(self.txt_nome)

        self.txt_telefone = QLineEdit()
        self.txt_telefone.setPlaceholderText("Telefone")
        self.layout.addWidget(self.txt_telefone)

        self.txt_email = QLineEdit()
        self.txt_email.setPlaceholderText("Email")
        self.layout.addWidget(self.txt_email)

        self.lbl_sexo = QLabel("sexo:")
        self.cb_genero = QComboBox()
        self.cb_genero.addItem("Outro")
        self.cb_genero.addItem("Masculino")
        self.cb_genero.addItem("Feminino")
        self.layout.addWidget(self.lbl_sexo)
        self.layout.addWidget(self.cb_genero)

        self.lbl_data_nascimento = QLabel("Data de nascimento:")
        self.txt_data_nascimento = QDateEdit()
        self.txt_data_nascimento.setDisplayFormat("dd/MM/yyyy")
        self.txt_data_nascimento.setCalendarPopup(True)
        self.layout.addWidget(self.lbl_data_nascimento)
        self.layout.addWidget(self.txt_data_nascimento)

        self.ck_pcd = QCheckBox("Pessoa com Deficiência")
        self.layout.addWidget(self.ck_pcd)

        self.btn_cadastrar_botao = QPushButton("Cadastrar Paciente")
        self.btn_cadastrar_botao.clicked.connect(self.cadastrar_paciente)
        self.layout.addWidget(self.btn_cadastrar_botao)

        self.btn_chamar_proximo_botao = QPushButton("Chamar Próximo")
        self.btn_chamar_proximo_botao.clicked.connect(self.chamar_proximo_paciente)
        self.layout.addWidget(self.btn_chamar_proximo_botao)

        self.txtb_exibir_fila = QTextBrowser()
        self.layout.addWidget(self.txtb_exibir_fila)

        self.central_widget.setLayout(self.layout)

        self.fila_espera = []

    def cadastrar_paciente(self):
        
        nome = self.txt_nome.text()
        telefone = self.txt_telefone.text()
        email = self.txt_email.text()
        genero = self.cb_genero.currentText()
        data_nascimento = self.txt_data_nascimento.date().toPython()
        pcd = self.ck_pcd.isChecked()
        
        if not (email and genero and data_nascimento):
            QMessageBox.warning(self, "Erro", "Todos os campos devem ser preenchidos.")
            return
        
        if not nome:
            QMessageBox.warning(self, "Erro", "O campo Nome deve ser preenchido.")
            return
        
        if not re.match(r'^[A-Za-z\s]*$', nome):
            QMessageBox.warning(self, "Erro", "O campo Nome não deve conter números.")
            return
        
        if not telefone:
            QMessageBox.warning(self, "Erro", "O campo Telefone deve ser preenchido.")
            return
        
        if not re.match(r'^\d+$', telefone):
            QMessageBox.warning(self, "Erro", "O campo Telefone deve conter apenas números.")
            return
        
        
        QMessageBox.information(self, "Sucesso", "Cadastro realizado com sucesso!")
        paciente = Paciente(nome, telefone, email, genero, data_nascimento, pcd)

        hora_chegada = datetime.now() 

        paciente.chegada_fila = hora_chegada  

        self.adicionar_paciente_na_fila(paciente)

        self.txtb_exibir_fila.append(f"Paciente cadastrado: {paciente}")

        self.txt_nome.clear()
        self.txt_telefone.clear()
        self.txt_email.clear()
        self.cb_genero.setCurrentIndex(0)
        self.txt_data_nascimento.setDate(datetime.now().date())
        self.ck_pcd.setChecked(False)

    def adicionar_paciente_na_fila(self, paciente):
        if self.ck_pcd.isChecked():
    
            self.fila_espera.insert(0,paciente)
            
        else:
            self.fila_espera.append(paciente)
        self.atualizar_fila()

    def atualizar_fila(self):
        self.fila_espera.sort(key=lambda paciente: (paciente.data_nascimento, paciente.pcd, paciente.genero, paciente.chegada_fila))
        self.txtb_exibir_fila.clear()
        for contador_fila, paciente in enumerate(self.fila_espera):
            self.txtb_exibir_fila.append(f"{contador_fila+1}. {paciente.nome} - {'PCD' if paciente.pcd else 'Não PCD'} - Data De Nascimento: {paciente.data_nascimento} - Genero: {paciente.genero} - Horario do cadastro {paciente.chegada_fila}") 
            
    def chamar_proximo_paciente(self):
        if self.fila_espera:
            paciente_chamado = self.fila_espera.pop(0)
            self.txtb_exibir_fila.clear()
            self.txtb_exibir_fila.append(f"Chamando: {paciente_chamado.nome}")
            self.atualizar_fila()
        else:
            self.txtb_exibir_fila.clear()
            self.txtb_exibir_fila.append("A fila está vazia.")