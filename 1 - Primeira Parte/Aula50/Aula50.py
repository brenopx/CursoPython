"""
Aula50 - Geradores, Iteradores e iteraveis em Pytohn
"""
import sys
import time

lista = 'String'
lista = [0, 1, 2, 3, 4, 5, 6]

# print(hasattr(lista, '__iter__'))
lista = iter(lista)

print(next(lista))
print(next(lista))

print(hasattr(lista, '__next__'))

# for v in lista:
#    print(v)

lista = list(range(1000))

print(sys.getsizeof(lista))


def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)


g = gera()

for v in g:
    print(v)

print(hasattr(g, '__iter__'))
print(hasattr(g, '__next__'))


def gera():
    variavel = 'Valor 1'
    yield variavel
    variavel = 'Valor 2'
    yield variavel
    variavel = 'Valor1'
    yield variavel


g = gera()

print(next(g))
print(next(g))
print(next(g))

for v in g:
    print(v)

lista = list(range(1000))
lista1 = [x for x in range(100000)]
print(type(lista))
lista2 = (x for x in range(100000))
print(type(lista))
print(sys.getsizeof(lista1))
print(sys.getsizeof(lista2))

for v in lista2:
    print(v)
