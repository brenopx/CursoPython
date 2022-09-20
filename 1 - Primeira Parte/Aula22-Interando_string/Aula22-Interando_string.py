""""
Aula22 - Interando string com while em python
         Indices, obs: um valor que possui indices e chamado de iterável
         0123456789 ..................... 33
"""
frase = 'o rato roeu a roupa  do rei de roma'
tamanho_frase = len(frase)
print(tamanho_frase)
print(frase[5])
nova_string = ''

perguta = input('Na frase o rato roeu a roupa do rei de roma,\
 escolha uma letra para ficar maiuscula: ')

contador = 0
while contador < tamanho_frase:
    if frase[contador] == perguta:
        nova_string += frase[contador].upper()
    else:
        nova_string += frase[contador]
    contador += 1

print(nova_string)
