"""
Aula66 - Criando, lendo, escrevendo e apagando arquivos
https://docs.python.org/3/library/functions.html#open
"""
# file = open('abc.txt', 'w+')
# file.write('Linha 1\n')
# file.write('Linha 2\n')
# file.write('Linha 3\n')
#
# file.seek(0, 0)
# print('Lendo linhas: ')
# print(file.read())
# print('###################')
#
# file.seek(0, 0)
# print(file.readline(), end='')
# print(file.readline(), end='')
# print(file.readline(), end='')
# print('###################')
#
# file.seek(0, 0)
# # print(file.readlines())
# # for linha in file.readlines():
# for linha in file:
#     print(linha, end='')
#
# file.close()
# try:
#     file = open('abc.txt', 'w+')
#     file.write('Linha')
#     file.seek(0)
#     print(file.read())
# finally:
#     file.close()

# with open('abc.txt', 'w+') as file:
#     file.write('Linha 1\n')
#     file.write('Linha 2\n')
#     file.write('Linha 3\n')
#
#     file.seek(0)
#     print(file.read())
#
# with open('abc.txt', 'r') as file:
#     print(file.read())
#
# with open('abc.txt', 'a+') as file:
#     file.write('Outra Linha\n')
#     file.seek(0)
#     print(file.read())
#
# import os
# os.remove('abc.txt')

import json

d1 = {
    'Pessoa 1': {
        'nome': 'Luiz',
        'idade': 25,
    },
    'Pessoa 2': {
        'nome': 'Rose',
        'idade': 30,
    },
}
print(d1)
d1_json = json.dumps(d1, indent=True)
print(d1_json)

with open('abc.json', 'w+') as file:
    file.write(d1_json)

