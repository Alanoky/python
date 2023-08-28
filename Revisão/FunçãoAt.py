def voto(idade):
    if idade < 16:
        print('Seu voto é negado')
    elif idade == 16 or idade == 17:
        print('Seu voto é opcional')
    else:
        print('Seu voto é obrigatório')

voto(220)