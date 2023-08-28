# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Cadastro pessoa fisica.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
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
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.lbl_nomeF = QLabel(self.frame)
        self.lbl_nomeF.setObjectName(u"lbl_nomeF")
        font1 = QFont()
        font1.setPointSize(10)
        self.lbl_nomeF.setFont(font1)

        self.verticalLayout_2.addWidget(self.lbl_nomeF)

        self.txt_nomeF = QLineEdit(self.frame)
        self.txt_nomeF.setObjectName(u"txt_nomeF")

        self.verticalLayout_2.addWidget(self.txt_nomeF)

        self.lbl_rendaF = QLabel(self.frame)
        self.lbl_rendaF.setObjectName(u"lbl_rendaF")
        self.lbl_rendaF.setFont(font1)

        self.verticalLayout_2.addWidget(self.lbl_rendaF)

        self.txt_rendaF = QLineEdit(self.frame)
        self.txt_rendaF.setObjectName(u"txt_rendaF")

        self.verticalLayout_2.addWidget(self.txt_rendaF)

        self.lbl_gastosF = QLabel(self.frame)
        self.lbl_gastosF.setObjectName(u"lbl_gastosF")
        self.lbl_gastosF.setFont(font1)

        self.verticalLayout_2.addWidget(self.lbl_gastosF)

        self.txt_gastosF = QLineEdit(self.frame)
        self.txt_gastosF.setObjectName(u"txt_gastosF")

        self.verticalLayout_2.addWidget(self.txt_gastosF)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font1)

        self.verticalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_3.addWidget(self.frame)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.textBrowser)

        self.btn_voltar = QPushButton(self.centralwidget)
        self.btn_voltar.setObjectName(u"btn_voltar")
        self.btn_voltar.setFont(font1)
        self.btn_voltar.setLayoutDirection(Qt.LeftToRight)
        self.btn_voltar.setAutoDefault(False)

        self.verticalLayout_3.addWidget(self.btn_voltar, 0, Qt.AlignRight)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Cadastro Pessoa F\u00edsica", None))
        self.lbl_nomeF.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.lbl_rendaF.setText(QCoreApplication.translate("MainWindow", u"Renda Anual", None))
        self.lbl_gastosF.setText(QCoreApplication.translate("MainWindow", u"Gastos de sa\u00fade", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_voltar.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
    # retranslateUi

