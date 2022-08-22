"""
Aula 131 - Singleton #2
"""


def singleton(the_class):
    instances = {}

    def get_class(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)
        return instances[the_class]

    return get_class


@singleton
class AppSettings:
    def __init__(self):
        self.tema = 'O Tema Escuro'
        self.font = '18px'


@singleton
class Teste:
    def __init__(self):
        print('OI')


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

    t1 = Teste()
    t2 = Teste()
    print(t1 == t2)
