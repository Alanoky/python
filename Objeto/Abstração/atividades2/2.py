class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def Latir(self):
        print('Woof!')


Pascal = Cachorro('Pascal', 9)

Pascal.Latir()