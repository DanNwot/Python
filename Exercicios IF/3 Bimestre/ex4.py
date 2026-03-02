class equipe:
    def __init__(self):
        self.pessoas = []
    def addpessoas(self, nome, time):
        self.addpessoas.append({'nome': nome, 'time': time})
        print(f"jogador'{nome}'de time '{time}' adicionado com sucesso, digite para para parar de adicionar")
        def listarjogadoresontatos(self):
            for i in self:
                print(i)
        while self.addpessoas != 'para':
            print(equipe.addpessoas)
