loja = [1, 2, 3, 4, 5]
produto = ["camisa", "calça", "tênis", "boné", "meia"]
print ('a loja {} vende o produto {}'.format (loja[0], produto[0]))

texto = 'oieusou@gmail.com'
textonovo = texto.replace('@', 'arroba')
print(textonovo)

produtos = ['camisa', 'calça', 'tenis', 'bone', 'meia', 'jaqueta', 'vestido', 'saia']
quantidade = [10, 15, 5, 8, 20, 7, 12, 9]
i = produtos.index('jaqueta')
qtdeestoque = quantidade[i]

print('o produto {} '. format(produtos[i]))
print('na posicao {}'. format(i))

print('possui {} de quantidade de estoque'. format (qtdeestoque))

produto = input('digite o nome do produto que deseja consultar: ')
if produto in produtos:
    i = produtos.index(produto)
    qtdeestoque = quantidade[produtos.index(produto)]
    print(f"O produto {produto} possui {qtdeestoque} unidades em estoque")
else:
    print('produto nao encontrado no estoque.')