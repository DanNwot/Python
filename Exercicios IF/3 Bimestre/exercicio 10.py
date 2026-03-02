class Agenda:
    def __init__(self):
        self.contatos = []
    def addContato(self,nome,Telefone):
        self.contatos.append({'nome' : nome , 'Telefone': Telefone})
        print(f"contato'{nome}'de numero '{Telefone}' adicionado com sucesso")
    def removerContato(self,nome):
        for contato in self.contatos:
            if contato[0] == "nome":
                self.contatos.remove(contato)
                print(f"o contato {nome} foi excluido com sucesso")
                return
            else:
                print(f"O contato {nome} nao encontrado")
        def listarContatos(self):
            for i in self.contatos:
                print(i)



Agenda1 = Agenda()
Agenda1.addContato("joao","359904")
Agenda1.addContato("jl","359874")
Agenda1.addContato("jm","359174")
Agenda1.addContato("jg","357974")
Agenda1.addContato("jj","379974")
print(Agenda1.listarContatos())