class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        print(f'{self.nome} faz um som.')

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome) #chama o construtor da classe pai
        self.raca = raca
c1=Cachorro('rex', 'labrador')
c1.fazer_som()