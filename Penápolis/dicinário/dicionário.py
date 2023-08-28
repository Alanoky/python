pessoa = {'Nome':'Davi', 'Idade': 16, 'Altura': 1.80}
print(pessoa['Nome'])

#pessoa = {}
#pessoa = dict()

pessoa['Peso'] = 60.5

del pessoa['Peso']

pessoa2 = {'Nome':'Biazoto', 'Peso': 60, 'Sexo': 'M'}
pessoa.update(pessoa2)
pessoa2['Idade'] = 15
print(pessoa)

print(pessoa.values())
print(pessoa.keys())
print(pessoa.items())

for k in pessoa.keys():
    print(k)

for v in pessoa.values():
    print(v)

for k,v in pessoa.items():
    print(f'O item {k} é `{v}')
    
idaded = int(input('Digite sua idade:'))
if idaded == pessoa['Idade']:
    print('Você tem a mesma idade que o Davi')