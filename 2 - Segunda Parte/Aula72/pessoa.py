from datetime import datetime

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def falar(self):
        print('Pessoa está falando')

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        # variavel = 'valor'
        # print(variavel)

    def chamando_nome(self):
        print(self.nome)

    def chamando_idade(self):
        print(self.idade)

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return
        if self.falando:
            print(f'{self.nome} não pode comer falando')
            return
        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar, pois está comendo.')
            return
        if self.falando:
            print(f'{self.nome} já esta falando sobre {assunto}')
        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não esta falando')
            return
        print(f'{self.nome} parou de falar.')
        self.falando = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
