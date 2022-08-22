"""
Aula64 - Criar Módulos em Python
"""
from Calculos import multiplica, dobra_lista, PI
from outro import fala_oi
import outro
import Calculos
print(Calculos.PI)

lista = [2, 4]
print(Calculos.multiplica(lista))
print(multiplica(lista))
fala_oi()
print(PI)
print(dobra_lista(lista))

