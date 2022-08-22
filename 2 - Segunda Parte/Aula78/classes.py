class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta

class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('Caneta está escrevendo ...')

class MaquinaDeEscrever:
    def escrever(self):
        print('Maquina de escrever está escrevendo ...')
    # def __init__(self, tipo):
    #     self.__tipo = tipo
    #
    # @property
    # def tipo(self):
    #     return self.__tipo
