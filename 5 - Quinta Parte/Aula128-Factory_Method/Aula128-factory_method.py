"""
Aula 128 - Factory Method
Factory method é um padrão de criação que permite definir uma interface para
criar objetos, mas deixa as subclasses decidirem quais objetos criar. O
Factory method permite adiar a instanciação para as subclasses, garantido o
baixo acoplamento entre classes.
"""
from abc import ABC, abstractmethod
from random import choice


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de Luxo está buscando o cliente ...')


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro Popular está buscando o cliente ...')


class MotoPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto Popular está buscando o cliente ...')


class MotoLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto de Luxo está buscando o cliente ...')


class VeiculoFactory(ABC):
    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)

    @staticmethod
    @abstractmethod
    def get_carro(tipo: str) -> Veiculo: pass

    def buscar_cliente(self):
        self.carro.buscar_cliente()


class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        if tipo == 'motopopular':
            return MotoPopular()
        if tipo == 'motoluxo':
            return MotoLuxo()
        assert 0, 'Veiculo não existe'


class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'popular':
            return CarroPopular()
        assert 0, 'Veiculo não existe'


if __name__ == '__main__':
    veiculos_disponiveis_zona_norte = ['luxo', 'popular', 'motopopular', 'motoluxo']
    veiculos_disponiveis_zona_sul = ['popular']

    print('ZONA NORTE')
    for i in range(10):
        carro = ZonaNorteVeiculoFactory(choice(
            veiculos_disponiveis_zona_norte))
        carro.buscar_cliente()

    print()

    print('ZONA SUL')
    for i in range(10):
        carro2 = ZonaSulVeiculoFactory(choice(veiculos_disponiveis_zona_sul))
        carro2.buscar_cliente()
