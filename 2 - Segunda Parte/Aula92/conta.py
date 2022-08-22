from abc import ABC, abstractmethod
from banco import Banco
from cliente import Cliente


class Conta:
    def __init__(self, agencia, numero_da_conta, saldo):
        self.agencia = agencia
        self.numero_da_conta = numero_da_conta
        self.saldo = saldo
        self.cliente = Cliente

    def deposito(self, valor):
        if Banco.autenticar(self):
            self.saldo += valor
            return self.saldo
        else:
            return

    @abstractmethod
    def sacar(self, valor):
        pass

