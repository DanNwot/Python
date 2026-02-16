produtos = ['iphone', 'samsung galaxy', 'xiaomi redmi', 'motorola moto g', 'asus zenfone', 'nokia lumia', 'lg k10', 'sony xperia']
vendas = [150, 200, 300, 100, 50, 80, 60, 40]
listazipada = zip(produtos, vendas)
dicionariovendas = dict(listazipada)
print(dicionariovendas)
for produto, quantidade in dicionariovendas.items():
    print(f'Vendemos {quantidade} unidades do produto {produto}')
    