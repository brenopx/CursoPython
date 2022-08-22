class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        if self.nomeclasse == 'ClienteVIP':
            print(f'O {self.nomeclasse} {self.nome} esta na classe Pessoa, falando ...')
        else:
            print(f'A {self.nomeclasse} {self.nome} esta na classe Pessoa, falando ...')


class Cliente(Pessoa):
    def comprar(self):
        print(f'O {self.nomeclasse} {self.nome} esta na classe Cliente, comprando ...')

    def falar(self):
        print(f'O {self.nomeclasse} {self.nome} está na classe Cliente, tentando falar ...')


class ClienteVIP(Cliente):
    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        # super().falar()  # aqui vai chamar a primeira classe pai.
        print(f'O {self.nomeclasse} {self.nome} {self.sobrenome} não fala, manda fazer.')

    def __init__(self, nome, sobrenome, idade):
        # super().__init__(self, nome, idade)
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome
