"""
Aula16 - Exercicios propostos (minhas respostas)

Faça um programa que peça ao usuario para digitar um numero inteiro
informa se este numero e par ou impar. Caso o usuario não digite um numero
inteiro, informe que não é um numero interio.
"""

numero = input("Digite um numero: ")

if numero.isdigit():
    numero = int(numero)
    op = numero % 2
    if op == 0:
        print(f"O {numero} e par")
    else:
        print(f"O numero {numero} e impar")
else:
    print("Nao foi digitado um numero.")


hora = input("Digite a hora sem os minutos: ")
if hora.isdigit():
    hora = int(hora)
    if hora >= 0 and hora <= 5:
        print(f"Vai dormi")
    elif hora >= 6 and hora <= 11:
        print(f"Bom dia")
    elif hora >= 12 and hora <= 17:
        print(f"Boa tarde")
    elif hora >= 17 and hora <= 23:
        print(f"Boa noite")
    else:
        print(f"Digite um horario que estava entre 0-23")
else:
    print(f"Digite um horario que estava entre 0-23")

"""
Faça um programa que peça o primeiro nome do usuario. Se o nome tiver 4 letras ou
menos escreva "Seu nome e curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome e muito grande".
"""

nome = input("Qual e o seu nome: ")
tamanho = len(nome)

if tamanho <= 4:
    print("Seu nome e curto")
elif tamanho <=6:
    print("Seu nome e normal")
else:
    print("Seu nome e grande")