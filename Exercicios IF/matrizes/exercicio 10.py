l = int (input('digite o numero de linhas:  '))
c = int (input('digite o numero de colunas: '))
lista= []

for i in range(l):
    linha=[]
    for j in range(c):
        x= int (input())
        linha.append(x)
    lista.append(linha)

print(lista[0][0])