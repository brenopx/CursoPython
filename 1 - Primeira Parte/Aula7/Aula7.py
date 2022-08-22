nome = 'Luiz Otavio' #string
idade = 32 #inteiro
altura = 1.80 #float
e_maior = idade > 18 #bool
peso = 80
imc = peso / (altura ** 2)

print (nome, 'tem', idade, 'anos de idade e seu imc e', imc)
print(f'{nome} tem {idade} anos de idade e seu imc e {imc:.2f}')
print('{} tem {} anos de idade e seu imc e {:.2f}'.format(nome, idade, imc))
print('{n} tem {i} anos de idade e seu imc e {im:.2f}'.format(n=nome, i=idade, im=imc))