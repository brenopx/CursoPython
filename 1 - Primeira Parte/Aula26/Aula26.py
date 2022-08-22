""""
Aula 26 - Split, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # list / objetos iteráveis
"""
"""
string = 'O Brasil é o pais do futebol, o Brasil é penta.'
lista_1 = string.split(' ')
lista_2 = string.split(',')

print(lista_1)
print(lista_2)


palavra = ''
contagem = 0
for valor in lista_1:
    print(valor)
    print(f'A palavra {valor} apareceu {lista_1.count(valor)}x na frase.')
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')

for valor in lista_2:
    print(valor.strip().capitalize())
    
# string = ['O', 'Brasil', 'é', 'penta.']
string = 'O Brasil é penta'
lista = string.split(' ')
string2 = ','.join(lista)

print(string)
print(lista)
print(string2)

"""
string = 'O Brasil é penta.'
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])

lista = [
    [0, 'Luiz'],
    [1, 'João'],
    [2, 'Maria'],
]
for indice, nome in lista:
    print(indice, nome)

n1, n2, n3 = lista

print(n2)





















