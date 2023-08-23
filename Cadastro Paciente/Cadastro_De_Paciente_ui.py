# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Cadastro_De_Paciente.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QFrame, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 796)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_cadastro_paciente = QFrame(self.centralwidget)
        self.frame_cadastro_paciente.setObjectName(u"frame_cadastro_paciente")
        self.frame_cadastro_paciente.setFrameShape(QFrame.StyledPanel)
        self.frame_cadastro_paciente.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_cadastro_paciente)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lbl_cadastro_paciente = QLabel(self.frame_cadastro_paciente)
        self.lbl_cadastro_paciente.setObjectName(u"lbl_cadastro_paciente")

        self.verticalLayout_6.addWidget(self.lbl_cadastro_paciente)

        self.frame_nome_completo = QFrame(self.frame_cadastro_paciente)
        self.frame_nome_completo.setObjectName(u"frame_nome_completo")
        self.frame_nome_completo.setFrameShape(QFrame.StyledPanel)
        self.frame_nome_completo.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_nome_completo)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_nome_completo = QLabel(self.frame_nome_completo)
        self.lbl_nome_completo.setObjectName(u"lbl_nome_completo")

        self.verticalLayout.addWidget(self.lbl_nome_completo)

        self.txt_nom_completo = QLineEdit(self.frame_nome_completo)
        self.txt_nom_completo.setObjectName(u"txt_nom_completo")

        self.verticalLayout.addWidget(self.txt_nom_completo)


        self.verticalLayout_6.addWidget(self.frame_nome_completo)

        self.frame_numero_telefone = QFrame(self.frame_cadastro_paciente)
        self.frame_numero_telefone.setObjectName(u"frame_numero_telefone")
        self.frame_numero_telefone.setFrameShape(QFrame.StyledPanel)
        self.frame_numero_telefone.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_numero_telefone)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_numero_telefone = QLabel(self.frame_numero_telefone)
        self.lbl_numero_telefone.setObjectName(u"lbl_numero_telefone")

        self.verticalLayout_2.addWidget(self.lbl_numero_telefone)

        self.txt_numero_telefone = QLineEdit(self.frame_numero_telefone)
        self.txt_numero_telefone.setObjectName(u"txt_numero_telefone")

        self.verticalLayout_2.addWidget(self.txt_numero_telefone)


        self.verticalLayout_6.addWidget(self.frame_numero_telefone)

        self.frame_email = QFrame(self.frame_cadastro_paciente)
        self.frame_email.setObjectName(u"frame_email")
        self.frame_email.setFrameShape(QFrame.StyledPanel)
        self.frame_email.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_email)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_email = QLabel(self.frame_email)
        self.lbl_email.setObjectName(u"lbl_email")

        self.verticalLayout_3.addWidget(self.lbl_email)

        self.txt_email = QLineEdit(self.frame_email)
        self.txt_email.setObjectName(u"txt_email")

        self.verticalLayout_3.addWidget(self.txt_email)


        self.verticalLayout_6.addWidget(self.frame_email)

        self.frame_genero = QFrame(self.frame_cadastro_paciente)
        self.frame_genero.setObjectName(u"frame_genero")
        self.frame_genero.setFrameShape(QFrame.StyledPanel)
        self.frame_genero.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_genero)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lbl_genero = QLabel(self.frame_genero)
        self.lbl_genero.setObjectName(u"lbl_genero")

        self.verticalLayout_4.addWidget(self.lbl_genero)

        self.cbx_genero = QComboBox(self.frame_genero)
        self.cbx_genero.addItem("")
        self.cbx_genero.addItem("")
        self.cbx_genero.addItem("")
        self.cbx_genero.setObjectName(u"cbx_genero")

        self.verticalLayout_4.addWidget(self.cbx_genero)


        self.verticalLayout_6.addWidget(self.frame_genero)

        self.frame_data_nascimento = QFrame(self.frame_cadastro_paciente)
        self.frame_data_nascimento.setObjectName(u"frame_data_nascimento")
        self.frame_data_nascimento.setFrameShape(QFrame.StyledPanel)
        self.frame_data_nascimento.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_data_nascimento)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lbl_data_nascimento = QLabel(self.frame_data_nascimento)
        self.lbl_data_nascimento.setObjectName(u"lbl_data_nascimento")

        self.verticalLayout_5.addWidget(self.lbl_data_nascimento)

        self.date_data_nascimento = QDateEdit(self.frame_data_nascimento)
        self.date_data_nascimento.setObjectName(u"date_data_nascimento")

        self.verticalLayout_5.addWidget(self.date_data_nascimento)


        self.verticalLayout_6.addWidget(self.frame_data_nascimento)

        self.ck_paciente_pcd = QCheckBox(self.frame_cadastro_paciente)
        self.ck_paciente_pcd.setObjectName(u"ck_paciente_pcd")

        self.verticalLayout_6.addWidget(self.ck_paciente_pcd)

        self.btn_adicionar_paciente = QPushButton(self.frame_cadastro_paciente)
        self.btn_adicionar_paciente.setObjectName(u"btn_adicionar_paciente")

        self.verticalLayout_6.addWidget(self.btn_adicionar_paciente)

        self.btn_chamar_proximo_fila = QPushButton(self.frame_cadastro_paciente)
        self.btn_chamar_proximo_fila.setObjectName(u"btn_chamar_proximo_fila")

        self.verticalLayout_6.addWidget(self.btn_chamar_proximo_fila)

        self.txtb_resultado_fila = QTextBrowser(self.frame_cadastro_paciente)
        self.txtb_resultado_fila.setObjectName(u"txtb_resultado_fila")

        self.verticalLayout_6.addWidget(self.txtb_resultado_fila)


        self.verticalLayout_7.addWidget(self.frame_cadastro_paciente)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cadastro_De_Paciente", None))
        self.lbl_cadastro_paciente.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Cadastro de Paciente</span></p></body></html>", None))
        self.lbl_nome_completo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Nome Completo</span></p></body></html>", None))
        self.lbl_numero_telefone.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Numero De telefone</span></p></body></html>", None))
        self.lbl_email.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Email</span></p></body></html>", None))
        self.lbl_genero.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">G\u00eanero</span></p></body></html>", None))
        self.cbx_genero.setItemText(0, QCoreApplication.translate("MainWindow", u"Outros", None))
        self.cbx_genero.setItemText(1, QCoreApplication.translate("MainWindow", u"Masculino", None))
        self.cbx_genero.setItemText(2, QCoreApplication.translate("MainWindow", u"Feminino", None))

        self.lbl_data_nascimento.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Data De Nascimento</p></body></html>", None))
        self.ck_paciente_pcd.setText(QCoreApplication.translate("MainWindow", u"Paciente (PCD)", None))
        self.btn_adicionar_paciente.setText(QCoreApplication.translate("MainWindow", u"Adicionar Paciente", None))
        self.btn_chamar_proximo_fila.setText(QCoreApplication.translate("MainWindow", u"Chamar o proximo da fila", None))
    # retranslateUi

