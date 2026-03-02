def soma(n, n1):
    return n + n1
def multiplicacao(n,n1):
    return n * n1
def divisao(n,n1):
    return n / n1

n = int(input('Digite um numero:\n'))
n1 = int(input('Digite outro numero:\n'))
tipo = input('Digite o tipo de soma que deseja realizar: \n X para multiplicacao \n + Para Soma \n / para divisao \n')

if tipo == 'x':
    print (multiplicacao (n, n1))

if tipo == '+':
    print(soma (n, n1))

if tipo == '/':
    print(divisao (n, n1))
