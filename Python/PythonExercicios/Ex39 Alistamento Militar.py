from datetime import date
dtatual = date.today().year
nasc = int(input("Ano de Nascimento: "))
idade = dtatual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, dtatual))
if idade == 18:
    print('Você tem que se Alistar Imediatamente.')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = dtatual + saldo
    print('Seu Alistamento será em {} anos.'.format(ano))
else:
    saldo = idade - 18
    print('Você deveria ter se Alistado há {} anos.'.format(saldo))
    ano = dtatual - saldo
    print('Seu Alistamento foi em {} anos.'.format(ano))
