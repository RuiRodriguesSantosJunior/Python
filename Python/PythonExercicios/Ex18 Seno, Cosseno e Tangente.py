import math

num = float(input('Informe o ângulo desejado: '))
seno = math.sin(math.radians(num))
print('O ângulo de {:.2f}º tem o SENO de {:.2f}'.format(num, seno))
coseno = math.cos(math.radians(num))
print('O ângulo de {:.2f}º tem o COSENO de {:.2f}'.format(num, coseno))
tangente = math.tan(math.radians(num))
print('O ângulo de {:.2f}º tem o TANGENTE de {:.2f}'.format(num, tangente))