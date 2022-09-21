"""Descrição Rápida e simples - About this Programming in Python Online Course on edX

This course starts from the beginning, covering the basics of how a computer interprets lines of code;
how to write programs, evaluate their output, and revise the code itself;
how to work with variables and their changing values; and how to use mathematical,
boolean, and relational operators.

By the end of this course, you'll be able to write small programs in Python that use variables,
mathematical operators, and logical operators.
For example, you could write programs that carry out complex mathematical operations,
like calculating the interest rate necessary to reach a savings goal, recommending apparel options
based on weather patterns, or calculating a grade based on multiple percentages.

Structurally, the course is comprised of several parts. Instruction is delivered via a series of
short (2-3 minute) videos. In between those videos, you'll complete both multiple choice questions
and coding problems to demonstrate your knowledge of the material that was just covered.
"""

variavel_1 = 'valor 1'

def soma(x, y):
    """Soma x e y"""
    return x + y

def multiplica(x, y, z=None):
    """Multiplica x, y, z

    Multiplica x, y e z. O programador por omitir a variavel z caso não tenha
    necessidade de usá-la.
    """
    if z:
        return x * y
    else:
        return x * y *z


variavel_2 = 'Valor 2'
variavel_3 = 'Valor 3'
variavel_4 = 'Valor 4'
