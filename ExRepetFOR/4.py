mediam = 0
qm = 0
mediah = 0
qh = 0
mediag = 0
qg = 0

for n in range (1, 11):
    sexo = int(input('defina seu sexo: 1 = masculino ou 2 = feminino\nR: '))
    idade = int(input('Defina sua idade: '))
    if sexo == 1:
        mediah += idade
        qh =+ 1
    if sexo == 2:
        mediam += idade
        qm += 1
    mediag += idade
    qg += 1

print(f'media homem = {mediah / qh}')
print(f'media mulher = {mediam / qm}')
print(f'media grupo = {mediag / qg}')
