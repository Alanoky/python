qh = 0
qm = 0
Mmenor20 = 0

for n in range (1, 9):
    nome = str(input('Defina seu nome:'))
    idade = int(input('Defina sua idade:'))
    sexo = int(input('Defina seu sexo: 1 = Masculino 2 = Feminino \nR:'))
    if sexo == 1:
        qh += 1
    elif sexo == 2:
        qm += 1,

    if sexo == 2 and idade < 20:
         Mmenor20 += 1
