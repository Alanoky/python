class Forma:
    def __int__(self, altura, largura):
        self.altura = altura
        self.largura = largura


class Retangulo(Forma):
    def __init__(self, altura, largura):
        super().__init__(altura, largura,)

    def area(self):
        print(self.altura * self.largura)


Roger = Retangulo(10, 30)
Roger.area()

# Eu não consigo entender o erro. Eu simplesmente não consigo