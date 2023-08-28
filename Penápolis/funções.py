print('--------------------')
print('SENAI Legal')
print('--------------------')

print('-'*20)
print('SENAI Legal')
print('-'*20)

def Linha():
    print('-'*20)

Linha()
print('SESI Legal')
Linha()


def Linha(txt):
    print('-'*20)
    print(txt)
    print('-'*20)


Linha('SESI Legal')
Linha('SENAI Legal')



def Soma(a, b=0):
    S = a + b
    print(f'A Soma é:{S}')


Soma(1, 300)



def Soma2(*valores):
    S = 0
    for c in valores:
        S+= c
    print(f'A soma é:{S}')


Soma2(300,2,600)



def Soma3(a,b):
    S = a + b
    return S

A = Soma(1,300)