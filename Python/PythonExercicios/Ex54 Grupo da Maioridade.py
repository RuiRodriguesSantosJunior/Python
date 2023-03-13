import datetime
from datetime import date
maior = 0
menor = 0
atual = date.today().year
nasc = 0
idade = 0
for c in range(1, 8):
    nasc = int(input('Em que ano a {}º pessoa  nasceu: '.format(int(c))))
    idade = atual - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas  maiores de idade!'.format(maior))
print('Ao todo tivemos {} pessoas  menores de idade!'.format(menor))