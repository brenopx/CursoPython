"""
Aula 55 - Combinations. Permutations e Product - Itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores unicos
Produto - Ordem importa e repete valores unicos
"""
from itertools import combinations, permutations, product
pessoas = ['Luiz', 'Andre', 'Eduardo', 'Leticia', 'Fabricio', 'Rose']
# A ordem não importa, ou seja, não vai repetir combinações.
for grupo in combinations(pessoas, 2):
    print(grupo)

print('')
# A ordem importa, ou seja, vai repetir combinações.
for grupo in permutations(pessoas, 2):
    print(grupo)

print('')
# repetindo o mesmo valor
for grupo in product(pessoas, repeat=2):
    print(grupo)
