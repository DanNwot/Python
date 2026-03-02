class usuario:
    def __init__(self, nome, genero, datanascimento, cpf):
        self.nome= nome
        self.genero= genero
        self.datanascimento= datanascimento
        self.cpf = cpf

class aluno(usuario):
    def __init__ (self, nome, genero, datanascimento, cpf):
        super().__init__(self, nome, genero, datanascimento, cpf):
        self.notas = notas
        self.serie = serie
        self.turma = turma
        self.ra = ra
    