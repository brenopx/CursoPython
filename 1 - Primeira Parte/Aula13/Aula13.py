"""
Aula13 - len
"""
usuario = 'Breno Pereira'  #input('Digite seu usuario: ')
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print('Voce precisa digitar pelo menos 6 caracteres')
else:
    print('Voce esta no sistema')

string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra coisa: ')

#soma = len(string1) + len(string2)
#print(f'{soma}')

print(f'A quantidade total de caracteres digitados foi {len(string1) + len(string2)}')
print(len(string2))
print(string2.__len__())