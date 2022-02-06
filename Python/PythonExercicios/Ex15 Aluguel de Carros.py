dias = int(input('Informe a quantidade de dias que alugou o carro: '))
km = float(input('Informe a quantidade em Km que percorreu com o mesmo: '))
PgDiaria = (60 * dias) + (km * 0.15)
print('O valor do carro alugado no período foi de R$ {:.2f}'.format(PgDiaria))