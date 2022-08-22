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

class MinhaClasse:
    """Documentação normal

    Conforme qualquer outra documentação que voce tenha usado anteriormente.
    """
    atributo = 1
    atributo2 = 'valor'

    def __init__(self, texto):
        """Inicializa os dados

        :param texto: o texto da classe
        :type texto: str
        """
        self.texto = texto
        self.exibe_texto(texto)

    @staticmethod
    def exibe_texto(texto):
        """Método que exibe um texto de 100 caracteres na tela

        :param texto: Um texto de 100 caracteres
        :type texto: str

        :return: O texto de 100 caracteres
        :rtype: str

        :raises ValueError: Se o texto tiver mais que 100 caracteres
        :raises TypeError: se o texto não for uma string
        """
        if not isinstance(texto, str):
            raise TypeError('texto precisa ser uma string.')
        if len(texto) > 100:
            raise ValueError('texto precisa ter 100 caracteres ou menos')

        return texto
