class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            return
        print(f'{self._nome} está LIGADO')
        self._ligado = True

    def desligar(self):
        if not self._ligado:
            return
        print(f'{self._nome} está DESLIGADO')
        self._ligado = False
