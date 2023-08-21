# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro_banco.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(997, 664)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_cadastro_banco = QFrame(self.centralwidget)
        self.frame_cadastro_banco.setObjectName(u"frame_cadastro_banco")
        self.frame_cadastro_banco.setFrameShape(QFrame.StyledPanel)
        self.frame_cadastro_banco.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_cadastro_banco)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lbl_cadastro_banco = QLabel(self.frame_cadastro_banco)
        self.lbl_cadastro_banco.setObjectName(u"lbl_cadastro_banco")

        self.verticalLayout_6.addWidget(self.lbl_cadastro_banco)

        self.frame_numero_conta = QFrame(self.frame_cadastro_banco)
        self.frame_numero_conta.setObjectName(u"frame_numero_conta")
        self.frame_numero_conta.setFrameShape(QFrame.StyledPanel)
        self.frame_numero_conta.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_numero_conta)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_numero_da_conta = QLabel(self.frame_numero_conta)
        self.lbl_numero_da_conta.setObjectName(u"lbl_numero_da_conta")

        self.verticalLayout.addWidget(self.lbl_numero_da_conta)

        self.txt_numero_da_conta = QLineEdit(self.frame_numero_conta)
        self.txt_numero_da_conta.setObjectName(u"txt_numero_da_conta")

        self.verticalLayout.addWidget(self.txt_numero_da_conta)


        self.verticalLayout_6.addWidget(self.frame_numero_conta)

        self.frame_nome_do_titular = QFrame(self.frame_cadastro_banco)
        self.frame_nome_do_titular.setObjectName(u"frame_nome_do_titular")
        self.frame_nome_do_titular.setFrameShape(QFrame.StyledPanel)
        self.frame_nome_do_titular.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_nome_do_titular)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_nome_do_titular = QLabel(self.frame_nome_do_titular)
        self.lbl_nome_do_titular.setObjectName(u"lbl_nome_do_titular")

        self.verticalLayout_2.addWidget(self.lbl_nome_do_titular)

        self.txt_nome_do_titular = QLineEdit(self.frame_nome_do_titular)
        self.txt_nome_do_titular.setObjectName(u"txt_nome_do_titular")

        self.verticalLayout_2.addWidget(self.txt_nome_do_titular)


        self.verticalLayout_6.addWidget(self.frame_nome_do_titular)

        self.frame_valor_de_deposito = QFrame(self.frame_cadastro_banco)
        self.frame_valor_de_deposito.setObjectName(u"frame_valor_de_deposito")
        self.frame_valor_de_deposito.setFrameShape(QFrame.StyledPanel)
        self.frame_valor_de_deposito.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_valor_de_deposito)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_valor_de_deposito = QLabel(self.frame_valor_de_deposito)
        self.lbl_valor_de_deposito.setObjectName(u"lbl_valor_de_deposito")

        self.verticalLayout_3.addWidget(self.lbl_valor_de_deposito)

        self.txt_valor_de_deposito = QLineEdit(self.frame_valor_de_deposito)
        self.txt_valor_de_deposito.setObjectName(u"txt_valor_de_deposito")

        self.verticalLayout_3.addWidget(self.txt_valor_de_deposito)


        self.verticalLayout_6.addWidget(self.frame_valor_de_deposito)

        self.btn_cadastrar = QPushButton(self.frame_cadastro_banco)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")

        self.verticalLayout_6.addWidget(self.btn_cadastrar)

        self.frame_valor_de_saque = QFrame(self.frame_cadastro_banco)
        self.frame_valor_de_saque.setObjectName(u"frame_valor_de_saque")
        self.frame_valor_de_saque.setFrameShape(QFrame.StyledPanel)
        self.frame_valor_de_saque.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_valor_de_saque)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lbl_valor_de_saque = QLabel(self.frame_valor_de_saque)
        self.lbl_valor_de_saque.setObjectName(u"lbl_valor_de_saque")

        self.verticalLayout_4.addWidget(self.lbl_valor_de_saque)

        self.txt_valor_de_saque = QLineEdit(self.frame_valor_de_saque)
        self.txt_valor_de_saque.setObjectName(u"txt_valor_de_saque")

        self.verticalLayout_4.addWidget(self.txt_valor_de_saque)


        self.verticalLayout_6.addWidget(self.frame_valor_de_saque)

        self.btn_deposito = QPushButton(self.frame_cadastro_banco)
        self.btn_deposito.setObjectName(u"btn_deposito")

        self.verticalLayout_6.addWidget(self.btn_deposito)

        self.btn_saque = QPushButton(self.frame_cadastro_banco)
        self.btn_saque.setObjectName(u"btn_saque")

        self.verticalLayout_6.addWidget(self.btn_saque)

        self.frame_resultados = QFrame(self.frame_cadastro_banco)
        self.frame_resultados.setObjectName(u"frame_resultados")
        self.frame_resultados.setMinimumSize(QSize(150, 150))
        self.frame_resultados.setFrameShape(QFrame.StyledPanel)
        self.frame_resultados.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_resultados)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.txt_resultado = QLineEdit(self.frame_resultados)
        self.txt_resultado.setObjectName(u"txt_resultado")
        self.txt_resultado.setMinimumSize(QSize(150, 150))
        self.txt_resultado.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.txt_resultado)


        self.verticalLayout_6.addWidget(self.frame_resultados)


        self.verticalLayout_7.addWidget(self.frame_cadastro_banco)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cadastro Banco", None))
        self.lbl_cadastro_banco.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Cadastro Banco</span></p></body></html>", None))
        self.lbl_numero_da_conta.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Numero Da Conta:</span></p></body></html>", None))
        self.lbl_nome_do_titular.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Nome Do Titular:</span></p></body></html>", None))
        self.lbl_valor_de_deposito.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Valor De Dep\u00f3sito:</span></p></body></html>", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.lbl_valor_de_saque.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Valor de Saque:</span></p></body></html>", None))
        self.btn_deposito.setText(QCoreApplication.translate("MainWindow", u"Dep\u00f3sito", None))
        self.btn_saque.setText(QCoreApplication.translate("MainWindow", u"Saque", None))
    # retranslateUi

