"""Faça um Programa que peça as 4 notas bimestrais e mostre a média."""

n1 = float(input('Informe uma nota: '))
n2 = float(input('Informe uma nota: '))
media = (n1 + n2) / 2
print('Sua média das notas {} e {} foi {}'.format(n1, n2, media))
"""
if media <= 5:
    print('Sua média foi {}, vocÊ está Reprovado!'.format(media))
if media > 5 and media <= 7:
    print('Sua média foi {}, vocÊ está Recuperação!'.format(media))
if media > 7:
    print('Sua média foi {}, vocÊ está Aprovado!'.format(media))
"""