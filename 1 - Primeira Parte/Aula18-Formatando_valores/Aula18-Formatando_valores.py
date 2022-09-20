""""
Aula18 - Formatando valores com modificadores
:s - Texto (string)
:d - Inteiros (int)
:.(NUMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esqueda
< - Direta
^ - Centro
"""

num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print('{:.2f}'.format(divisao))

nome = 'Luiz Otavio'
print(f'{nome:s}')

num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150
print(f"{num_2:.5f}")

nome = 'Otavio Miranda'
print((50-len(nome)) / 2)

print(f'{nome: ^50}')
print(f'{nome:#^50}')


nome_formatado = '{:@>50}'.format(nome)
print(nome_formatado)

nome_formatado = '{n:^50}'.format(n=nome)
print(nome_formatado)

nome = 'Otavio'
sobrenome = 'Miranda'
nome_formatado = '{} {}'.format(nome, sobrenome)
nome_formatado = '{0} {1}'.format(nome, sobrenome)
print(nome_formatado)

nome = 'Luiz Otavio'
nome = nome.ljust(20, '#')
print(nome)
print(nome.lower())  # tudo minusculo
print(nome.upper())  # tudo maiusculo
print(nome.title())  # Primeiras Letras maiusculas
