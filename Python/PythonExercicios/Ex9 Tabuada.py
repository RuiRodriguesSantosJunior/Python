t = int(input('Informe a tabuada que deseja: '))
print('-----------')
lista = [0,1,2,3,4,5,6,7,8,9,10]
for c in lista:
    r = t * lista[c]
    print('{} x {:2} = {:2} |'.format(t, c, r))
print('-----------')
