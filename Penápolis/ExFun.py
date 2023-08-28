def PArOuInpar(a):
    if a %2 == 0:
        print('É par')
    else:
        print('É impar ')


num = int(input('Insira um número: '))
PArOuInpar(num)


def ENum(b):
    if b.isnumeric():
        print('É um número')
    else:
        print('Não é um número')

var = str(input('Inaira um número: '))
ENum(var)