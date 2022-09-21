from eletronico import Eletronico
from log import LogMixin


class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        # Eletronico.__init__(self.nome)
        self._conectado = False

    def conetar(self):
        if not self._ligado:
            error = f'{self._nome} não esta LIGADO.'
            print(error)
            self.log_infro(error)
            return
        if self._conectado:
            error = f'{self._nome} já está CONECTADO.'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} está CONECTADO.'
        print(info)
        self.log_infro(info)
        self._conectado = True

    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} não está CONECTADO.'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} foi DESLIGADO com sucesso.'
        self.log_infro(info)
        self._conectado = False


