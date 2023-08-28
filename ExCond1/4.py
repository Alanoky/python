anonascimento = int(input('Informe seu ano de nascimento:'))
anoatual = 2023
resultado = anoatual - anonascimento
if resultado >= 18:
    print('Você é maior de idade!')
else:
    print('Você é menor de idade!')