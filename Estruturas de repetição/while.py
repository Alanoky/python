while 30 <20:
    print('Olá mundo!')



num = 0
while num < 20:
    print(num)
    num= num + 1

res = 'S'
while res =='S':
    num = int(input('Digite:'))
    res = str(input('Deseja continoar? (S/N)'))
res = 'S'
while res == 'S':
    num= int(input('Digite:'))
    if num >= 999:
        print('Número muito grande:')
        break
        res = str(input('Deseja continuar?(S/N)'))


while True:
    ini = str(input('Digite Começar:'))
    if ini != 'Começar':
        print('Não digiotu Começar')
    else:
        break

ini = 0
ini2 = 1
whileini = int(input('Digite 1 para iniciar:'))
print('Não Digitou 2')
print('Iniciando...')