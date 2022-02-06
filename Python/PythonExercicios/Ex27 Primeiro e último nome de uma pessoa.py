nome = str(input('Informe seu nome completo: ')).strip().upper()
n = nome.split()
print('Muito prazer te conhecer {}, esse é seu primeiro nome!'.format(n[0]))
print('Seu ultimo nome é {}'.format(n[len(n)-1]))