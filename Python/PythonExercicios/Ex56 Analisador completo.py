media = 0
velho = 0
novo = 0
masc = 0
fem = 0
somaidade = 0
nomevelho = ''
nomenovo = ''

for c in range(1, 4):
    print('----- {}º Pessoa -----'.format(c))
    nome = str(input('Nome: ')).upper()
    idade = int(input('Idade: '))
    somaidade += idade
    media = idade / (c)
    if c == 1:
        velho = idade
        novo = idade
    else:
        if idade > velho:
            velho = idade
            nomevelho = nome
        if idade < novo:
            novo = idade
            nomenovo = nome
    sexo = str(input('Sexo [M/F]: ')).upper()
    if sexo == 'F':
        fem += 1
    elif sexo == 'M':
        masc += 1

print('A média de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(velho, nomevelho))
print('O homem mais novo tem {} anos e se chama {}'.format(novo, nomenovo))
print('Ao todo são {} mulheres e {} homens'.format(fem, masc))