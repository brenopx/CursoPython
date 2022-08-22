"""
Aula 118 - Deque - Trabalhando com LIFO e FIFO
Pilhas e filas
Pilha (stack) - LiFO - last in, first out.
    Exemplo: Pilha de livros que são adicionados um sobre o outro
Fila (queue) - FIFO - first in, first out.
    Exemplo: Uma fila de banco (ou qualquer fila da vida real)
Filas podem ter efeitos colaterais em desempenho, porque a cada item alterado,
todos os índices serão modificados.
"""
from collections import deque
from time import sleep

# livros = list()
# livros.append('Livro 1')  # 1
# livros.append('Livro 2')  # 2
# livros.append('Livro 3')  # 3
# livros.append('Livro 4')  # 4
# livros.append('Livro 5')  # 5
# livro_removido = livros.pop()  # 5
# livro_removido = livros.pop()  # 4
# livro_removido = livros.pop()  # 3
# livro_removido = livros.pop()  # 2
# livro_removido = livros.pop()  # 1
#
# print(livros)
# print(livros, livro_removido)

# fila = deque()
# print(fila)
# fila.append('Joãozinho')
# fila.append('Maria')
# fila.append('Luiz Otávio')
# fila.append('Marcos')
# fila.append('José')
# print(f'Saiu: {fila.popleft()}')
# print(f'Saiu: {fila.popleft()}')
# print(f'Saiu: {fila.popleft()}')

# fila = deque(maxlen=5)
# fila.extend([1, 2, 3, 4])
# fila.append(5)
# fila.append(6)
# fila.append(7)
#
# print(fila)

fila = deque(maxlen=10)

# for i in range(1000):
#     fila.append(i)
#     sleep(1)
#     print(fila)

# fila.extend([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# fila.insert(2, 'Luiz Otávio')
fila.extend([10, 20, 30, 40, 50, 60, 70, 80])
# fila.reverse()
# print(fila.index(50, 0, 5))
fila.rotate(1)
print(fila)




