l = float(input('Largura da Parede: '))
a = float(input('Altura da Parede: '))
area = l * a
tinta = area / 2.00
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(l,a,area))
print('Para pintar essa parede, você precisará de {}l de tinta'.format(tinta))