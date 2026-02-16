vendas = [1000, 1500, 2000, 2500, 3000, 3500, 4000]
meta = 2750
qtdebateumeta= 0

for venda in vendas:
    if venda >= meta:
        qtdebateumeta += 1
        print(f'Venda de {venda} atingiu a meta!')
    else:
        print(f'Venda de {venda} nao atingiu a meta.')

qtdefuncionarios = len(vendas)
print(f'\n{qtdefuncionarios} funcionarios realizaram vendas hoje.')
print(f'{qtdebateumeta} vendas atingiram a meta.')
print(f'{(qtdebateumeta/qtdefuncionarios)*100:.2f}% das vendas atingiram a meta.')