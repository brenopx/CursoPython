"""
Aula 127 - Simple Factory
Na programação POo, o termo factory (fábrica) refere-se a um classe ou método
que é responsável por criar objetos.
Vantagens:
    Permitem criar um sistema com baixo acoplamento entre classes porque
    ocultam as classes que criam os objetos do código cliente.

    Facilitam a adição de novas classes ao código, porque o cliente não
    conhece e nem utiliza a implementação da classe (utiliza a factory).

    Podem facilitar o processo de "cache" ou criação de 'singletons" porque a
    fábrica pode retorna um objeto já criado para o cliente, ao invés de criar
    novos objetos sempre que o cliente precisar.

Desvantagens:
    Podem introduzir muitas classses no código

vaamos ver 2 tipos de Factory da Gof: Factory method e Abstract Factory

Nessa aula:
Simple Factory <- Uma espécie de Factory Method parametrizado
Simple Factory pode não ser considerado um padrão de projeto po si só
Simple Factory pode quebrar princípios de SOLID
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


class VeiculoFactory:
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


if __name__ == '__main__':
    Carros_disponiveis = ['luxo', 'popular', 'motopopular', 'motoluxo']

    for i in range(10):
        carro = VeiculoFactory.get_carro(choice(Carros_disponiveis))
        carro.buscar_cliente()
