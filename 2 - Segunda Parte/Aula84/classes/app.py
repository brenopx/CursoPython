"""
Polimorfismo é o principio que permite que classes derivaas de uma
mesma superclasse tenha, métodos iguais (de mesma assinatura) mas
comportamentos diferentes.
Mesma assinatura = Mesma quantidade e tipo de parãmetros
"""
from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def fala(self, msg): pass


class B(A):
    def fala(self, msg):
        print(f'B esta falando {msg}')


class C(A):
    def fala(self, msg):
        print(f'C esta falando {msg}')

b = B()
c = C()
b.fala("Um Assunto")
c.fala("Outro Assunto")

