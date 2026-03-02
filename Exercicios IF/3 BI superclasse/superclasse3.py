from datetime import datetime

# Classe base
class ContaBancaria:
    def __init__(self, titular, cpf, saldo, numero, agencia):
        self.titular = titular
        self.cpf = cpf
        self.saldo = saldo
        self.numero = numero
        self.agencia = agencia

    def sacar(self):
        x = float(input('Quanto deseja sacar:\n'))
        self.saldo -= x

    def depositar(self):
        x = float(input('Quanto deseja depositar:\n'))
        self.saldo += x

# Conta Poupança
class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, cpf, saldo, numero, agencia, rendimento_mensal):
        super().__init__(titular, cpf, saldo, numero, agencia)
        self.rendimento_mensal = rendimento_mensal
        self.taxa_manutencao = 20
        self.data_menu = 20
        self.v_fatura = 1500
        self.data_fatura = 15
        self.taxa_de_rendimento = 0.05

    def investimento(self):
        x = float(input('Quanto deseja investir:\n'))
        self.saldo = self.saldo - x + (x * self.taxa_de_rendimento)

    def sacar(self):
        x = float(input('Quanto deseja sacar:\n'))
        self.saldo -= x

    def depositar(self):
        x = float(input('Quanto deseja depositar:\n'))
        self.saldo += x

    def aplicar_juros(self):
        self.saldo -= self.saldo * 0.15

    def cobrar_fatura(self):
        if datetime.now().day == self.data_fatura:
            self.saldo -= self.v_fatura

# Conta Corrente
class ContaCorrente(ContaBancaria):
    def __init__(self, titular, cpf, saldo, numero, agencia, limite_de_credito, taxa_de_manutencao, limite_cheque):
        super().__init__(titular, cpf, saldo, numero, agencia)
        self.limite_cheque = limite_cheque
        self.taxa_de_manutencao = taxa_de_manutencao
        self.limite_de_credito = limite_de_credito

    def sacar(self):
        x = float(input('Quanto deseja sacar:\n'))
        self.saldo -= x

    def depositar(self):
        x = float(input('Quanto deseja depositar:\n'))
        self.saldo += x

    def aplicar_taxa_manutencao(self):
        self.saldo -= self.saldo * 0.05

    def verificar_limite_credito(self):
        if self.saldo > self.limite_de_credito:
            print('Você está excedendo o limite do seu crédito.')

# Instâncias
p1 = ContaCorrente('Daniel', 15999999, 2400, 2, 'Bradesco', 5000, 50, 50)
p2 = ContaPoupanca('Daniel', 15892929, 33, 1, 'Banco do Brasil', 0.02)
