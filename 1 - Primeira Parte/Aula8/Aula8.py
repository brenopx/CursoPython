"""
*Cria variáveis para nome (str), idade (int),
*Altura (float) e peso (float) de uma pessoa
*Criar variável com o ano atual (int)
*Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
*Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
*Exibir um texto com todos os valores na tela usando F-Strings ( com as chaves)
"""

nome = 'Breno Pereira Xavier'
idade = 23
altura = 1.68
peso = 65
ano_atual = 2021
nascimento = ano_atual - idade
imc = peso / (altura ** 2)

#print(f'{nome} tem {idade} anos, com {peso} kg, {altura} de altura, nasceu em {nascimento} e tem um imc de {imc:.2f}')
print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}Kg.')
print(f'O IMC de {nome} e {imc:.2f}.')
print(f'{nome} nasceu em {nascimento}.')