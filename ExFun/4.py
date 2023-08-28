def voto(nascimento):
    S = 2023 - nascimento
    if S < 15:
        print('Voto Negado')
    elif S >= 15 and S <= 17:
        print('Voto opcional')
    else:
        print('Voto obrigatório')


na = int(input('Insira o ano de nascimento: '))
voto(na)