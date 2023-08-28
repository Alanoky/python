for variável in range (0, 100):
    print('Olá mundo!')

for n in range (1, 6):
    print('Olá mundo!')
print('fim')

for n in range(1, 6):
    print(n)
print('fim')

for n in range(0, 10, 2):
    print( n,'Olá Mundo!')

for n in range(0,10, 2):
    print(n)
    print('fim')

i = int(input('Início:'))
f = int(input('Fim:'))
p = int(input('Passo:'))
for n in range (i,f,p):
    print(n)

fim = int(input('Fim:'))
fim2= fim + 1
for n in range(1,fim2):
    if n > 50:
        n2=int(input('Digite novamente:'))
    print('Fim')