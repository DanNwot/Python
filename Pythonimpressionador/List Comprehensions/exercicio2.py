preco_produtos = [100, 150, 300, 5500]
produtos = ['vinho', 'cafeiteira', 'microondas', 'iphone']

listazipada= list(zip(produtos, preco_produtos))
listazipada.sort(reverse=True)

produtos = [produtos for vendas, produtos in listazipada]
print(produtos)
