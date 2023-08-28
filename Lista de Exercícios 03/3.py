numpar = 0
numimpar = 0
for n in range (1, 7):
    num = int(input('Digite um número inteiro:'))
    if n % 2 == 0:
        numpar += 1
    else:
        numimpar += 1
print(f'Há {numpar} números pares e {numimpar} números ímpares')