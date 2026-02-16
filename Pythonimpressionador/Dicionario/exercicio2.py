vendastecnologia = {'notebook': 2500, 'smartphone': 1500, 'tablet': 1200, 'smartwatch': 800, 'notebook gamer': 4500, 'notebook hp': 3000}

itens_dicionario = vendastecnologia.items()
for item, preco in itens_dicionario:
    print(f'O preço do {item} é R$ {preco:.2f}')
    if preco > 2000:
        print(f'O {item} custa mais de R$ 2000!')
    else:
        pass