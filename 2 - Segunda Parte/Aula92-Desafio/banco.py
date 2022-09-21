class Banco:
    def __init__(self, conta, cliente):
        self.conta = conta
        self._cliente = cliente
        self.AGENCIA = 111
        self.CLIENTES = ['João', 'Maria']
        self.CONTAS = [100, 101]

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def conta(self, cliente):
        self.cliente = cliente

    def autenticar(self):
        conta_cliente = self.numero_da_conta
        agencia_cliente = self.agencia
        if self.AGENCIA == agencia_cliente:
            for conta in self.CONTAS:
                if conta_cliente == conta:
                    return True
                else:
                    print(f'Essa pessoa  não tem conta na nossa agencia')
                    return False
        else:
            print(f'Essa pessoa não é cliente da nossa agencia')
            return False


