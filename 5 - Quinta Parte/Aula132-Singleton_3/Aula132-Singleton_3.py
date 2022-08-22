"""
Aula 132 - Singleton #3
"""


# class Meta(type):
#     def __call__(cls, *args, **kwargs):
#         print('CALL é executado')
#         return super().__call__(*args, **kwargs)


# class Pessoa(metaclass=Meta):
#     def __new__(cls, *args, **kwargs):
#         print('NEW é executado')
#         return super().__new__(cls)

#     def __init__(self, nome):
#         print('INIt é executado')
#         self.nome = nome

#     def __call__(self, x, y):
#         print('call chamado', self.nome, x + y)


# p1 = Pessoa('Luiz')
# p1(2, 2)
# print(p1.nome)
from typing import Dict


class Singleton(type):
    _instances: Dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class AppSettings(metaclass=Singleton):
    def __init__(self):
        self.tema = 'O Tema Escuro'
        self.font = '18px'


if __name__ == "__main__":
    as1 = AppSettings()

    as1.tema = 'O Tema Claro'
    print(as1.tema)

    as2 = AppSettings()

    print(as1.tema)
    print(as2.tema)

    as3 = AppSettings()

    print(as3.tema)
