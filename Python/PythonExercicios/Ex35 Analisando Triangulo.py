print('*' * 54)
print('------- Condição de existência de um triângulo -------'.upper())
print('*' * 54)

r1 = float(input('Informe o comprimento da 1ª reta: '))
r2 = float(input('Informe o comprimento da 2ª reta: '))
r3 = float(input('Informe o comprimento da 3ª reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('PARABÉNS! É possível formar um triângulo com essas retas!')
else:
    print('DESCULPA. Não é possível formar um triângulo com essas retas.')

