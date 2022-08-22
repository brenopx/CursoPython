"""
Aula 142 - Iterator
Iterator e um padrão comportamental que tem a
intenção de fornecer um meio de acessar,
sequencialmente, os elementos de um objeto
agregado sem expor sua representação subjacente.

 -Uma coleção deve fornecer um meio de acessar
    seus elementos sem expor sua estrutura interna
 -Uma coleção pode ter maneiras e percursos diferentes
    para expor seus elementos
 -Você deve separar a complexidade dos algoritmos
    de iteração da coleção em si

A ideia principal do padrão é retirar a responsabilidade
de acesso e percuso de uma coleção, delegando tais
tarefas para um objeto iterador.
"""
from collections.abc import Iterator, Iterable
from typing import List, Any


class MyIterator(Iterator):
    def __init__(self, collection: List[Any]) -> None:
        self._collection = collection
        self._index = 0

    def next(self):
        try:
            return self.__next__()
        except IndexError:
            raise StopIteration

    def __next__(self) -> None:
        try:
            item = self._collection[self._index]
            self._index += 1
            return item
        except IndexError:
            raise StopIteration


class ReverseIterator(Iterator):
    def __init__(self, collection: List[Any]) -> None:
        self._collection = collection
        self._index = -1

    def next(self):
        try:
            return self.__next__()
        except IndexError:
            raise StopIteration

    def __next__(self) -> None:
        try:
            item = self._collection[self._index]
            self._index -= 1
            return item
        except IndexError:
            raise StopIteration


class MyList(Iterable):
    def __init__(self) -> None:
        self._items: List[Any] = []
        self._my_iterator = MyIterator(self._items)

    def add(self, value: Any) -> None:
        self._items.append(value)

    def __iter__(self) -> Iterator:
        return self._my_iterator

    def reverse_iterator(self) -> Iterator:
        return ReverseIterator(self._items)

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self._items})'


if __name__ == "__main__":
    mylist = MyList()
    mylist.add('Luiz')
    mylist.add('Maria')
    mylist.add('Joao')

    # print(mylist)

    print('ROUBEI UM VALOR:', next(iter(mylist)))
    # print('ROUBEI UM VALOR:', next(mylist.__iter__()))
    # print('ROUBEI UM VALOR:', mylist.__iter__().next())

    # iterator = mylist.__iter__()
    # print('Roubei um valor:', iterator.next())

    for value in mylist:
        print(value)

    for value in mylist:
        print(value)

    print()

    for value in mylist.reverse_iterator():
        print(value)
