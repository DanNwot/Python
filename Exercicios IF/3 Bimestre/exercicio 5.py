class Retangulo:
    def __init__(self, Altura, Base):
        self.Altura = Altura
        self.Base = Base
    
    def Perimetro(self):
        return self.Base + self.Base + self.Altura + self.Altura
        

    def Area(self):
        return self.Base * self.Altura
        
    
x= int(input('Digite a Altura:\n'))
y= int(input('Digite a Base:\n'))
Retangulo1= Retangulo(x, y)
i= int (input('digite se quer ver a area ou o perimetro\n 1 Para a Area\n 2 Para o Perimetro: \n'))
if i == 1:
    print(Retangulo1.Perimetro())
else:
    print(Retangulo1.Area())

        
