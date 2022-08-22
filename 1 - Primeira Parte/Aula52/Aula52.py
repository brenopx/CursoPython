"""
Aula 52 - Zip - Unido iteráveis
          Zip_longest - Itertools
"""

from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Outra']
estados = ['SP', 'MG', 'BA']

# cidades_estados = zip_longest(estados, cidades, fillvalue='Estado')
cidades_estados = zip(indice, estados, cidades)
#print(list(cidades_estados))

for indice, estado, cidade in cidades_estados:
    print(indice, estado, cidade)

