class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def Ligado(self):
        print('O carro ligou')

meu_carro= Carro('Ford', 'Mustang', 2023)

print(meu_carro.marca)
print(meu_carro.modelo)
print(meu_carro.ano)

meu_carro.Ligado()