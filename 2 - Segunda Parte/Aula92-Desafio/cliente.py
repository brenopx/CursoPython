from pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        Pessoa.__init__(self, nome, idade)
        self._conta = conta

    @property
    def conta(self):
        return self._conta

    @conta.setter
    def conta(self, conta):
        self.conta = conta

    def lista_contas(self):
        print(f'O Clinete {self.nome} tem a conta de numero {self.conta.numero_da_conta}'
              f' com o saldo de {self.conta.saldo}')



