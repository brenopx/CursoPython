""""
Aula 24 - Lista em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
# texto = 'Valor'
# lista1 = [1, 2, 3, 4, 'Luiz Otavio', True, False]
#
# #         0    1    2    3    4
# lista = ['A', 'B', 'C', 'D', 'E']
# #        -5   -4   -3   -2   -1
# lista[4] = 'Qualquer outra coisa'
# string = 'ABCDE'
#
# print(lista[1])
# print(lista[-1])
# print(lista)
# print(lista[0:3])
# print(lista[:3])
# print(lista[2:])
# print(lista[::2])
# print(lista[::-1])  # Mostrar a lista invertida, te tras pra frente
#
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# print(l1)
# print(l2)
#
# l3 = l1 + l2
# print(l3)
#
#
# l1.extend(l2)
# print(l1)
# l1.extend('7')
# print(l1)
#
# l2.append(7)
# print(l2)
#
# l2.insert(0, 'banana')
# print(l2)
#
# l2.pop()
# print(l2)
#
# l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(l2)
# l2.insert(0, 'Banana')
# print(l2)
# del(l2[0])
# print(l2)
# print(max(l2))
# print(min(l2))
#
# l2 = range(1,10)
# print(l2)
#
# l2 = list(range(1,5))
# print(l2)
#
# l2 = list(range(0, 100, 8))
#
# for valor in l2:
#     print(valor)
#
# l2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# soma = 0
# for valor in l2:
#     soma = soma + valor
#
# print(valor)
#
# l = ['string', True, 10, -20.5]
#
# for elem in l:
#     print(f'O tipo de {elem} e {type(elem)}')

# Minha resposta ao desafio
# secreto = 'perfume'
# res = input("Digite uma letra para tentar advinhar qual e a palavra ou tente acertar de primeira: ")
#
# while True:
#     if res == 'perfume':
#         print("Parabens, voce acertou!!!!!!")
#         break
#     elif len(res) > 1 and not res == 'perfume':
#         print('Voce errou, tente novamente')
#         break
#     while len(res) <= 1:
#         contador = 1
#         for re in secreto:
#             if re == res:
#                 print(f'{re}, essa letra esta na palavra, na posição {contador}!!!')
#             if contador == 7:
#                 break
#             contador = contador + 1
#         break
#     res = input("Digite uma letra para tentar advinhar qual e a palavra ou tente acertar de primeira: ")

secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Voce perdeu!!!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahhh isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'Certo, a letrs "{letra}" existe na palavra secreta.')
    else:
        print(f'Errrou, a letra "{letra}" Não existe na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Que legal, Voce ganhou!!! A palavra era {secreto_temporario}.')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances.')
    print()

















