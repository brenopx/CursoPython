""""
Aula23 - For in em Python
Iterando strings com for
Função range (start = 0, stop, step = 1)
"""
texto = 'Python'

c = 0
while c < len(texto):
    print(texto[c])
    c += 1

for letra in texto:
    print(letra)

for n, letra in enumerate(texto):
    print(n, letra)

for numero in range(10):
    print(numero)

for n in range(20, 10, -1):
    print(n)

for n in range(0, 100, 8):
    print(n)

print('#################')

for n in range(100):
    if n % 8 == 0:
        print(n)

texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)

# continue = Pular para a proxima setença do laço
# break = Termina do laço




















