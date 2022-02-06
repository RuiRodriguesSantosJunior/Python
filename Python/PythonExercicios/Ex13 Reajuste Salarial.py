Sal = float(input('Qual Salário do Funcionário: R$ '))
NSal = Sal + (Sal * 15 / 100)
print('O Funcionário que ganhava R$ {:.2f}, com 15% de aumento, passa a receber R$ {:.2f}'.format(Sal, NSal))