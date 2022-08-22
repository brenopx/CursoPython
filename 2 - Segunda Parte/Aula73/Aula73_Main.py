"""
Aula 73 - Métodos de classes - Python Orientada a Objeto
"""
from pessoa import Pessoa
# p1 = Pessoa('Luiz', 32)
# p1.get_ano_nascimento()
# print(Pessoa.ano_atual)
# p2 = Pessoa('Jõao', 25)
# print(p1.idade)
# p1.get_ano_nascimento()
p1 = Pessoa.por_ano_nascimento('Luiz', 1987)
print(p1.idade)
p1.get_ano_nascimento()
print(Pessoa.gera_id())
print(p1.gera_id())
