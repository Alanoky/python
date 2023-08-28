num = []
print('Se quiser finalizar o processo, digite "0".')
while True:
    virate = num.append(int(input('Digite um número:')))
    if num == 0 or num.__contains__(0):
        num.sort()
        del num[0]
    if num.__contains__(num):

        break
