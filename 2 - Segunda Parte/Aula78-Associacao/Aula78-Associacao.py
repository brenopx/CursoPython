"""
Aula 78 - Associação - Python Orientada a Objeto
"""
from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Machado de Assis')
caneta = Caneta('BIC')
maquina = MaquinaDeEscrever()
# print(f'O nome do escritor é {escritor.nome}')
# print(f'O nome da marca de caneta é {caneta.marca}')
# caneta.escrever()
# maquina.escrever()
escritor.ferramenta = caneta
escritor.ferramenta.escrever()
escritor.ferramenta = maquina
escritor.ferramenta.escrever()

