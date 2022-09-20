"""
Aula 69 - Problema dos parametros mutáveis em funções
"""
# Objetos Mutaveis
# Listas, Dicionarios ....
# Objetos Imutaveis
# Tuplas, string, numeros, True, ....


def lista_de_clientes(clientes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista


lista_clientes_1 = ['Fabrício']
print(lista_clientes_1)
clientes1 = lista_de_clientes(['João', 'Maria', 'Eduardo'], lista_clientes_1)
clientes2 = lista_de_clientes(['Marcos', 'Jonas', 'Zico'])
clientes3 = lista_de_clientes(['Jose'])

print(lista_clientes_1)
print(clientes1)
print(clientes2)
print(clientes3)
