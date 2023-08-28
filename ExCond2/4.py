num = int(input('Defina o primeiro número:'))
num2 = int(input('Defina o segundo número:'))
operação = str(input('Escolha se deseja somar(+), subtrair(-), multiplicar(*) ou dividir(/):'))
soma = num + num2
subtração = num - num2
multiplicação = num * num2
divisão = num / num2

if operação == '+':
    print(f'{soma}')
elif operação == '-':
    print(f'{subtração}')
elif operação == '*':
    print(f'{multiplicação}')
elif operação == '/':
    print(f'{divisão}')