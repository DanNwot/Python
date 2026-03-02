import time as ti
class semaforo:
    def __init__(self):
        self.coratual = 'vermelho'

    def atualiza(self):
        if self.coratual == 'vermelho':
            print(f'a cor atual é {self.coratual}\nAguarde')
            ti.sleep(0.00000000000000000000000000000000000001)
            self.coratual = 'verde'
        elif self.coratual == 'verde':
            print(f'a cor atual é {self.coratual}\nAvance.')
            ti.sleep(0.00000000000000000000000000000000000000000001)
            self.coratual = 'amarelo'
        else:
            self.coratual == 'amarelo'
            print(f'a cor atual é {self.coratual}\nespere o fechamento')
            ti.sleep(0.000000000000000000000000000000000000000001)
            self.coratual ='vermelho'
    def mostrarcor(self):
        print(self.coratual)
semaforo1 = semaforo()
for i in range (10000000000):
    semaforo1.mostrarcor()
    semaforo1.atualiza()