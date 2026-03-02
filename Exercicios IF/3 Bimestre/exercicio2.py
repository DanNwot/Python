class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular= titular
        self.saldo= saldo
    
    def depositar(self, valor):
        self.saldo += valor
        return self.saldo
    
    def sacar(self,valor):
        if self.saldo >= valor:
           self.saldo -= valor
        else:
            print('Voce nao possui esta quantia')
    def mostrar_saldo(self):
        return self.saldo

minhaconta= ContaBancaria('Daniel', 4444)

valores= int(input('digite a quantia que deseja depositar: \n'))
print (minhaconta.depositar(valores))