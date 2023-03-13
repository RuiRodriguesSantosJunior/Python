n1 = float(input('Informe a Primeira Nota: '))
n2 = float(input('Informe a Segunda Nota: '))
media = (n1 + n2) / 2
print('Tirando as respectivas notas {:.2f} e {:.2f} a média do aluno é {:.2f}'.format(n1, n2, media))
if media < 5:
    print('O aluno teve média {:.2f}. Portanto está Reprovado!!!'.format(media))
elif media >= 5 and media < 8:
    print('O aluno teve média {:.2f}. Portanto está de Recuperação!!!'.format(media))
else:
    print('O aluno teve média {:.2f}. Portanto está Aprovado!!!'.format(media))
