class ContaBancaria:
    def __init__(self, titular, saldo, numero):
        self.titular = titular
        self.saldo = saldo
        self.numero = numero

    def depositar(self):
        self.deposito = int(input('Insira o valor a ser depositado:'))

    def sacar(self):
        self.saque = int(input('Insira o valor a ser retirado:'))

    def exibir(self):
        print(self.saldo + self.deposito - self.saque)


Abjamalo = ContaBancaria('?', 2000, '?')

Abjamalo.depositar()
Abjamalo.sacar()
Abjamalo.exibir()