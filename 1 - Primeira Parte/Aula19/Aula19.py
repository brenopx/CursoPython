""""
Manipulando strings - Aula 19
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc....
Essas funções podem ser usadas diretamente em casa tipo.

Você pode conferir tudo isso em:
https://docs.python.org/3/library/stdtypes.html (tipos built-in)
https://docs.python.org/3/library/functions.html (funções built built-in)
"""
# positivos [012345678]
texto = 'Python s2'
# negativo -[987654321]  o indice negativo e usado para pegar os ultimos

print(texto[2])

url = 'www.google.com.br/'
print(url[:-1])

nova_string = texto[2:6]
print(nova_string)
nova_string = texto[:6]  # [0:6]
print(nova_string)
nova_string = texto[7:]  # [7:9]
print(nova_string)
nova_string = texto[-1]
print(nova_string)
nova_string = texto[-9:-3]
print(nova_string)
nova_string = texto[0::2]  # usado para ficar pulando, por exemplo de dois em dois
print(nova_string)
nova_string = texto[0:8:4]
print(nova_string)

print(len(texto))

for letra in texto:
    print(letra)