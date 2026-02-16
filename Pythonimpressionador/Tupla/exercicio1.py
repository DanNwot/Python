vendas = [
    ('20/08', 'iphone x', 'azul', ' 128gb', 350, 4000),
    ('25/08', 'samsung s10', 'preto', ' 256gb', 250, 3200),
    ('30/08', 'xiaomi mi9', 'branco', ' 128gb', 150, 2200),
    ('05/09', 'motorola g8', 'cinza', ' 64gb', 100, 1800),
    ('10/09', 'asus zenfone 6', 'prata', ' 128gb', 50, 3000),
    ('15/09', 'lg g8', 'vermelho', ' 128gb', 80, 2800),
    ('20/09', 'iphone x', 'preto', ' 256gb', 200, 5000),
    ('20/09', 'samsung s10', 'branco', ' 128gb', 150, 3000),
    ('20/09', 'xiaomi mi9', 'azul', ' 64gb', 120, 2000),
]

#data, modelo, cor, armazenamento, quantidade, preco = vendas[0]
#faturamento = quantidade * preco
#print(faturamento)


for item in vendas:
    data, modelo, cor, armazenamento, quantidade, preco = item
    if modelo == 'iphone x':
        faturamento = quantidade * preco
        print(f'Faturamento do {modelo} na data {data}: R$ {faturamento}')
   
   
produtomaisvendido= ''
quantidademaisvenda= 0

for item in vendas:
    data, modelo, cor, armazenamento, quantidade, preco = item
    if data == '20/09':
        if quantidade > quantidademaisvenda:
            quantidademaisvenda = quantidade
            produtomaisvendido = modelo
print(f'O produto mais vendido na data 20/09 foi {produtomaisvendido} com {quantidademaisvenda} unidades vendidas.')