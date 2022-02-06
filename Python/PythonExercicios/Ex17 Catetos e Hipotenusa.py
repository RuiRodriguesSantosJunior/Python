# co = float(input("Comprimento do Cateto Oposto: "))
# ca = float(input("Comprimento do Cateto Adjacente: "))
# hip = ((ca ** 2 + co ** 2) ** (1/2))
# print('A hipotenusa vai medir: {:.2f}'.format(hip))

from math import hypot
co = float(input("Comprimento do Cateto Oposto: "))
ca = float(input("Comprimento do Cateto Adjacente: "))
hip = hypot(ca,co)
print('A hipotenusa vai medir: {:.2f}'.format(hip))