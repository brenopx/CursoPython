""""
Aula 28 - Desempacotamento de listas em Python
"""

lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]

n1, n2, *outra_lista, ultimo_da_lista = lista
*outra_lista, n1, n2, n3 = lista

print(n1, n2, n3)
