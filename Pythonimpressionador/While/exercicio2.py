vendas = [500, 400, 400, 150, 149, 145, 130, 120, 110, 100, 90, 80]
vendedores = ['Ana', 'Bruno', 'Carla', 'Daniel', 'Eduardo', 'Fernanda', 'Gustavo', 'Helena', 'Igor', 'Juliana', 'Kleber', 'Larissa']
meta = 100

i = 0
while vendas [i] >= meta:
    print(f'Vendedor: {vendedores[i]} - Vendas: {vendas[i]} - Bateu a meta!')
    i += 1
