num = int(input('Informe um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        tot =+ 1
        print('{} '.format(c), end='')
print('\nO número {} foi divisível {} vezes!'.format(num, tot))
if tot == 2:
    print('É por isso que ele é Primo!')
else:
    print('É por isso que ele Não é Primo!')