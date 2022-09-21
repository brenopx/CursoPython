"""
Aula 87 - Métodos Mágicos - Python Orientado a Objeto
https://rszalski.github.io/magicmethods
"""


class A:
    # def __new__(cls, *args, **kwargs):
    #     # print('Eu sou o new')
    #     # cls.nome = 'Luiz Otávio'
    #     #
    #     # def haha(*args, **kwargs):
    #     #     print('Fala OI')
    #     #
    #     # cls.haha = haha
    #     # return super().__new__(cls)
    #     # return object.__new__(cls)
    #
    #     if not hasattr(cls, '_jaexiste'):
    #         cls._jaexiste = object.__new__(cls)
    #
    #     return cls._jaexiste

    def __init__(self):
        print('Eu sou o INIT')

    def __call__(self, *args, **kwargs):
        # print(args)
        # print(kwargs)
        resultado = 1

        for i in args:
            resultado *= i

        return resultado

    def fala_oi(self):
        print('Oi')

    # def __setattr__(self, key, value):
    #     if key == 'nome':
    #         self.__dict__[key] = 'Voce não pode fazer isso'
    #     else:
    #         self.__dict__[key] = value
    #
    #     # self.__dict__[key] = value  # Esse e o comportamento padrão

    def __del__(self):
        print('Objeto coletado.')

    # def __str__(self):
    #     # return 'Essa é a class A criada para tal coisa'
    #     return "<class 'A'>"

    def __len__(self):
        return 55


# a = A()
# b = A()
# c = A()

# print(a == b)
# print(b == c)
# print(id(a), id(b), id(c))
# print(a.nome)
# a.haha()

# a(1, 2, 3, 4, 5, nome= 'Luiz')
# variavel = a(1, 2, 4, 5, 3, 7, 8, 9, 10)
# print(variavel)
# a.fala_oi()
# a = A()
# a.nome = 'Luiz Otávio'
# a.qualquer = 255
# print(a.qualquer)
# print(a.nome)
# a = A()
# print(a)
a = A()
print(len(a))
