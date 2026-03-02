class Livro:
    def __init__(self, Nome, Autor, Ano):
        self.Nome= Nome
        self.Autor= Autor
        self.Ano= Ano
    def mostrar(self):
        print(f'{self.Nome}, {self.Autor}, {self.Ano}')

LaranjaMecanica= Livro ('LaranjaMecanica', 'Stanley Kubrick', 1998)

LaranjaMecanica.mostrar()