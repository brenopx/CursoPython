"""
Aula57 - Mapeamento
"""
from Dados import produtos, pessoas, lista


def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05)
    return p


def aumenta_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.2)
    return p


print(lista)

# nova_lista = map(lambda x: x * 2, lista)
nova_lista = [x * 2 for x in lista]
print(list(nova_lista))

for produto in produtos:
    print(produto)

# precos = map(lambda p: p['preco'], produtos)
novos_produtos = map(aumenta_preco, produtos)
for produto in novos_produtos:
    print(produto)

print(pessoas)
# nomes = map(lambda p: p['nome'], pessoas)
nomes = map(aumenta_idade, pessoas)

for pessoa in nomes:
    print(pessoa)
