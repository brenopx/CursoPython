from conta import Conta
from banco import Banco


class ContaCorrente(Conta):
    def __init__(self, agencia, numero_da_conta, saldo, limite=100):
        Conta.__init__(self, agencia, numero_da_conta, saldo)
        self.limite = limite
        self.AGENCIA = 111
        self.CLIENTES = ['João', 'Maria']
        self.CONTAS = [100, 101]

    def sacar(self, valor):
        if (self.saldo + self.limite) >= valor and Banco.autenticar(self):
            self.saldo = (self.saldo + self.limite) - valor
            return print(f'Novo saldo sera {self.saldo}')
        else:
            print('Saldo Insuficiente ou Sua conta não da agencia')
