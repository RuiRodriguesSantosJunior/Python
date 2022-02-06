from random import shuffle

a1 = str(input('Informe o nome do 1º Aluno: '))
a2 = str(input('Informe o nome do 2º Aluno: '))
a3 = str(input('Informe o nome do 3º Aluno: '))
a4 = str(input('Informe o nome do 4º Aluno: '))

lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem apresentada é: {}'.format(lista))