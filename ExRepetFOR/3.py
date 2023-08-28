P = int(input('Digite a quantidade de pessoas: '))
media = 0
for n in range (0, P + 1):
    t = float(input('Digite a temperatura:'))
    if t <= 37.2:
        print('A temperatura está normal')
    elif t >= 37.3 and t < 38:
        print('A temperatura é febril')
    elif t >= 38 and t <= 39:
        print('A temperatura é de febre')
    else:
        print('A temperatura é de febre alta')


    media = media + t
print(f'media {media / P}')
