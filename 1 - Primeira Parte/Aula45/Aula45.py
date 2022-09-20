"""
Aula 45 - Sets (conjuntos) em Python
Sets é muito para eliminar elementos repitidos de uma lista
add (adiciona), update (atualiza), clear (limpa), discard(remover)
union | (une)
intersection & ( todos os elementos presentes nos dois sets)
differente - (Elementos apenas no set da esquerda)
symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)
"""

s1 = {1, 2, 3, 4, 5, 6, 7}

print(s1)

for v in s1:
    print(v)

s2 = set()
s2.add(1)
s2.add(2)
s2.add((1, 2, 3, 4, 'Luiz'))
s2.discard(2)
s2.update('a')
# s2.update('Python')  não usar pois fica mudando a ordem
s2.add('Python')
print(s2)

l1 = [1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 8, 'Luiz', 'Luiz']
print(l1)
l1 = set(l1)
l1 = list(l1)

print(l1)

s2 = {1, 2, 3, 4, 5, 7}
s3 = {1, 2, 3, 4, 5, 6}
s4 = s2 | s3  # uniao entre eles
s5 = s2 & s3  # intercção entre os dois
s6 = s2 - s3  # Elementos apenas no set da esquerda
s7 = s2 ^ s3  # Elementos que estão nos dois sets, mas não em ambos

print(s4)
print(s5)
print(s6)
print(s7)

lista = ['Luiz', 'João', 'Maria']
lista1 = ['João', 'Maria', 'Maria', 'João', 'João', 'João', 'Luiz']

#  lista = list(set(lista))
#  lista1 = list(set(lista1))
#  print(lista == lista1)

if set(lista) == set(lista1):
    print('L1 é igual a l2')
else:
    print('L1 é diferente de L2')
