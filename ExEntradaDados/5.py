valor = float(input('Digite o valor: '))
tempo = int(input('Digite o tempo:'))
taxa = float(input('Digite a taxa: '))

prestação = valor + (valor * (taxa/100) * tempo)

print(prestação)