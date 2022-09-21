"""
Aula 88 - Context Manager - Criando e Usado gerenciadores de contexto
"""
# arquivo = open('abc.txt', 'w')
# arquivo.write('Alguma coisa')
# arquivo.close()
#
# with open('abc.txt', 'w') as arquivo:
#     arquivo.write('alguma coisa')
#
# class Arquivo:
#     def __init__(self, arquivo, modo):
#         print('Abrindo arquivo')
#         self.arquivo = open(arquivo, modo)
#
#     def __enter__(self):
#         print('retornando arquivo')
#         return self.arquivo
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('fechando arquivo')
#         self.arquivo.close()
#         # print(exc_type)
#         # print(exc_val)
#         # print(exc_tb)
#         # Tratei a exceção
#         return True
#
#
# with Arquivo('abc.txt', 'w') as arquivo:
#     arquivo.write('alguma coisa de novo')

from contextlib import contextmanager


@contextmanager
def abrir(arquivo, modo):
    try:
        print('Abrindo Arquivo')
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        print('fechado arquivo')
        arquivo.close()


with abrir('abc.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
