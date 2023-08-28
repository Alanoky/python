class Carro:
    def __init__(self, nome, cor , marca):
        self.nome = nome
        self .cor = cor
        self.marca = marca

    def Ligar(self):
        print(f'ligando o {self.nome}')


class CarroCitroen(Carro):
    def __init__(self, nome, cor, portas):
        super().__init__(nome, cor, 'Citroen')
        self.portas = portas


Car1 = CarroCitroen('C3', 'Branco', 4)
Car2 = CarroCitroen('Cactus', 'Azul', 2)