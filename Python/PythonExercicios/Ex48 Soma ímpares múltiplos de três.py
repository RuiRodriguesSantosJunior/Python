soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('A soma de todos {} valores solicitados é {}'.format(cont, soma))
"""        if c % 3 == 0:
            somaImpar += c
            print(somaImpar)"""
