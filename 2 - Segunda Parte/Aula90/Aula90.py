"""
Aula 90 - Metaclasse
EM PYTHON TUDO É UM OBJETO: incluindo classes
Metaclasses são as "classes" que criam classes.
type é uma metaclasses (!!!????)
"""
class Meta(type):
    def __new__(mcs, name, bases, namespace):
        # print(name)
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        # print(namespace)
        # if 'b_fala' not in namespace:
        #     print(f'Oi, voce precisa criar o metodo b_fala em {name}')
        # else:
        #     if not callable(namespace['b_fala']):
        #         print(f'b_fala precisa ser um metodo, não atributo em {name}')

        if 'attr_classe' in namespace:
            print(f'{name} tentou sobrescrever o atributo.')
            del namespace['attr_classe']

        return type.__new__(mcs, name, bases, namespace)


# class A(metaclass=Meta):
#     def falar(self):
#         self.b_fala()
#
#
# class B(A):
#     teste = 'Valor'
#     b_fala = 'wow'
#
#     def b_fala(self):
#         print('oi')
#
#     def sei_la(self):
#         pass

class A(metaclass=Meta):
    attr_classe = 'Valor A'


class B(A):
    attr_classe = 'Valor B'


class C(B):
    attr_classe = 'Valor C'


# b = B()
# print(b.attr_classe)
c = C()
print(c.attr_classe)


class Pai:
    nome = 'Teste'


D = type(
    'D',
    (Pai,),
    {
        'attr': 'Ola Mundo !'
    }
)

d = D()
print(d.attr)
print(d.nome)
print(type(d))
