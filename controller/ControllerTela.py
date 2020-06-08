from PyQt5.QtWidgets import QMainWindow
from view.tela import Ui_MainWindow
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from model.Viagem import Viagem
from openpyxl import Workbook
import getpass
import time


class ControllerTela(QMainWindow):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.tela = Ui_MainWindow()
        self.tela.setupUi(self)
        self.tela.botaoTelaInicialCadastrarViagem.clicked.connect(
            self.mostrarFrameCadastrarViagem)
        self.tela.botaoCadastrarViagemVoltar.clicked.connect(
            self.mostrarFrameTelaInicial)
        self.tela.botaoTelaInicialRelatorioDeViagens.clicked.connect(
            self.mostrarFrameRleatorioDeViagens)
        self.tela.botaoExcluirViagemExcluir.clicked.connect(
            self.excluirViagem)
        self.tela.relatorioDeViagensBotaoBuscar.clicked.connect(
            self.listarViagens)

        self.tela.botaoRelatorioDeViagensExportar.clicked.connect(
            self.exportarExcel)

        self.tela.botaoTelaInicialModificarViagem.clicked.connect(
            self.mostrarFrameExcluirViagem)

        self.tela.botaoExcluirViagemVoltar.clicked.connect(
            self.mostrarFrameTelaInicial)


        self.tela.botaoRelatorioDeViagensVoltar.clicked.connect(
            self.mostrarFrameTelaInicial)
        self.tela.botaoCadastroDeViagemSalvar.clicked.connect(
            self.adicionarViagem)

        self.tela.botaoTelaInicialSair.clicked.connect(exit)

    def mostrarFrameTelaInicial(self):
        self.esconderTodosOsFramesDeUso()
        self.tela.frameTelaInicial.show()

    def mostrarFrameCadastrarViagem(self):
        self.esconderTodosOsFramesDeUso()
        self.tela.frameCadastrarViagem.show()

    def mostrarFrameRleatorioDeViagens(self):
        self.esconderTodosOsFramesDeUso()
        self.tela.frameRelatorioDeViagens.show()

    def mostrarFrameExcluirViagem(self):
        self.esconderTodosOsFramesDeUso()
        self.tela.frameExcluirViagem.show()

    def esconderTodosOsFramesDeUso(self):
        self.tela.frameTelaInicial.hide()
        self.tela.frameCadastrarViagem.hide()
        self.tela.frameRelatorioDeViagens.hide()
        self.tela.frameExcluirViagem.hide()

    def adicionarViagem(self):
        motorista = self.tela.cadastroDeViagemEntradaMotorista.text()
        auxiliar1 = self.tela.cadastroDeViagemEntradaAuxiliar1.text()
        auxiliar2 = self.tela.cadastroDeViagemEntradaAuxiliar2.text()
        cidade = self.tela.cadastroDeViagemEntradaCidade.text()
        veiculo = self.tela.cadastroDeViagemEntradaVeiculo.text()
        horariodesaida = self.tela.cadastroDeViagemEntradaHorarioSaida.text()
        horariodechegada = self.tela.cadastroDeViagemEntradaHorarioChegada.text()
        data = self.tela.cadastroDeViagemEntradaData.text()
        observacoes = self.tela.cadastroDeViagemEntradaObservacoes.toPlainText()

        viagem = Viagem()
        viagem.adicionarViagem(motorista, auxiliar1, auxiliar2, cidade, veiculo,
                               horariodesaida, horariodechegada, data, observacoes)
        self.limparTelaCadastrarViagem()

    def listarViagens(self):
        self.tela.tabelaListagemViagens.setRowCount(0)
        viagem = Viagem()
        viagens = viagem.listarViagens(self.tela.relatorioDeViagensDataDatade.text(
        ), self.tela.relatorioDeViagensDataDataate.text())
        for elemento in viagens:
            atual = self.tela.tabelaListagemViagens.rowCount()
            self.tela.tabelaListagemViagens.insertRow(atual)
            self.tela.tabelaListagemViagens.setItem(
                atual, 0, QTableWidgetItem(str(elemento[0])))
            self.tela.tabelaListagemViagens.setItem(
                atual, 1, QTableWidgetItem(str(elemento[1])))
            self.tela.tabelaListagemViagens.setItem(
                atual, 2, QTableWidgetItem(str(elemento[2])))
            self.tela.tabelaListagemViagens.setItem(
                atual, 3, QTableWidgetItem(str(elemento[3])))
            self.tela.tabelaListagemViagens.setItem(
                atual, 4, QTableWidgetItem(str(elemento[4])))
            self.tela.tabelaListagemViagens.setItem(
                atual, 5, QTableWidgetItem(str(elemento[5])))
            self.tela.tabelaListagemViagens.setItem(
                atual, 6, QTableWidgetItem(str(elemento[6])))
            self.tela.tabelaListagemViagens.setItem(
                atual, 7, QTableWidgetItem(str(elemento[7])))
            self.tela.tabelaListagemViagens.setItem(
                atual, 8, QTableWidgetItem(str(elemento[8])))
            self.tela.tabelaListagemViagens.setItem(
                atual, 9, QTableWidgetItem(str(elemento[9])))

    def exportarExcel(self):
        viagem = Viagem()
        viagens = viagem.listarViagens(self.tela.relatorioDeViagensDataDatade.text(
        ), self.tela.relatorioDeViagensDataDataate.text())
        viagens = list(viagens)
        wb = Workbook()
        ws = wb.active
        for row in viagens:
            # print(row)
            ws.append(tuple(row))
        wb.save("C:/Users/{}/Desktop/{}.xlsx".format(getpass.getuser(),
                                                     "relatorio{}".format(time.time())))

    def excluirViagem(self):
        viagem = Viagem()
        viagem.removerViagem(self.tela.entradaIdViagemExcluir.text())
        self.tela.labelExcluirViagemMensagem.setText("VIAGEM EXCLUIDA")

    def limparTelaCadastrarViagem(self):
        self.tela.cadastroDeViagemEntradaMotorista.clear()
        self.tela.cadastroDeViagemEntradaAuxiliar1.clear()
        self.tela.cadastroDeViagemEntradaAuxiliar2.clear()
        self.tela.cadastroDeViagemEntradaCidade.clear()
        self.tela.cadastroDeViagemEntradaVeiculo.clear()
        self.tela.cadastroDeViagemEntradaHorarioSaida.clear()
        self.tela.cadastroDeViagemEntradaHorarioChegada.clear()
        self.tela.cadastroDeViagemEntradaData.clear()
        self.tela.cadastroDeViagemEntradaObservacoes.clear()
        self.tela.cadastroDeViagemLabelErro.setText("REGISTRO SALVO!")
