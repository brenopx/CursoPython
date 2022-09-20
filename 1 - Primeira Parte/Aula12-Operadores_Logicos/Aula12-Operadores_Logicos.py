""""
Operadores Lógicos - Aula12
and = E
or = OU
not = negaçao ou inversor
in =
not in =
"""
comparacao = 1
# ( Verdadeiro E Verdadeiro) as duas tem que ser verdadeiro
comparacao == comparacao and comparacao == comparacao

# ( Verdadeiro Ou Verdadeiro) somente uma das duas tem que ser verdadeiro
comparacao == comparacao or comparacao == comparacao

a = 2
b = 3
# O Inversor e muito usado para conferir se o valor esta vazio
if not b > a:
    print('B é maior do que A.')
else:
    print('A e maior do que B.')

nome = 'Breno Pereira'

if 'B' in nome:
    print("Existe a letra B no seu nome")
if 'b' in nome:
    print("Existe a letra b no seu nome")
if 'b' not in nome:
    print("Não existe a letra b no seu nome")

usuario = input('Nome do usuario: ')
senha = input('Senha do Usuario: ')

usuario_bd = 'breno'
senha_bd = '123'

if usuario_bd == usuario and senha_bd == senha:
    print('Voce esta logado no sistema')
else:
    print('Usuario ou senha incorreto')
