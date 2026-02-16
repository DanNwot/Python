vendastecnologia = {'notebook': 2500, 'smartphone': 1500, 'tablet': 1200, 'smartwatch': 800, 'notebook gamer': 4500, 'notebook hp': 3000}
for item, preco in vendastecnologia.items():
    print(f'O preço do {item} é R$ {preco:.2f}')

totalnotebooks = 0
for item, preco in vendastecnologia.items():
    if 'notebook' in item:
        totalnotebooks += preco
print(f'O total de vendas de notebooks é R$ {totalnotebooks:.2f}')