"""
Aula 126 - Type hints e MyPy
https://docs.python.org/3/library/typing.html
"""
from email import iterators
from typing import List, Union, Tuple, Dict, Any, NewType, Callable, Sequence, Iterable

# Primitivos
numero: int = 10
flutuante: float = 10.5
booleano: bool = False
string: str = 'Luiz Otávio'
string: str = '1'

# Sequencias
lista: List[int] = [1, 2, 3]
lista_str_int: List[Union[int, str]] = [1, 2, 3, 'Luiz']
tupla: Tuple[int, int, int, str] = (1, 2, 3, 'Luiz')

# Dicionário e Conjuntos
pessoa: Dict[str, Union[str, int]] = {'nome': 'Luiz Otávio', 'sobrenome': 'Miranda', 'idade': 30}
pessoa2: Dict[str, Any] = {'nome': 'Luiz Otávio', 'sobrenome': 'Miranda', 'idade': 30}

# Meu tipo
MeuDict = Dict[str, Union[str, int, List[int]]]  # Alias
pessoa3: MeuDict = {'nome': 'Luiz Otávio', 'sobrenome': 'Miranda', 'l': [1, 2]}

# Meu outro tipo
UserId = NewType('UserId', str)
user_id = UserId(325456789)


def retorna_funcao(funcao: Callable[[], None]) -> Callable:
    return funcao


def fala_oi():
    print('oi')


def soma(x: int, y: int) -> int:
    return print(f'{x + y}')


retorna_funcao(fala_oi())
retorna_funcao(soma(1, 2))


class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int) -> None:
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.idade: int = idade

    def fala(self) -> None:
        print(f'{self.nome} {self.sobrenome} está falando ....')


def iterar(sequencia: Sequence[int]):
    return [x * 2 for x in sequencia]


def iterar2(sequencia: Iterable[int]):
    return [x * 2 for x in sequencia]


print(iterar([1, 2, 3]))
print(iterar((1, 2, 3)))
print(iterar2([1, 2, 3]))
print(iterar2((1, 2, 3)))
