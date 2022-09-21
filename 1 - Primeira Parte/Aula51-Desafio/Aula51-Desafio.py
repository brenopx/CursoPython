"""
Aula51 - Desafio
carrinho = [] -> calcular a soma do valor dos produtos
"""
carrinho = []
carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 50))
carrinho.append(('Produto 4', 30))
carrinho.append(('Produto 5', 20))
carrinho.append(('Produto 6', 50))

produto, preco = carrinho[0]
print(produto, preco)

total = [(x, y) for x, y in carrinho]
print(total)
total = sum([float(y) for x, y in carrinho])
print(total)
