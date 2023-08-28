def Linha(txt):
    print('-'*20)
    print(txt)
    print('-'*20)

Linha("I'm the Scatman!")

def Soma(a,b=0):
    S = a + b
    print('A Soma é:',S)

Soma(1,300)


def Soma2(*valores):
    S = 0
    for C in valores:
        S += C
    print('A soma é:',S)

Soma2(300,2,600)
Soma2(300,2,600,3,5,20,333,148)

def Soma3(a,b):
    S = a + b
    return

A = Soma3(1,300)
print('A sOma é:', A)
