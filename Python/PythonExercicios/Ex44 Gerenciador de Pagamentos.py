print(11*'=' + ' LOJAS RODRIGUES ' + 11*'=')
preco = float(input('Preço das Compras: R$ '))
print('''FORMA DE PAGAMENTO
[ 1 ] à vista DINHEIRO/CHEQUE'
[ 2 ] à vista CARTÃO'
[ 3 ] 2x ou mais no CARTÃO''')
opcao = int(input('Qual a opção desejada: '))
if opcao == 1:
    precofinal = preco - (preco * 0.10)
    print('Sua compra de R$ {:.2f} vai custar {:.2f} no final.'.format(preco, precofinal))
elif opcao == 2:
    precofinal = preco - (preco * 0.05)
    print('Sua compra de R$ {:.2f} vai custar {:.2f} no final.'.format(preco, precofinal))
elif opcao == 3:
    qtdparcela = int(input('Qual a quantidade de parcelas: '))
    if qtdparcela <= 2:
       precofinal = preco / qtdparcela
       print('Sua compra foi de R$ {:.2f} e será parcelada em {}x de R$ {:.2f}'.format(preco, qtdparcela, precofinal))
    else:
        precofinal = (preco + (preco * 0.20))
        juros = precofinal / qtdparcela
        print('Sua compra foi de R$ {:.2f} e será parcelada em {}x de R$ {:.2f}'.format(precofinal, qtdparcela, juros))
else:
    print('Opção Inválida!!')

