from time import sleep
print("Esperamos 10 segundos")
print('Fogos de artifício em...')
for c in range(10, -1, -1):
    print(c,end= '...\n')
    sleep(0.7)
print('Parabéns Pelos Fogos!!!')
