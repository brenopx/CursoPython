from conta import Conta
from banco import Banco


class ContaPoupanca(Conta):
    def __init__(self, agencia, numero_da_conta, saldo):
        Conta.__init__(self, agencia, numero_da_conta, saldo)
        self.AGENCIA = 111
        self.CLIENTES = ['João', 'Maria']
        self.CONTAS = [100, 101]

    def sacar(self, valor):
        if self.saldo >= valor and Banco.autenticar(self):
            self.saldo = self.saldo - valor
            return print(f'Novo saldo sera {self.saldo}')
        else:
            print('Saldo Insuficiente ou sua conta não da agencia')
