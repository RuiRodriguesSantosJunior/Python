maior = 0
menor = 0
for c in range(1, 5):
    peso = float(input('Pelo da {}º pessoa: '.format(c)))
    if c ==1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido  foi de {:.2f}kg'.format(maior))
print('O menor peso lido foi de {:.2f}kg'.format(menor))