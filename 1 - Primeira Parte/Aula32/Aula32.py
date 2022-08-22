"""
Aula 32 - Desafio do contador
for / while
0 10
1 09
2 08
3 07
4 06
5 05
6 04
7 03
8 02
"""

var1 = 0
var2 = 10

while var1 < 10 and var2 > 0:
    print(var1, var2)
    var1 += 1
    var2 -= 1

print()
#Solução do professor

for p, r in enumerate(range(10, 1, -1)):
    print(p, r)

