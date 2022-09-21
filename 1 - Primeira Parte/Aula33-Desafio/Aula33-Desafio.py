""""
Aula 33 - Desafio - Valide um cpf

CPF = 168.995.350-09
_______________________________
1 * 10 = 10         #         1 * 11 = 11 <-
8 * 8 = 64          #         6 * 10 = 60
9 * 7 = 63          #         8 * 09 = 72
9 * 6 = 54          #         9 * 08 = 72
5 * 5 = 25          #         9 * 07 = 63
3 * 4 = 12          #         5 * 06 = 30
5 * 3 =15           #         3 * 05 = 15
0 * 2 = 0           #         5 * 04 = 20
                    #         0 * 03 = 0
                    #         0 * 02 = 0
       297          #                 343
11- (297 % 11 ) = 11#         11 - (343 % 11) = 9
11 > 9 = 0          #         Digito 2 = 9
Digito 1 = 0        #
                    #
"""
print('doi')
while True:
    cpf = input("Digite um CPF: ")
    novo_cpf = cpf[:-2]  # novo_cpf = cpf[:9]
    reverso = 10
    total = 0

    for index in range(19):
        if index > 8:
            index -= 9
        # print(index, reverso)

        total += int(novo_cpf[index]) * reverso

        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
                total = 0
                novo_cpf += str(d)
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)
    if cpf == novo_cpf and not sequencia:
        print('Valido')
    else:
        print('Invalido')
