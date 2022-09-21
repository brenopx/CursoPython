"""
Aula 54 - count - Itertools
"""
# from types import GeneratorType
# variavel = zip('Alo', 'Alo')
# print(list(variavel))
# print(next(variavel))
# print(next(variavel))
# print(next(variavel))

# variavel = ((x, y) for x, y in zip('Alo', 'Alo'))
# print(isinstance(variavel, GeneratorType))
# print(list(variavel))

from itertools import count

contador = count()  # contador sem fim, muito cuidado!!!!
# for valor in contador:    # laço infinito
#    print(valor)

# contador = count(start=5)
# contador = count(start=5, step=2)
# contador = count(start=5, step=0.1)
contador = count(start=9, step=-0.1)  # andando pra tras

for valor in contador:
    # print(valor)
    print(round(valor, 2))

    if valor >= 10 or valor <= -10:
        break

contador = count()
lista = ['Luiz', 'Joao', 'Maria', 'Jose', 'Silva', 'Eduardo']
lista = zip(contador, lista)
print(list(lista))
