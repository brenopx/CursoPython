"""
Aula 56 - Groupby - Agrupando valores
"""
from itertools import groupby

alunos = [
    {
        'nome': 'Luiz', 'nota': 'A'
    },
    {
        'nome': 'Leticia', 'nota': 'B'
    },
    {
        'nome': 'Fabricio', 'nota': 'C'
    },
    {
        'nome': 'Rosemary', 'nota': 'B'
    },
    {
        'nome': 'Joana', 'nota': 'A'
    },
    {
        'nome': 'João', 'nota': 'D'
    },
    {
        'nome': 'Eduardo', 'nota': 'D'
    },
    {
        'nome': 'Andre', 'nota': 'D'
    },
    {
        'nome': 'Anderson', 'nota': 'C'
    },
    {
        'nome': 'Jose', 'nota': 'B'
    },
]
print(alunos)
ordena = lambda item: item['nota']
alunos.sort(key=ordena)  # ordanar os alunos com base em suas notas
# print(alunos)
# for aluno in alunos:
#    print(aluno)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    print(f'Agrupamento: {agrupamento}')
    for aluno in valores_agrupados:
        print(aluno)
        for nome in aluno:
            print('nome' in aluno.va)
