class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class Livro(Produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco,)
        self.autor = autor


Livro1 = Livro("AAA", 21, "Jonas Macartney")
print(Livro1.autor)


class Eletronico(Produto):
    def __init__(self, nome, preco, voltagem):
        super().__init__(nome, preco)
        self.voltagem = voltagem


Liquidificador = Eletronico('Liquidificador', 200, 12431)
print(Liquidificador.nome)