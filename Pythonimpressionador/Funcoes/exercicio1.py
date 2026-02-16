lista = [300, 200, 100, 400, 500]
listaorganizada = lista.sort()
print(lista)

def cadastrarproduto():
    listaprodutos = []
    listaprecos = []
    
    demanda = int(input("Quantos produtos deseja cadastrar? "))
    for i in range(demanda):
        produto = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        produto = produto.casefold()
        
        listaprodutos.append(produto)
        listaprecos.append(preco)
        
    print("\nProdutos cadastrados:")
    for produto, preco in zip(listaprodutos, listaprecos):
        print(f"Produto: {produto} - Preço: R$ {preco:.2f}")

variavelcadastrar = cadastrarproduto()