from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QFont, Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QFrame, QLabel, QLineEdit, QPushButton, QTextBrowser, QSizePolicy, QComboBox
from Cadastro_pJuridico import Juridico
from error_mensagens import MensagemErro


class Ui_MainWindow_Juridico(QWidget):
    def __init__(self):
        super().__init__()
        self.centralwidget = QWidget()
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_titulo = QLabel(self.frame_2)
        self.lbl_titulo.setObjectName(u"lbl_titulo")
        font = QFont()
        font.setPointSize(15)
        self.lbl_titulo.setFont(font)

        self.verticalLayout.addWidget(self.lbl_titulo)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.lbl_nomeJ = QLabel(self.frame)
        self.lbl_nomeJ.setObjectName(u"lbl_nomeJ")
        font1 = QFont()
        font1.setPointSize(10)
        self.lbl_nomeJ.setFont(font1)

        self.verticalLayout_2.addWidget(self.lbl_nomeJ)

        self.txt_nomeJ = QLineEdit(self.frame)
        self.txt_nomeJ.setObjectName(u"txt_nomeJ")

        self.verticalLayout_2.addWidget(self.txt_nomeJ)

        self.lbl_rendaJ = QLabel(self.frame)
        self.lbl_rendaJ.setObjectName(u"lbl_rendaJ")
        self.lbl_rendaJ.setFont(font1)

        self.verticalLayout_2.addWidget(self.lbl_rendaJ)

        self.txt_rendaJ = QLineEdit(self.frame)
        self.txt_rendaJ.setObjectName(u"txt_rendaJ")

        self.verticalLayout_2.addWidget(self.txt_rendaJ)

        self.lbl_gastosJ = QLabel(self.frame)
        self.lbl_gastosJ.setObjectName(u"lbl_gastosJ")
        self.lbl_gastosJ.setFont(font1)

        self.verticalLayout_2.addWidget(self.lbl_gastosJ)

        self.cb_numero_funcionario = QComboBox(self.frame)
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.addItem("")
        self.cb_numero_funcionario.setObjectName(u"cb_numero_funcionario")

        self.verticalLayout_2.addWidget(self.cb_numero_funcionario, 0, Qt.AlignLeft)

        self.btn_cadastroJ = QPushButton(self.frame)
        self.btn_cadastroJ.setObjectName(u"btn_cadastroJ")
        self.btn_cadastroJ.setFont(font1)
        self.btn_cadastroJ.clicked.connect(self.pessoa_juridica_cadastro)

        self.verticalLayout_2.addWidget(self.btn_cadastroJ)


        self.verticalLayout_3.addWidget(self.frame)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.textBrowser)

        self.btn_cadastrar = QPushButton(self.centralwidget)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setFont(font1)
        self.btn_cadastrar.setLayoutDirection(Qt.LeftToRight)
        self.btn_cadastrar.setAutoDefault(False)

        self.verticalLayout_3.addWidget(self.btn_cadastrar, 0, Qt.AlignRight)

        self.setLayout(self.verticalLayout_3)
        self.lbl_titulo.setText(QCoreApplication.translate("MainWindow", u"Cadastro Pessoa Jur\u00eddica", None))
        self.lbl_nomeJ.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.lbl_rendaJ.setText(QCoreApplication.translate("MainWindow", u"Renda Anual", None))
        self.lbl_gastosJ.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de Funcion\u00e1rios", None))
        self.cb_numero_funcionario.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.cb_numero_funcionario.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.cb_numero_funcionario.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.cb_numero_funcionario.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.cb_numero_funcionario.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.cb_numero_funcionario.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.cb_numero_funcionario.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.cb_numero_funcionario.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))
        self.cb_numero_funcionario.setItemText(8, QCoreApplication.translate("MainWindow", u"8", None))
        self.cb_numero_funcionario.setItemText(9, QCoreApplication.translate("MainWindow", u"9", None))
        self.cb_numero_funcionario.setItemText(10, QCoreApplication.translate("MainWindow", u"10", None))
        self.cb_numero_funcionario.setItemText(11, QCoreApplication.translate("MainWindow", u"11", None))
        self.cb_numero_funcionario.setItemText(12, QCoreApplication.translate("MainWindow", u"12", None))
        self.cb_numero_funcionario.setItemText(13, QCoreApplication.translate("MainWindow", u"13", None))
        self.cb_numero_funcionario.setItemText(14, QCoreApplication.translate("MainWindow", u"14", None))
        self.cb_numero_funcionario.setItemText(15, QCoreApplication.translate("MainWindow", u"15", None))
        self.cb_numero_funcionario.setItemText(16, QCoreApplication.translate("MainWindow", u"16", None))
        self.cb_numero_funcionario.setItemText(17, QCoreApplication.translate("MainWindow", u"17", None))
        self.cb_numero_funcionario.setItemText(18, QCoreApplication.translate("MainWindow", u"18", None))
        self.cb_numero_funcionario.setItemText(19, QCoreApplication.translate("MainWindow", u"19", None))
        self.cb_numero_funcionario.setItemText(20, QCoreApplication.translate("MainWindow", u"20", None))
        self.cb_numero_funcionario.setItemText(21, QCoreApplication.translate("MainWindow", u"21", None))
        self.cb_numero_funcionario.setItemText(22, QCoreApplication.translate("MainWindow", u"22", None))
        self.cb_numero_funcionario.setItemText(23, QCoreApplication.translate("MainWindow", u"23", None))
        self.cb_numero_funcionario.setItemText(24, QCoreApplication.translate("MainWindow", u"24", None))
        self.cb_numero_funcionario.setItemText(25, QCoreApplication.translate("MainWindow", u"25", None))
        self.cb_numero_funcionario.setItemText(26, QCoreApplication.translate("MainWindow", u"26", None))
        self.cb_numero_funcionario.setItemText(27, QCoreApplication.translate("MainWindow", u"27", None))
        self.cb_numero_funcionario.setItemText(28, QCoreApplication.translate("MainWindow", u"28", None))
        self.cb_numero_funcionario.setItemText(29, QCoreApplication.translate("MainWindow", u"29", None))
        self.cb_numero_funcionario.setItemText(30, QCoreApplication.translate("MainWindow", u"30", None))
        self.cb_numero_funcionario.setItemText(31, QCoreApplication.translate("MainWindow", u"31", None))
        self.cb_numero_funcionario.setItemText(32, QCoreApplication.translate("MainWindow", u"32", None))
        self.cb_numero_funcionario.setItemText(33, QCoreApplication.translate("MainWindow", u"33", None))
        self.cb_numero_funcionario.setItemText(34, QCoreApplication.translate("MainWindow", u"34", None))
        self.cb_numero_funcionario.setItemText(35, QCoreApplication.translate("MainWindow", u"35", None))
        self.cb_numero_funcionario.setItemText(36, QCoreApplication.translate("MainWindow", u"36", None))
        self.cb_numero_funcionario.setItemText(37, QCoreApplication.translate("MainWindow", u"37", None))
        self.cb_numero_funcionario.setItemText(38, QCoreApplication.translate("MainWindow", u"38", None))
        self.cb_numero_funcionario.setItemText(39, QCoreApplication.translate("MainWindow", u"39", None))
        self.cb_numero_funcionario.setItemText(40, QCoreApplication.translate("MainWindow", u"40", None))
        self.cb_numero_funcionario.setItemText(41, QCoreApplication.translate("MainWindow", u"41", None))
        self.cb_numero_funcionario.setItemText(42, QCoreApplication.translate("MainWindow", u"42", None))
        self.cb_numero_funcionario.setItemText(43, QCoreApplication.translate("MainWindow", u"43", None))
        self.cb_numero_funcionario.setItemText(44, QCoreApplication.translate("MainWindow", u"44", None))
        self.cb_numero_funcionario.setItemText(45, QCoreApplication.translate("MainWindow", u"45", None))
        self.cb_numero_funcionario.setItemText(46, QCoreApplication.translate("MainWindow", u"46", None))
        self.cb_numero_funcionario.setItemText(47, QCoreApplication.translate("MainWindow", u"47", None))
        self.cb_numero_funcionario.setItemText(48, QCoreApplication.translate("MainWindow", u"48", None))
        self.cb_numero_funcionario.setItemText(49, QCoreApplication.translate("MainWindow", u"49", None))
        self.cb_numero_funcionario.setItemText(50, QCoreApplication.translate("MainWindow", u"50", None))
        self.cb_numero_funcionario.setItemText(51, QCoreApplication.translate("MainWindow", u"51", None))
        self.cb_numero_funcionario.setItemText(52, QCoreApplication.translate("MainWindow", u"52", None))
        self.cb_numero_funcionario.setItemText(53, QCoreApplication.translate("MainWindow", u"53", None))
        self.cb_numero_funcionario.setItemText(54, QCoreApplication.translate("MainWindow", u"54", None))
        self.cb_numero_funcionario.setItemText(55, QCoreApplication.translate("MainWindow", u"55", None))
        self.cb_numero_funcionario.setItemText(56, QCoreApplication.translate("MainWindow", u"56", None))
        self.cb_numero_funcionario.setItemText(57, QCoreApplication.translate("MainWindow", u"57", None))
        self.cb_numero_funcionario.setItemText(58, QCoreApplication.translate("MainWindow", u"58", None))
        self.cb_numero_funcionario.setItemText(59, QCoreApplication.translate("MainWindow", u"59", None))
        self.cb_numero_funcionario.setItemText(60, QCoreApplication.translate("MainWindow", u"60", None))
        self.cb_numero_funcionario.setItemText(61, QCoreApplication.translate("MainWindow", u"61", None))
        self.cb_numero_funcionario.setItemText(62, QCoreApplication.translate("MainWindow", u"62", None))
        self.cb_numero_funcionario.setItemText(63, QCoreApplication.translate("MainWindow", u"63", None))
        self.cb_numero_funcionario.setItemText(64, QCoreApplication.translate("MainWindow", u"64", None))
        self.cb_numero_funcionario.setItemText(65, QCoreApplication.translate("MainWindow", u"65", None))
        self.cb_numero_funcionario.setItemText(66, QCoreApplication.translate("MainWindow", u"66", None))
        self.cb_numero_funcionario.setItemText(67, QCoreApplication.translate("MainWindow", u"67", None))
        self.cb_numero_funcionario.setItemText(68, QCoreApplication.translate("MainWindow", u"68", None))
        self.cb_numero_funcionario.setItemText(69, QCoreApplication.translate("MainWindow", u"69", None))
        self.cb_numero_funcionario.setItemText(70, QCoreApplication.translate("MainWindow", u"70", None))
        self.cb_numero_funcionario.setItemText(71, QCoreApplication.translate("MainWindow", u"71", None))
        self.cb_numero_funcionario.setItemText(72, QCoreApplication.translate("MainWindow", u"72", None))
        self.cb_numero_funcionario.setItemText(73, QCoreApplication.translate("MainWindow", u"73", None))
        self.cb_numero_funcionario.setItemText(74, QCoreApplication.translate("MainWindow", u"74", None))
        self.cb_numero_funcionario.setItemText(75, QCoreApplication.translate("MainWindow", u"75", None))
        self.cb_numero_funcionario.setItemText(76, QCoreApplication.translate("MainWindow", u"76", None))
        self.cb_numero_funcionario.setItemText(77, QCoreApplication.translate("MainWindow", u"77", None))
        self.cb_numero_funcionario.setItemText(78, QCoreApplication.translate("MainWindow", u"78", None))
        self.cb_numero_funcionario.setItemText(79, QCoreApplication.translate("MainWindow", u"79", None))
        self.cb_numero_funcionario.setItemText(80, QCoreApplication.translate("MainWindow", u"80", None))
        self.cb_numero_funcionario.setItemText(81, QCoreApplication.translate("MainWindow", u"81", None))
        self.cb_numero_funcionario.setItemText(82, QCoreApplication.translate("MainWindow", u"82", None))
        self.cb_numero_funcionario.setItemText(83, QCoreApplication.translate("MainWindow", u"83", None))
        self.cb_numero_funcionario.setItemText(84, QCoreApplication.translate("MainWindow", u"84", None))
        self.cb_numero_funcionario.setItemText(85, QCoreApplication.translate("MainWindow", u"85", None))
        self.cb_numero_funcionario.setItemText(86, QCoreApplication.translate("MainWindow", u"86", None))
        self.cb_numero_funcionario.setItemText(87, QCoreApplication.translate("MainWindow", u"87", None))
        self.cb_numero_funcionario.setItemText(88, QCoreApplication.translate("MainWindow", u"88", None))
        self.cb_numero_funcionario.setItemText(89, QCoreApplication.translate("MainWindow", u"89", None))
        self.cb_numero_funcionario.setItemText(90, QCoreApplication.translate("MainWindow", u"90", None))
        self.cb_numero_funcionario.setItemText(91, QCoreApplication.translate("MainWindow", u"91", None))
        self.cb_numero_funcionario.setItemText(92, QCoreApplication.translate("MainWindow", u"92", None))
        self.cb_numero_funcionario.setItemText(93, QCoreApplication.translate("MainWindow", u"93", None))
        self.cb_numero_funcionario.setItemText(94, QCoreApplication.translate("MainWindow", u"94", None))
        self.cb_numero_funcionario.setItemText(95, QCoreApplication.translate("MainWindow", u"95", None))
        self.cb_numero_funcionario.setItemText(96, QCoreApplication.translate("MainWindow", u"96", None))
        self.cb_numero_funcionario.setItemText(97, QCoreApplication.translate("MainWindow", u"97", None))
        self.cb_numero_funcionario.setItemText(98, QCoreApplication.translate("MainWindow", u"98", None))
        self.cb_numero_funcionario.setItemText(99, QCoreApplication.translate("MainWindow", u"99", None))
        self.cb_numero_funcionario.setItemText(100, QCoreApplication.translate("MainWindow", u"100", None))

        self.btn_cadastroJ.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.total_imposto = []
    # retranslateUi

    def pessoa_juridica_cadastro(self):
        try:
            nome = self.txt_nomeJ.text()
            renda_anual = float(self.txt_rendaJ.text())
            num_func = self.cb_numero_funcionario.currentIndex()


        except:
            self.erro_mensagem = MensagemErro()
            self.erro_mensagem.erro_cadastro()


        else:
            if renda_anual <= 0:
                self.erro_mensagem.erro_cadastro()
                pass
            
            else:
                pessoa_juridica = Juridico(num_func,nome,renda_anual)
                self.total_imposto.append(pessoa_juridica.imposto())
                total_imposto = sum(self.total_imposto)
                self.textBrowser.append(f"Nome: {pessoa_juridica.nome}\nRenda_Anual: {pessoa_juridica.renda}\nImposto Arrecadado: {pessoa_juridica.imposto()}")
                self.textBrowser.append(f"\nTotal de Imposto Arrecadado: {total_imposto}")
                

    def voltar(self):
        self.hide()



