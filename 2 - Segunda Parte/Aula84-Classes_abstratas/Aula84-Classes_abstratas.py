"""
Aula 84 - Classes abstratas - Python Orientado a Objeto
"""
# from classes.conta import Conta
from classes.contaPoupanca import ContaPoupanca
from classes.contaCorrente import ContaCorrente

cp = ContaPoupanca(1111, 2222, 0)
cp.depositar(10)
cp.sacar(5)
cp.sacar(5)
cp.sacar(1)
# conta = Conta(111, 222, 0)
print('############################')
cc = ContaCorrente(agencia=1111, conta=3333, saldo=0, limite=500)
cc.depositar(100)
cc.sacar(250)
cc.sacar(500)
cc.depositar(1000)
cc.sacar(2000)
