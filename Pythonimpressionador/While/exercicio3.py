#listavendas = []
#   vendas= [
#        ['maca', 5],
#       ['banana', 8],
#        ['laranja', 12],
#       ['uva', 3],
#        ['pera', 7]
#   ]

vendas = []
while True:
    produto = input("Digite o nome do produto que deseja verificar as vendas\nDigite sair para parar: ")
    if produto == "sair":
        break
    qtde = int(input("Digite a quantidade vendida: "))
    vendas.append([produto, qtde])
print (vendas)