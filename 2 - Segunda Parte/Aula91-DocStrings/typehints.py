""" Documentação deste modulo

Ele não faz nada, mas é só um exemplo pra voce.
Typing - https://decs.python.org/3/library/typing.html
"""
from typing import Union

x: int = 10
y: float = 10.5
z: bool = False


def funcao(p1: float, p2: str, p3: dict) -> float:
    return 10.10


# def funcao() -> list, dict:
def funcao() -> Union[list, dict]:
    pass
