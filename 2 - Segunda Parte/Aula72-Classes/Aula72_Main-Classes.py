"""
Aula 72 - Classes - Python Orientado a Objeto
"""
from pessoa import Pessoa

p1 = Pessoa('Luiz', 29)
p2 = Pessoa('Jõao', 32)

# print(p1)
# print(p2)
# p1.nome = 'Luiz'
# p2.nome = 'Jõao'
#
# print(p1.nome)
# print(p2.nome)
#
# p1.falar()

# p1.chamando_nome()
# p2.chamando_nome()
# p1.chamando_idade()
# p2.chamando_idade()
# p1.comer('Jõao')
# p2.comer('Luiz')
# p1.comer('Jõao')
# p1.parar_comer()
# p2.parar_comer()
# p2.parar_comer()

# p1.comer('Jõao')
# p1.falar('Jõao')
# p1.parar_comer()
# p1.falar('Jõao')
# p1.comer('Jõao')
# p1.parar_falar()
# p1.falar('Jõao')

p1.falar('POO')
p2.falar('Flimes')
p1.comer('churrasco')
print(p1.ano_atual)
print(Pessoa.ano_atual)
print(f'O ano de nascimento de {p1.nome} foi {p1.get_ano_nascimento()}')
