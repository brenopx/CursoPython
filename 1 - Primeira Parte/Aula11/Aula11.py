""""
Operadores Relacionais - Aula 11
== igualdade
> maior que
>= maior que ou igual a
< menor que
<= menor que ou igual a
!= diferente de
"""

num_1 = 2 #inteiro
num_2 = '2' #string

expressao = num_1 == num_2

print(expressao)

num_1 = 2 #inteiro
num_2 = 2 #inteiro

expressao = num_1 > num_2

print(expressao)

num_1 = 2 #inteiro
num_2 = 2 #inteiro

expressao = num_1 >= num_2

print(expressao)

num_1 = 2 #inteiro
num_2 = '2' #string

expressao = num_1 != num_2

print(expressao)

var_1 = 'Breno'
var_2 = 'breno'

comparacao = var_1 != var_2

print(comparacao)

#nome = input("Qual e o seu nome? ")
#idade = int(input("Qual e a sua idade? "))

#if idade >= 18:
#    print(f"{nome} esta apto para pegar um emprestimo")
#else:
#    print(f"{nome} NAO esta apto para pegar um emprestimo")

nome = input("Qual e o seu nome? ")
idade = int(input("Qual e a sua idade? "))

if idade >= 20 and idade <=30:
#if idade >= 20 | idade <= 30:
    print(f'{nome} pode fazer um emprestimo')
else:
    print(f'Com a sua idade, voce nao pode fazer um emprestimo')