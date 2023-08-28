lista = []
lista2 = []
while True:
    nome = str(input('Insira o nome:'))
    idade = int(input('Insira a idade:'))
    telefone = int(input('Insira o telefone: '))
    lista.append(nome)
    lista.append(idade)
    lista.append(telefone)
    lista2.append(lista)
    lista.clear()
    res = input('Deseja continuar? S/N')
    if res == 'N'or res == 'n':
        break
