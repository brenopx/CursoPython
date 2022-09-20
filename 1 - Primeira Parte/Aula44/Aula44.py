""""
Aula 44 - Sistema de perguntas e respostas com dicionarios em Python
"""

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '2',
            'd': '0',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 2 - 2',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '2',
            'd': '0',
        },
        'resposta_certa': 'd',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 2 * 2',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '2',
            'd': '0',
        },
        'resposta_certa': 'b',
    },
}

respostas_certas = 0
for chave_pergunta, pergunta_valores in perguntas.items():
    print(f'{chave_pergunta}: {pergunta_valores["pergunta"]}')

    print('Respostas: ')
    for resposta_chave, resposta_valores in pergunta_valores['respostas'].items():
        print(f'[{resposta_chave}]: {resposta_valores}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pergunta_valores['resposta_certa']:
        print("Acertou!!!!!")
        respostas_certas += 1
    else:
        print('Errrrrrou!!!!')
    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100
print(f"Voce acertou {respostas_certas}, isso e {porcentagem_acerto} das perguntas")
