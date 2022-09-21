""""
Aula 41 - Função Anonimas em Python
"""


def funcao(arg1, arg2):
    return arg1 * arg2


var = funcao(2, 2)
a = lambda x, y: x * y


print(a(2, 2))

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

# def func(item):
#    return item[1]
# lista.sort(key=lambda item: item[1], reverse=True)
# print(lista)

print(sorted(lista, key=lambda i: i[1], reverse=True))
