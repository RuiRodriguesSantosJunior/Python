soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Informe o {}º valor: '.format(c)))
    if num % 2 == 0:
        cont += 1
        soma += num
print('Você informou {} número(s) pare(s). Sua somatória é {} !'.format(cont, soma))