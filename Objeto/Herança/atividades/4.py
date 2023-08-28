class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas, rodas):
        super().__init__(marca, modelo,ano)
        self.protas = portas
        self.rodas = rodas


Carro1 = Carro('Wolkswagen', 'AAA', 2022, 4, 4)
print(Carro1.ano)


class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, rodas, pneu):
        super().__init__(marca, modelo, ano)
        self.rodas = rodas
        self.pneu = pneu


Moto1 = Moto('Suzuki', 'Burgman', 2005, 2 , 'Flac')
print(Moto1.marca)