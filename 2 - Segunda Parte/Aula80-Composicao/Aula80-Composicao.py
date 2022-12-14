"""
Aula 80 - Composição - Python Orientado a Objetos
"""
from classes import Cliente

cliente1 = Cliente('Luiz', 32)
cliente1.insere_endereco('Belo Horizonte', 'Mg')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()

cliente2 = Cliente('Maria', 55)
cliente2.insere_endereco('São Paulo', 'SP')
cliente2.insere_endereco('Rio de Janeiro', 'RJ')
cliente2.insere_endereco('Salvador', 'BA')
print(cliente2.nome)
cliente2.lista_enderecos()
del cliente2
print()

cliente3 = Cliente('João', 19)
cliente3.insere_endereco('São Paulo', 'SP')
print(cliente3.nome)
cliente3.lista_enderecos()
del cliente3
print()

print('##############################################')