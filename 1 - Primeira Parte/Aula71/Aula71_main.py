"""
Aula 71 - Desafio Valide um CNPJ
04.252.011/0001-10  40.688.134/0001-61  71.506.168/0001-11  12.544.992/0001-05

0  4  2  5  2  0  1  1  0  0  0  1  x  x
5  4  3  2  9  8  7  6  5  4  3  2
0  16 6  10 18 0  7  6  0  0  0  2 = 65 ##
Formula -> 11 - (65 % 11) = 1
Primeiro digito = 1

0  4  2  5  2  0  1  1  0  0  0  0  1  x
6  5  4  3  2  9  8  7  6  5  4  0  2
0  20 8  15 4  0  8  7  0  0  0  3  2 = 67 ##
Formula -> 11 - (67 % 11) = 11 (Como o resultado e maior que 9, entao e 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10

Recap.
543298765432 -> Primeiro Digito
6543298765432 -> Segundo Digito
"""
import cnpj
cnpj1 = '04.252.011./0001-10'
cnpj2 = '11.111.111./1111-11'
cnpj3 = '00.000.000./0000-00'
cnpj4 = '71.506.168/0001-11'
cnpj5 = 'Breno Pereira'

if cnpj.valida(cnpj1):
    print(f'{cnpj1} é válido')
else:
    print(f'{cnpj1} é inválido')
cnpj.valida(cnpj2)
cnpj.valida(cnpj3)
if cnpj.valida(cnpj4):
    print(f'{cnpj4} é válido')
else:
    print(f'{cnpj4} é inválido')
if cnpj.valida(cnpj5):
    print(f'{cnpj5} é válido')
else:
    print(f'{cnpj5} é inválido')

for i in range(100):
    novo_cnpj = cnpj.gera()
    formatado = cnpj.formata(novo_cnpj)
    print(formatado)

