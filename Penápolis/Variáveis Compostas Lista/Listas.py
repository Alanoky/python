fruta = ['Maçã', 'Banana', 'Abacaxi', 'Uva']
fruta[3] = 'Melância'
fruta.append('Laranja')
print(fruta)

fruta.insert(0,'Morango')

del fruta[3]
# (alternativo) fruta.pop[3]
# (alternativo) fruta.remove['Abacaxi']

for c in fruta:
    if c =='Abacaxi':
        fruta.remove('Abacaxi')
else:
        print('Não Encontrado')

if 'Abacaxi' in fruta:
    fruta.remove('Abacaxi')
else:
    print('Não Encontrado')

if 'Abacaxi' not in fruta:
    print('Não Encontrado')
else:
    fruta.remove('Abacaxi')

maior = max(fruta, key=len)
menor = min(fruta, key=len)
print(f'Maior: {maior}')
print(f'Menor: {menor}')