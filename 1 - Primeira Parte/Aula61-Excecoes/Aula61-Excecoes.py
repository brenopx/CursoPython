"""
Aula 61 - Levantando exceções em Python
"""


def divide(n1, n2):
    if n2 == 0:
        raise ValueError("n2 não pode ser zero")
    return n1 / n2
    # try:
    #    return n1 / n2
    # except ZeroDivisionError as error:
    #    print('Log: ', error)
    #    raise


try:
    print(divide(2, 1))
    print(divide(2, 0))
except ValueError as erro:
    print('Você está tentando dividir por 0.')
    print('Log: ', erro)
