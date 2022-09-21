""""
Aula 30 - Operador ternário em Python
"""

logged_user = True

if logged_user:
    msg = 'Usuario logado.'
else:
    msg = 'Usuario nao logado.'

msg = 'Usuario dentro.' if logged_user else 'Usuario fora.'

print(msg)

idade = input('Qual a sua idade?')

"""
if idade >= 18:
    print('Pode acessar')
else:
    print('Não pode acessar')

e_de_maior = (idade >= 18)

msg = 'Pode acessar' if e_de_maior else 'Não pode acessar.'
"""

if not idade.isnumeric():
    print('Voce precisa digitar apenas número')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = 'Pode acessar' if e_de_maior else 'Não pode acessar'

print(msg)
