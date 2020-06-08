from PyQt5.QtWidgets import QMainWindow
from view.tela import Ui_MainWindow
from model.Viagem import Viagem


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
        self.tela.botaoCadastroDeViagemSalvar.clicked.connect(
            self.adicionarViagem)

    def mostrarFrameTelaInicial(self):
        self.esconderTodosOsFramesDeUso()
        self.tela.frameTelaInicial.show()

    def mostrarFrameCadastrarViagem(self):
        self.esconderTodosOsFramesDeUso()
        self.tela.frameCadastrarViagem.show()

    def esconderTodosOsFramesDeUso(self):
        self.tela.frameTelaInicial.hide()
        self.tela.frameCadastrarViagem.hide()

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
    # adicionar valor a tabela venda
    def adicionarValorATabelaVenda(self):
        valor = self.tela.entradaValorVenda.text()
        atual = self.tela.tabelaVendaItens.rowCount()
        self.tela.tabelaVendaItens.insertRow(atual)
        self.tela.tabelaVendaItens.setItem(atual, 0, QTableWidgetItem(valor))

        self.totalVendaAtual += float(valor)
        self.tela.labelTotalVenda.setText(
            "Total: {}".format(self.totalVendaAtual))
    # fim adicionar valor a tabela venda
        def listarEntradas(self):
            self.tela.tabelaEntradas.setRowCount(0)
            entrada = Entrada()
            entradas = entrada.listarEntradas()
            for elemento in entradas:
                atual = self.tela.tabelaEntradas.rowCount()
                self.tela.tabelaEntradas.insertRow(atual)
                self.tela.tabelaEntradas.setItem(
                    atual, 0, QTableWidgetItem(str(elemento[0])))
                self.tela.tabelaEntradas.setItem(
                    atual, 1, QTableWidgetItem(str(elemento[1])))
                self.tela.tabelaEntradas.setItem(
                    atual, 2, QTableWidgetItem(str(elemento[2])))
                self.tela.tabelaEntradas.setItem(
                    atual, 3, QTableWidgetItem(str(elemento[3])))
