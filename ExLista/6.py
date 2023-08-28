num = []
print('Se quiser finalizar o processo, digite "0".')
while True:
    num.append(int(input('Digite um número:')))
    if num == 0 or num.__contains__(0):
        num.sort()
        del num[0]
        break
print('A quantidade de números digitados foi de ',num.__len__())
num.sort()
num.sort(reverse = True)
print(f'A ordem decrescente dos números é: {num}')
if num.__contains__(5):
    print('O valor 5 foi digitado')