vendas = ('Daniel', '25/08/1990', 1500.75, 'SP')
nome = vendas[0]
data_nascimento = vendas[1]
salario = vendas[2]
estado = vendas[3]
print(f'Nome: {nome}')
print(f'Data de Nascimento: {data_nascimento}')
print(f'Salário: {salario}')
print(f'Estado: {estado}')
print('--- Desempacotamento Completo ---')

#=============================================================================

nome, data_nascimento, salario, estado = vendas
print(f'Nome: {nome}')
print(f'Data de Nascimento: {data_nascimento}')
print(f'Salário: {salario}')
print(f'Estado: {estado}')
print('--- Desempacotamento Simplificado ---')