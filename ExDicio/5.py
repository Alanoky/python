notas = {}
qnotas = +1
while True:
    materia = str(input('Digite a materia:'))
    notas[materia] = float(input(f'Digite a nota de {materia}:'))
    res =str(input('Deseja continuar (S/N):'))
    sum(notas)

    if res in "Nn":
        break
print(notas)