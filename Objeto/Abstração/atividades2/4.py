class Retangulo:
    def __init__(self,base, altura):
        self.base = base
        self.altura = altura

    def area(self):
       print( self.base * self.altura)


Ronald = Retangulo(20, 40)

Ronald.area()