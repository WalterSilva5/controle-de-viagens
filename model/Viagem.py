from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Float, String, DateTime, Integer
from sys import path
from datetime import datetime


class Viagem():
    __tablename__ = "viagem"
    valor = Column(Float)
    motorista = Column(String(100))
    auxiliar1 = Column(String(100))
    auxiliar2 = Column(String(100))
    cidade = Column(String(100))
    veiculo = Column(String(100))
    horariodesaida = Column(String(100))
    horariodechegada = Column(String(100))
    data = Column(DateTime)
    observacoes = Column(String(100))
    idviagem = Column(Integer, primary_key=True)

    def __init__(self):
        self.engine = create_engine(
            "sqlite:///{}/sql/base.db".format(path[0]), echo=True)
        self.conn = self.engine.connect()

    def adicionarViagem(self, motorista, auxiliar1, auxiliar2, cidade, veiculo,
                        horariodesaida, horariodechegada, data, observacoes):
        self.engine.execute("INSERT INTO viagem (motorista, auxiliar1, auxiliar2, cidade, veiculo, horariodesaida, horariodechegada, data, observacoes) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
            motorista, auxiliar1, auxiliar2, cidade, veiculo, horariodesaida, horariodechegada, data, observacoes))

    def listarViagens(self,de,ate):
        lista = (self.engine.execute("SELECT * FROM viagem WHERE data BETWEEN '{}' and '{}'".format(de, ate))).fetchall()
        return lista