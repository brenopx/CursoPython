"""
Aula49 - Compreeção de Dicionario em Python
"""

lista = [
        ('chave', 'valor'),
        ('chave2', 'valor2'),
]

d1 = {x: y.upper() * 2 for x, y in lista}
#  d1 = dict(lista)
print(d1)

d2 = {x: y for x, y in enumerate(range(5))}
print(d2)

d3 = {f'chave_{x}': x**2 for x in range(5)}
print(d3, type(d3))
