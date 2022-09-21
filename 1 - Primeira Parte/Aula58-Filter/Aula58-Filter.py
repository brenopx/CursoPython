"""
Aula58 - Filter
"""
from Dados import produtos, pessoas, lista


def filtra(produto):
    if produto['preco'] > 50:
        return True
    else:
        return False


def filtrar(pessoa):
    if pessoa['idade'] >= 18:
        return True
    else:
        return False


# nova_lista = filter(lambda x: x > 5, lista)
nova_lista = [x for x in lista if x > 5]
print(list(nova_lista))

# nova_lista = filter(lambda p: p['preco'] > 50, produtos)
nova_lista = filter(filtra, produtos)

for produto in nova_lista:
    print(produto)

print()

maior_de_idade = filter(filtrar, pessoas)

for idade in maior_de_idade:
    print(idade)
