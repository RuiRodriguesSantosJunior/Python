casa = float(input('Informe o valor da casa que deseja comprar: '))
sal = float(input('Informe seu salário: '))
anos = int(input('Informe em quantos anos deseja pagar do financiamento: '))
prestacao = casa / (anos * 12)
minimo = (sal * 30) / 100
if prestacao <= minimo:
    print('Empréstimo Concedido! Parabéns!')
else:
    print('Empréstimo Negado!')
    print(('Para pagar uma casa de R$ {:.2f} em {} anos, sua prestação será de R$ {:.2f}').format(casa,anos,prestacao))

print("Para pagar uma casa de R$ {:.2f} em {} anos".format(casa, anos), end='')
print("a prestação será de R$ {:.2f}".format(prestacao))
print("Comparando tem que pagar {:.2f} e o máximo de parcela é de {:.2f}".format(prestacao, minimo))