# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Pagamento Dos Funcionarios.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1076, 830)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_pagamento_funcionarios = QFrame(self.centralwidget)
        self.frame_pagamento_funcionarios.setObjectName(u"frame_pagamento_funcionarios")
        self.frame_pagamento_funcionarios.setFrameShape(QFrame.StyledPanel)
        self.frame_pagamento_funcionarios.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_pagamento_funcionarios)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lbl_pagamento_dos_funcionarios = QLabel(self.frame_pagamento_funcionarios)
        self.lbl_pagamento_dos_funcionarios.setObjectName(u"lbl_pagamento_dos_funcionarios")

        self.verticalLayout_6.addWidget(self.lbl_pagamento_dos_funcionarios)

        self.frame_nome = QFrame(self.frame_pagamento_funcionarios)
        self.frame_nome.setObjectName(u"frame_nome")
        self.frame_nome.setFrameShape(QFrame.StyledPanel)
        self.frame_nome.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_nome)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_nome = QLabel(self.frame_nome)
        self.lbl_nome.setObjectName(u"lbl_nome")

        self.verticalLayout.addWidget(self.lbl_nome)

        self.txt_nome = QLineEdit(self.frame_nome)
        self.txt_nome.setObjectName(u"txt_nome")

        self.verticalLayout.addWidget(self.txt_nome)


        self.verticalLayout_6.addWidget(self.frame_nome)

        self.frame_horas_trabalhadas = QFrame(self.frame_pagamento_funcionarios)
        self.frame_horas_trabalhadas.setObjectName(u"frame_horas_trabalhadas")
        self.frame_horas_trabalhadas.setFrameShape(QFrame.StyledPanel)
        self.frame_horas_trabalhadas.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_horas_trabalhadas)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_horas_trabalhadas = QLabel(self.frame_horas_trabalhadas)
        self.lbl_horas_trabalhadas.setObjectName(u"lbl_horas_trabalhadas")

        self.verticalLayout_2.addWidget(self.lbl_horas_trabalhadas)

        self.txt_horas_trabalhadas = QLineEdit(self.frame_horas_trabalhadas)
        self.txt_horas_trabalhadas.setObjectName(u"txt_horas_trabalhadas")

        self.verticalLayout_2.addWidget(self.txt_horas_trabalhadas)


        self.verticalLayout_6.addWidget(self.frame_horas_trabalhadas)

        self.frame_valor_horas = QFrame(self.frame_pagamento_funcionarios)
        self.frame_valor_horas.setObjectName(u"frame_valor_horas")
        self.frame_valor_horas.setFrameShape(QFrame.StyledPanel)
        self.frame_valor_horas.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_valor_horas)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_valor_horas = QLabel(self.frame_valor_horas)
        self.lbl_valor_horas.setObjectName(u"lbl_valor_horas")

        self.verticalLayout_3.addWidget(self.lbl_valor_horas)

        self.txt_valor_horas = QLineEdit(self.frame_valor_horas)
        self.txt_valor_horas.setObjectName(u"txt_valor_horas")

        self.verticalLayout_3.addWidget(self.txt_valor_horas)


        self.verticalLayout_6.addWidget(self.frame_valor_horas)

        self.frame_despesa_funcionario_terceirizado = QFrame(self.frame_pagamento_funcionarios)
        self.frame_despesa_funcionario_terceirizado.setObjectName(u"frame_despesa_funcionario_terceirizado")
        self.frame_despesa_funcionario_terceirizado.setFrameShape(QFrame.StyledPanel)
        self.frame_despesa_funcionario_terceirizado.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_despesa_funcionario_terceirizado)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lbl_despesa_funcionario_terceirizado = QLabel(self.frame_despesa_funcionario_terceirizado)
        self.lbl_despesa_funcionario_terceirizado.setObjectName(u"lbl_despesa_funcionario_terceirizado")

        self.verticalLayout_5.addWidget(self.lbl_despesa_funcionario_terceirizado)

        self.txt_despesa_funcionario_terceirizado = QLineEdit(self.frame_despesa_funcionario_terceirizado)
        self.txt_despesa_funcionario_terceirizado.setObjectName(u"txt_despesa_funcionario_terceirizado")

        self.verticalLayout_5.addWidget(self.txt_despesa_funcionario_terceirizado)


        self.verticalLayout_6.addWidget(self.frame_despesa_funcionario_terceirizado)

        self.ck_funcionarios_terceirizado = QCheckBox(self.frame_pagamento_funcionarios)
        self.ck_funcionarios_terceirizado.setObjectName(u"ck_funcionarios_terceirizado")

        self.verticalLayout_6.addWidget(self.ck_funcionarios_terceirizado)

        self.ck_funcionario_proprios = QCheckBox(self.frame_pagamento_funcionarios)
        self.ck_funcionario_proprios.setObjectName(u"ck_funcionario_proprios")

        self.verticalLayout_6.addWidget(self.ck_funcionario_proprios)

        self.btn_registrar = QPushButton(self.frame_pagamento_funcionarios)
        self.btn_registrar.setObjectName(u"btn_registrar")

        self.verticalLayout_6.addWidget(self.btn_registrar)

        self.btn_dados_funcionarios = QPushButton(self.frame_pagamento_funcionarios)
        self.btn_dados_funcionarios.setObjectName(u"btn_dados_funcionarios")

        self.verticalLayout_6.addWidget(self.btn_dados_funcionarios)

        self.frame_resultado = QFrame(self.frame_pagamento_funcionarios)
        self.frame_resultado.setObjectName(u"frame_resultado")
        self.frame_resultado.setMinimumSize(QSize(160, 210))
        self.frame_resultado.setFrameShape(QFrame.StyledPanel)
        self.frame_resultado.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_resultado)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.txt_resultado = QLineEdit(self.frame_resultado)
        self.txt_resultado.setObjectName(u"txt_resultado")
        self.txt_resultado.setMinimumSize(QSize(150, 200))
        self.txt_resultado.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.txt_resultado)


        self.verticalLayout_6.addWidget(self.frame_resultado)


        self.verticalLayout_7.addWidget(self.frame_pagamento_funcionarios)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Pagamento dos Funcionarios", None))
        self.lbl_pagamento_dos_funcionarios.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Pagamento Dos Funcion\u00e1rios</span></p></body></html>", None))
        self.lbl_nome.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Nome</span></p></body></html>", None))
        self.lbl_horas_trabalhadas.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Horas Trabalhadas</span></p></body></html>", None))
        self.lbl_valor_horas.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Valor por Hora </span></p></body></html>", None))
        self.lbl_despesa_funcionario_terceirizado.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Despesa Adicional de Funcionario Terceirizados</span></p></body></html>", None))
        self.ck_funcionarios_terceirizado.setText(QCoreApplication.translate("MainWindow", u"Funcion\u00e1rios Terceirizados", None))
        self.ck_funcionario_proprios.setText(QCoreApplication.translate("MainWindow", u"Funcion\u00e1rios Pr\u00f3prios", None))
        self.btn_registrar.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.btn_dados_funcionarios.setText(QCoreApplication.translate("MainWindow", u"Dados de Funcionarios", None))
    # retranslateUi

