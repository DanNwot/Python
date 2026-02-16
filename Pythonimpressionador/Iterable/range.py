# Exemplos de Range em Python
# range (início, fim, passo)
# range (fim)
# range (início, fim)
produtos = ['Arroz', 'Feijão', 'Carne', 'Macarrão', 'Batata']
estoque = [20, 15, 30, 10, 25]

# Exemplo 1: Usando range para iterar sobre índices
for produto in range(len(produtos)):
    print(f'Produto: {produtos[produto]} - Estoque: {estoque[produto]} unidades')

# Exemplo 2: Usando range com início, fim
for i in range (1,5):
    print(f'Número: {i}')
    
# Exemplo 3: Usando range com início, fim e passo
for i in range (0,1000,10):
    print(i)