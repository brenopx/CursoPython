"""
Aula 35 - Funções - def em Python (Parte 1)
"""


def saudacao(mgs='Ola', nome='Usuario'):
    nome = nome.replace('e', '3')
    print(mgs, nome)


saudacao()
saudacao(nome='Breno')
saudacao('Eu posso')
saudacao('Escrever agora?')
