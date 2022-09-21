"""
Aula 121 - Asserções (Assertions)
"""
from Calculadora import soma


# print(soma(10, 20))
# print(soma(-10, 20))
# print(soma(1.5, 2.5))
# print(soma('15', 15))

# try:
#     print(soma('15', 15))
# except TypeError as e:
#     print('Conta inválida')
#     print(e)

try:
    print(soma('15', 15))
except AssertionError as e:
    print(f'Conta inválida: {e}')

print(f'A soma de 15 + 15 = {soma(15, 15)}')
print('Chegou no final, ate mais :)')
