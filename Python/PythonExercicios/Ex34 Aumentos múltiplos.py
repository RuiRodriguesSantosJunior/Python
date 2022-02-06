sal = float(input('Informe seu salário: '))
if sal <= 1250:
    new = sal + (sal * 0.15)
    print('Seu novo salário é: R$ {:.2f}'.format(new))
else:
    #sal > 1250:
    new = sal + (sal * 0.10)
    print('Seu novo salario é: R$ {:.2f}'.format(new))
print('Quem granhava R$ {:.2f}, passa a ganhar R$ {:.2f}'.format(sal, new))
