num = int(input("Digite um Número: "))
print("""'Escolha uma das bases para conversão:'
      [ 1 ] Converter para Binário
      [ 2 ] Converter para Octal
      [ 3 ] Converter para Hexadecimal""")
opcao = int(input("Sua opção: "))
if opcao == 1:
    print("O número {} convertido em Binário é {}".format(num, bin(num)[2:]))
elif opcao == 2:
    print("O número {} convertido em Octal é {}".format(num, oct(num)[2:]))
elif opcao == 3:
    print("O número {} convertido em Hexadecimal é {}".format(num, hex(num)[2:]))
else:
    print("Nenhuma das opções escolhidas!")
