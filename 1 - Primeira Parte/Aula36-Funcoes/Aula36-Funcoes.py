"""
Aula 36 - Funções - def em Python (Parte 2)
"""


def funcao(var):
    return var


variavel = funcao('Valor')

if variavel:
    print(variavel)
else:
    print('Nenhum valor')


def divisao(n1, n2):
    if n2 == 0:
        return
    return n1 / n2


divide = divisao(8, 0)

if divide:
    print(divide)
else:
    print('Conta inválida')


def dumb():
    return [1, 2, 3, 4]


print(dumb(), type(dumb()))


def f(var):
    print(var)


def dumb():
    return f


var = dumb()('E colocar o meu valor aqui.')
print(id(var), id(f))


def dumb():
    return ('Luiz', 'Otavio')


var = dumb()

print(var[1], type(var))
