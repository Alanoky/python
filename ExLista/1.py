num = []
while True:
    num.append(int(input('Digite um número:')))
    res = str(input('Digite qualquer caractere para continuar. Caso não deseje continuar, digite "0".\n '))
    if res == '0':
        break
    soma = sum(num)
    mult = soma * soma
    maior = max(num)
    menor = min(num)
    print(f'Os números são: {num}')
    print(f'A soma dos números é: {soma}')
    print(f'A multiplicação do total dos números é: {mult}')
    print(f'O maior número é: {maior}')
    print(f'O menor número é: {menor}')


