class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        print((self.nota1 + self.nota2) / 2)


Noresto = Aluno('João Carlos Noresto', 7, 9)

Noresto.calcular_media()