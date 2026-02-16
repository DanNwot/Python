for i in range (5):
    print(i)
    
produtos = ['arroz', 'feijao', 'macarrao', 'carne', 'frango']
producao = [100, 200, 150, 300, 250]

tamanho = len(produtos)

for i in range(tamanho):
    print(f'Produto: {produtos[i]} - Producao: {producao[i]} unidades')