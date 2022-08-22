"""
Aula 139 - Template Method
Template Method (comportamental) tem a intenção de definir
um algoritmo em um método, postergando alguns passos
para as subclasses por herança. Template method permite
que subclasses redefinam certos passos de um algoritmo
sem mudar a estrutura do mesmo.

Também é possivel definir hooks para que as subclassses
utilizem caso necessário.

The hollywood principle: "Don't Call Us, We' ll Call You."
(loC - Inversão de controle)
"""
from abc import ABC, abstractmethod


class Abstract(ABC):
    def template_method(self):
        self.hook()
        self.operation1()
        self.base_class_method()
        self.operation2()

    def hook(self): pass

    def base_class_method(self):
        print('OLÁ, EU SOU DA CLASSE ABSTRATA E SEREI EXECUTADO TAMBÉM')

    @abstractmethod
    def operation1(self): pass

    @abstractmethod
    def operation2(self): pass


class ConcreteClass1(Abstract):
    def hook(self):
        print('Olha, eu vou ulilizar o hook')

    def operation1(self):
        print('Operação 1 concluída')

    def operation2(self):
        print('Operação 2 concluída')


class ConcreteClass2(Abstract):
    def operation1(self):
        print('Operação 1 concluída de maneira diferente')

    def operation2(self):
        print('Operação 2 concluída de maneira diferente')


if __name__ == "__main__":
    c1 = ConcreteClass1()
    c2 = ConcreteClass2()
    c1.template_method()
    c2.template_method()
