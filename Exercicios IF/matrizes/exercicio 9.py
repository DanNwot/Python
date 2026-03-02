l = int (input('digite o numero de linhas:  '))
c = int (input('digite o numero de colunas: '))
lista= []

for i in range(l):
    linha=[]
    for j in range(c):
        x= int (input())
        linha.append(x)
    lista.append(linha)

i = int (input ('digite a linha que deseja ver: '))
j = int (input ('digite a coluna que deseja ver: '))
print(lista[i][j])