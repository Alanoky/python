dicionario = {'Jonas': 43, 'Micto': 23}


while True:
    escolha = str(input('Escolha entre Jonas ou Micto: '))

    if escolha in dicionario:
        idade = dicionario[escolha]
        print(f'{escolha} possui {idade} anos de idade.')
        break

    else:
        print(f'{escolha} não existe no dicionário')