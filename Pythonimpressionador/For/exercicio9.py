vendas = [100, 200, 300, 400, 500]
meta = 299
for venda in vendas:
    if venda < meta:
        print('a loja nao ganha bonus')
        break
    print(venda)

vendedores = ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo']
meta = 130
for venda in vendas:
    if venda < meta:
        continue
    print(venda)
        
    
