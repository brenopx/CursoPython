"""
Aula 82 - Sobreposição de membros - Python Orientado a Objetos
Associação - Usa | Agragação - Tem | Composição - E dono | Herança - E
"""
from classes import *
p1 = Pessoa('João', 20)
p1.falar()

print()

c1 = Cliente('Luiz', 23)
c1.comprar()

print()

c2 = ClienteVIP('Ronda', 'Rousey', 25)
c2.falar()
