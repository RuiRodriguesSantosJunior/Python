"""n1 = int(input('Informe o n1 valor: '))
n2 = int(input('Informe o n2 valor: '))
n3 = int(input('Informe o terceiro valor: '))
maior = n1
menor = n1
if n1 > n2 and n1 > n3:
    maior = n1
    print('O maior valor digitado foi: {}'.format(maior))
    if n2 > n3:
        menor = n3
        print('O menor valor digitado foi: {}'.format(menor))
    else:
        menor = n2
        print('O menor valor digitado foi: {}'.format(menor))
elif n2 > n1 and n2 > n3:
    maior = n2
    print('O maior valor digitado foi: {}'.format(maior))
    if n1 > n3:
        menor = n3
        print('O menor valor digitado foi: {}'.format(menor))
    else:
        menor = n1
        print('O menor valor digitado foi: {}'.format(menor))
elif n3 > n1 and n3 > n2:
    maior = n3
    print('O maior valor digitado foi: {}'.format(maior))
    if n2 > n1:
        menor = n1
        print('O menor valor digitado foi: {}'.format(menor))
    else:
        menor = n2
        print('O menor valor digitado foi: {}'.format(menor))
"""

p = int(input('n1 valor: '))
s = int(input('n2 valor: '))
t = int(input('Terceiro valor: '))
maximo = max(p, s, t)
minimo = min(p, s, t)

print(f'O menor valor digitado foi {minimo}')
print(f'O maior valor digitado foi {maximo}')