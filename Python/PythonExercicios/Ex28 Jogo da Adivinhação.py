class bcolors:
    OK = '\033[92m'  # GREEN
    WARNING = '\033[93m'  # YELLOW
    FAIL = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR está lá para definir a cor de volta ao padrão.

from time import sleep
from random import randint

print('-='*30)
print('Vou pensat em um número entre 0 e 5. Tente adivinhar...')
print('-='*30)
computador = randint(0, 5) # Faz o computador escolher numero aleatorio
print(computador)
pessoa = int(input('Em que numero pensei? ')) # Jogador escolhe um número
print('PROCESSANDO...')
sleep(2)
if pessoa < 0 or pessoa > 5:
    print(bcolors.WARNING + 'Repita o jogo, número fora da regra!!!' + bcolors.RESET)
elif computador == pessoa:
    print(bcolors.OK + 'PARABÉNS! Você conseguiu acertar o número!!!!' + bcolors.RESET)
else:
    print(bcolors.FAIL + 'GANHEI!! Eu pensei que o numero fosse {} e não {}' .format(computador, pessoa) + bcolors.RESET)
