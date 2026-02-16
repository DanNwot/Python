produtos = ['iphone', 'ipad', 'macbook', 'airpods', 'apple watch', 'imac', 'homepod', 'tv']
precos = [6999, 4999, 8999, 1499, 3999, 10999, 2999, 7999]
listajunta = zip(produtos, precos)
acrescimo = 1.1

for produto, preco in listajunta:
    preconovo = preco * acrescimo
    aumento = preconovo - preco
    print(f'O produto {produto} tinha o preço de R$ {preco},00 e agora custa R$ {preconovo:.0f},00, com um aumento de R$ {aumento:.0f},00')