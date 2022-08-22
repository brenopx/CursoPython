"""
Aula 81 - Herança simples - Python Orientado a Objeto
Associação - Usa | Agregação - Tem | Composição - È dono | Herança - E
"""
from classes import *

c1 = Cliente('Luiz', 45)
print(c1.nome)
c1.falar()
c1.comprar()

a1 = Aluno('Maria', 52)
print(a1.nome)
a1.falar()
a1.estudar()

p1 = Pessoa('João', 43)
p1.falar()
