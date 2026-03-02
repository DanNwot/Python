lista=[]
x= input('digite o nome de frutas, digite 1 para parar:')
lista.append(x)
while x != "1":
    x= input('digite o nome de frutas, digite 1 para parar:')
    lista.append(x)
for i in lista:
    print (i.upper())