"""
Aula 43 - Dicionario em Python
"""
import copy


d1 = {'chave1': 'valor da chave'}
d1['nova_chave'] = 'Valor da nova chave'

print(d1)
print(d1['chave1'])

d2 = dict(chave1='Valor da chave', chave2='Valor da outra chave')
print(d2)

d3 = {'chave1': 'valor', 'chave2': 'valor', 'chave3': 'valor real'}
print(d3)

d4 = {1: 'valor', 2: 'valor', 3: 'valor real'}
print(d4)

d5 = {
    'str': 'valor',
    123: 'outro valor',
    (1, 2, 3, 4): 'Tupla',
}

print(d5[(1, 2, 3, 4)])
print(d5.get('nomedachave'))

d5['str'] = 'Atualizando'
d5.update({'nova_chave': 'novo_valor'})

del d5['str']  # excluindo

print('str' in d5)
print('str' in d5.keys())
print('valor' in d5.values())

print(d5)
print(len(d5))

d6 = {
    'chave1': 'valor',
    'chave2': 'outro valor',
    'chave3': 'Mais um valor',
}

for k in d6:
    print(k)

for v in d6.values():
    print(v)

for k in d6.items():
    print(k[0], k[1])

for k, v in d6.items():
    print(k, v)

clientes = {
    'cliente1': {
        'nome': 'Luiz',
        'sobrenome': 'Otavio',
    },
    'cliente2': {
        'nome': 'João',
        'sobrenome': 'Moreira',
    },
    'cliente3': {
        'nome': 'Maria',
        'sobrenome': 'Moreira',
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')

d7 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Luiz', 'Otavio']}
v = d7.copy()  # copia fraca, qualquer alteração vai ser feita nos dois

v[1] = 'Luiz'

print(v['d'][0])

v1 = copy.deepcopy(d7)  # copia verdadeira, cria dois dicionarios
v1['d'][0] = 'Joãozinho'

print(d7)
print(v)

lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
]

d8 = dict(lista)
print(d8)

d9 = {
    1: 2,
    2: 3,
    4: 5,
}

d10 = {
    'a': 'b',
    'c': 'd',
}
d1.update(d2)

d1.pop(4)
# d1.popitem() excluir o ultimo
print(d1)
