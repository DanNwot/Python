lista = ['maçã', 'banana', 'laranja', 'uva']
vendas = [150, 200, 100, 250]
tamanho = len(lista)
print(f"A lista contém {tamanho} elementos.")
maior = max(vendas)
menor = min(vendas)
print(f'O maior numero de vendas da lista é {maior} e o menor é {menor}.')

i = vendas.index(maior)
ii = vendas.index(menor)
produto_mais_vendido = lista[i]
produto_menos_vendido = lista[ii]
print(f'O produto mais vendido foi {produto_mais_vendido} com {maior} vendas e o menos vendido foi {produto_menos_vendido} com {menor} vendas.')