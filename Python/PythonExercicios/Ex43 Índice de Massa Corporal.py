import math
from math import pow
peso = float(input('Qual é o seu peso: '))
altura = float(input('Qual a sua altura: '))
imc = peso / pow(altura,2)
if imc < 18.5:
    print('Você está com o IMC {:.2f} e está abaixo do Peso Normal.'.format(imc))
elif imc < 25:
    print('Você está com o IMC {:.2f} e está com Peso Ideal.'.format(imc))
elif imc < 30:
    print('Você está com o IMC {:.2f} e está com Sobrepeso.'.format(imc))
elif imc < 40:
    print('Você está com o IMC {:.2f} e está com Obesidade.'.format(imc))
elif imc >= 40:
    print('Você está com o IMC {:.2f} e está com Obesidade Mórbida.'.format(imc))