"""
Aula17 - Exercicios propostos (respostas do professor)

Faça um programa que peça ao usuario para digitar um numero inteiro
informa se este numero e par ou impar. Caso o usuario não digite um numero
inteiro, informe que não é um numero interio.
"""
numero_inteiro = input('Digite um numero inteiro: ')

if numero_inteiro.isdigit():
    numero_inteiro = int(numero_inteiro)

    if numero_inteiro % 2 == 0:
        print(f"{numero_inteiro} e par")
    else:
        print(f"{numero_inteiro} e impar")
else:
    print('Isso nao  um numero inteiro')

numero_inteiro = input('Digite um numero inteiro: ')

if not numero_inteiro.isdigit():
    print('Isso nao e um numero inteiro')
else:
    numero_inteiro = int(numero_inteiro)

    if not numero_inteiro % 2 == 0:
        print(f'{numero_inteiro} e impar')
    else:
        print(f'{numero_inteiro} e par')

"""
Faça um progrma que pergunta a hora ao usuario e, baseando-se no horario
descrito, exiba a saudação apropriada. EX.
Bom dia 06-11, Boa tarde 12-17, Boa noite 18-23, Vai dormi 00-05.  
"""
horario = input("Digite um horario (0-23): ")
if horario.isdigit():
    horario = int(horario)
    if horario <0 or horario > 23:
        print("Horario deve estar entre 0 e 23")
    else:
        if horario <= 11:
            print("Bom dia!")
        elif horario <=17:
            print("Boa Tarde!")
        else:
            print("Boa Noite!")
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
    print("Seu nome e muito grande")