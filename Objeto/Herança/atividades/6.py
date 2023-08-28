class Bebida:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.nome = tipo


class Refrigerante(Bebida):
    def __init__(self, nome, tipo, sabor, teor_de_acucar):
        super().__init__(nome, tipo)
        self.sabor = sabor
        self.teor_de_acucar = teor_de_acucar

Pepsi = Refrigerante('Pepsi', 'Pepsico','Limão', '???')


class Cafe(Bebida):
    def __init__(self, nome, tipo, densidade):
        super().__init__(nome, tipo)
        self.densidade = densidade


Três_C = Cafe('Três Corações', 'Café', '???')
print(Três_C.nome)