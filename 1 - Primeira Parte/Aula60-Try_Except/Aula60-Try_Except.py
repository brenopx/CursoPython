"""
Aula 60 - Try, Except - Tratando Exceções em python
"""
try:
    a = 0
    try:
        a = 1 / 0
    except:
        print('Erro')
except NameError as erro:
    print('Erro do desenvolvedor, fale com ele.', erro)
except (IndexError, KeyError) as erro:
    print('Erro de índice ou chave.')
except Exception as erro:
    print('Ocorreu um erro inesperado.')
else:
    pass
    # print('Seu código foi executado com sucesso')
finally:
    pass
    # print('Finalmente.')
    a = None
print(a)
print('Bora continuar.....')
