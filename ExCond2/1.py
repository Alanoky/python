time1 = int(input('Informe os gols do time 1:'))
time2 = int(input('Informe os gols do time 2:'))
if time1 > time2:
    print('O time 1 ganhou!')
elif time2 > time1:
    print('O time 2 ganhou!')
else:
    print('Foi empate!')