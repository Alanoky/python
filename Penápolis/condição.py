idade = int(input('Digite sua idade:'))
if idade < 30:
    print('Você é novo')
print('Bom Dia')


nome = str(input('Digite seu nome:'))
if nome.lower() == 'Yan' or 'yan':
    print('Filho do Bruno')

if nome != 'Yan':
    print('Não é o filho do Bruno')

num = int(input('Digite um número:'))
if num %2 == 0:
    print('Par')
else:
    print('Impar')


idade2 = int(input('Digite sua idade:'))
if idade2 <= 20:
    print('Você é novo')
elif idade2 >= 70:
    print('Você é velho')
else:
    print('Você é adulto')


idade3 = int(input('Digite sua idade:'))
if idade3 <= 20 and idade3 >= 5:
    print('Você é novo')
elif idade3 >= 70 and idade3 <= 100:
    print('Você é velho')
elif idade3 > 100:
    print('Você é centenário! Congrats!')