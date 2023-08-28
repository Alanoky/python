maior = 0
menor = 0
media = 0
for n in range (1, 11):
    num = int(input('Digite um número inteiro:'))
    if n==1:
        maior = num
        menor = num
        media = num
else:
    if num > maior:
        maior = num
    elif num < menor:
        menor= num
print(f'O maior é {maior}')
print(f'O menor é {menor}')