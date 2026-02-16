preco_produtos = [100, 150, 300, 5500]
produtos = ['vinho', 'cafeiteira', 'microondas', 'iphone']

impostos = [preco * 0.2 for preco in preco_produtos]
print(impostos)