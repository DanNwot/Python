funcionarios = ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo', 'Fernanda', 'Gabriel', 'Helena']
cadafunc = 0
for funcionario in funcionarios:
    cadafunc += 1
    print(f'{cadafunc}: {funcionario}')
    
for i, funcionario in enumerate (funcionarios):
    print(f'{i} é o funcionario {funcionario}')
    
    
    
estoque = [50, 30, 20, 15, 40, 25, 10, 5, 60, 80, 90, 70, 100, 55, 35, 45]
produtos = ['coca', 'pepsi', 'fanta', 'sprite', 'guarana', 'agua', 'suco', 'energetico', 'chocolate', 'biscoito', 'salgadinho', 'pao de queijo', 'bolo', 'torta', 'docinho', 'pipoca']
nivelminimo = 25
for i, quantidade in enumerate (estoque):
    if quantidade < nivelminimo:
        print(f'Produto {i} está com estoque baixo: {quantidade} unidades')
    else:
        print(f'Produto {i} está com estoque ok: {quantidade} unidades')