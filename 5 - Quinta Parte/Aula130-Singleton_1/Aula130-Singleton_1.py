"""
Aula 130 - Singleton #1
O Sigleton tem a intenção de garantir que uma classe tenha somente
uma instância e fornece um ponto global de acesso para a mesma.

when discussing which patterns to drop, we found
that we still love them all.
(Not really-I'm in favor of dropping Singleton.
Its use is almosts always a design smell.)
- Erich Gamma, em entrevista para informIT
http://www.informit.com/articles/article.aspx?p=1404456
"""


class AppSettings:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.tema = 'O Tema Escuro'
        self.font = '18px'


if __name__ == "__main__":
    as1 = AppSettings()
    as1.tema = 'O Tema Claro'
    print(as1.tema)
    as2 = AppSettings()
    print(as1.tema)
    as3 = AppSettings()

    # as1.nome = 'Luiz'
    # print(as3.nome)

    # as1.tema = 'Tema Escuro'
    # print(as3.tema)
