listaproduto = []
quantidade = []

while True:
    produto = input("Digite o nome do produto ou 'sair' para encerrar: ")
    if produto == "sair":
        break
    listaproduto.append(produto)
    
    qtd = int(input(f"Digite a quantidade de {produto}: "))
    quantidade.append(qtd)

listazipada = list(zip(listaproduto, quantidade))

print("A lista de produtos e quantidade foi de:")
for prod, qtd in listazipada:
    print(f"{prod}: {qtd}")
