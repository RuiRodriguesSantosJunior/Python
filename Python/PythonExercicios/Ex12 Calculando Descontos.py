preco = float(input('Qual o preço do Produto: '))
total = preco - (preco * 5 / 100)
print('O produto que custava R$ {:.2f}, na promoção com o desconto de 5%, vai custar R$ {:.2f}'.format(preco, total))