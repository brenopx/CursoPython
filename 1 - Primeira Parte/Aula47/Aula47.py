"""
Aula47 - Compleençõa de listas em Python
"""

lista = [1, 3, 4, 5, 6, 8, 9]
exemplo1 = [variavel for variavel in lista]

exemplo2 = [v * 2 for v in lista]
exemplo3 = [(v, v2) for v in lista for v2 in range(3)]
print(exemplo3)

lista2 = ['Luiz', 'Mauro', 'Maria']
exemplo4 = [v.replace('a', '@').upper() for v in lista2]

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)
exemplo5 = [(y, x) for x, y in tupla]
exemplo5 = dict(exemplo5)

print(exemplo5)

lista3 = list(range(100))
exemplo6 = [v for v in lista3 if v % 3 == 0 if v % 8 == 0]
print(exemplo6)

exemplo7 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in lista3]
print(exemplo7)
