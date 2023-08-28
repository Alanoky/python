class Carro:
    Nome = ''
    def Ligar(self):
        print(f'Ligando o {self.Nome}')

CitroenC3 = Carro()
CitroenC3.Nome = 'Citroën C3'
CitroenC3.Ligar()