"""
Aula 77 - Reforço - Getters e Setters - Parte1
O que é um Setters? E uma função que vai configurar o valor de algo (O Setters Não funciona sozinho)
O que é um Getters? E uma função que vai obter um valor de algo configurado com o Setter ou não (ele pode estar sozinho)
"""
class Pessoa:
    # def __init__(self):
    #     self._nome = 'inicial'
    def __init__(self, nome):
        # self._nome = nome # Não vai passar pelo setter
        self.nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        print('O SETTER FOI EXECUTADO')
        # nome += ' Sei lá'
        self._nome = nome

    @property
    def sobrenome(self):
        return 'DESCONHECIDO'

p1 = Pessoa('Otávio')
# print(p1.nome())
# p1.nome = 'João'
print(p1.nome)
print(p1.sobrenome)
