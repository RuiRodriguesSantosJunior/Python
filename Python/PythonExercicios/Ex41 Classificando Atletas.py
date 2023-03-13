from datetime import date
dtatual = date.today().year
nasc = int(input("Ano de Nascimento: "))
idade = dtatual - nasc
if idade <5:
    print('O Atleta tem {} anos.'.format(idade))
    print('Classificação: Infantil.')
elif idade < 12:
    print('O Atleta tem {} anos.'.format(idade))
    print('Classificação: Mirim.')
elif idade < 18:
    print('O Atleta tem {} anos.'.format(idade))
    print('Classificação: Junior.')
elif idade < 21:
    print('O Atleta tem {} anos.'.format(idade))
    print('Classificação: Sênior.')
else:
    print('O Atleta tem {} anos.'.format(idade))
    print('Classificação: Adulto.')