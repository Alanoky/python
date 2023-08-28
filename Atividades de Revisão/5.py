import random
while True:
    num = random.randint in range(0,10)
    adiv = int(input('Tente adivinhar um número entre 0 e 10: '))
    if adiv == num:
        print('Número correto!')
        break

    else:
        print('try again.')