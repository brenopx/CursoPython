"""
Condições IF, ELSE e ELSE - Aula 10
"""
if True:
    print("Verdadeiro.")

    num_1 = 2
    num_2 = 4

    print(num_1 + num_2)

if False:
    print("Verdadeiro.")

print('A minha expressao nao e verdadeira.')

if True:
    print("verdade")
else:
    print('falsa')

if False:
    print('Verdadeiro')
    print('O que sera a verdadeira verdade?')
elif False:
    print('Agora e verdadeiro')
    nome = input('Qual e a sua verdade? ')

    print(f'{nome}, essa e a sua verdade, ta brincando?')
elif False:
    print('Sera que um dia foi verdadeiro?')
else:
    print('Nunca foi verdadeiro')
    print('Sera sempre foi a verdade')