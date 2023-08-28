A = int(input('Digite o número que será dividido:'))
B = int(input('Digite o número divisor:'))
if A % B == 0:
    print(f'{A} é divisível por {B}')
else:
    print(f'{A} não é divisível por {B}')