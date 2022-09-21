"""
Aula 37 - Exercicios Propostos

1 - Crie uma função que exibe uma saudação com os
parametros saudação e nome.

2 - Crie uma função que recebe 3 número como parametros
e exiba a soma ente eles.

3- Crie uma função que receba 2 numeros. O primeiro é o
valor e o segundo um percentual (ex. 10%)
Retorne o valor d primeiro numero somado do auumento
percentual do mesmo

4 - Fizz Buzz - Se o paramentro da função for divisivel
por 3, retorne fizz, se o paramentro da função for divisivel
por 5, retorne buzz. Se o paramentro da funçao for divisivel
por 5 e por 3, retorne fizzBuzz, caso contrario, retorne o
numero enviado.
"""
from random import randint


def sau(saudacao='Ola', nome='Usuario'):
    print(f'{saudacao}, {nome}')


def soma(a, b, c):
    return a + b + c


sau(nome='breno')
print(soma(1, 2, 3))


def por(a, b):
    v = (b/100) * a
    return v + a


print(por(10, 10))


def fb(a):
    if a % 3 == 0 and a % 5 == 0:
        return 'fizzBuzz'
    elif a % 3 == 0:
        return 'fizz'
    elif a % 5 == 0:
        return 'Buzz'
    else:
        return a


print(fb(15))


for i in range(100):
    aleatorio = randint(0, 100)

    print(fb(aleatorio))
