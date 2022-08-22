from abc import ABC, abstractmethod


class Pizza(ABC):
    """ Classe abstrata """

    def prepare(self) -> None:
        """ Template method """
        self.hook_before_add_ingredients()  # Hook
        self.add_ingrentients()  # Abstract
        self.hook_after_add_ingredients()    # Hook
        self.cook()              # Abstract
        self.cut()               # Concreto
        self.serve()             # Concreto

    def hook_before_add_ingredients(self) -> None:
        pass

    def hook_after_add_ingredients(self) -> None:
        pass

    def cut(self) -> None:
        print(f'{self.__class__.__name__} - Cortando Pizza')

    def serve(self) -> None:
        print(f'{self.__class__.__name__} - Servindo Pizza')

    @abstractmethod
    def add_ingrentients(self) -> None: pass

    @abstractmethod
    def cook(self) -> None: pass


class AModa(Pizza):
    def add_ingrentients(self) -> None:
        print(f'{self.__class__.__name__} - adicionando ingredientes: molho,'
              f' presunto, queijo, tomate, azeitona e cebola')

    def cook(self) -> None:
        print(f'{self.__class__.__name__} - cozinhado por 45min')


class Veg(Pizza):
    def hook_before_add_ingredients(self) -> None:
        print(f'{self.__class__.__name__} - Lavando ingredientes')

    def add_ingrentients(self) -> None:
        print(f'{self.__class__.__name__} - adicionando ingredientes: molho,'
              f'  tomate, palmito e manjericão')

    def cook(self) -> None:
        print(f'{self.__class__.__name__} - cozinhado por 30min')


if __name__ == "__main__":
    a_moda = AModa()
    a_moda.prepare()
    veg = Veg()
    veg.prepare()
