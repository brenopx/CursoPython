from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Agencia: {self.agencia} '
              f'Conta: {self.conta} '
              f'Saldo: {self.saldo}')

    @abstractmethod
    def sacar(self, valor): pass


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficientes')
            return

        self.saldo -= valor
        self.detalhes()


class ContaCorrente(Conta):
    def __init__(self, agencia, numero_da_conta, saldo, limite=100):
        Conta.__init__(self, agencia, numero_da_conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficientes')
            return

        self.saldo -= valor
        self.detalhes()

