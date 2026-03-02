class animal:
    def __init__(self, Especie, Classe):
        self.__Especie = Especie
        self.__Classe = Classe

    def fornecerclasse(self):
        return self.__Classe

    def informacoes(self):
        print(f'Especie: {self.__Especie}\n Classe: {self.__Classe}')
    
class perro(animal):
    def __init__(self, Especie, Classe, Raca):
        super().__init__(Especie, Classe)
        self.Raca = Raca

    def latir(self):
        print(f'AUAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUAUUUUUUUUUUUUUU')

    def informacoes(self):
        print(f'Classe: {self.fornecerclasse()}\n')
    
    def mostrarraca(self):
        print(f'A Raca é {self.Raca}')
    
class jacare(animal):
    def __init__(self, Especie, Classe, tipodecouro):
        super().__init__(Especie, Classe)
        self.tipodecouro = tipodecouro
    
    def informacoes(self):
        print(f'A Classe é {self.fornecerclasse()}\n O animal é Jacaré')

    def coletarcouro(self):
        print(f'O couro coletado foi {self.tipodecouro}\n')

cachorro1= perro('Cachorro', 'Mamifero', 'Pitbull')
cachorro1.informacoes()
cachorro1.latir()

jacare1= jacare('Jacaré', 'Réptil', 'Bolsa')
jacare1.informacoes()
jacare1.coletarcouro
