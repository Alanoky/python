from random import randint
jogador1 = randint(1,6)


bib = {}
while True:
    chave = str(input('Digite o nome da Chave:'))
    bib[chave] = str(input(f'Digite o valor de {chave}:'))
    res =str(input('Deseja continuar (S/N):'))

    if res in "Nn":
        break
print(bib)