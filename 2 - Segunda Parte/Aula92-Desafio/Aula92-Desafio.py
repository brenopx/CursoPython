"""
Aula 92 - Desafio POO
Exercicio com Abstração, Herança, Encapsulamento e Polimorfismo
criar um sistema bancario (extremamente simples) que tem clientes,
contas e um banco.
A idade é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente temum limite extra.
Banco tem clientes e contas
"""
from cliente import Cliente
from contaCorrente import ContaCorrente
from contaPoupanca import ContaPoupanca


ccorrente = ContaCorrente(111, 10, 50)
cpoupanca = ContaPoupanca(111, 10, 50)
c1 = Cliente('João', 30, ccorrente)
c2 = Cliente('Maria', 30, cpoupanca)

c1.lista_contas()
c2.lista_contas()
print()

cpoupanca.deposito(500)
ccorrente.deposito(500)

c1.lista_contas()
c2.lista_contas()
print()

# cpoupanca.sacar(551)
# ccorrente.sacar(651)
cpoupanca.sacar(5)
ccorrente.sacar(6)

c1.lista_contas()
c2.lista_contas()
