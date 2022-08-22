#import vendas.calc_preco
from vendas.calc_preco import aumento, reducao
#import vendas.formata.preco
import vendas.formata.preco as formata

preco = 49.90
# preco_com_aumento = vendas.calc_preco.aumento(49.9, 15)
preco_com_aumento = aumento(preco, 15, formata=True)
print(preco_com_aumento)

preco_com_reducao = reducao(preco, 15, formata=True)
print(preco_com_reducao)

# print(vendas.formata.preco.real(preco))
print(formata.real(preco))


