nome = str(input('Digite seu nome: '))
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu nome n1 nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu nome n1 nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))