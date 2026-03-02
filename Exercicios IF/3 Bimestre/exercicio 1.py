class Pessoa:
    def __init__(self, nome, idade):
        self.nome= nome
        self.idade= idade

daniel= Pessoa('Daniel', 18)

print(daniel.nome)
print(daniel.idade)