# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frameCadastrarViagem = QtWidgets.QFrame(self.centralwidget)
        self.frameCadastrarViagem.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.frameCadastrarViagem.setMinimumSize(QtCore.QSize(800, 600))
        self.frameCadastrarViagem.setMaximumSize(QtCore.QSize(800, 600))
        self.frameCadastrarViagem.setStyleSheet("background-color: white;\n"
"PushButton\n"
"{\n"
"   background-color:red;\n"
"}")
        self.frameCadastrarViagem.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameCadastrarViagem.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameCadastrarViagem.setObjectName("frameCadastrarViagem")
        self.labelTelaInicialTitulo1_2 = QtWidgets.QLabel(self.frameCadastrarViagem)
        self.labelTelaInicialTitulo1_2.setGeometry(QtCore.QRect(260, 0, 511, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.labelTelaInicialTitulo1_2.setFont(font)
        self.labelTelaInicialTitulo1_2.setStyleSheet("color:blue;")
        self.labelTelaInicialTitulo1_2.setObjectName("labelTelaInicialTitulo1_2")
        self.label_5 = QtWidgets.QLabel(self.frameCadastrarViagem)
        self.label_5.setGeometry(QtCore.QRect(40, 218, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:blue;")
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.frameCadastrarViagem)
        self.label_4.setGeometry(QtCore.QRect(40, 184, 91, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:blue;")
        self.label_4.setObjectName("label_4")
        self.botaoCadastrarViagemVoltar = QtWidgets.QPushButton(self.frameCadastrarViagem)
        self.botaoCadastrarViagemVoltar.setGeometry(QtCore.QRect(34, 510, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.botaoCadastrarViagemVoltar.setFont(font)
        self.botaoCadastrarViagemVoltar.setStyleSheet("color: red;\n"
"border:1px solid red;\n"
"border-radius:5px;")
        self.botaoCadastrarViagemVoltar.setObjectName("botaoCadastrarViagemVoltar")
        self.cadastroDeViagemEntradaAuxiliar1 = QtWidgets.QLineEdit(self.frameCadastrarViagem)
        self.cadastroDeViagemEntradaAuxiliar1.setGeometry(QtCore.QRect(234, 116, 525, 28))
        font = QtGui.QFont()
        font.setFamily("Akaash")
        font.setPointSize(14)
        self.cadastroDeViagemEntradaAuxiliar1.setFont(font)
        self.cadastroDeViagemEntradaAuxiliar1.setStyleSheet("border:1px solid blue;\n"
"border-radius:5px;\n"
"color:black;")
        self.cadastroDeViagemEntradaAuxiliar1.setText("")
        self.cadastroDeViagemEntradaAuxiliar1.setObjectName("cadastroDeViagemEntradaAuxiliar1")
        self.label_9 = QtWidgets.QLabel(self.frameCadastrarViagem)
        self.label_9.setGeometry(QtCore.QRect(40, 354, 161, 47))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:blue;")
        self.label_9.setObjectName("label_9")
        self.label_7 = QtWidgets.QLabel(self.frameCadastrarViagem)
        self.label_7.setGeometry(QtCore.QRect(40, 286, 201, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:blue;")
        self.label_7.setObjectName("label_7")
        self.cadastroDeViagemEntradaCidade = QtWidgets.QLineEdit(self.frameCadastrarViagem)
        self.cadastroDeViagemEntradaCidade.setGeometry(QtCore.QRect(234, 184, 525, 28))
        font = QtGui.QFont()
        font.setFamily("Akaash")
        font.setPointSize(14)
        self.cadastroDeViagemEntradaCidade.setFont(font)
        self.cadastroDeViagemEntradaCidade.setStyleSheet("border:1px solid blue;\n"
"border-radius:5px;\n"
"color:black;")
        self.cadastroDeViagemEntradaCidade.setText("")
        self.cadastroDeViagemEntradaCidade.setObjectName("cadastroDeViagemEntradaCidade")
        self.label = QtWidgets.QLabel(self.frameCadastrarViagem)
        self.label.setGeometry(QtCore.QRect(40, 82, 131, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:blue;")
        self.label.setObjectName("label")
        self.cadastroDeViagemEntradaHorarioSaida = QtWidgets.QTimeEdit(self.frameCadastrarViagem)
        self.cadastroDeViagemEntradaHorarioSaida.setGeometry(QtCore.QRect(234, 250, 91, 27))
        self.cadastroDeViagemEntradaHorarioSaida.setStyleSheet("border:1px solid blue;\n"
"border-radius:5px;\n"
"\n"
"color: balck;")
        self.cadastroDeViagemEntradaHorarioSaida.setCalendarPopup(True)
        self.cadastroDeViagemEntradaHorarioSaida.setObjectName("cadastroDeViagemEntradaHorarioSaida")
        self.cadastroDeViagemEntradaVeiculo = QtWidgets.QLineEdit(self.frameCadastrarViagem)
        self.cadastroDeViagemEntradaVeiculo.setGeometry(QtCore.QRect(234, 218, 161, 28))
        font = QtGui.QFont()
        font.setFamily("Akaash")
        font.setPointSize(14)
        self.cadastroDeViagemEntradaVeiculo.setFont(font)
        self.cadastroDeViagemEntradaVeiculo.setStyleSheet("border:1px solid blue;\n"
"border-radius:5px;\n"
"color:black;")
        self.cadastroDeViagemEntradaVeiculo.setText("")
        self.cadastroDeViagemEntradaVeiculo.setObjectName("cadastroDeViagemEntradaVeiculo")
        self.cadastroDeViagemEntradaObservacoes = QtWidgets.QTextEdit(self.frameCadastrarViagem)
        self.cadastroDeViagemEntradaObservacoes.setGeometry(QtCore.QRect(234, 354, 525, 141))
        self.cadastroDeViagemEntradaObservacoes.setStyleSheet("border:1px solid blue;\n"
"border-radius:5px;\n"
"color:black;")
        self.cadastroDeViagemEntradaObservacoes.setObjectName("cadastroDeViagemEntradaObservacoes")
        self.label_8 = QtWidgets.QLabel(self.frameCadastrarViagem)
        self.label_8.setGeometry(QtCore.QRect(40, 320, 71, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:blue;")
        self.label_8.setObjectName("label_8")
        self.label_2 = QtWidgets.QLabel(self.frameCadastrarViagem)
        self.label_2.setGeometry(QtCore.QRect(40, 116, 121, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:blue;")
        self.label_2.setObjectName("label_2")
        self.botaoCadastroDeViagemSalvar = QtWidgets.QPushButton(self.frameCadastrarViagem)
        self.botaoCadastroDeViagemSalvar.setGeometry(QtCore.QRect(594, 510, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.botaoCadastroDeViagemSalvar.setFont(font)
        self.botaoCadastroDeViagemSalvar.setStyleSheet("color: green;\n"
"border:1px solid green;\n"
"border-radius:5px;\n"
"hover\n"
"{\n"
"   background-color:white;\n"
"}")
        self.botaoCadastroDeViagemSalvar.setObjectName("botaoCadastroDeViagemSalvar")
        self.cadastroDeViagemLabelErro = QtWidgets.QLabel(self.frameCadastrarViagem)
        self.cadastroDeViagemLabelErro.setGeometry(QtCore.QRect(234, 510, 341, 51))
        self.cadastroDeViagemLabelErro.setObjectName("cadastroDeViagemLabelErro")
        self.cadastroDeViagemEntradaData = QtWidgets.QDateEdit(self.frameCadastrarViagem)
        self.cadastroDeViagemEntradaData.setGeometry(QtCore.QRect(234, 310, 110, 27))
        self.cadastroDeViagemEntradaData.setStyleSheet("border:1px solid blue;\n"
"border-radius:5px;\n"
"color:black;\n"
"")
        self.cadastroDeViagemEntradaData.setCalendarPopup(True)
        self.cadastroDeViagemEntradaData.setDate(QtCore.QDate(2020, 1, 1))
        self.cadastroDeViagemEntradaData.setObjectName("cadastroDeViagemEntradaData")
        self.cadastroDeViagemEntradaHorarioChegada = QtWidgets.QTimeEdit(self.frameCadastrarViagem)
        self.cadastroDeViagemEntradaHorarioChegada.setGeometry(QtCore.QRect(234, 280, 91, 27))
        self.cadastroDeViagemEntradaHorarioChegada.setStyleSheet("border:1px solid blue;\n"
"border-radius:5px;\n"
"color:black;")
        self.cadastroDeViagemEntradaHorarioChegada.setCalendarPopup(True)
        self.cadastroDeViagemEntradaHorarioChegada.setObjectName("cadastroDeViagemEntradaHorarioChegada")
        self.cadastroDeViagemEntradaAuxiliar2 = QtWidgets.QLineEdit(self.frameCadastrarViagem)
        self.cadastroDeViagemEntradaAuxiliar2.setGeometry(QtCore.QRect(234, 150, 525, 28))
        font = QtGui.QFont()
        font.setFamily("Akaash")
        font.setPointSize(14)
        self.cadastroDeViagemEntradaAuxiliar2.setFont(font)
        self.cadastroDeViagemEntradaAuxiliar2.setStyleSheet("border:1px solid blue;\n"
"border-radius:5px;\n"
"color:black;")
        self.cadastroDeViagemEntradaAuxiliar2.setText("")
        self.cadastroDeViagemEntradaAuxiliar2.setObjectName("cadastroDeViagemEntradaAuxiliar2")
        self.label_6 = QtWidgets.QLabel(self.frameCadastrarViagem)
        self.label_6.setGeometry(QtCore.QRect(40, 252, 171, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:blue;")
        self.label_6.setObjectName("label_6")
        self.cadastroDeViagemEntradaMotorista = QtWidgets.QLineEdit(self.frameCadastrarViagem)
        self.cadastroDeViagemEntradaMotorista.setGeometry(QtCore.QRect(234, 82, 525, 28))
        font = QtGui.QFont()
        font.setFamily("Akaash")
        font.setPointSize(14)
        self.cadastroDeViagemEntradaMotorista.setFont(font)
        self.cadastroDeViagemEntradaMotorista.setStyleSheet("border:1px solid blue;\n"
"border-radius:5px;\n"
"color:black;")
        self.cadastroDeViagemEntradaMotorista.setText("")
        self.cadastroDeViagemEntradaMotorista.setObjectName("cadastroDeViagemEntradaMotorista")
        self.label_3 = QtWidgets.QLabel(self.frameCadastrarViagem)
        self.label_3.setGeometry(QtCore.QRect(40, 150, 131, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:blue;")
        self.label_3.setObjectName("label_3")
        self.frameTelaInicial = QtWidgets.QFrame(self.centralwidget)
        self.frameTelaInicial.setGeometry(QtCore.QRect(0, 10, 800, 600))
        self.frameTelaInicial.setMinimumSize(QtCore.QSize(800, 600))
        self.frameTelaInicial.setMaximumSize(QtCore.QSize(800, 600))
        self.frameTelaInicial.setStyleSheet("background-color:white;")
        self.frameTelaInicial.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameTelaInicial.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameTelaInicial.setObjectName("frameTelaInicial")
        self.botaoTelaInicialRelatorioDeViagens = QtWidgets.QPushButton(self.frameTelaInicial)
        self.botaoTelaInicialRelatorioDeViagens.setGeometry(QtCore.QRect(140, 320, 531, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.botaoTelaInicialRelatorioDeViagens.setFont(font)
        self.botaoTelaInicialRelatorioDeViagens.setStyleSheet("border:1px solid blue;\n"
"color:blue;\n"
"border-radius:5px;")
        self.botaoTelaInicialRelatorioDeViagens.setObjectName("botaoTelaInicialRelatorioDeViagens")
        self.botaoTelaInicialCadastrarViagem = QtWidgets.QPushButton(self.frameTelaInicial)
        self.botaoTelaInicialCadastrarViagem.setGeometry(QtCore.QRect(140, 100, 531, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.botaoTelaInicialCadastrarViagem.setFont(font)
        self.botaoTelaInicialCadastrarViagem.setStyleSheet("border:1px solid blue;\n"
"color:blue;\n"
"border-radius:5px;")
        self.botaoTelaInicialCadastrarViagem.setObjectName("botaoTelaInicialCadastrarViagem")
        self.botaoTelaInicialModificarViagem = QtWidgets.QPushButton(self.frameTelaInicial)
        self.botaoTelaInicialModificarViagem.setGeometry(QtCore.QRect(140, 210, 531, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.botaoTelaInicialModificarViagem.setFont(font)
        self.botaoTelaInicialModificarViagem.setStyleSheet("border:1px solid blue;\n"
"color:blue;\n"
"border-radius:5px;")
        self.botaoTelaInicialModificarViagem.setObjectName("botaoTelaInicialModificarViagem")
        self.labelTelaInicialTitulo1 = QtWidgets.QLabel(self.frameTelaInicial)
        self.labelTelaInicialTitulo1.setGeometry(QtCore.QRect(160, 20, 551, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.labelTelaInicialTitulo1.setFont(font)
        self.labelTelaInicialTitulo1.setStyleSheet("color:blue;")
        self.labelTelaInicialTitulo1.setObjectName("labelTelaInicialTitulo1")
        self.botaoTelaInicialSair = QtWidgets.QPushButton(self.frameTelaInicial)
        self.botaoTelaInicialSair.setGeometry(QtCore.QRect(50, 520, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.botaoTelaInicialSair.setFont(font)
        self.botaoTelaInicialSair.setStyleSheet("color: red;\n"
"border:1px solid red;\n"
"border-radius:5px;")
        self.botaoTelaInicialSair.setObjectName("botaoTelaInicialSair")
        self.frameRelatorioDeViagens = QtWidgets.QFrame(self.centralwidget)
        self.frameRelatorioDeViagens.setGeometry(QtCore.QRect(10, 10, 800, 600))
        self.frameRelatorioDeViagens.setMinimumSize(QtCore.QSize(800, 600))
        self.frameRelatorioDeViagens.setMaximumSize(QtCore.QSize(800, 600))
        self.frameRelatorioDeViagens.setStyleSheet("background-color:white;")
        self.frameRelatorioDeViagens.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameRelatorioDeViagens.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameRelatorioDeViagens.setObjectName("frameRelatorioDeViagens")
        self.labelRelatorioDeViagensTitulo = QtWidgets.QLabel(self.frameRelatorioDeViagens)
        self.labelRelatorioDeViagensTitulo.setGeometry(QtCore.QRect(230, 10, 551, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.labelRelatorioDeViagensTitulo.setFont(font)
        self.labelRelatorioDeViagensTitulo.setStyleSheet("color:blue;")
        self.labelRelatorioDeViagensTitulo.setObjectName("labelRelatorioDeViagensTitulo")
        self.frame = QtWidgets.QFrame(self.frameRelatorioDeViagens)
        self.frame.setGeometry(QtCore.QRect(10, 70, 771, 61))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.relatorioDeViagensDataDatade = QtWidgets.QDateEdit(self.frame)
        self.relatorioDeViagensDataDatade.setGeometry(QtCore.QRect(200, 10, 111, 31))
        self.relatorioDeViagensDataDatade.setCalendarPopup(True)
        self.relatorioDeViagensDataDatade.setDate(QtCore.QDate(2020, 1, 1))
        self.relatorioDeViagensDataDatade.setObjectName("relatorioDeViagensDataDatade")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(80, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(330, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.relatorioDeViagensDataDataate = QtWidgets.QDateEdit(self.frame)
        self.relatorioDeViagensDataDataate.setGeometry(QtCore.QRect(470, 10, 111, 31))
        self.relatorioDeViagensDataDataate.setCalendarPopup(True)
        self.relatorioDeViagensDataDataate.setDate(QtCore.QDate(2020, 1, 1))
        self.relatorioDeViagensDataDataate.setObjectName("relatorioDeViagensDataDataate")
        self.relatorioDeViagensBotaoBuscar = QtWidgets.QPushButton(self.frame)
        self.relatorioDeViagensBotaoBuscar.setGeometry(QtCore.QRect(610, 10, 81, 31))
        self.relatorioDeViagensBotaoBuscar.setObjectName("relatorioDeViagensBotaoBuscar")
        self.tabelaListagemViagens = QtWidgets.QTableWidget(self.frameRelatorioDeViagens)
        self.tabelaListagemViagens.setGeometry(QtCore.QRect(10, 140, 771, 381))
        self.tabelaListagemViagens.setObjectName("tabelaListagemViagens")
        self.tabelaListagemViagens.setColumnCount(9)
        self.tabelaListagemViagens.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaListagemViagens.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaListagemViagens.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaListagemViagens.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaListagemViagens.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaListagemViagens.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaListagemViagens.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaListagemViagens.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaListagemViagens.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaListagemViagens.setHorizontalHeaderItem(8, item)
        self.botaoRelatorioDeViagensVoltar = QtWidgets.QPushButton(self.frameRelatorioDeViagens)
        self.botaoRelatorioDeViagensVoltar.setGeometry(QtCore.QRect(20, 540, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.botaoRelatorioDeViagensVoltar.setFont(font)
        self.botaoRelatorioDeViagensVoltar.setStyleSheet("color: red;\n"
"border:1px solid red;\n"
"border-radius:5px;")
        self.botaoRelatorioDeViagensVoltar.setObjectName("botaoRelatorioDeViagensVoltar")
        self.botaoRelatorioDeViagensExportar = QtWidgets.QPushButton(self.frameRelatorioDeViagens)
        self.botaoRelatorioDeViagensExportar.setGeometry(QtCore.QRect(480, 540, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.botaoRelatorioDeViagensExportar.setFont(font)
        self.botaoRelatorioDeViagensExportar.setStyleSheet("color: green;\n"
"border:1px solid green;\n"
"border-radius:5px;")
        self.botaoRelatorioDeViagensExportar.setObjectName("botaoRelatorioDeViagensExportar")
        self.frameCadastrarViagem.raise_()
        self.frameRelatorioDeViagens.raise_()
        self.frameTelaInicial.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Frinex - CONTROLE DE VIAGENS"))
        self.labelTelaInicialTitulo1_2.setText(_translate("MainWindow", "CADASTRO DE VIAGEM"))
        self.label_5.setText(_translate("MainWindow", "VEICULO"))
        self.label_4.setText(_translate("MainWindow", "CIDADE"))
        self.botaoCadastrarViagemVoltar.setText(_translate("MainWindow", "voltar"))
        self.label_9.setText(_translate("MainWindow", "OBSERVAÇÕES!"))
        self.label_7.setText(_translate("MainWindow", "HORARIO CHEGADA"))
        self.label.setText(_translate("MainWindow", "MOTORISTA"))
        self.label_8.setText(_translate("MainWindow", "DATA"))
        self.label_2.setText(_translate("MainWindow", "AUXILIAR 1"))
        self.botaoCadastroDeViagemSalvar.setText(_translate("MainWindow", "salvar"))
        self.cadastroDeViagemLabelErro.setText(_translate("MainWindow", "aguardando entrada"))
        self.label_6.setText(_translate("MainWindow", "HORARIO SAIDA"))
        self.label_3.setText(_translate("MainWindow", "AUXILIAR 2"))
        self.botaoTelaInicialRelatorioDeViagens.setText(_translate("MainWindow", "RELATORIO DE VIAGENS"))
        self.botaoTelaInicialCadastrarViagem.setText(_translate("MainWindow", "CADASTRAR VIAGEM"))
        self.botaoTelaInicialModificarViagem.setText(_translate("MainWindow", "MODIFICAR VIAGEM"))
        self.labelTelaInicialTitulo1.setText(_translate("MainWindow", "CONTROLE DE VIAGENS FRINEX"))
        self.botaoTelaInicialSair.setText(_translate("MainWindow", "sair"))
        self.labelRelatorioDeViagensTitulo.setText(_translate("MainWindow", "RELATORIO DE VIAGENS"))
        self.label_10.setText(_translate("MainWindow", "DO DIA"))
        self.label_11.setText(_translate("MainWindow", "ATÉ O DIA"))
        self.relatorioDeViagensBotaoBuscar.setText(_translate("MainWindow", "BUSCAR"))
        item = self.tabelaListagemViagens.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "MOTORISTA"))
        item = self.tabelaListagemViagens.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "AUXILIAR 1"))
        item = self.tabelaListagemViagens.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "AUXILIAR 2"))
        item = self.tabelaListagemViagens.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "CIDADE"))
        item = self.tabelaListagemViagens.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "VEICULO"))
        item = self.tabelaListagemViagens.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "H SAIDA"))
        item = self.tabelaListagemViagens.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "H CHEGADA"))
        item = self.tabelaListagemViagens.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "DATA"))
        item = self.tabelaListagemViagens.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "OBSERVAÇÕES"))
        self.botaoRelatorioDeViagensVoltar.setText(_translate("MainWindow", "voltar"))
        self.botaoRelatorioDeViagensExportar.setText(_translate("MainWindow", "EXPORTAR COMO EXCEL"))
