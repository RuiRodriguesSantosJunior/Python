class bcolors:
    OK = '\033[92m'  # GREEN
    WARNING = '\033[93m'  # YELLOW
    FAIL = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR está lá para definir a cor de volta ao padrão.

km = float(input('Informe a distância da Viagem: '))
if km <= 0:
    print(bcolors.FAIL + 'Por Favor informar um km válido!!' + bcolors.RESET)
elif km <= 200:
    preco = (km * 0.50)
    print(bcolors.OK + 'Você está prestes a iniciar uma viagem de {:.2f} km!'.format(km) + bcolors.RESET)
    print(bcolors.OK + 'O preço da sua passagem será de R$ {:.2f}'.format(preco) + bcolors.RESET)
else:
    preco = (km * 0.45)
    print(bcolors.OK + 'Você está prestes a iniciar uma viagem de {:.2f} km!'.format(km) + bcolors.RESET)
    print(bcolors.OK + 'O preço da sua passagem será de R$ {:.2f}'.format(preco) + bcolors.RESET)

