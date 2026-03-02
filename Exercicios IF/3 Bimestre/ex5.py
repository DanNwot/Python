class empregado:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    def aumento(self):
            if self.salario >= 1500:
                salarioatual = self.salario + self.salario*0.30
                print(f'o aumento de salario de {self.nome} foi de {self.salario} para {salarioatual}')
                return
            else:
                print(f'desgraçado lavore')
desemprego = empregado("joao",1500)
desemprego.aumento()