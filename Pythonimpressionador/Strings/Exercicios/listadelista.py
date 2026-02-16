vendedores = ['joão', 'maria', 'josé', 'ana']
produtos = ['ipad', 'iphone']
vendas = [
    [1500, 2000],  # vendas do joão
    [3000, 2500],  # vendas da maria
    [1200, 1800],  # vendas do josé
    [2200, 2700]   # vendas da ana
]

vendasipadjoao = vendas[0][0]
print(f'O joão vendeu {vendasipadjoao} em ipads.')
vendasiphonejoao = vendas[0][1]
print(f'O joão vendeu {vendasiphonejoao} em iphones.')

vendasipadjoaoatualizado = vendas [0][1] = 50
print(f'O joão vendeu agora {vendasipadjoaoatualizado} em ipads.')

print(f'{vendas}')

vendasmac = [1500, 3000, 1200, 2200]
vendas[0].append(vendasmac[0])
vendas[1].append(vendasmac[1])
vendas[2].append(vendasmac[2])
vendas[3].append(vendasmac[3])
print(f'{vendas}')