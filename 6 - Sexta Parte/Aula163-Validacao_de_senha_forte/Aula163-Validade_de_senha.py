from random import randint, choice, shuffle
import re


senha_forte_regexp = re.compile(
    r'^'
    r'(?=.*[a-z])'
    r'(?=.*[A-Z])'
    r'(?=.*[0-9])'
    r'(?=.*[ -\/:-@[-`{-~])'
    r'.{12,}'
    r'$',
    flags=re.M
)


def zero_a_nove():
    return chr(randint(48, 57))


def a_a_z():
    return chr(randint(97, 122))


def A_a_Z():
    return chr(randint(65, 90))


def strange_chars():
    rand_range = [
        randint(32, 47),  # \u0020-\u002F [ -\/]
        randint(58, 64),  # \u003A-\u0040 [ :-@]
        randint(91, 96),  # \u005B-\u0060 [ [-']
        randint(123, 126),  # \u007B-\u007E [ [-~]
    ]

    # [\u0020-\u002F\u003A-\u0040\u005B-\u0060\u007B-\u007E]
    # [-\/ :-@  [-' [-~]

    return chr(choice(rand_range))


def create_pass(
    length=12,
    upper=True,
    lower=True,
    numbers=True,
    chars=True
):
    password = []

    for i in range(length):
        if numbers:
            password.append(zero_a_nove())
        if lower:
            password.append(a_a_z())
        if upper:
            password.append(A_a_Z())
        if chars:
            password.append(strange_chars())

    password = password[:length]
    shuffle(password)
    return ''.join(password)


if __name__ == "__main__":
    string = '''
VÁLIDAS
v2Ts7<o9T~}Y
j25TTbjJ:6{<
s`Mu6T;4M1!y
Li`hk6:3WX>3
d.D09}^dI2Vn
SEM MINÚSCULAS
I7^Y3RS^ 9]7
[P6W"83L5V{[
B7=;K8D6_}W5
1B_RT`93R%>1
EZU{7;2&D:64
SEM MINÚSCULAS E NÚMEROS
E}LV`C?X_G:{
AJH[@HD*V~=<
A~AC{_V~MG
W<-T}W:QAF'{
~YJ}|FILN>~)
SEM NÚMEROS CARACTERES E MINÚSCULAS
PBDZDPECUDNN
EJQWFWFFDEHY
XRCNLNRHYOZJ
TWIYPLWUDMNN
JMDTJSEPKVON
QUANTIDADE INVÁLIDA (6)
Iu4<1j
1x`P6g
@9t3Ry
qf9_6H
0o`9fO
'''

print(senha_forte_regexp.findall(string))
#     print('VALIDAS')
#     for i in range(5):
#         print(create_pass(
#             length=12,
#             chars=True,
#             upper=True,
#             lower=True,
#             numbers=True
#         ))
#     print()

#     print('SEM MINÚSCULAS')
#     for i in range(5):
#         print(create_pass(
#             length=12,
#             chars=True,
#             upper=True,
#             lower=False,
#             numbers=True
#         ))
#     print()

#     print('SEM MINÚSCULAS E NÚMEROS')
#     for i in range(5):
#         print(create_pass(
#             length=12,
#             chars=True,
#             upper=True,
#             lower=False,
#             numbers=False
#         ))
#     print()

#     print('SEM NUMEROS CARACTERES E MINÚSCULAS')
#     for i in range(5):
#         print(create_pass(
#             length=12,
#             chars=False,
#             upper=True,
#             lower=False,
#             numbers=False
#         ))
#     print()

#     print('QUANTIDADE INVÁLIDA (6)')
#     for i in range(5):
#         print(create_pass(
#             length=6
#         ))
#     print()
