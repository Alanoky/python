class Surpresa:
    def __init__(self, tipo, nome, cor, idadeR, material, caracteristica, preco, fabricante, dimensoes, peso):
        self.tipo = tipo
        self.nome = nome
        self.cor = cor
        self.idadeR = idadeR
        self.material = material
        self.caracteristica = caracteristica
        self.preco = preco
        self.fabricante = fabricante
        self.dimensoes = dimensoes
        self.peso = peso

    def Abrir(self):
        print('Abrindo...')


transformer_de_segunda_mao = Surpresa('veículo',
                                      'Indefinido',
                                      'laranja, preto, cinza claro, cinza escuro',
                                      'Acima de 3',
                                      'plastico',
                                      'rodas móveis',
                                      1,
                                      'Ferrero',
                                      '4cm, 2.5cm',
                                      '5gm')

transformer_de_segunda_mao.Abrir()
