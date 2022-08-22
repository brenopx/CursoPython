"""
Aula 106 - CSV - Comma Separated Values
Comma Separated Values - CVS (Valores separados por vírgula)
É um formato de dados muito usado em tabela (Excel, Google Sheets),
bases de dodos, clientes de e-mail, etc...
"""
import csv

with open('clientes.csv', 'r') as arquivo:
    # dados = csv.reader(arquivo)
    # dados = csv.DictReader(arquivo)
    # next(dados)

    # for dado in dados:
    #     print(dado['Nome'], dado['Sobrenome'], dado['E-mail'], dado['Telefone'])
    dados = [x for x in csv.DictReader(arquivo)]

# for dado in dados:
#     print(dado)

with open('cliente2.csv', 'w') as arquivo:
    escreve = csv.writer(
        arquivo,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )

    chaves = dados[0].keys()
    chaves = list(chaves)
    escreve.writerow(
        [
            chaves[0],
            chaves[1],
            chaves[2],
            chaves[3]
        ]
    )

    for dado in dados:
        # print(dado['Nome'])
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone']
            ]
        )



