maçã = {'Nome': 'maçã', 'Calorias': 52}
banana = {'Nome': 'banana', 'Calorias': 89}
abacaxi = {'Nome': 'abacaxi', 'Calorias': 50}
uva = {'Nome': 'uva', 'Calorias': 67}

frutas = []
frutas.append(maçã.copy())
frutas.append(banana.copy())
frutas.append(abacaxi)
frutas.append(uva)
maçã['Calorias'] = 67

frutas2 = [['maçã', 52], ['banana', 89], ['abacaxi', 50], ['uva', 67]]
print(frutas2[0])
print(frutas2[0][0])
print(frutas2[2][1])

for c in frutas2:
    print(f'A fruta {c[0]} tem {c[1]} calorias')

res = str(input('Digite uma fruta:'))
if res in c:
    print('Fruta encontrada')
else:
    print('Fruta não encontrada')