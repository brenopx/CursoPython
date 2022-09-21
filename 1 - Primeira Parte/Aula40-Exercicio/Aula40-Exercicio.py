"""
Aula 40 - Exercicios

1 - Crie uma função1 que recebe uma função2
como parametro e retorne o valor da função2
executada.

2 - Crie uma função1 que recebe uma função2
como paramentro e retorne o valor da função2
executada. Faça a função1 executar duas funções
que recebam um numero diferente de argumento
"""


def fun2(a, b):
    soma = a + b
    return soma


def fun1(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


ex = fun1(fun2, 3, 3)
print(ex)
ex = fun1(fun2, 3, 9)
print(ex)
ex = fun1(fun2, '3', '3')
print(ex)


def ola_mundo():
    return 'Ola mundo'


def mestre(funcao):
    return funcao()


executando = mestre(ola_mundo)
print(executando)


def mestre(funcao, *args, **wkargs):
    return funcao(*args, **wkargs)


def fala_oi(nome):
    return f'Oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


executando = mestre(fala_oi, 'Luiz')
executando2 = mestre(saudacao, 'Ola', 'Breno')
print(executando)
print(executando2)
