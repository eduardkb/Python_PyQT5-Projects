# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wProprietarios.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Proprietarios(object):
    def setupUi(self, Proprietarios):
        Proprietarios.setObjectName("Proprietarios")
        Proprietarios.resize(800, 319)
        Proprietarios.setMinimumSize(QtCore.QSize(800, 319))
        self.centralwidget = QtWidgets.QWidget(Proprietarios)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.txtNome = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNome.setObjectName("txtNome")
        self.gridLayout.addWidget(self.txtNome, 4, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnLimapr = QtWidgets.QPushButton(self.centralwidget)
        self.btnLimapr.setObjectName("btnLimapr")
        self.horizontalLayout_2.addWidget(self.btnLimapr)
        self.btnProcurar = QtWidgets.QPushButton(self.centralwidget)
        self.btnProcurar.setObjectName("btnProcurar")
        self.horizontalLayout_2.addWidget(self.btnProcurar)
        self.btnSalvar = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalvar.setAutoRepeatInterval(100)
        self.btnSalvar.setAutoDefault(True)
        self.btnSalvar.setDefault(True)
        self.btnSalvar.setObjectName("btnSalvar")
        self.horizontalLayout_2.addWidget(self.btnSalvar)
        self.gridLayout.addLayout(self.horizontalLayout_2, 10, 3, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 8, 0, 1, 5)
        self.txtRG = QtWidgets.QLineEdit(self.centralwidget)
        self.txtRG.setObjectName("txtRG")
        self.gridLayout.addWidget(self.txtRG, 2, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 3, 1, 1)
        self.txtSobrenome = QtWidgets.QLineEdit(self.centralwidget)
        self.txtSobrenome.setObjectName("txtSobrenome")
        self.gridLayout.addWidget(self.txtSobrenome, 4, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 7, 0, 1, 5)
        self.txtCpf = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCpf.setToolTipDuration(-1)
        self.txtCpf.setFrame(True)
        self.txtCpf.setObjectName("txtCpf")
        self.gridLayout.addWidget(self.txtCpf, 2, 2, 1, 1)
        self.txtIdade = QtWidgets.QLineEdit(self.centralwidget)
        self.txtIdade.setObjectName("txtIdade")
        self.gridLayout.addWidget(self.txtIdade, 5, 2, 1, 1)
        self.txtTelCom = QtWidgets.QLineEdit(self.centralwidget)
        self.txtTelCom.setClearButtonEnabled(False)
        self.txtTelCom.setObjectName("txtTelCom")
        self.gridLayout.addWidget(self.txtTelCom, 6, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 5)
        self.txtTelCel = QtWidgets.QLineEdit(self.centralwidget)
        self.txtTelCel.setObjectName("txtTelCel")
        self.gridLayout.addWidget(self.txtTelCel, 6, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(85, 170, 114);\n"
"color: rgb(0, 85, 0);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 5)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnSair = QtWidgets.QPushButton(self.centralwidget)
        self.btnSair.setObjectName("btnSair")
        self.horizontalLayout_3.addWidget(self.btnSair)
        self.gridLayout.addLayout(self.horizontalLayout_3, 12, 3, 1, 2)
        Proprietarios.setCentralWidget(self.centralwidget)
        self.statusText = QtWidgets.QStatusBar(Proprietarios)
        self.statusText.setStatusTip("")
        self.statusText.setObjectName("statusText")
        Proprietarios.setStatusBar(self.statusText)
        self.label_6.setBuddy(self.label_6)

        self.retranslateUi(Proprietarios)
        QtCore.QMetaObject.connectSlotsByName(Proprietarios)
        Proprietarios.setTabOrder(self.txtCpf, self.txtRG)
        Proprietarios.setTabOrder(self.txtRG, self.txtNome)
        Proprietarios.setTabOrder(self.txtNome, self.txtSobrenome)
        Proprietarios.setTabOrder(self.txtSobrenome, self.txtIdade)
        Proprietarios.setTabOrder(self.txtIdade, self.txtTelCel)
        Proprietarios.setTabOrder(self.txtTelCel, self.txtTelCom)
        Proprietarios.setTabOrder(self.txtTelCom, self.btnSalvar)
        Proprietarios.setTabOrder(self.btnSalvar, self.btnSair)
        Proprietarios.setTabOrder(self.btnSair, self.btnLimapr)
        Proprietarios.setTabOrder(self.btnLimapr, self.btnProcurar)

    def retranslateUi(self, Proprietarios):
        _translate = QtCore.QCoreApplication.translate
        Proprietarios.setWindowTitle(_translate("Proprietarios", "Cadastro de Proprietários"))
        self.label_6.setText(_translate("Proprietarios", "Telefone Cel."))
        self.btnLimapr.setText(_translate("Proprietarios", "Limpar"))
        self.btnProcurar.setText(_translate("Proprietarios", "Procurar"))
        self.btnSalvar.setText(_translate("Proprietarios", "Salvar"))
        self.btnSalvar.setShortcut(_translate("Proprietarios", "Ctrl+S"))
        self.label_3.setText(_translate("Proprietarios", "Nome"))
        self.label_2.setText(_translate("Proprietarios", "RG"))
        self.label_7.setText(_translate("Proprietarios", "Telefone Com."))
        self.label_5.setText(_translate("Proprietarios", "Idade"))
        self.label_4.setText(_translate("Proprietarios", "Sobrenome"))
        self.label_8.setText(_translate("Proprietarios", "Cadastro de Proprietários"))
        self.label.setText(_translate("Proprietarios", "CPF"))
        self.btnSair.setText(_translate("Proprietarios", "Sair"))
