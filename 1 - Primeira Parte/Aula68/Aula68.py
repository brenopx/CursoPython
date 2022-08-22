"""
Funções decoradoras e decoradores
"""
# def fala_oi():
#     print('OI')
#
# variavel = fala_oi
# variavel()
# fala_oi()
# print(type(variavel))

# def master(funcao):
#     def slave(*args, **kwargs):
#         print("Agora estou decorada!!!!")
#         funcao(*args, **kwargs)
#     return slave
#
# @master
# def fala_oi():
#     print('OI')
#
# @master
# def outra_funcao(mgs):
#     print(mgs)
#
# # fala_oi = master(fala_oi)
# # fala_oi()
# outra_funcao('Olá, eu sou o Breno!!!')
#
# print(type(fala_oi))
from time import time
from time import sleep

def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time)
        print(f'A função {funcao.__name__} levou {tempo:.2f} segundos para executar.')
        return resultado
    return interna

@velocidade
def demora():
    for i in range(5):
        print(i)
        sleep(1)

demora()
