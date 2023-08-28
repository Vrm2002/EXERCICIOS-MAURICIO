# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Cadastro exercircio3.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(348, 120)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_cadastro = QLabel(self.frame)
        self.lbl_cadastro.setObjectName(u"lbl_cadastro")
        font = QFont()
        font.setPointSize(15)
        self.lbl_cadastro.setFont(font)

        self.horizontalLayout_2.addWidget(self.lbl_cadastro)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_pessoa_fisica = QPushButton(self.frame_2)
        self.btn_pessoa_fisica.setObjectName(u"btn_pessoa_fisica")

        self.horizontalLayout.addWidget(self.btn_pessoa_fisica)

        self.btn_pessoa_juridica = QPushButton(self.frame_2)
        self.btn_pessoa_juridica.setObjectName(u"btn_pessoa_juridica")

        self.horizontalLayout.addWidget(self.btn_pessoa_juridica)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.lbl_cadastro.setText(QCoreApplication.translate("MainWindow", u"Qual o tipo de Cadastro ser\u00e1 feito?", None))
        self.btn_pessoa_fisica.setText(QCoreApplication.translate("MainWindow", u"Pessoa F\u00edsica", None))
        self.btn_pessoa_juridica.setText(QCoreApplication.translate("MainWindow", u"Pessoa Jur\u00eddica", None))
    # retranslateUi

