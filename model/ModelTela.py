from PyQt5.QtCore import QObject
class ModelTela(QObject):
    def __init__(self):
        self._mensagem = ""
    @property
    def mensagem(self):
        return self._mensagem

    @mensagem.setter
    def mensagem(self, mensagem):
        self._mensagem = mensagem
        