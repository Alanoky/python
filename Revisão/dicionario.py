pessoa = {'Nome': 'Duda', 'Idade': 16, 'Altura': 1.50}
print(pessoa['Nome'])
pessoa2 = {}
pessoa3 = dict()

pessoa4 = {'Nome': 'Duda', 'Idade': 16, 'Altura': 1.50}
pessoa5 = {'Nome': 'Brenda', 'Peso':60, 'Sexo':'F'}
pessoa.update(pessoa2)
pessoa5['Idade'] = 15

print(pessoa4.values())
print(pessoa4.keys())
print(pessoa4.items())

for k in pessoa4.keys():
    print(k)

for v in pessoa4.values():
    print(v)

for k,v in pessoa4.items():
    print(f'O item {k} é {v}')

