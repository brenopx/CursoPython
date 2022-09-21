"""
Aula 89 - Herança Simples(Tirando Dúvidas)
Animal -> respirar (é um Animal())
    Lobo(Animal) -> respirar / uivar (lobo é um Lobo e um Animal())
    Cachorro(Lobo) -> respirar / uivar / viver em cidade / latir
    (Cachorro é um Cachorro(), Támbém é um Lobo() e um Animal())

class Animal:
    def __init__(self):
        self.nomeclasse = self.__class__.__name__

    def respirar(self):
        print(f'O {self.nomeclasse} esta respirando')

class Lobo(Animal):
    def uivar(self):
        print(f'O {self.nomeclasse} esta uivando')

class Cachorro(Lobo):
    def viver_em_cidade(self):
        print(f'O {self.nomeclasse} esta vivendo na cidade')

    def latir(self):
        print(f'O {self.nomeclasse} esta latindo')

c = Cachorro()
c.viver_em_cidade()
c.latir()
c.uivar()
c.respirar()
l = Lobo()
l.uivar()
l.respirar()
a = Animal()
a.respirar()
"""
"""
Biblioteca -> chama_interface
    Interface(Biblioteca) -> metodo_interface
       metodo_da_interface

main -> interface
"""
from classes.interface import Interface


i1 = Interface()
i1.chama_metodo_da_interface()
