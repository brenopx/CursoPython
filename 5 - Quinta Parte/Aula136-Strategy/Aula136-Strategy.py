"""
Aula 136 - Strategy
strategy é um padrão de projeto comportamental que tem
a intenção de definir uma família de algoritmos,
encapsular cada uma delas e torná-las intercambiáveis.
Strategy permite que o algoritimo varie independentemente
dos clientes que o utilizam.

Principio do aberto/fechado (Open/closed principle)
Entidades devem ser abertas para extansão, mas fachadas para modificação
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Order:
    def __init__(self, total: float, discount: Discountstrategy):
        self._total = total
        self._discount = discount

    @property
    def total(self):
        return self._total

    @property
    def total_with_discount(self):
        return self._discount.calculate(self.total)


class Discountstrategy(ABC):
    @abstractmethod
    def calculate(self, value: float) -> float: pass


class TwentyPercent(Discountstrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.2)


class FiftyPercent(Discountstrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.5)


class NoDiscount(Discountstrategy):
    def calculate(self, value: float) -> float:
        return value


class CustomDiscount(Discountstrategy):
    def __init__(self, discount):
        self.discount = discount / 100

    def calculate(self, value: float) -> float:
        return value - (value * self.discount)


if __name__ == "__main__":
    twenty_percent = TwentyPercent()
    fifty_percent = FiftyPercent()
    no_discount = NoDiscount()
    five_percent = CustomDiscount(5)

    order = Order(1000, twenty_percent)
    print(order.total, order.total_with_discount)

    order = Order(1000, fifty_percent)
    print(order.total, order.total_with_discount)

    order = Order(1000, no_discount)
    print(order.total, order.total_with_discount)

    order = Order(1000, five_percent)
    print(order.total, order.total_with_discount)

    order = Order(1000, CustomDiscount(13))
    print(order.total, order.total_with_discount)
