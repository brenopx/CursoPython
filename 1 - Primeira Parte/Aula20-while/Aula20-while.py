""""
while em Python - Aula20
utilizando para realizar ações enquando
uma condição for verdadeira

Requisitos: Entender condições e operadores
while = enquanto
while condição:
    pass

"""

x = 0
while x <= 10:
    if x == 3:
        x = x + 1
        continue
    if x == 7:
        break
    print(x)
    x = x + 1

x = 0  # coluna
y = 0  # linha

while x < 10:
    y = 0
    while y < 5:
        print(f'X vale {x} e Y vale {y}')
        y += 1
    x += 1

while True:
    num_1 = input('Digite um valor inteiro: ')
    num_2 = input('Digite um outro valor inteiro: ')
    operador = input('Digite o operador: ')

    if (not num_1.isnumeric() and not num_2.isnumeric()) and \
       (not operador == '+' and not operador == '-' and not operador == '*'
       and not operador == '/'):
        print('Voce precisa digitar um numero no primeiro, outro no segundo\
        valor e um operador valido !!!')
        continue
    if not num_1.isnumeric() and (not operador == '+' and
       not operador == '-' and
       not operador == '*' and not operador == '/'):
        print('Digite em valor inteiro no primeiro e um operador valido!!!!')
        continue
    if not num_2.isnumeric() and (not operador == '+' and
       not operador == '-' and not operador == '*' and not operador == '/'):
        print('Digite em valor inteiro no segundo e um operador valido!!!!')
        continue
    if not num_1.isnumeric() and not num_2.isnumeric():
        print('Digite em cada um dos dois valores, numeros inteiros!!!!')
        continue
    if not num_1.isnumeric():
        print('Voce precisa digitar um numero no primeiro valor!!!!')
        continue
    if not num_2.isnumeric():
        print('Voce precisa digitar um numero no segundo valor!!!!!')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 * num_2)
    elif operador == '/':
        print(num_1 / num_2)
    else:
        print('Digite um operador valido!!!!!')

    sair = input('Deseja sair? [s]im ou [n]ão: ')
    sair = sair.lower()

    while not sair == 's' and not sair == 'n':
        print(sair)
        print('Responda a pergunta com s ou n!!!!!')
        sair = input('Deseja sair? [s]im ou [n]ão: ')
    if sair == 's':
        print(sair)
        break
    if sair == 'n':
        print(sair)
        continue
print('Acabou!!!')
