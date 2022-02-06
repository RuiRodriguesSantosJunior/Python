print('-------------------------------------------------')
print("ESCOLHA A MOEDA QUE DESEJA COMPRAR PELO NUMERO!!")
print('-------------------------------------------------')
print("1- DOLLAR R$ 5.26\n"
       "2- EURO R$ 6.26\n"
       "3- LIBRA ESTERLINA R$ 7.93")
print('-------------------------------------------------')

moeda = float(input("Qual moeda deseja comprar: "))

if moeda == 1:
    real = float(input("Qual valor em reais deseja comprar: "))
    dollar = real / 5.26
    print('Você comprou R$ {:.2f} reais, totalizando US$ {:.2f} dólares.'.format(real, dollar))
elif moeda == 2:
    real = float(input("Qual valor em reais deseja comprar: "))
    euro = real / 6.20
    print('Você comprou R$ {:.2f} reais, totalizando EUR {:.2f} euros.'.format(real, euro))
elif moeda == 3:
    real = float(input("Qual valor em reais deseja comprar: "))
    libra = real / 7.93
    print('Você comprou R$ {:.2f} reais, totalizando GBP {:.2f} libras.'.format(real, libra))
else:
    print('Opção informada inválida! Tente Novamente!!!')
    print('-------------------------------------------------')



