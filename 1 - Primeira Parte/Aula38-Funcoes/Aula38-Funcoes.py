"""
Aula 38 - Funções (def) em Python - *args **kwargs - Parte 3
"""

# def func(*args):
# print(args)

# lista = [1,2,3,3]
# n1, n2, *n = lista
# print(n1, n2, *n)

# print(lista)
# print(*lista, sep = '-')


def func(*args):
    print(args)
    print(args[0])
    print(args[-1])
    print(f'Tamanho do args = {len(args)}')


func(1, 2, 3)
func(1, 2, 3, 4, 5)


def func(*args):
    args = list(args)
    args[0] = 20
    print(args)


func(1, 2, 3, 3, 4, 5)


def func(*args):
    for v in args:
        print(v)


func(1, 2, 3, 3, 4, 5)


def func(*args):
    print(args)


lista = [1, 2, 3, 4]
lista2 = [50, 60, 70, 80, 90]
func(*lista, 10, 20, 30, 40, *lista2)


def func(*args, **kwargs):
    print(args)
    print(kwargs)
    print(kwargs['nome'], kwargs['sobrenome'])

    idade = kwargs.get('idade')

    if idade is not None:
        print(idade)
    else:
        print('Idade não existe')


lista = [1, 2, 3, 4]
lista2 = [50, 60, 70, 80, 90]
func(*lista, 10, 20, 30, 40, *lista2,
     nome='Luiz', sobrenome='Miranda')
