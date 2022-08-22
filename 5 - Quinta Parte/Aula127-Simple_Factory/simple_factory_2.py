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


class VeiculoFactory:
    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)

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

    def buscar_cliente(self):
        self.carro.buscar_cliente()


if __name__ == '__main__':
    Carros_disponiveis = ['luxo', 'popular', 'motopopular', 'motoluxo']

    for i in range(10):
        carro = VeiculoFactory(choice(Carros_disponiveis))
        carro.buscar_cliente()
