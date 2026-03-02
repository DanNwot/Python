class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo = saldo_inicial #Atributo privado


    def ver_saldo(self):
        return f'Saldo atual: R$ {self.__saldo:.2f}' #Para editar um atributo usando return
    def m_saldo(self):
        return self.__saldo
    
    def depositar (self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('valor de deposito invalido')

    def sacar (self, valor):
        if valor < 0 <= self.saldo:
            self.saldo -= valor
        else:
            print('valor indisponivel.')

class contapoupanca(ContaBancaria):
    def __init__(self, titular, saldo_inicial, taxa_juros):
        super().__init__(titular, saldo_inicial)
        self.taxa_juros = taxa_juros
    def calcular_juros (self, taxa):
        juros = self.msaldo()*(taxa/100)
        self.depositar(juros)
        return self.msaldo


conta = ContaBancaria('Lucia', 1000)
conta1 =contapoupanca('Lucia', 1000, 10)
print(conta1.calcular_juros(10))
    