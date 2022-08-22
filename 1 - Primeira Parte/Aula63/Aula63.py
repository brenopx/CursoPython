"""
Aula63 - Módulo padrão em Python
Módulo padrão do Python:
Módulo são arquivo .py (que contém código python) e servem para expandir
as funcionalidades padrão do Python em:
https://docs.python.org/3/py-modindex.html
"""
from sys import platform as so
from random import randint as randint_original

def randint(*args):
    return 'HaHaHa'

for i in range(5):
    print(randint_original(0, 10))
    print(randint(0, 10))

print(so)
