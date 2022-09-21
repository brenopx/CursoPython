"""
Aula 107 - Random - núremos aleatórios e mais
"""
import random
import string

# Gera um número inteiro entre A e B
# inteiro = random.randint(10, 20)

# Gera um número aleatório usando a função range()
inteiro = random.randrange(900, 1000, 10)

# Gera um número de ponto flutuante entre A e B
# flutuante = random.uniform(10, 20)

# Gera um número de ponto flutuante entre 0 e 1
flutuante = random.random()

print(inteiro)
print(flutuante)

lista = ['Luiz', 'Otávio', 'Maria', 'Rose', 'Jenny', 'Danilo', 'Felipe']

# Seleciona aleatóriamente valores de uma lista
# sorteio = random.choice(lista)
# sorteio = random.choices(lista, k=2)   # Pode repetir
sorteio = random.sample(lista, 2)

# Embaralha a lista
random.shuffle(lista)

# Gera senha aleatória
letras = string.ascii_letters
digitos = string.digits
caracteres = '!@#$%&*._-'
geral = letras + digitos + caracteres
senha = "".join(random.choices(geral, k=20))

print(sorteio)
print(lista)
print(senha)
