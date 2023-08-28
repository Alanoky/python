num = list(range(1, 7))
num2 = [7,5,3,0,9,6]

num2.sort()
print(num2)

num2.sort()
num2.sort(reverse = True)
print(num2)

soma = sum(num2)
print(f'Soma: {soma}')

maior = max(num2)
menor = min(num2)
print(f'Maior: {maior}')
print(f'Menor: {menor}')

num3 = num2[:]
num3[1] = 2
print(f'Lista 2: {num2}')
print(f'Lista 3: {num3}')

num4 = []
while True:
    num4.append(int(input('Digite um número:')))
    res = str(input('Deseja continuar? [S´/N]'))
    if res.lower() == 'n':
        break
print(f'Os números são: {num4}')