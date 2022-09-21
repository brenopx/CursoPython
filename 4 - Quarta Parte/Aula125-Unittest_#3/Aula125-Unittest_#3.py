"""
Aula 125 - Unittest #3

class Pessoa:
    def__init__(self):
        nome str
        sobrenome str
        dados_obtidos bool = False

    API:
        obter_todos_os_dados -> method
            OK
            404

            (dados_obtidos se torna True se dados obtidos com sucesso)

"""
import requests


class Pessoa:
    def __init__(self, nome, sobrenome, dados_obtidos=False):
        self.nome = nome
        self.sobrenome = sobrenome
        self.dados_obtidos = False

    def obter_todos_os_dados(self):
        resposta = requests.get('https://jsonplaceholder.typicode.com/users/1')

        if resposta.ok:
            self.dados_obtidos = True
            return 'CONECTADO'
        else:
            self.dados_obtidos = False
            return 'ERRO 404'
