def maior(valores):
    a = max(valores)
    print(f'O {a}, é o maior número')


lista = []

while True:
    lista.append(str(input('Digite um número; ')))
    res = str(input('Deseja continuar? (S/N): '))
    if res in 'Nn':
        break

maior(lista)