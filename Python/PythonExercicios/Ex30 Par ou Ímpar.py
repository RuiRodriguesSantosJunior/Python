class bcolors:
    OK = '\033[92m'  # GREEN
    WARNING = '\033[93m'  # YELLOW
    FAIL = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR está lá para definir a cor de volta ao padrão.

num = int(input('Informe um número: '))
if num <= 0:
    print(bcolors.FAIL + 'Informe um número positivo!'.format(num) + bcolors.RESET)
elif num // 2:
    print(bcolors.OK + 'O número {} é par!'.format(num) + bcolors.RESET)
else:
    print(bcolors.WARNING + 'O número {} é ímpar!'.format(num) + bcolors.RESET)