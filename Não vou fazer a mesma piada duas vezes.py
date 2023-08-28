while True:
    diametro = int(input('Defina o diâmetro do objeto: '))
    mel = int(input('Defina o volume do mel em centimetros cubicos: '))

    if mel > 10000 or mel < 1:
        print('Volume inválido')

    if diametro > 100 or diametro < 1:
        print('diâmetro inválido.')
    else:
        break

volume = mel * mel * mel
area = diametro /2 *  3.14
area2 = area * 2.96 
print(area)
print(area2)

