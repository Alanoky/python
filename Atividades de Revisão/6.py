frutas = ('Laranja', 'Maracujá', 'Maçã')

while True:
    escolha = str(input('Escolha uma fruta:'))
    if escolha in frutas:
        print('A fruta está na tupla')
        break
    else:
        print('A fruta não está na tupla.')
        print('Tente outra.')
