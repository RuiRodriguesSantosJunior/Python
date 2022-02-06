class bcolors:
    OK = '\033[92m'  # GREEN
    WARNING = '\033[93m'  # YELLOW
    FAIL = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR está lá para definir a cor de volta ao padrão.

km = float(input("Qual a velocidade do carro: "))
if km < 0:
    print(bcolors.OK + "Índice de velocidade inexistente! Digite indice de velocidade correto!" + bcolors.RESET)
elif km == 0:
    print(bcolors.OK + "Carro está parado Acelera esse carro!!!!" + bcolors.RESET)
elif km > 0 and km <= 80:
    print(bcolors.WARNING + "Tenha um bom dia! Dirija com cuidado!" + bcolors.RESET)
else:
    multa = (km - 80) * 7.00
    print(bcolors.FAIL + "MULTADO! Você excedeu o limite de velocidade permitido de 80km/h" + bcolors.RESET)
    print(bcolors.FAIL + 'VocÊ deve pagar uma multa de' + bcolors.WARNING + ' R$ {:.2f}!'.format(multa) + bcolors.RESET)
    print(bcolors.WARNING + "Tenha um bom dia! Dirija com cuidado!" + bcolors.RESET)

