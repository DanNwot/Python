produtos = ['iphone', 'ipad', 'macbook', 'airpods', 'apple watch', 'imac', 'homepod', 'tv']
precos = [6999, 4999, 8999, 1499, 3999, 10999, 2999, 7999]

for preco in precos:
    print(f'O preço do produto é R$ {preco * 1.1},00')

for i in range (len(produtos)):
    novo_preco = precos[i] * 1.1
    print(f'O produto {produtos[i]} tinha o preço de R$ {precos[i]},00 e agora custa R$ {novo_preco:.0f},00')
    
for i, preco in enumerate (precos):
    novo_preco = preco * 1.1
    print(f'O produto {produtos[i]} tinha o preço de R$ {preco},00 e agora custa R$ {novo_preco:.0f},00')