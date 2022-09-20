"""
Iniciar com letra, pode conter números, separar com _, letras minúsculas
"""
nome = 'Luiz Otávio'  # string
idade = 32  # inteiro
altura = 1.80  # float
e_maior = idade > 18  # bool
peso = 80  # inteiro
data_1 = True  # bool
data_atual = 2021  # inteiro
# imc = peso / (altura * altura)
imc = peso / (altura ** 2)
print(nome, type(nome))
print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('E maior de idade:', e_maior)
var = """80"""
print(var, type(var))

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
