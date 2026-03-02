class Aluno:
    def __init__ (self, Nota, Nome):
        self.Nome= Nome
        self.Notas= []
    def addnotas(self, Nota):
        self.notas.append(Nota)
    def media(self):
        media = self.Notas / len(self.Notas)