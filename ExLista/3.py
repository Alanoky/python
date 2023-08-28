num = []
print('Se quiser finalizar o processo, digite "0".')
while True:
    num.append(int(input('Digite um número:')))
    if num == 0 or num.__contains__(0):
        num.sort()
        del num[0]
        break
soma = sum(num)
menor = min(num)
print(f'A soma de todos os números é: {soma}')
print(f'O menor dos números é: {menor}')