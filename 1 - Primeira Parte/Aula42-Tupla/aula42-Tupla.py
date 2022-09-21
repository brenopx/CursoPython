""""
Aula 42 - Tupla em Python
"""
t1 = (1, 2, 3, 'a', 'Luiz')
print(type(t1))
print(t1)

for v in t1:
    print(v)

print(t1[2:])

t2 = 2,
t3 = 6, 63, 52, 2
t4 = (t2 + t3) * 20
print(t4)

t1 = (1, 2, 3, 4, 5)
t1 = list(t1)
t1[1] = 3
t1 = tuple(t1)

print(t1)
