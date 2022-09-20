"""
Aula14 - Documentação e funçoes buil-in uteis
"""
num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ')

# isnumeric isdigit isdecimal
# numeros e positivos (123456789)
print(num1.isnumeric())
print(num2.isnumeric())

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(f'A soma dos dois nmeros sera {num1 + num2}')
else:
    print('Nao pude converter os numeros para realizar contas.')

try:
    num1 = float(num1)
    num2 = float(num2)
    print(f'A soma dos dois nmeros sera {num1 + num2} em float')
except:
    print('ERROR')
